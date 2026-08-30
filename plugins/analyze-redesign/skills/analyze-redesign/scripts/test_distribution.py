#!/usr/bin/env python3
"""Exercise fail-closed privacy and exact-target distribution behavior with synthetic data."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path


def digest_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def run(command: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, cwd=cwd, text=True, capture_output=True, check=False)


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    reconcile = root / "scripts" / "reconcile_public_target.py"
    privacy = root / "scripts" / "privacy_gate.py"
    failures: list[str] = []

    with tempfile.TemporaryDirectory(prefix="distribution-self-test-") as temporary:
        base = Path(temporary)
        snapshot = base / "snapshot"
        snapshot.mkdir()
        content = b"public synthetic fixture\n"
        (snapshot / "SKILL.md").write_bytes(content)
        manifest = {
            "schemaVersion": 1,
            "skill": "analyze-redesign",
            "version": "0.0.0",
            "sourceOfTruth": "installed-personal-skill",
            "syncDirection": "installed-to-github-only",
            "repositoryImportAllowed": False,
            "validation": {
                "preExportReleaseGate": "passed",
                "strictSnapshotPrivacy": "passed",
                "snapshotIntegrity": "passed",
            },
            "files": [
                {
                    "path": "SKILL.md",
                    "sha256": digest_bytes(content),
                    "size": len(content),
                    "mode": "0644",
                }
            ],
        }
        manifest_path = snapshot / "PUBLIC_SNAPSHOT_MANIFEST.json"
        write_json(manifest_path, manifest)

        prefix = "plugins/analyze-redesign/skills/analyze-redesign"
        license_content = b"synthetic locked legal fixture\n"
        policy = {
            "schema_version": 1,
            "canonical_prefix": prefix,
            "preserve_files": [
                {
                    "path": "LICENSE",
                    "sha256": digest_bytes(license_content),
                    "mode": "100644",
                }
            ],
        }
        policy_path = base / "policy.json"
        write_json(policy_path, policy)

        repository = base / "repository"
        repository.mkdir()
        target = repository / prefix
        target.mkdir(parents=True)
        (target / "SKILL.md").write_bytes(content)
        (target / "PUBLIC_SNAPSHOT_MANIFEST.json").write_bytes(manifest_path.read_bytes())
        (repository / "LICENSE").write_bytes(license_content)
        if run(["git", "init", "-q"], repository).returncode != 0:
            failures.append("synthetic Git repository could not initialize")
        run(["git", "add", "--all"], repository)
        test_email = "distribution-test" + chr(64) + "example.invalid"
        committed = run(
            [
                "git",
                "-c",
                "user.name=Distribution Test",
                "-c",
                f"user.email={test_email}",
                "commit",
                "-qm",
                "synthetic baseline",
            ],
            repository,
        )
        first_head = run(["git", "rev-parse", "HEAD"], repository).stdout.strip()
        if committed.returncode != 0 or not first_head:
            failures.append("synthetic Git head could not be created")

        positive = run(
            [sys.executable, str(reconcile), str(snapshot), str(repository), first_head, str(policy_path)],
            root,
        )
        if positive.returncode != 0:
            failures.append("exact Git target did not pass")

        extra_name = "unapproved-synthetic-file.txt"
        (repository / extra_name).write_bytes(b"extra\n")
        run(["git", "add", "--all"], repository)
        run(
            [
                "git",
                "-c",
                "user.name=Distribution Test",
                "-c",
                f"user.email={test_email}",
                "commit",
                "-qm",
                "synthetic unexpected file",
            ],
            repository,
        )
        second_head = run(["git", "rev-parse", "HEAD"], repository).stdout.strip()
        negative = run(
            [sys.executable, str(reconcile), str(snapshot), str(repository), second_head, str(policy_path)],
            root,
        )
        negative_output = negative.stdout + negative.stderr
        if negative.returncode != 1 or "outside_unapproved: 1" not in negative_output:
            failures.append("unapproved target file did not fail closed")
        if extra_name in negative_output:
            failures.append("target reconciliation exposed an unapproved path")
        stale_head = run(
            [sys.executable, str(reconcile), str(snapshot), str(repository), first_head, str(policy_path)],
            root,
        )
        if stale_head.returncode != 2 or "exact requested revision" not in (stale_head.stdout + stale_head.stderr):
            failures.append("reconciliation did not bind verification to checked-out HEAD")

        privacy_root = base / "privacy"
        (privacy_root / "config").mkdir(parents=True)
        secret_value = "synthetic-test-value-without-real-credentials"
        (privacy_root / "VERSION").write_text("api" + "_key=" + secret_value + "\n", encoding="utf-8")
        write_json(
            privacy_root / "config" / "public-export.json",
            {
                "sync_direction": "installed-to-github-only",
                "repository_import_allowed": False,
                "files": ["VERSION"],
                "generated_files": [],
            },
        )
        privacy_negative = run([sys.executable, str(privacy), str(privacy_root)], root)
        privacy_output = privacy_negative.stdout + privacy_negative.stderr
        if privacy_negative.returncode != 1 or "credential-assignment" not in privacy_output:
            failures.append("credential assignment did not fail closed")
        if secret_value in privacy_output:
            failures.append("privacy gate exposed a detected value")

    if failures:
        print(f"distribution self-test failed with {len(failures)} issue(s):", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1
    print("distribution self-test passed: privacy redaction and exact target reconciliation")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
