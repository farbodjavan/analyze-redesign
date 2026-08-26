#!/usr/bin/env python3
"""Regenerate canonical skill hashes and optionally bump the plugin version."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import date
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
SKILL_ROOT = REPO_ROOT / "plugins" / "analyze-redesign" / "skills" / "analyze-redesign"
PLUGIN_PATH = REPO_ROOT / "plugins" / "analyze-redesign" / ".codex-plugin" / "plugin.json"
MANIFEST_PATH = REPO_ROOT / "SYNC_MANIFEST.json"
SEMVER = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+$")


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: dict) -> None:
    rendered = json.dumps(value, indent=2, ensure_ascii=False) + "\n"
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(rendered, encoding="utf-8")
    temporary.replace(path)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", help="New semantic plugin version")
    parser.add_argument("--date", default=date.today().isoformat(), dest="sync_date")
    args = parser.parse_args()

    plugin = read_json(PLUGIN_PATH)
    if args.version:
        if not SEMVER.fullmatch(args.version):
            parser.error("--version must use MAJOR.MINOR.PATCH")
        plugin["version"] = args.version
        write_json(PLUGIN_PATH, plugin)

    version = plugin.get("version")
    if not isinstance(version, str) or not SEMVER.fullmatch(version):
        raise SystemExit("plugin.json contains an invalid version")

    files = {
        path.relative_to(SKILL_ROOT).as_posix(): sha256(path)
        for path in sorted(SKILL_ROOT.rglob("*"))
        if path.is_file()
    }
    if "SKILL.md" not in files:
        raise SystemExit("Canonical SKILL.md is missing")

    manifest = {
        "schemaVersion": 1,
        "skillName": "analyze-redesign",
        "pluginVersion": version,
        "canonicalPath": "plugins/analyze-redesign/skills/analyze-redesign",
        "hashAlgorithm": "SHA-256",
        "syncedOn": args.sync_date,
        "evolutionPolicy": "EVOLUTION_POLICY.md",
        "privacyGate": ".github/scripts/privacy_gate.py",
        "files": files,
    }
    write_json(MANIFEST_PATH, manifest)
    print(f"Updated {len(files)} canonical hashes for plugin {version}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
