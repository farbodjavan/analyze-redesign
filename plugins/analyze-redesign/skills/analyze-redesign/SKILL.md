---
name: analyze-redesign
description: Evidence-led product experience analysis, redesign, visual prototyping, implementation guidance, recovery, and design QA for websites, apps, games, dashboards, enterprise workflows, AI products, and design systems. Use for UX/UI audits, story-to-screen redesigns, journey or information-architecture repair, visual-system work, responsive/RTL/accessibility review, design-to-code fidelity, baseline recovery, owner-review packages, and continuation masters. Do not use as proof of real user research, legal compliance, production verification, or independent expert participation unless that evidence actually exists.
metadata:
  version: "2.0.0"
---

# Analyze and Redesign

## Mission

Turn a weak, drifting, incomplete, or inconsistent digital experience into one coherent product direction that is evidence-backed, visually reviewable, implementation-ready, and testable. Operate as a virtual multidisciplinary design organization: apply relevant specialist lenses in separate passes to the same evidence, adjudicate conflicts, preserve approved work, and maintain traceability from intent through verified result.

The virtual council is a structured analysis by the active agent. It is not a real team, user study, focus group, expert panel, certification body, or statistical simulation. Never imply otherwise and never use scale language as evidence.

## Establish the action contract first

Infer the narrowest authorized mode. The verb and requested deliverable control permission.

| User intent | Allowed action |
| --- | --- |
| Diagnose, inspect, review, compare, explain, or plan | Read-only investigation and report |
| Redesign, specify, storyboard, wireframe, or mock up | Produce design artifacts; do not change product code unless requested |
| Build, implement, fix, repair, or apply | Change only the accepted scope, then build and verify |
| Identify or compare a recoverable/approved version | Read-only baseline forensics; do not alter a working tree |
| Reconstruct a missing state | Work only in a disposable copy/branch and label every inference |
| Restore or apply a proven state | Mutate only the explicitly authorized target after baseline proof |
| Publish, deploy, merge, message, purchase, delete, or change production | Require explicit authorization for that external action |

Useful modes are audit, redesign specification, visual concept, implementation, recovery/comparison, QA evidence package, and continuation master. Combine modes only when the user asks for an end-to-end result. Do not turn approval to analyze into approval to mutate.

Record a `phase_cap` whenever the user limits how far work may proceed. “Before design” normally stops at the accepted EXPERIENCE architecture; include STRUCTURE only when the user explicitly asks for flows, objects, or IA. “No implementation” forbids executable product changes; any implementation mapping is planning-only and must be labeled as such. A deep pass increases rigor inside the cap—it never authorizes later phases.

## Calibrate depth by consequence

- **Focused pass:** One surface or bounded question. Use outcome, user task, interaction, content, accessibility, visual hierarchy, and verification lenses.
- **Standard pass:** A feature or journey. Add evidence quality, IA, responsive/platform behavior, design-system consistency, trust, metrics, and adjacent regression risk.
- **Deep pass:** A product, high-impact journey, redesign, implementation, or regulated/high-risk experience. Activate every relevant council lane, complete all stage gates, and run a separate adversarial pass.
- **Forensic recovery pass:** Version drift, conflicting masters, lost approvals, incomplete builds, or repeated regressions. Hash and identify evidence, reconstruct chronology, distinguish verified state from claims, and fail closed when the baseline cannot be established.

Default a full-product audit or redesign to deep pass. Depth means broader evidence and stronger verification, not longer prose or arbitrary repeated review counts.

## Build the project control plane

Before judging or changing anything, create the minimum project dossier described in [references/project-control-plane.md](references/project-control-plane.md). It must identify:

- target outcome, users, jobs, platform, locale, risk, and deliverable;
- exact baseline or the strongest available candidate;
- artifact inventory and evidence quality;
- preserve locks, no-go areas, permissions, assumptions, and unknowns;
- routes/screens, roles, objects, journeys, states, and output destinations relevant to scope;
- decision owner, review cadence, phase cap, and what requires another approval.

Resolve baseline conflicts in this order:

1. Current explicit user instruction
2. Current acceptance criteria or governing master
3. Explicitly approved and locked behavior or visuals
4. Reproducible source/build with identity evidence
5. Live environment captured with role, route, state, viewport, locale, and time
6. Earlier context and inspiration

Never replace a verified baseline merely because another version is newer-looking or easier to run. Never remove, merge, hide, or rename a product capability in the name of simplicity without tracing the consequence and obtaining the required decision.

## Use the stage system

For standard, deep, implementation, and recovery work, progress through these states:

`FRAME → EVIDENCE → EXPERIENCE → STRUCTURE → INTERACTION → VISUAL SYSTEM → PROTOTYPE → IMPLEMENTATION → VERIFICATION → OWNER DECISION`

Each state has entry evidence, required outputs, exit criteria, and blockers in [references/operating-system.md](references/operating-system.md). Do not advance past a blocking contradiction or fabricate missing evidence. Re-open an earlier state when later work exposes a broken premise.

When the user requests staged review, show the real review artifact at each agreed checkpoint and stop at `OWNER DECISION`. A text description is not a substitute for a requested visual; a generated concept is not a functional build; a screenshot is not proof of hidden interaction.

## Load knowledge progressively

Read the smallest set that fully covers the task. For deep work, read every relevant module, not every file by default.

| Signal | Required module |
| --- | --- |
| Workflow, stage gates, re-entry, owner checkpoints | [references/operating-system.md](references/operating-system.md) |
| Baseline, evidence inventory, locks, decisions, private project context | [references/project-control-plane.md](references/project-control-plane.md) |
| Multidisciplinary analysis or conflicting recommendations | [references/design-council.md](references/design-council.md) |
| Severity, confidence, root cause, prioritization, coverage | [references/evaluation-framework.md](references/evaluation-framework.md) |
| Current standards, benchmarks, or citations | [references/source-registry.md](references/source-registry.md) |
| Story, PRD, value, pacing, narrative, core loop, experience architecture | [references/story-experience-architecture.md](references/story-experience-architecture.md) |
| Product strategy, research, behavior, experiments, metrics | [references/research-strategy-metrics.md](references/research-strategy-metrics.md) |
| IA, navigation, roles, workflows, forms, content, errors, service | [references/interaction-content-service.md](references/interaction-content-service.md) |
| Art direction, typography, color, layout, motion, tokens, systems | [references/visual-systems-craft.md](references/visual-systems-craft.md) |
| Wireframes, mockups, 3D/art direction, owner visual review | [references/visual-prototyping.md](references/visual-prototyping.md) |
| Accessibility, inclusion, privacy, safety, ethics, trust | [references/accessibility-inclusion-trust.md](references/accessibility-inclusion-trust.md) |
| Platform, responsive/adaptive, Persian, RTL/LTR, localization | [references/platform-responsive-localization.md](references/platform-responsive-localization.md) |
| Games and interactive experiences | [references/game-experience.md](references/game-experience.md) |
| Enterprise, admin, dashboard, data, marketplace, AI | [references/enterprise-data-ai.md](references/enterprise-data-ai.md) |
| Other product domains | [references/domain-lenses.md](references/domain-lenses.md) |
| Code mapping, implementation, drift repair, recovery | [references/implementation-recovery.md](references/implementation-recovery.md) |
| Test matrix, visual/accessibility QA, telemetry, release gates | [references/verification-design-ops.md](references/verification-design-ops.md) |
| Formal output package | [references/deliverable-contracts.md](references/deliverable-contracts.md) |
| Working alongside product, architecture, research, or QC skills | [references/collaboration-contract.md](references/collaboration-contract.md) |
| Skill maintenance, behavioral evals, public export, GitHub sync | [references/evolution-safety.md](references/evolution-safety.md) |

## Run one council over one evidence ledger

For standard and deep work:

1. Activate only lenses that can materially change the result and state why.
2. Give every lens the same project dossier and evidence ledger.
3. Separate observation, interpretation, decision, and unverified hypothesis.
4. Cluster repeated symptoms under systemic causes such as story/promise, object model, navigation, state machine, typography, layout primitives, permissions, data contracts, or implementation drift.
5. Resolve conflicts with [references/design-council.md](references/design-council.md); never simulate a majority vote.
6. Keep a dissent record for a valid rejected alternative, including tradeoff and reversal trigger.
7. End with one recommended direction, dependencies, acceptance criteria, verification, and explicit unknowns.

A separate adversarial pass must try to disprove the recommendation across failure, recovery, role escalation, assistive technology, low connectivity, mixed directionality, stale data, destructive action, interruption, monetization pressure, and metric gaming as applicable.

## Map the whole experience before polishing screens

- Trace entry, orientation, primary task, success, failure, recovery, return, and exit.
- Enumerate routes, screens, overlays, navigation, roles, permissions, objects, transitions, and state ownership.
- Include first use, returning use, loading, empty, partial, error, offline, stale, conflict, permission denied, interrupted, resumed, completed, archived, and destructive states where relevant.
- Inspect desktop, mobile, tablet, landscape, resize edges, zoom/text scaling, keyboard, pointer, touch, assistive modes, themes, locales, and RTL/LTR according to support scope.
- Inspect visual foundations, components, tokens, motion, assets, content, performance, data provenance, telemetry, and operational handoffs.
- For code, read repository instructions before routes, components, data contracts, styles, tests, analytics, and build configuration.
- For live products, record URL/build, account or role, route, state, viewport, locale, input mode, and timestamp. Do not infer hidden behavior from screenshots.

Create a journey × role × state × viewport/platform × locale/input coverage matrix whenever three or more dimensions materially vary. State the denominator; sampled coverage is not exhaustive coverage.

## Diagnose and redesign with traceability

Every material finding should include a stable ID, surface/state, evidence, evidence grade, observation, impact, root cause, severity, confidence, reach, lock impact, recommendation, acceptance criterion, and verification method.

Redesign in dependency order:

1. User promise, story/experience thesis, outcome, guardrails, and success definition
2. Service model, roles, objects, permissions, content model, and result destinations
3. Journeys, navigation, state transitions, feedback, recovery, resume, and exit
4. Screen hierarchy, responsive/adaptive composition, content, forms, and edge cases
5. Art direction, typography, color roles, grid, density, imagery/3D, iconography, motion, tokens, and components
6. Accessibility, localization, RTL/LTR, trust, privacy, safety, performance, and telemetry
7. Prototype or visual proof at the fidelity required for the decision
8. Implementation mapping, migration, verification, rollback, and post-release measurement

Do not patch a screenshot symptom when a shared primitive or product rule causes it. Do not optimize onboarding, documentation, or polish around a broken core experience. Recommend one direction; show alternatives only when a meaningful owner choice remains.

## Treat visuals as decision evidence, not decoration

- Use exact diagrams for topology, tables for mappings, code-native/vector layouts for precise UI, and raster generation for art direction, scenes, illustration, textures, or non-exact exploration.
- Label every visual as evidence capture, structural wireframe, exact UI specification, concept art, interactive prototype, or implemented build.
- Show key before/after states when it clarifies the decision.
- Include viewport, route, role, state, locale, theme, and build where relevant.
- If the user asks to see each implementation step, provide a rendered result before advancing; do not substitute prose, placeholder boxes, or unrelated inspiration.
- For 3D or motion, specify camera, scale, lighting, material, interaction, transition, performance tier, reduced-motion alternative, and how fidelity will be verified.

## Control implementation and recovery

When code changes are authorized:

1. Record baseline identifier, worktree state, affected surfaces, preserve locks, and expected behavior.
2. Preserve unrelated user changes and approved decisions.
3. Build a requirement-to-code map before a broad rewrite.
4. Make the smallest coherent change that repairs the root cause; escalate scope only when architecture blocks the accepted design.
5. Keep navigation, data/permission contracts, responsive behavior, accessibility, localization, telemetry, assets, and states aligned.
6. Build and test after meaningful batches; capture evidence under stable conditions.
7. Compare result with baseline, accepted specification, adjacent journeys, and no-go areas.
8. Report deviations before calling the work complete.

Never publish, deploy, merge, or modify production solely because implementation was requested.

## Verify claims, not intentions

- Record passed, failed, blocked, and not-run checks separately.
- Distinguish automated tests, manual checks, heuristic review, synthetic scenarios, analytics, actual research, and owner approval.
- Pair automated accessibility checks with relevant keyboard, zoom/reflow, semantic/screen-reader, visual, motion, and task checks.
- Use stable visual-regression conditions and human review; pixel difference reveals change, not correctness.
- Re-run affected journeys plus adjacent navigation, layout, role, data, locale, input, performance, and telemetry risks.
- Never claim real users, real experts, compliance, production delivery, persistence, exhaustive coverage, repeated review counts, or zero defects without receipts.
- Stop at a genuine blocker and identify the smallest missing evidence, authority, or input needed.

## Evolve and distribute safely

Maintenance must follow [references/evolution-safety.md](references/evolution-safety.md) and pass the deterministic checks in `scripts/`. This installed personal skill is the only source of truth. Public GitHub and marketplace copies are untrusted downstream mirrors. Never import repository content into this skill. Author and validate here, create an allowlisted public snapshot, scan it for private data and secrets, then export outward through a reviewable change. Repository drift may be inspected only to verify or repair the downstream copy.

Private project facts, conversations, memory, files, screenshots, code, logs, analytics, credentials, unpublished URLs, and connected-app data must never enter public evolution evidence or exports.

## Communicate for decisions

Lead with the outcome or blocker. Keep progress updates short and evidence-oriented. In the final handoff state what was inspected, what changed, what was rendered, what was verified, what remains, and where evidence lives. Keep the final answer self-contained.
