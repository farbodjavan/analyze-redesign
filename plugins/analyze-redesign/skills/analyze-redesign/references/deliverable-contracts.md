# Deliverable Contracts

Choose the smallest contract that satisfies the request. Combine contracts for end-to-end work.

## Contents

- Quick audit
- Deep audit
- Redesign specification
- Visual package
- Implemented redesign
- QA evidence package
- Continuation master

## Quick audit

Include:

1. One-paragraph diagnosis
2. The three to seven highest-impact findings with evidence
3. The recommended direction
4. Immediate next actions
5. Important unknowns or blockers

## Deep audit

Include:

1. Objective, users, scope, baseline, and inspected evidence
2. Active council lenses, activation rationale, source ledger, and evidence gaps
3. Product/role/route and journey inventory
4. Surface-by-state coverage matrix with explicit denominator and untested areas
5. Prioritized finding ledger using the evaluation framework
6. Root-cause clusters, dissent notes, strengths, and preserve locks
7. Accessibility, responsive, localization, trust, privacy, performance, and domain findings where applicable
8. Recommended direction, meaningful alternatives, tradeoffs, and repair sequence with dependencies
9. Acceptance criteria, research/measurement plan, and verification matrix

## Redesign specification

Include:

1. Design thesis and success definition
2. Evidence, assumptions, research questions, goals/signals/metrics, and guardrails
3. Revised service model, object model, information architecture, and navigation
4. Primary, exception, failure, recovery, cancellation, and return journeys
5. Screen-by-screen hierarchy, actions, content, permissions, and state contract
6. Art direction, component architecture, and design-token specification
7. Responsive, adaptive, platform, localization, and RTL/LTR behavior
8. Motion, feedback, latency, loading, empty, error, success, offline, stale, and conflict behavior
9. Accessibility, privacy, safety, trust, and content rules
10. Implementation phases, dependencies, migration, risks, acceptance criteria, and verification

Use exact labels and mappings. Provide recommended copy when wording is part of the problem.

## Visual package

Include only visuals that help review or implementation:

- annotated current-state evidence
- IA or journey diagrams
- low-fidelity wireframes for structural decisions
- high-fidelity key screens after structure is settled
- before/after comparisons
- component/state sheet
- representative desktop, mobile, tablet, or landscape states
- asset manifest naming every file and its purpose

Do not present a generated image as a functional build. Do not use mood art for exact interface measurements.

## Implemented redesign

Include:

1. Exact baseline and scope changed
2. Files or systems changed
3. Preserved locks and unrelated areas left untouched
4. Build, lint, type, unit, integration, visual, accessibility, and journey checks actually run
5. Responsive, platform, locale, RTL, theme, role, and input-mode coverage actually exercised
6. Reproducible screenshots, recordings, logs, traces, or reports for affected states
7. Performance and telemetry checks when relevant
8. Deviations, known gaps, remaining risks, and rollback notes
9. Run or review instructions

Never label unrun tests as passed.

## QA evidence package

For each test, record:

| Field | Requirement |
|---|---|
| Test ID | Stable identifier |
| Build | Commit, version, checksum, or URL |
| Context | Device/viewport, role, locale, route, and state |
| Steps | Reproducible sequence |
| Expected | Observable acceptance condition |
| Actual | Observed result |
| Status | Pass, fail, blocked, or not tested |
| Evidence | Screenshot, recording, log, or test output |

Cover changed surfaces plus adjacent regression risks. State evidence gaps plainly.

## Continuation master

Make a continuation master self-contained and unambiguous. Include:

1. Goal and non-goals
2. Exact source of truth: files, version, branch, commit, build, URL, checksum, and date as available
3. Authority and action boundaries
4. Approved and locked decisions
5. Completed work with evidence
6. Current state and reproducible blockers
7. Remaining work in dependency order
8. Prohibited regressions and no-go areas
9. Acceptance gates and required evidence
10. Deliverable paths and run/review instructions
11. The first exact action for the next session

Do not carry stale facts forward. Mark anything unverified, inferred, or pending.
