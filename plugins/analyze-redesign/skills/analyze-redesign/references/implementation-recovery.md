# Implementation, Fidelity, Recovery, and Drift Control

Use this module when applying an accepted redesign, comparing design with code, recovering an approved build, or repairing repeated regressions. Implementation is complete only when accepted behavior and visual decisions are reproducible in the target build.

## Baseline checkpoint

Before edits capture:

- repository/workspace instructions and authorization boundary;
- branch, commit, worktree state, submodules/dependencies, and generated files;
- build variant, environment, feature flags, seed/fixture identity, and external dependencies;
- package/build identifier, checksum, URL, or deployment identity as available;
- relevant routes, roles, states, locales, viewports/devices, themes, and input modes;
- accepted specification, visual captures, component/state sheet, and active locks;
- known defects and tests already failing.

Preserve unrelated user changes. Do not clean, reset, replace, migrate, or regenerate broadly merely to obtain a convenient baseline.

## Requirement-to-code map

Before a broad change, map:

`requirement/decision → surface/state → route/view/scene → component/system → data/permission contract → asset/token/content → analytics → test → owner`

Identify shared primitives whose repair can fix multiple symptoms. Also identify blast radius, compatibility requirements, migration, and rollback.

If an accepted capability has no code or data path, report the gap; do not simulate it with a visual placeholder unless the artifact is explicitly a prototype.

## Change budget and preserve contract

For every batch define:

- root cause being repaired;
- files/systems allowed to change;
- surfaces expected to change visibly or behaviorally;
- locks and unrelated areas that must remain unchanged;
- data/schema/API/navigation/asset implications;
- test and rollback plan.

Prefer a coherent root-cause patch over scattered style overrides. Avoid broad rewrites when a stable primitive can be repaired. Escalate architecture only with evidence that the accepted design cannot be implemented safely within the current structure.

Do not delete, hide, merge, rename, or disable a capability merely to match a simpler mockup. Trace the requirement and obtain the necessary decision.

## Design-to-code fidelity

Compare by contract, not screenshot resemblance alone:

- information and action hierarchy;
- route and state transitions;
- content, terminology, permissions, and result destination;
- grid, container, spacing, alignment, type roles, color roles, elevation, icons, imagery, and motion;
- component anatomy, variants, focus/keyboard/semantics, loading/error/empty/success, and content extremes;
- responsive/adaptive, locale, direction, theme, zoom/text scale, and safe-area behavior;
- performance, telemetry, persistence, offline/conflict, and recovery behavior.

Record deviations as accepted, defect, implementation constraint, or specification defect. Never silently update a baseline to make a mismatch pass.

## Recovery protocol

Choose and record one mode before acting:

- **IDENTIFY/COMPARE:** Read-only. Inventory candidates, establish identity and approval evidence, and produce a delta. No working-tree mutation.
- **RECONSTRUCT:** Create an explicitly disposable copy or branch when the original cannot be recovered. Label inferred elements and do not overwrite candidates.
- **RESTORE/APPLY:** Mutate the explicitly authorized target only after the source state is proven, blast radius and rollback are known, and preserve locks are recorded.

Then:

1. Freeze unauthorized mutation and inventory every candidate baseline.
2. Record checksums/commits/build identities and capture reproducible behavior.
3. Reconstruct chronology from authoritative records without treating recency as approval.
4. Build a delta table: approved state, current state, evidence, cause, risk, and repair.
5. Separate approved features, known defects, unapproved changes, missing artifacts, and uncertain claims.
6. Perform only the selected recovery mode; preserve all candidate evidence.
7. Verify the result against locks and representative journeys before new redesign work.
8. Create a new named checkpoint and continuation record.

If the original bytes cannot be recovered, call the result a reconstruction, not a restoration, and list every inferred element.

## Visual-regression discipline

Capture baseline and result under matching:

`build · route/screen/scene · role · state · viewport/device · pixel density · locale/direction · theme · font/text scale · fixture · clock/random seed · animation point · network condition`

Use automated diff to locate change and human review to judge correctness. Define masks only for genuinely nondeterministic regions and document them. Excessive masking, broad thresholds, or baseline replacement can hide regressions.

Check neighboring widths and states after a fix. A screenshot-specific offset is not a system repair.

## Implementation slices

Use vertical slices that can be reviewed and verified:

1. data/permission and state contract;
2. route/scene and interaction behavior;
3. component/system foundations;
4. exact content and visual composition;
5. responsive/locale/accessibility states;
6. telemetry, tests, captures, and rollback.

The order may vary, but a slice should end in a runnable artifact and evidence. When the owner requires per-step review, stop after the rendered verified slice.

## Build and test evidence

Record command/tool, version, environment, exit status, duration if useful, and artifact path. Distinguish:

- static/lint/type/schema checks;
- unit/component/pattern tests;
- integration/end-to-end journeys;
- visual regression;
- accessibility automation and manual checks;
- performance/resource/thermal/network checks;
- packaging/install/upgrade/restore checks;
- telemetry and data-contract validation.

Do not infer release behavior from a debug/development build when packaging, minification, signing, assets, permissions, audio, native integration, or environment configuration can differ.

## Drift prevention

- Give accepted visuals and states stable IDs connected to tests and code owners.
- Centralize tokens and shared behavior; remove accidental duplicates only after migration evidence.
- Store decision rationale and approved exceptions beside the implementation or governing record.
- Require review for baseline changes and explain intentional diffs.
- Keep design, content, data contract, code, test, and analytics terminology aligned.
- Add regression coverage for every repeated or high-cost defect.
- Monitor production evidence only when authorized and privacy-safe; do not declare production health from local tests.

## Completion gate

An implementation handoff must state:

- exact baseline and final build identity;
- files/systems changed and preserved;
- decisions and locks satisfied or challenged;
- actual tests/captures with pass/fail/blocked/not-run;
- representative coverage and denominator;
- deviations, known risks, rollback, and monitoring needs;
- review/run instructions;
- whether deployment/merge/publication occurred, with receipt if so.

No receipt means no claim of external completion.
