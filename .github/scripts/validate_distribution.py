#!/usr/bin/env python3
"""Validate the distributed Analyze & Redesign skill using only Python stdlib."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
PLUGIN_ROOT = REPO_ROOT / "plugins" / "analyze-redesign"
SKILL_ROOT = PLUGIN_ROOT / "skills" / "analyze-redesign"
MANIFEST_PATH = REPO_ROOT / "SYNC_MANIFEST.json"
PLUGIN_MANIFEST_PATH = PLUGIN_ROOT / ".codex-plugin" / "plugin.json"
MARKETPLACE_PATH = REPO_ROOT / ".agents" / "plugins" / "marketplace.json"


def fail(message: str) -> None:
    raise AssertionError(message)


def read_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"{path.relative_to(REPO_ROOT)} is not valid JSON: {exc}")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    manifest = read_json(MANIFEST_PATH)
    if manifest.get("schemaVersion") != 1:
        fail("Unsupported SYNC_MANIFEST.json schemaVersion")
    if manifest.get("skillName") != "analyze-redesign":
        fail("Unexpected skillName in SYNC_MANIFEST.json")
    if manifest.get("canonicalPath") != "plugins/analyze-redesign/skills/analyze-redesign":
        fail("Unexpected canonicalPath in SYNC_MANIFEST.json")
    if manifest.get("hashAlgorithm") != "SHA-256":
        fail("SYNC_MANIFEST.json must use SHA-256")

    expected = manifest.get("files")
    if not isinstance(expected, dict) or not expected:
        fail("SYNC_MANIFEST.json files must be a non-empty object")

    actual_paths = sorted(
        path.relative_to(SKILL_ROOT).as_posix()
        for path in SKILL_ROOT.rglob("*")
        if path.is_file()
    )
    expected_paths = sorted(expected)
    if actual_paths != expected_paths:
        missing = sorted(set(expected_paths) - set(actual_paths))
        extra = sorted(set(actual_paths) - set(expected_paths))
        fail(f"Canonical skill file set differs; missing={missing}, extra={extra}")

    for relative_path, expected_digest in expected.items():
        path = SKILL_ROOT / relative_path
        actual_digest = sha256(path)
        if actual_digest != expected_digest:
            fail(
                f"SHA-256 mismatch for {relative_path}: "
                f"expected {expected_digest}, got {actual_digest}"
            )

    skill_path = SKILL_ROOT / "SKILL.md"
    skill_text = skill_path.read_text(encoding="utf-8")
    if not skill_text.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")
    frontmatter_end = skill_text.find("\n---\n", 4)
    if frontmatter_end < 0:
        fail("SKILL.md frontmatter is not closed")
    frontmatter = skill_text[4:frontmatter_end]

    name_match = re.search(r"^name:\s*(.+?)\s*$", frontmatter, re.MULTILINE)
    description_match = re.search(
        r"^description:\s*(.+?)\s*$", frontmatter, re.MULTILINE
    )
    if not name_match or name_match.group(1).strip("'\"") != "analyze-redesign":
        fail("SKILL.md frontmatter name must be analyze-redesign")
    if not description_match or not description_match.group(1).strip("'\""):
        fail("SKILL.md frontmatter description must be non-empty")

    referenced_files = sorted(
        set(re.findall(r"\breferences/[A-Za-z0-9._/-]+\.md\b", skill_text))
    )
    if not referenced_files:
        fail("SKILL.md must route to reference files")
    for relative_path in referenced_files:
        if not (SKILL_ROOT / relative_path).is_file():
            fail(f"SKILL.md references a missing file: {relative_path}")

    forbidden_markers = (
        "/root/.codex/",
        "BEGIN OPENSSH PRIVATE KEY",
        "BEGIN RSA PRIVATE KEY",
        "github_pat_",
        "ghp_",
    )
    for path in SKILL_ROOT.rglob("*"):
        if not path.is_file():
            continue
        content = path.read_text(encoding="utf-8")
        for marker in forbidden_markers:
            if marker in content:
                fail(f"Forbidden account-specific or secret marker in {path.relative_to(SKILL_ROOT)}")
        if re.search(r"\\bskill-[0-9a-f]{32}\\b", content):
            fail(f"Account-specific skill identifier in {path.relative_to(SKILL_ROOT)}")

    plugin = read_json(PLUGIN_MANIFEST_PATH)
    if plugin.get("name") != "analyze-redesign":
        fail("Plugin manifest name must be analyze-redesign")
    if plugin.get("version") != manifest.get("pluginVersion"):
        fail("Plugin version differs from SYNC_MANIFEST.json")
    if plugin.get("skills") != "./skills/":
        fail("Plugin manifest skills path must be ./skills/")
    interface = plugin.get("interface")
    if not isinstance(interface, dict) or interface.get("displayName") != "Analyze & Redesign":
        fail("Plugin interface metadata is incomplete")
    for icon_field in ("composerIcon", "logo"):
        icon_value = interface.get(icon_field)
        if not isinstance(icon_value, str) or not (PLUGIN_ROOT / icon_value).is_file():
            fail(f"Plugin interface {icon_field} does not resolve to a file")

    marketplace = read_json(MARKETPLACE_PATH)
    entries = marketplace.get("plugins")
    if not isinstance(entries, list):
        fail("Marketplace plugins must be an array")
    matching = [entry for entry in entries if entry.get("name") == "analyze-redesign"]
    if len(matching) != 1:
        fail("Marketplace must contain exactly one analyze-redesign entry")
    entry = matching[0]
    expected_source = {
        "source": "local",
        "path": "./plugins/analyze-redesign",
    }
    if entry.get("source") != expected_source:
        fail("Marketplace source must target ./plugins/analyze-redesign")
    if entry.get("category") != "Productivity":
        fail("Marketplace category must be Productivity")
    policy = entry.get("policy")
    if policy != {
        "installation": "AVAILABLE",
        "authentication": "ON_INSTALL",
    }:
        fail("Marketplace policy is incomplete or unexpected")

    print(
        f"Validated {len(expected_paths)} canonical skill files, "
        f"{len(referenced_files)} routed references, plugin metadata, and marketplace metadata."
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
