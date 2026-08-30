#!/usr/bin/env python3
"""Create a deterministic, allowlisted outbound snapshot from the installed skill."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path, PurePosixPath


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            value.update(chunk)
    return value.hexdigest()


def safe_relative(value: str) -> str:
    path = PurePosixPath(value)
    if path.is_absolute() or not value or any(part in {"", ".", ".."} for part in path.parts):
        raise ValueError("unsafe export path")
    return path.as_posix()


def run(command: list[str], cwd: Path) -> None:
    completed = subprocess.run(command, cwd=cwd, text=True, capture_output=True, check=False)
    if completed.returncode:
        message = (completed.stdout + completed.stderr).strip()
        raise RuntimeError(message or "validation command failed")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source")
    parser.add_argument("destination")
    args = parser.parse_args()

    source = Path(args.source).resolve()
    destination = Path(args.destination).resolve()
    if not source.is_dir():
        print("snapshot failed: source is not a directory", file=sys.stderr)
        return 2
    if destination.exists():
        print("snapshot failed: destination must not already exist", file=sys.stderr)
        return 2
    try:
        destination.relative_to(source)
    except ValueError:
        pass
    else:
        print("snapshot failed: destination cannot be inside the source skill", file=sys.stderr)
        return 2
    if not destination.parent.is_dir():
        print("snapshot failed: destination parent does not exist", file=sys.stderr)
        return 2

    created = False
    try:
        config = json.loads((source / "config" / "public-export.json").read_text(encoding="utf-8"))
        if config.get("sync_direction") != "installed-to-github-only":
            raise ValueError("outbound-only sync invariant is missing")
        if config.get("repository_import_allowed") is not False:
            raise ValueError("repository import is not disabled")
        files = [safe_relative(item) for item in config["files"]]
        if len(files) != len(set(files)):
            raise ValueError("duplicate export path")

        run([sys.executable, "scripts/validate_skill.py", str(source), "--release"], source)
        destination.mkdir()
        created = True
        manifest_files: list[dict[str, object]] = []
        for relative in files:
            origin = source / relative
            if origin.is_symlink() or not origin.is_file():
                raise ValueError(f"allowlisted source is missing or symlinked: {relative}")
            target = destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(origin, target)
            mode = origin.stat().st_mode & 0o777
            os.chmod(target, mode)
            manifest_files.append(
                {
                    "path": relative,
                    "sha256": digest(target),
                    "size": target.stat().st_size,
                    "mode": format(mode, "04o"),
                }
            )

        version = (source / "VERSION").read_text(encoding="utf-8").strip()
        manifest = {
            "schemaVersion": 1,
            "skill": "analyze-redesign",
            "version": version,
            "sourceOfTruth": "installed-personal-skill",
            "syncDirection": "installed-to-github-only",
            "repositoryImportAllowed": False,
            "validation": {
                "preExportReleaseGate": "passed",
                "strictSnapshotPrivacy": "pending",
                "snapshotIntegrity": "pending",
            },
            "files": sorted(manifest_files, key=lambda item: str(item["path"])),
        }
        manifest_path = destination / "PUBLIC_SNAPSHOT_MANIFEST.json"
        manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

        run(
            [
                sys.executable,
                str(source / "scripts" / "privacy_gate.py"),
                str(destination),
                "--strict-tree",
            ],
            source,
        )
        manifest["validation"]["strictSnapshotPrivacy"] = "passed"
        for item in manifest_files:
            relative = str(item["path"])
            target = destination / relative
            if digest(target) != item["sha256"]:
                raise RuntimeError("snapshot integrity changed after copy")
            if target.stat().st_size != item["size"]:
                raise RuntimeError("snapshot size changed after copy")
            if format(target.stat().st_mode & 0o777, "04o") != item["mode"]:
                raise RuntimeError("snapshot mode changed after copy")
        manifest["validation"]["snapshotIntegrity"] = "passed"
        manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        run(
            [
                sys.executable,
                str(source / "scripts" / "privacy_gate.py"),
                str(destination),
                "--strict-tree",
            ],
            source,
        )
    except (OSError, KeyError, ValueError, json.JSONDecodeError, RuntimeError) as exc:
        if created and destination.is_dir():
            shutil.rmtree(destination)
        print(f"snapshot failed: {exc}", file=sys.stderr)
        return 1

    print(f"public snapshot created: {len(manifest_files)} files, version {version}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
