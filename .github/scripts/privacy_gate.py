#!/usr/bin/env python3
"""Reject non-public paths or content by deriving the exact committed Git tree."""

from __future__ import annotations

import collections
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path, PurePosixPath


REPO_ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = REPO_ROOT / "PUBLIC_SYNC_ALLOWLIST.json"


def fail(message: str) -> None:
    raise AssertionError(message)


def load_config() -> dict:
    try:
        value = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"public allowlist is invalid: {exc}")
    if value.get("schemaVersion") != 1:
        fail("unsupported public allowlist schema")
    for field in ("allowedFiles", "allowedPrefixes", "allowedSkillExtensions", "allowedSkillBasenames"):
        if not isinstance(value.get(field), list):
            fail("public allowlist is missing a required list")
    if not isinstance(value.get("lockedFiles"), dict):
        fail("public allowlist must define locked files")
    return value


def git(arguments: list[str]) -> bytes:
    completed = subprocess.run(
        ["git", *arguments],
        cwd=REPO_ROOT,
        capture_output=True,
        check=False,
    )
    if completed.returncode:
        fail("unable to verify the committed Git tree")
    return completed.stdout


def committed_entries() -> list[tuple[str, str, str]]:
    raw = git(["ls-tree", "-r", "-z", "--full-tree", "HEAD"])
    entries: list[tuple[str, str, str]] = []
    for record in raw.split(b"\0"):
        if not record:
            continue
        try:
            metadata, encoded_path = record.split(b"\t", 1)
            mode_bytes, kind_bytes, object_bytes = metadata.split(b" ", 2)
            mode = mode_bytes.decode("ascii")
            kind = kind_bytes.decode("ascii")
            object_id = object_bytes.decode("ascii")
            path = encoded_path.decode("utf-8")
        except (UnicodeDecodeError, ValueError) as exc:
            fail("committed Git tree contains an invalid entry")
        if kind != "blob" or mode not in {"100644", "100755"}:
            fail("committed Git tree contains a symlink, submodule, or unsupported mode")
        entries.append((mode, object_id, path))
    return entries


def is_safe_path(path: str) -> bool:
    value = PurePosixPath(path)
    return bool(path) and not value.is_absolute() and all(part not in {"", ".", ".."} for part in value.parts)


def is_allowed(path: str, config: dict) -> bool:
    return path in set(config["allowedFiles"]) or any(
        path.startswith(prefix) for prefix in config["allowedPrefixes"]
    )


def compiled_patterns() -> list[tuple[str, re.Pattern[str]]]:
    local_roots = [
        "/work" + "space/",
        "/ro" + "ot/",
        "/ho" + "me/",
        "/tm" + "p/",
        "/Us" + "ers/",
    ]
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
            re.compile(r"(?:^|[\s\"'`=(])(?:" + "|".join(re.escape(item) for item in local_roots) + r"|[A-Za-z]:\\Users\\)", re.IGNORECASE),
        ),
        ("installed-skill-identifier", re.compile(r"skill" + r"-[0-9a-f]{24,}", re.IGNORECASE)),
        ("email-address", re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE)),
        (
            "private-network-address",
            re.compile(r"(?<![0-9])(?:127\.0\.0\.1|10(?:\.[0-9]{1,3}){3}|192\.168(?:\.[0-9]{1,3}){2}|172\.(?:1[6-9]|2[0-9]|3[01])(?:\.[0-9]{1,3}){2})(?![0-9])"),
        ),
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
    return normalized.startswith(("${", "{{", "<")) or set(normalized) <= {"*", "x", "-", "_"}


def inspect(mode: str, object_id: str, path: str, config: dict) -> set[str]:
    findings: set[str] = set()
    if not is_safe_path(path):
        findings.add("unsafe-path")
    if not is_allowed(path, config):
        findings.add("path-not-allowlisted")
    parts = {part.lower() for part in PurePosixPath(path).parts}
    if any(part.lower() in parts for part in config["forbiddenPathParts"]):
        findings.add("forbidden-path-part")
    suffix = PurePosixPath(path).suffix.lower()
    if suffix in set(config["forbiddenExtensions"]):
        findings.add("forbidden-file-type")
    if path.startswith(config["canonicalSkillPrefix"]):
        if suffix not in set(config["allowedSkillExtensions"]) and PurePosixPath(path).name not in set(
            config["allowedSkillBasenames"]
        ):
            findings.add("skill-file-type-not-allowlisted")

    data = git(["cat-file", "blob", object_id])
    if len(data) > int(config["maxFileBytes"]):
        findings.add("file-too-large")
    if b"\0" in data:
        findings.add("binary-content")
        return findings
    locked = config["lockedFiles"].get(path)
    if locked is not None and hashlib.sha256(data).hexdigest() != locked:
        findings.add("locked-file-modified")
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        findings.add("non-utf8-content")
        return findings
    for line in text.splitlines():
        for label, pattern in compiled_patterns():
            if pattern.search(line):
                findings.add(label)
        assignment = ASSIGNMENT.search(line)
        if assignment and not looks_placeholder(assignment.group(2)):
            findings.add("credential-assignment")
    return findings


def main() -> int:
    config = load_config()
    entries = committed_entries()
    paths = {path for _mode, _object_id, path in entries}
    counts: collections.Counter[str] = collections.Counter()
    for locked_path in config["lockedFiles"]:
        if locked_path not in paths:
            counts["locked-file-missing"] += 1
    for mode, object_id, path in entries:
        for finding in inspect(mode, object_id, path, config):
            counts[finding] += 1
    if counts:
        print("Privacy gate blocked the exact committed tree:", file=sys.stderr)
        for label in sorted(counts):
            print(f"- {label}: {counts[label]}", file=sys.stderr)
        print("Suspected paths and values are intentionally not printed.", file=sys.stderr)
        return 1
    print(f"Privacy gate passed: {len(entries)} regular files in exact HEAD")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"Privacy gate error: {exc}", file=sys.stderr)
        raise SystemExit(1)
