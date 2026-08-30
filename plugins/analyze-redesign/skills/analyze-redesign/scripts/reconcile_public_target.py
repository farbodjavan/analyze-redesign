#!/usr/bin/env python3
"""Reconcile an outbound snapshot against every blob in an exact checked-out Git head."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path, PurePosixPath


SHA256 = re.compile(r"^[0-9a-f]{64}$")
COMMIT_ID = re.compile(r"^[0-9a-fA-F]{40,64}$")
ALLOWED_GIT_MODES = {"100644", "100755"}
MAX_BLOB_BYTES = 10_000_000


def safe_relative(value: object) -> str:
    if not isinstance(value, str):
        raise ValueError("path must be text")
    path = PurePosixPath(value)
    if path.is_absolute() or not value or any(part in {"", ".", ".."} for part in path.parts):
        raise ValueError("path must be normalized and relative")
    return path.as_posix()


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            value.update(chunk)
    return value.hexdigest()


def git_mode(snapshot_mode: object) -> str:
    if not isinstance(snapshot_mode, str) or not re.fullmatch(r"0[0-7]{3}", snapshot_mode):
        raise ValueError("snapshot mode is invalid")
    return "100755" if int(snapshot_mode, 8) & 0o111 else "100644"


def load_json(path: Path, label: str) -> dict:
    if path.is_symlink() or not path.is_file():
        raise ValueError(f"{label} is missing or symlinked")
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"{label} must be an object")
    return data


def run_git(repository: Path, arguments: list[str]) -> bytes:
    completed = subprocess.run(
        ["git", "-C", str(repository), *arguments],
        capture_output=True,
        check=False,
    )
    if completed.returncode:
        raise ValueError("Git object verification failed")
    return completed.stdout


def load_snapshot(snapshot: Path) -> dict[str, tuple[str, str]]:
    manifest_path = snapshot / "PUBLIC_SNAPSHOT_MANIFEST.json"
    manifest = load_json(manifest_path, "snapshot manifest")
    if manifest.get("syncDirection") != "installed-to-github-only":
        raise ValueError("snapshot direction is not outbound-only")
    if manifest.get("repositoryImportAllowed") is not False:
        raise ValueError("snapshot repository import is not disabled")
    validation = manifest.get("validation")
    required = {"preExportReleaseGate", "strictSnapshotPrivacy", "snapshotIntegrity"}
    if not isinstance(validation, dict) or any(validation.get(key) != "passed" for key in required):
        raise ValueError("snapshot validation record is incomplete")
    entries = manifest.get("files")
    if not isinstance(entries, list) or not entries:
        raise ValueError("snapshot file manifest is empty")

    result: dict[str, tuple[str, str]] = {}
    for item in entries:
        if not isinstance(item, dict):
            raise ValueError("snapshot file entry is invalid")
        relative = safe_relative(item.get("path"))
        claimed = item.get("sha256")
        if not isinstance(claimed, str) or not SHA256.fullmatch(claimed):
            raise ValueError("snapshot digest is invalid")
        path = snapshot / relative
        if path.is_symlink() or not path.is_file() or digest(path) != claimed:
            raise ValueError("snapshot content does not match its manifest")
        if relative in result:
            raise ValueError("snapshot contains duplicate paths")
        result[relative] = (claimed, git_mode(item.get("mode")))

    result["PUBLIC_SNAPSHOT_MANIFEST.json"] = (digest(manifest_path), "100644")
    return result


def load_git_head(repository: Path, revision: str) -> dict[str, tuple[str, str]]:
    if not repository.is_dir() or not (repository / ".git").exists():
        raise ValueError("target is not a Git checkout")
    if not COMMIT_ID.fullmatch(revision):
        raise ValueError("revision must be an exact commit identifier")
    resolved = run_git(repository, ["rev-parse", "--verify", revision + "^{commit}"]).decode("ascii").strip()
    head = run_git(repository, ["rev-parse", "--verify", "HEAD^{commit}"]).decode("ascii").strip()
    if resolved.lower() != revision.lower() or head.lower() != resolved.lower():
        raise ValueError("checked-out HEAD does not equal the exact requested revision")

    raw_tree = run_git(repository, ["ls-tree", "-r", "-z", "--full-tree", resolved])
    result: dict[str, tuple[str, str]] = {}
    for raw_entry in raw_tree.split(b"\0"):
        if not raw_entry:
            continue
        try:
            metadata, raw_path = raw_entry.split(b"\t", 1)
            mode_bytes, kind_bytes, object_bytes = metadata.split(b" ", 2)
            mode = mode_bytes.decode("ascii")
            kind = kind_bytes.decode("ascii")
            object_id = object_bytes.decode("ascii")
            relative = safe_relative(raw_path.decode("utf-8"))
        except (UnicodeDecodeError, ValueError) as exc:
            raise ValueError("Git tree contains an invalid entry") from exc
        if kind != "blob" or mode not in ALLOWED_GIT_MODES:
            raise ValueError("Git tree contains a symlink, submodule, or unsupported object mode")
        if relative in result:
            raise ValueError("Git tree contains duplicate normalized paths")
        size_text = run_git(repository, ["cat-file", "-s", object_id]).decode("ascii").strip()
        if not size_text.isdigit() or int(size_text) > MAX_BLOB_BYTES:
            raise ValueError("Git tree contains an oversized or invalid blob")
        content = run_git(repository, ["cat-file", "blob", object_id])
        result[relative] = (hashlib.sha256(content).hexdigest(), mode)
    return result


def load_policy(path: Path) -> tuple[str, dict[str, tuple[str, str]]]:
    policy = load_json(path, "target preservation policy")
    if policy.get("schema_version") != 1:
        raise ValueError("target preservation policy schema is invalid")
    prefix = safe_relative(policy.get("canonical_prefix"))
    entries = policy.get("preserve_files")
    if not isinstance(entries, list):
        raise ValueError("target preservation policy must list exact files")
    preserved: dict[str, tuple[str, str]] = {}
    for item in entries:
        if not isinstance(item, dict):
            raise ValueError("target preservation entry is invalid")
        relative = safe_relative(item.get("path"))
        claimed = item.get("sha256")
        mode = item.get("mode")
        if relative == prefix or relative.startswith(prefix + "/"):
            raise ValueError("preserved files cannot overlap the canonical snapshot")
        if not isinstance(claimed, str) or not SHA256.fullmatch(claimed):
            raise ValueError("preserved file digest is invalid")
        if mode not in ALLOWED_GIT_MODES:
            raise ValueError("preserved file mode is unsupported")
        if relative in preserved:
            raise ValueError("target preservation policy contains duplicate paths")
        preserved[relative] = (claimed, mode)
    return prefix, preserved


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("snapshot")
    parser.add_argument("repository")
    parser.add_argument("revision")
    parser.add_argument("policy")
    args = parser.parse_args()

    try:
        snapshot = Path(args.snapshot).resolve()
        if not snapshot.is_dir():
            raise ValueError("snapshot is not a directory")
        expected_relative = load_snapshot(snapshot)
        target = load_git_head(Path(args.repository).resolve(), args.revision)
        prefix, preserved = load_policy(Path(args.policy).resolve())
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"public target reconciliation failed: {exc}", file=sys.stderr)
        return 2

    expected = {f"{prefix}/{path}": value for path, value in expected_relative.items()}
    canonical = {path: value for path, value in target.items() if path.startswith(prefix + "/")}
    outside = {path: value for path, value in target.items() if not path.startswith(prefix + "/")}

    counts = {
        "canonical_missing": len(set(expected) - set(canonical)),
        "canonical_extra": len(set(canonical) - set(expected)),
        "canonical_changed": len(
            {path for path in set(expected) & set(canonical) if expected[path] != canonical[path]}
        ),
        "outside_unapproved": len(set(outside) - set(preserved)),
        "preserved_missing": len(set(preserved) - set(outside)),
        "preserved_changed": len(
            {path for path in set(preserved) & set(outside) if preserved[path] != outside[path]}
        ),
    }
    if any(counts.values()):
        print("public target reconciliation failed:", file=sys.stderr)
        for label, count in counts.items():
            print(f"- {label}: {count}", file=sys.stderr)
        return 1

    print(
        "public target reconciliation passed: "
        f"{len(canonical)} canonical files, {len(outside)} exact preserved files"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
