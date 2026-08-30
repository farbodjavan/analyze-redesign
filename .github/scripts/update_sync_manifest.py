#!/usr/bin/env python3
"""Bind the immutable outbound snapshot to downstream plugin packaging."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import date
from pathlib import Path, PurePosixPath


REPO_ROOT = Path(__file__).resolve().parents[2]
SKILL_ROOT = REPO_ROOT / "plugins" / "analyze-redesign" / "skills" / "analyze-redesign"
SNAPSHOT_PATH = SKILL_ROOT / "PUBLIC_SNAPSHOT_MANIFEST.json"
PLUGIN_PATH = REPO_ROOT / "plugins" / "analyze-redesign" / ".codex-plugin" / "plugin.json"
MANIFEST_PATH = REPO_ROOT / "SYNC_MANIFEST.json"
SEMVER = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+$")
SHA256 = re.compile(r"^[0-9a-f]{64}$")


def read_json(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise SystemExit("JSON root must be an object")
    return value


def write_json(path: Path, value: dict) -> None:
    rendered = json.dumps(value, indent=2, ensure_ascii=False) + "\n"
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(rendered, encoding="utf-8")
    temporary.replace(path)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def safe_relative(value: object) -> str:
    if not isinstance(value, str):
        raise SystemExit("snapshot path must be text")
    path = PurePosixPath(value)
    if path.is_absolute() or not value or any(part in {"", ".", ".."} for part in path.parts):
        raise SystemExit("snapshot path is unsafe")
    return path.as_posix()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", default=date.today().isoformat(), dest="sync_date")
    args = parser.parse_args()

    snapshot = read_json(SNAPSHOT_PATH)
    if snapshot.get("syncDirection") != "installed-to-github-only":
        raise SystemExit("snapshot direction is not outbound-only")
    if snapshot.get("repositoryImportAllowed") is not False:
        raise SystemExit("snapshot repository import is not disabled")
    validation = snapshot.get("validation")
    required = {"preExportReleaseGate", "strictSnapshotPrivacy", "snapshotIntegrity"}
    if not isinstance(validation, dict) or any(validation.get(key) != "passed" for key in required):
        raise SystemExit("snapshot validation is incomplete")

    version = (SKILL_ROOT / "VERSION").read_text(encoding="utf-8").strip()
    plugin = read_json(PLUGIN_PATH)
    if not SEMVER.fullmatch(version) or snapshot.get("version") != version or plugin.get("version") != version:
        raise SystemExit("skill, snapshot, and plugin versions must match")

    files: dict[str, dict[str, object]] = {}
    entries = snapshot.get("files")
    if not isinstance(entries, list) or not entries:
        raise SystemExit("snapshot file list is empty")
    for item in entries:
        if not isinstance(item, dict):
            raise SystemExit("snapshot file entry is invalid")
        relative = safe_relative(item.get("path"))
        expected = item.get("sha256")
        if not isinstance(expected, str) or not SHA256.fullmatch(expected):
            raise SystemExit("snapshot digest is invalid")
        path = SKILL_ROOT / relative
        if path.is_symlink() or not path.is_file() or sha256(path) != expected:
            raise SystemExit("canonical file differs from the outbound snapshot")
        mode = "100755" if int(str(item.get("mode")), 8) & 0o111 else "100644"
        files[relative] = {
            "sha256": expected,
            "size": path.stat().st_size,
            "mode": mode,
        }

    generated = "PUBLIC_SNAPSHOT_MANIFEST.json"
    files[generated] = {
        "sha256": sha256(SNAPSHOT_PATH),
        "size": SNAPSHOT_PATH.stat().st_size,
        "mode": "100644",
    }
    actual = {
        path.relative_to(SKILL_ROOT).as_posix()
        for path in SKILL_ROOT.rglob("*")
        if path.is_file()
    }
    if actual != set(files):
        raise SystemExit("canonical file set differs from the outbound snapshot")

    manifest = {
        "schemaVersion": 2,
        "skillName": "analyze-redesign",
        "authority": "installed-personal-skill",
        "syncDirection": "installed-to-github-only",
        "repositoryImportAllowed": False,
        "pluginVersion": version,
        "canonicalPath": "plugins/analyze-redesign/skills/analyze-redesign",
        "sourceSnapshotManifest": "plugins/analyze-redesign/skills/analyze-redesign/PUBLIC_SNAPSHOT_MANIFEST.json",
        "hashAlgorithm": "SHA-256",
        "syncedOn": args.sync_date,
        "evolutionPolicy": "EVOLUTION_POLICY.md",
        "privacyGate": ".github/scripts/privacy_gate.py",
        "files": dict(sorted(files.items())),
    }
    write_json(MANIFEST_PATH, manifest)
    print(f"Bound {len(files)} canonical files to plugin {version}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
