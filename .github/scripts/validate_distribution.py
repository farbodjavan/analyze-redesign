#!/usr/bin/env python3
"""Validate the exact public snapshot, plugin package, and one-way governance."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
PLUGIN_ROOT = REPO_ROOT / "plugins" / "analyze-redesign"
SKILL_ROOT = PLUGIN_ROOT / "skills" / "analyze-redesign"
SNAPSHOT_PATH = SKILL_ROOT / "PUBLIC_SNAPSHOT_MANIFEST.json"
SYNC_PATH = REPO_ROOT / "SYNC_MANIFEST.json"
PLUGIN_PATH = PLUGIN_ROOT / ".codex-plugin" / "plugin.json"
MARKETPLACE_PATH = REPO_ROOT / ".agents" / "plugins" / "marketplace.json"
ALLOWLIST_PATH = REPO_ROOT / "PUBLIC_SYNC_ALLOWLIST.json"
LICENSE_PATH = REPO_ROOT / "LICENSE"
LICENSE_ID = "LicenseRef-Analyze-Redesign-No-Derivatives-1.0"
LICENSE_SHA256 = "32d09f539a12996735c5723ad7c733584b91af86a8d9f0209931e6d150425ba4"
SEMVER = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+$")


def fail(message: str) -> None:
    raise AssertionError(message)


def read_json(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"required JSON is invalid: {exc}")
    if not isinstance(value, dict):
        fail("required JSON root must be an object")
    return value


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(command: list[str]) -> str:
    completed = subprocess.run(command, cwd=REPO_ROOT, text=True, capture_output=True, check=False)
    output = (completed.stdout + completed.stderr).strip()
    if completed.returncode:
        fail(output or "bundled validation command failed")
    return output


def git_paths() -> set[str]:
    completed = subprocess.run(
        ["git", "ls-tree", "-r", "-z", "--name-only", "HEAD"],
        cwd=REPO_ROOT,
        capture_output=True,
        check=False,
    )
    if completed.returncode:
        fail("unable to enumerate exact Git head")
    try:
        return {item.decode("utf-8") for item in completed.stdout.split(b"\0") if item}
    except UnicodeDecodeError:
        fail("Git head contains a non-UTF-8 path")
    return set()


def main() -> int:
    allowlist = read_json(ALLOWLIST_PATH)
    prefix = allowlist.get("canonicalSkillPrefix")
    if prefix != "plugins/analyze-redesign/skills/analyze-redesign/":
        fail("canonical skill prefix is unexpected")
    allowed_files = allowlist.get("allowedFiles")
    if not isinstance(allowed_files, list) or len(allowed_files) != len(set(allowed_files)):
        fail("outside-file allowlist is invalid")
    committed = git_paths()
    outside = {path for path in committed if not path.startswith(prefix)}
    if outside != set(allowed_files):
        fail(
            "exact outside file set differs from policy; "
            f"missing_count={len(set(allowed_files) - outside)}, extra_count={len(outside - set(allowed_files))}"
        )

    snapshot = read_json(SNAPSHOT_PATH)
    if snapshot.get("skill") != "analyze-redesign":
        fail("snapshot skill name is unexpected")
    if snapshot.get("sourceOfTruth") != "installed-personal-skill":
        fail("snapshot source of truth is not the personal skill")
    if snapshot.get("syncDirection") != "installed-to-github-only":
        fail("snapshot direction is not outbound-only")
    if snapshot.get("repositoryImportAllowed") is not False:
        fail("snapshot repository import is not disabled")
    validation = snapshot.get("validation")
    required_snapshot_gates = {"preExportReleaseGate", "strictSnapshotPrivacy", "snapshotIntegrity"}
    if not isinstance(validation, dict) or any(validation.get(key) != "passed" for key in required_snapshot_gates):
        fail("snapshot validation record is incomplete")

    sync = read_json(SYNC_PATH)
    if sync.get("schemaVersion") != 2:
        fail("unsupported sync manifest schema")
    invariants = {
        "skillName": "analyze-redesign",
        "authority": "installed-personal-skill",
        "syncDirection": "installed-to-github-only",
        "repositoryImportAllowed": False,
        "canonicalPath": "plugins/analyze-redesign/skills/analyze-redesign",
        "sourceSnapshotManifest": "plugins/analyze-redesign/skills/analyze-redesign/PUBLIC_SNAPSHOT_MANIFEST.json",
        "hashAlgorithm": "SHA-256",
        "evolutionPolicy": "EVOLUTION_POLICY.md",
        "privacyGate": ".github/scripts/privacy_gate.py",
    }
    for key, expected in invariants.items():
        if sync.get(key) != expected:
            fail("sync manifest one-way invariant is invalid")
    expected_files = sync.get("files")
    if not isinstance(expected_files, dict) or not expected_files:
        fail("sync manifest file map is empty")
    actual_files = {
        path.relative_to(SKILL_ROOT).as_posix()
        for path in SKILL_ROOT.rglob("*")
        if path.is_file()
    }
    if actual_files != set(expected_files):
        fail(
            "canonical file set differs from sync manifest; "
            f"missing_count={len(set(expected_files) - actual_files)}, extra_count={len(actual_files - set(expected_files))}"
        )
    for relative, record in expected_files.items():
        if not isinstance(record, dict):
            fail("sync manifest file record is invalid")
        path = SKILL_ROOT / relative
        expected_mode = "100755" if path.stat().st_mode & 0o111 else "100644"
        if (
            sha256(path) != record.get("sha256")
            or path.stat().st_size != record.get("size")
            or expected_mode != record.get("mode")
        ):
            fail("canonical file hash, size, or mode differs from sync manifest")

    snapshot_entries = snapshot.get("files")
    if not isinstance(snapshot_entries, list):
        fail("snapshot file list is invalid")
    snapshot_paths: set[str] = set()
    for item in snapshot_entries:
        if not isinstance(item, dict) or not isinstance(item.get("path"), str):
            fail("snapshot file entry is invalid")
        relative = item["path"]
        snapshot_paths.add(relative)
        bound = expected_files.get(relative)
        expected_mode = "100755" if int(str(item.get("mode")), 8) & 0o111 else "100644"
        if not isinstance(bound, dict) or (
            bound.get("sha256") != item.get("sha256")
            or bound.get("size") != item.get("size")
            or bound.get("mode") != expected_mode
        ):
            fail("sync manifest does not bind the exact source snapshot")
    if snapshot_paths | {"PUBLIC_SNAPSHOT_MANIFEST.json"} != set(expected_files):
        fail("snapshot and sync-manifest file sets differ")

    version = (SKILL_ROOT / "VERSION").read_text(encoding="utf-8").strip()
    plugin = read_json(PLUGIN_PATH)
    if not SEMVER.fullmatch(version):
        fail("canonical version is not semantic")
    if snapshot.get("version") != version or sync.get("pluginVersion") != version or plugin.get("version") != version:
        fail("canonical, snapshot, sync, and plugin versions differ")
    if plugin.get("name") != "analyze-redesign" or plugin.get("skills") != "./skills/":
        fail("plugin manifest identity or skill path is invalid")
    if plugin.get("license") != LICENSE_ID:
        fail("plugin license identifier is invalid")
    interface = plugin.get("interface")
    if not isinstance(interface, dict) or interface.get("displayName") != "Analyze & Redesign":
        fail("plugin interface metadata is incomplete")
    for field in ("composerIcon", "logo"):
        value = interface.get(field)
        if not isinstance(value, str) or not (PLUGIN_ROOT / value).resolve().is_file():
            fail("plugin icon path is invalid")

    marketplace = read_json(MARKETPLACE_PATH)
    entries = marketplace.get("plugins")
    matching = [entry for entry in entries if isinstance(entry, dict) and entry.get("name") == "analyze-redesign"] if isinstance(entries, list) else []
    if len(matching) != 1 or matching[0].get("source") != {
        "source": "local",
        "path": "./plugins/analyze-redesign",
    }:
        fail("marketplace plugin routing is invalid")

    if sha256(LICENSE_PATH) != LICENSE_SHA256:
        fail("owner-approved license changed")
    if allowlist.get("lockedFiles", {}).get("LICENSE") != LICENSE_SHA256:
        fail("public policy does not lock the owner-approved license")

    release_output = run([sys.executable, str(SKILL_ROOT / "scripts" / "validate_skill.py"), str(SKILL_ROOT), "--release"])
    strict_privacy_output = run(
        [sys.executable, str(SKILL_ROOT / "scripts" / "privacy_gate.py"), str(SKILL_ROOT), "--strict-tree"]
    )
    print(release_output)
    print(strict_privacy_output)
    print(
        f"Validated public distribution {version}: {len(expected_files)} canonical files, "
        f"{len(outside)} exact outside files, immutable license, and outbound-only authority."
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"Distribution validation failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
