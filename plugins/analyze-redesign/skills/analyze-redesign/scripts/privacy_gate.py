#!/usr/bin/env python3
"""Fail closed when an outbound skill snapshot contains private or secret material."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path, PurePosixPath


TEXT_SUFFIXES = {".md", ".txt", ".json", ".yaml", ".yml", ".py", ".svg"}
MAX_TEXT_BYTES = 2_000_000


def safe_relative(value: str) -> str:
    path = PurePosixPath(value)
    if path.is_absolute() or not value or any(part in {"", ".", ".."} for part in path.parts):
        raise ValueError("export path is not a normalized relative path")
    return path.as_posix()


def load_config(root: Path, relative: str) -> tuple[dict, Path]:
    config_rel = safe_relative(relative)
    config_path = root / config_rel
    if config_path.is_symlink() or not config_path.is_file():
        raise ValueError("export configuration is missing or is a symlink")
    data = json.loads(config_path.read_text(encoding="utf-8"))
    if data.get("sync_direction") != "installed-to-github-only":
        raise ValueError("sync direction is not outbound-only")
    if data.get("repository_import_allowed") is not False:
        raise ValueError("repository import must be explicitly disabled")
    if not isinstance(data.get("files"), list) or not data["files"]:
        raise ValueError("public file allowlist is empty")
    return data, config_path


def compiled_patterns() -> list[tuple[str, re.Pattern[str]]]:
    unix_roots = [
        "/work" + "space/",
        "/ro" + "ot/",
        "/ho" + "me/",
        "/tm" + "p/",
        "/op" + "t/",
    ]
    windows_root = "C:" + "\\\\Users\\\\"
    remote_skill = r"skill" + r"-[0-9a-f]{24,}"
    return [
        ("private-key", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----")),
        ("github-token", re.compile(r"gh" + r"[pousr]_[A-Za-z0-9]{20,}")),
        ("github-fine-grained-token", re.compile(r"github" + r"_pat_[A-Za-z0-9_]{20,}")),
        ("openai-style-secret", re.compile(r"(?<![A-Za-z0-9])sk" + r"-[A-Za-z0-9_-]{20,}")),
        ("aws-access-key", re.compile(r"AK" + r"IA[0-9A-Z]{16}")),
        ("slack-token", re.compile(r"xo" + r"[aprsb]-[A-Za-z0-9-]{16,}")),
        ("jwt", re.compile(r"eyJ[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}")),
        ("credential-in-url", re.compile(r"https?://[^/\s:@]+:[^/\s@]+@", re.IGNORECASE)),
        ("secret-query-parameter", re.compile(r"[?&](?:token|key|secret|password|signature)=[^&#\s]+", re.IGNORECASE)),
        (
            "local-absolute-path",
            re.compile(
                r"(?:^|[\s\"'`=(])(?:"
                + "|".join(re.escape(item) for item in unix_roots)
                + "|"
                + windows_root
                + ")",
                re.IGNORECASE,
            ),
        ),
        ("installed-skill-identifier", re.compile(remote_skill, re.IGNORECASE)),
        ("email-address", re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE)),
    ]


ASSIGNMENT = re.compile(
    r"\b(api[_-]?key|client[_-]?secret|access[_-]?token|refresh[_-]?token|password|passwd|cookie|authorization)\b"
    r"\s*[:=]\s*[\"']?([^\s,\"'}#]+)",
    re.IGNORECASE,
)


def looks_placeholder(value: str) -> bool:
    normalized = value.strip().lower()
    if normalized in {"none", "null", "false", "true", "redacted", "placeholder", "example", "changeme"}:
        return True
    return (
        normalized.startswith("${")
        or normalized.startswith("{{")
        or normalized.startswith("<")
        or set(normalized) <= {"*", "x", "-", "_"}
    )


def scan_text(relative: str, text: str) -> list[tuple[str, int]]:
    findings: list[tuple[str, int]] = []
    patterns = compiled_patterns()
    for number, line in enumerate(text.splitlines(), start=1):
        for label, pattern in patterns:
            if pattern.search(line):
                findings.append((label, number))
        assignment = ASSIGNMENT.search(line)
        if assignment and not looks_placeholder(assignment.group(2)):
            findings.append(("credential-assignment", number))
    return findings


def inspect_file(root: Path, relative: str) -> list[tuple[str, int | None]]:
    path = root / relative
    problems: list[tuple[str, int | None]] = []
    if path.is_symlink():
        return [("symlink", None)]
    if not path.is_file():
        return [("missing-file", None)]
    is_text = path.suffix.lower() in TEXT_SUFFIXES or path.name in {"VERSION"}
    if path.stat().st_size > MAX_TEXT_BYTES and is_text:
        return [("oversized-text-file", None)]
    if not is_text:
        return problems
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return [("non-utf8-text", None)]
    return [(label, line) for label, line in scan_text(relative, text)]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    parser.add_argument("--config", default="config/public-export.json")
    parser.add_argument("--strict-tree", action="store_true")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    if not root.is_dir():
        print("privacy gate failed: root is not a directory", file=sys.stderr)
        return 2

    try:
        config, _ = load_config(root, args.config)
        allowed = [safe_relative(item) for item in config["files"]]
        generated = [safe_relative(item) for item in config.get("generated_files", [])]
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"privacy gate failed: {exc}", file=sys.stderr)
        return 2

    if len(set(allowed)) != len(allowed):
        print("privacy gate failed: duplicate allowlist entry", file=sys.stderr)
        return 2

    failures: list[tuple[str, str, int | None]] = []
    for relative in allowed:
        for label, line in inspect_file(root, relative):
            failures.append((relative, label, line))

    if args.strict_tree:
        permitted = set(allowed + generated)
        present = {
            path.relative_to(root).as_posix()
            for path in root.rglob("*")
            if path.is_file() or path.is_symlink()
        }
        for extra in sorted(present - permitted):
            failures.append((extra, "unallowlisted-file", None))

    if failures:
        print(f"privacy gate failed with {len(failures)} finding(s):", file=sys.stderr)
        for relative, label, line in failures:
            location = f"{relative}:{line}" if line else relative
            print(f"- {location}: {label}", file=sys.stderr)
        return 1

    print(f"privacy gate passed: {len(allowed)} allowlisted files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
