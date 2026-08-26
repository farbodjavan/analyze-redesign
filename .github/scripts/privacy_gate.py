#!/usr/bin/env python3
"""Reject files or content that do not belong in the public skill repository."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = REPO_ROOT / "PUBLIC_SYNC_ALLOWLIST.json"

SECRET_PATTERNS = (
    ("private-key", re.compile(r"-----BEGIN(?: [A-Z0-9]+)? PRIVATE KEY-----")),
    (
        "github-token",
        re.compile(r"(?<![A-Za-z0-9])(?:ghp_|github_pat_)[A-Za-z0-9_]{20,}"),
    ),
    (
        "openai-key",
        re.compile(r"(?<![A-Za-z0-9])sk-(?:proj-)?[A-Za-z0-9_-]{20,}"),
    ),
    ("aws-access-key", re.compile(r"(?<![A-Z0-9])AKIA[0-9A-Z]{16}(?![A-Z0-9])")),
    (
        "slack-token",
        re.compile(r"(?<![A-Za-z0-9])xox[baprs]-[A-Za-z0-9-]{20,}"),
    ),
    (
        "jwt",
        re.compile(
            r"(?<![A-Za-z0-9_-])eyJ[A-Za-z0-9_-]{10,}\."
            r"[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}"
        ),
    ),
    (
        "credentialed-url",
        re.compile(r"https?://[^\s/:]+:[^@\s/]+@[^\s/]+", re.IGNORECASE),
    ),
    (
        "client-secret",
        re.compile(
            r'(?i)["\']?(?:client[_-]?secret|private[_-]?token|access[_-]?token)'
            r'["\']?\s*[:=]\s*["\'][A-Za-z0-9_./+=-]{12,}["\']'
        ),
    ),
)

PII_AND_LOCAL_PATTERNS = (
    (
        "email-address",
        re.compile(
            r"(?i)\b[A-Z0-9.!#$%&'*+/=?^_~-]+@"
            r"[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?"
            r"(?:\.[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?)+\b"
        ),
    ),
    (
        "local-absolute-path",
        re.compile(r"(?:/(?:root|home|Users)/|[A-Za-z]:\\Users\\)"),
    ),
    (
        "private-network-address",
        re.compile(
            r"(?<![0-9])(?:127\.0\.0\.1|10(?:\.[0-9]{1,3}){3}|"
            r"192\.168(?:\.[0-9]{1,3}){2}|"
            r"172\.(?:1[6-9]|2[0-9]|3[01])(?:\.[0-9]{1,3}){2})(?![0-9])"
        ),
    ),
    (
        "account-specific-skill-id",
        re.compile(r"\bskill-[0-9a-f]{32}\b"),
    ),
)


def fail(message: str) -> None:
    raise AssertionError(message)


def load_config() -> dict:
    try:
        config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"PUBLIC_SYNC_ALLOWLIST.json is invalid: {exc}")
    if config.get("schemaVersion") != 1:
        fail("Unsupported PUBLIC_SYNC_ALLOWLIST.json schemaVersion")
    return config


def tracked_entries() -> list[tuple[str, str]]:
    try:
        raw = subprocess.check_output(
            ["git", "ls-files", "-s", "-z"],
            cwd=REPO_ROOT,
        )
    except (OSError, subprocess.CalledProcessError) as exc:
        fail(f"Unable to enumerate tracked files: {exc}")

    entries: list[tuple[str, str]] = []
    for record in raw.split(b"\0"):
        if not record:
            continue
        metadata, encoded_path = record.split(b"\t", 1)
        mode, _object_id, stage = metadata.decode("ascii").split()
        if stage != "0":
            fail("Unmerged index entry detected")
        entries.append((mode, encoded_path.decode("utf-8")))
    return entries


def is_allowed(path: str, config: dict) -> bool:
    if path in set(config["allowedFiles"]):
        return True
    return any(path.startswith(prefix) for prefix in config["allowedPrefixes"])


def inspect_path(mode: str, path: str, config: dict) -> list[str]:
    findings: list[str] = []
    normalized = Path(path).as_posix()

    if normalized != path or path.startswith("/") or ".." in Path(path).parts:
        findings.append("unsafe-path")
    if mode not in {"100644", "100755"}:
        findings.append("unsupported-git-mode")
    if not is_allowed(path, config):
        findings.append("path-not-allowlisted")

    lower_parts = {part.lower() for part in Path(path).parts}
    for part in config["forbiddenPathParts"]:
        if part.lower() in lower_parts:
            findings.append("forbidden-path-part")
            break

    suffix = Path(path).suffix.lower()
    if suffix in set(config["forbiddenExtensions"]):
        findings.append("forbidden-file-type")

    canonical_prefix = config["canonicalSkillPrefix"]
    if path.startswith(canonical_prefix):
        if suffix not in set(config["allowedSkillExtensions"]):
            findings.append("skill-file-type-not-allowlisted")

    absolute = REPO_ROOT / path
    try:
        data = absolute.read_bytes()
    except OSError:
        findings.append("unreadable-file")
        return findings

    if len(data) > int(config["maxFileBytes"]):
        findings.append("file-too-large")
    if b"\0" in data:
        findings.append("binary-content")
        return findings

    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        findings.append("non-utf8-content")
        return findings

    for label, pattern in SECRET_PATTERNS + PII_AND_LOCAL_PATTERNS:
        if pattern.search(text):
            findings.append(label)

    return sorted(set(findings))


def main() -> int:
    config = load_config()
    failures: list[tuple[str, str]] = []

    for mode, path in tracked_entries():
        for rule in inspect_path(mode, path, config):
            failures.append((path, rule))

    if failures:
        for path, rule in failures:
            print(f"BLOCKED: {path} [{rule}]", file=sys.stderr)
        print(
            f"Privacy gate rejected {len(failures)} finding(s); "
            "suspected values are intentionally not printed.",
            file=sys.stderr,
        )
        return 1

    print("Privacy gate passed: tracked paths and UTF-8 content are public-safe by policy.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
