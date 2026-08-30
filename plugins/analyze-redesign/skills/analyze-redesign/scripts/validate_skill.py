#!/usr/bin/env python3
"""Validate structural, routing, privacy, and evaluation invariants for the skill."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import stat
import subprocess
import sys
from pathlib import Path, PurePosixPath


LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
URL = re.compile(r"https://[^\s)>\]]+")
SEMVER = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+$")


def run_check(command: list[str], root: Path) -> tuple[bool, str]:
    completed = subprocess.run(command, cwd=root, text=True, capture_output=True, check=False)
    output = (completed.stdout + completed.stderr).strip()
    return completed.returncode == 0, output


def normalized_relative(value: str) -> bool:
    path = PurePosixPath(value)
    return bool(value) and not path.is_absolute() and all(part not in {"", ".", ".."} for part in path.parts)


def attestation_issues(
    name: str, value: object, root: Path, public_files: set[str]
) -> list[str]:
    issues: list[str] = []
    if not isinstance(value, dict):
        return [f"{name} attestation must be a structured record"]
    if value.get("status") != "passed":
        issues.append(f"{name} attestation is not passed")
    if not isinstance(value.get("reviewer_role"), str) or not value["reviewer_role"].strip():
        issues.append(f"{name} attestation needs a reviewer role")
    recorded = value.get("recorded")
    try:
        recorded_date = dt.date.fromisoformat(recorded) if isinstance(recorded, str) else None
    except ValueError:
        recorded_date = None
    if recorded_date is None or recorded_date > dt.date.today():
        issues.append(f"{name} attestation has an invalid recorded date")
    if not isinstance(value.get("method"), str) or len(value["method"].strip()) < 20:
        issues.append(f"{name} attestation needs a concrete method")
    coverage = value.get("coverage")
    if not isinstance(coverage, list) or len(coverage) < 3 or not all(
        isinstance(item, str) and item.strip() for item in coverage
    ):
        issues.append(f"{name} attestation needs at least three coverage records")
    evidence = value.get("evidence")
    if not isinstance(evidence, list) or not evidence:
        issues.append(f"{name} attestation needs public evidence paths")
    else:
        for item in evidence:
            if not isinstance(item, str) or not normalized_relative(item):
                issues.append(f"{name} attestation contains an unsafe evidence path")
                continue
            if item not in public_files or not (root / item).is_file():
                issues.append(f"{name} attestation evidence is not allowlisted and present")
    return issues


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    parser.add_argument("--quick-validator", default="")
    parser.add_argument("--release", action="store_true")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    failures: list[str] = []

    skill_path = root / "SKILL.md"
    try:
        skill_text = skill_path.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"skill validation failed: {exc}", file=sys.stderr)
        return 2

    if not skill_text.startswith("---\n") or "\n---\n" not in skill_text[4:]:
        failures.append("SKILL.md frontmatter is missing or malformed")
        frontmatter = ""
    else:
        frontmatter = skill_text.split("---\n", 2)[1]
    if not re.search(r"(?m)^name:\s*analyze-redesign\s*$", frontmatter):
        failures.append("frontmatter name must be analyze-redesign")
    description = re.search(r"(?m)^description:\s*(.+)$", frontmatter)
    if not description or len(description.group(1).strip()) < 80:
        failures.append("frontmatter description is missing or not discriminating")

    try:
        version = (root / "VERSION").read_text(encoding="utf-8").strip()
    except OSError:
        version = ""
    if not SEMVER.fullmatch(version):
        failures.append("VERSION must be semantic major.minor.patch")
    metadata_version = re.search(r"(?m)^\s+version:\s*[\"']?([^\"'\s]+)", frontmatter)
    if not metadata_version or metadata_version.group(1) != version:
        failures.append("frontmatter metadata.version must match VERSION")

    required_ui = ["display_name:", "short_description:", "default_prompt:", "allow_implicit_invocation: true"]
    try:
        ui_text = (root / "agents" / "openai.yaml").read_text(encoding="utf-8")
    except OSError:
        ui_text = ""
    for marker in required_ui:
        if marker not in ui_text:
            failures.append(f"agents/openai.yaml missing {marker}")

    markdown_files = [skill_path] + sorted((root / "references").glob("*.md"))
    for markdown in markdown_files:
        try:
            text = markdown.read_text(encoding="utf-8")
        except OSError as exc:
            failures.append(f"cannot read {markdown.relative_to(root)}: {exc}")
            continue
        for raw_target in LINK.findall(text):
            target = raw_target.split("#", 1)[0].strip()
            if not target or target.startswith(("https://", "http://", "mailto:")):
                continue
            candidate = (markdown.parent / target).resolve()
            try:
                candidate.relative_to(root)
            except ValueError:
                failures.append(f"link escapes skill root: {markdown.relative_to(root)} -> {target}")
                continue
            if not candidate.exists():
                failures.append(f"broken local link: {markdown.relative_to(root)} -> {target}")

    try:
        export = json.loads((root / "config" / "public-export.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        failures.append(f"invalid public export configuration: {exc}")
        export = {"files": []}
    public_files = export.get("files", [])
    if not isinstance(public_files, list) or len(public_files) != len(set(public_files)):
        failures.append("public export allowlist is missing or has duplicates")
        public_files = []
    for relative in public_files:
        if not isinstance(relative, str) or not normalized_relative(relative):
            failures.append("public export contains an unsafe path")
            continue
        path = root / relative
        if path.is_symlink() or not path.is_file():
            failures.append(f"allowlisted path missing or symlinked: {relative}")

    registry_path = root / "references" / "source-registry.md"
    try:
        registry_text = registry_path.read_text(encoding="utf-8")
    except OSError:
        registry_text = ""
    urls = [item.rstrip(".,") for item in URL.findall(registry_text)]
    if len(set(urls)) < 50:
        failures.append("source registry has insufficient authoritative-source coverage")
    duplicate_urls = sorted({item for item in urls if urls.count(item) > 1})
    if duplicate_urls:
        failures.append(f"source registry contains {len(duplicate_urls)} duplicate URL(s)")

    try:
        provenance = json.loads((root / "config" / "public-provenance.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        failures.append(f"invalid public provenance: {exc}")
        provenance = {"releases": []}
    releases = provenance.get("releases", [])
    current = [item for item in releases if isinstance(item, dict) and item.get("version") == version]
    if len(current) != 1:
        failures.append("public provenance must contain exactly one current-version release")
    else:
        release = current[0]
        if not isinstance(release.get("capabilities"), list) or not release["capabilities"]:
            failures.append("current provenance release needs capability records")
        sources = release.get("sources")
        if not isinstance(sources, list) or not sources:
            failures.append("current provenance release needs public sources")
        else:
            registry_urls = set(urls)
            for source in sources:
                if not isinstance(source, dict):
                    failures.append("provenance source must be an object")
                    continue
                source_url = source.get("url")
                if source_url not in registry_urls:
                    failures.append("provenance source URL is not registered in source-registry.md")
                if not source.get("publisher") or not source.get("title") or not source.get("accessed"):
                    failures.append("provenance source is missing publisher, title, or access date")
        validation = release.get("validation", {})
        if args.release:
            required_results = {
                "source_state",
                "privacy_gate",
                "structural_validation",
                "eval_schema",
                "pre_export",
            }
            if any(validation.get(key) != "passed" for key in required_results):
                failures.append("pre-export release validation record is not fully passed")
            failures.extend(
                attestation_issues(
                    "behavioral_forward_test",
                    validation.get("behavioral_forward_test"),
                    root,
                    set(public_files),
                )
            )
            failures.extend(
                attestation_issues(
                    "semantic_provenance_review",
                    validation.get("semantic_provenance_review"),
                    root,
                    set(public_files),
                )
            )

    for script_name in [
        "privacy_gate.py",
        "validate_evals.py",
        "validate_skill.py",
        "build_public_snapshot.py",
        "reconcile_public_target.py",
        "test_distribution.py",
    ]:
        script = root / "scripts" / script_name
        if not script.is_file():
            failures.append(f"missing script: {script_name}")
        elif not (script.stat().st_mode & stat.S_IXUSR):
            failures.append(f"script is not owner-executable: {script_name}")

    eval_ok, eval_output = run_check([sys.executable, "scripts/validate_evals.py", str(root)], root)
    if not eval_ok:
        failures.append("behavioral eval validation failed: " + eval_output)
    privacy_ok, privacy_output = run_check([sys.executable, "scripts/privacy_gate.py", str(root)], root)
    if not privacy_ok:
        failures.append("privacy gate failed: " + privacy_output)
    distribution_ok, distribution_output = run_check(
        [sys.executable, "scripts/test_distribution.py"], root
    )
    if not distribution_ok:
        failures.append("distribution self-test failed: " + distribution_output)

    if args.quick_validator:
        quick = Path(args.quick_validator)
        if not quick.is_file():
            failures.append("requested quick validator does not exist")
        else:
            quick_ok, quick_output = run_check([sys.executable, str(quick), str(root)], root)
            if not quick_ok:
                failures.append("platform quick validator failed: " + quick_output)

    if failures:
        print(f"skill validation failed with {len(failures)} issue(s):", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print(
        "skill validation passed: "
        f"version {version}, {len(markdown_files) - 1} references, "
        f"{len(set(urls))} registered source URLs, {len(public_files)} public files"
    )
    print(eval_output)
    print(privacy_output)
    print(distribution_output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
