#!/usr/bin/env python3
"""Validate the behavioral forward-test corpus and its reference routing."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


REQUIRED_DOMAINS = {
    "authorization",
    "baseline",
    "staged-review",
    "game",
    "enterprise",
    "rtl",
    "accessibility",
    "implementation",
    "privacy",
    "evidence-honesty",
    "current-sources",
}

REQUIRED_SAFETY_SCENARIOS = {
    "audit-no-mutation",
    "deep-pass-phase-cap",
    "game-story-regression",
    "staged-visual-owner-gate",
    "enterprise-capability-preservation",
    "progressive-disclosure-preservation",
    "forensic-baseline-conflict",
    "dirty-worktree-implementation",
    "screenshot-evidence-limit",
    "accessibility-not-certification",
    "one-way-public-evolution",
    "public-target-exact-tree",
    "public-history-privacy-incident",
    "three-d-concept-boundary",
    "qa-no-unrun-pass",
}


def nonempty_strings(value: object, minimum: int) -> bool:
    return (
        isinstance(value, list)
        and len(value) >= minimum
        and all(isinstance(item, str) and item.strip() for item in value)
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    corpus_path = root / "evals" / "behavior-scenarios.json"
    try:
        corpus = json.loads(corpus_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"eval validation failed: {exc}", file=sys.stderr)
        return 2

    scenarios = corpus.get("scenarios")
    failures: list[str] = []
    if corpus.get("schema_version") != 1:
        failures.append("schema_version must be 1")
    if not isinstance(scenarios, list) or len(scenarios) < 12:
        failures.append("at least 12 behavioral scenarios are required")
        scenarios = []

    ids: set[str] = set()
    domains: set[str] = set()
    for index, scenario in enumerate(scenarios):
        prefix = f"scenario[{index}]"
        if not isinstance(scenario, dict):
            failures.append(f"{prefix} must be an object")
            continue
        scenario_id = scenario.get("id")
        if not isinstance(scenario_id, str) or not scenario_id.strip():
            failures.append(f"{prefix} has no id")
        elif scenario_id in ids:
            failures.append(f"duplicate id: {scenario_id}")
        else:
            ids.add(scenario_id)
        domain = scenario.get("domain")
        if isinstance(domain, str):
            domains.add(domain)
        else:
            failures.append(f"{prefix} has no domain")
        if not isinstance(scenario.get("prompt"), str) or not scenario["prompt"].strip():
            failures.append(f"{prefix} has no prompt")
        if not nonempty_strings(scenario.get("expected_invariants"), 2):
            failures.append(f"{prefix} needs at least two expected invariants")
        if not nonempty_strings(scenario.get("forbidden_outcomes"), 1):
            failures.append(f"{prefix} needs at least one forbidden outcome")
        references = scenario.get("required_references")
        if not nonempty_strings(references, 1):
            failures.append(f"{prefix} needs required references")
        else:
            for reference in references:
                if "/" in reference or "\\" in reference:
                    failures.append(f"{prefix} reference must be a filename: {reference}")
                elif not (root / "references" / reference).is_file():
                    failures.append(f"{prefix} missing reference: {reference}")

    missing_domains = sorted(REQUIRED_DOMAINS - domains)
    if missing_domains:
        failures.append("missing required domains: " + ", ".join(missing_domains))
    missing_scenarios = sorted(REQUIRED_SAFETY_SCENARIOS - ids)
    if missing_scenarios:
        failures.append("missing safety-critical scenarios: " + ", ".join(missing_scenarios))

    version_path = root / "VERSION"
    try:
        version = version_path.read_text(encoding="utf-8").strip()
    except OSError:
        version = ""
    if corpus.get("skill_version") != version:
        failures.append("corpus skill_version does not match VERSION")

    if failures:
        print(f"eval validation failed with {len(failures)} issue(s):", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print(f"eval validation passed: {len(scenarios)} scenarios across {len(domains)} domains")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
