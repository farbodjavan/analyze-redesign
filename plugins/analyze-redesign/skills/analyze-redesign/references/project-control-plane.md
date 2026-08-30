# Project Control Plane

Use this module to keep a design effort anchored across long sessions, conflicting files, staged approvals, implementation, and handoff. The control plane is task-scoped project state, not permanent private training data.

## Project dossier

Create only fields relevant to the task:

```text
project_id
objective / non_goals
primary_users / excluded_users
jobs / stakes / context
platforms / form_factors / input_modes
locales / direction / content_constraints
risk_class / jurisdictions_to_verify
requested_mode / deliverables / authority_boundary
phase_cap / stop_condition
baseline_id / baseline_confidence
artifact_inventory
surface_inventory
decision_owner / review_cadence
preserve_locks / no_go_areas
assumptions / unknowns / blockers
```

Do not invent a project ID, version, role, metric, or approval. Use `UNKNOWN` with impact when evidence is missing.

## Artifact inventory

For each supplied or discovered artifact record:

`artifact_id · kind · location · version/date · checksum or commit if available · author/owner if known · scope · evidence grade · conflicts · allowed use`

Kinds include master/specification, acceptance record, screenshot, recording, design file, source tree, build, live URL, analytics, research, test output, asset, and inspiration reference.

Classify allowed use as:

- **governing:** can set requirements or locks;
- **observational:** shows behavior or appearance under known conditions;
- **supporting:** helps interpret but cannot override stronger evidence;
- **inspiration only:** may inform direction but is not a baseline;
- **untrusted/blocked:** identity, provenance, permission, or safety is unresolved.

## Baseline proof

For recovery or implementation, prefer a baseline record with:

`version/commit · branch · build/package ID · checksum · environment/URL · capture time · reproducible commands · expected screens/journeys · known defects · lock set`

When candidates conflict, create a comparison table and choose only under the precedence in `SKILL.md`. If identity cannot be proven, preserve all candidates and restrict work to read-only analysis or a disposable copy.

## Surface inventory

Inventory what can change or regress:

- roles, permissions, tenant/workspace/environment scope;
- objects, lifecycle states, ownership, dependencies, and history;
- routes, screens, dialogs, sheets, overlays, notifications, emails, and help;
- entry, success, failure, recovery, return, resume, cancellation, and exit;
- compact/medium/expanded layouts, orientation, themes, locales, direction, and input modes;
- data sources, derived outputs, provenance, freshness, export, and deletion;
- components, tokens, assets, audio, motion, 3D scenes, and platform integrations.

Use stable IDs so findings, decisions, code, tests, and captures can reference the same surface.

## Lock ledger

A lock protects an explicitly accepted decision without hiding risk.

| Field | Meaning |
| --- | --- |
| Lock ID | Stable identifier |
| Scope | Exact surface, behavior, copy, asset, token, or rule |
| Accepted state | What must remain true |
| Evidence | Approval record and accepted artifact/build |
| Owner/date | Who accepted it and when |
| Strength | Preserve, preferred, or provisional |
| Allowed variation | Responsive, locale, platform, data, or implementation tolerance |
| Dependencies | Other locks/contracts it relies on |
| Break condition | Safety, feasibility, contradiction, or owner change that reopens it |
| Status | Active, challenged, superseded, or released |

Never say “everything is locked” without an explicit inventory. A lock on appearance does not automatically lock broken navigation, inaccessible behavior, privacy risk, or implementation defects. Surface the conflict and request the correct decision.

## Decision ledger

Record consequential choices as:

`decision_id · question · options · evidence · selected direction · rationale · tradeoff · owner · date · affected locks · acceptance criteria · reversal trigger · status`

Distinguish:

- **proposal:** not accepted;
- **owner decision:** explicitly accepted/rejected;
- **implementation decision:** technical choice within authority;
- **inference:** low-risk assumption, clearly labeled;
- **external requirement:** platform, contract, law, or standard, with scope and source.

Do not rewrite history when a decision changes. Mark the earlier record superseded and link the successor.

## Coverage ledger

For audits and QA, define a denominator before a percentage:

`journeys × roles × states × viewports/platforms × locales/directions × input/assistive modes × themes/data conditions`

Use risk-based sampling, but list untested combinations. “All screens” means the inventory count is known and every in-scope screen has a result; otherwise say representative sample.

## Private project boundary

Project dossiers, evidence ledgers, locks, screenshots, code maps, and decision histories may contain private information. Keep them in the authorized project workspace or user deliverable, not in the reusable skill, public source registry, behavioral eval fixtures, or public repository.

If a reusable principle emerges from private work, re-derive it independently from public authoritative evidence. Do not transfer project wording, names, URLs, measurements, structures, or examples into the public skill.

## Continuation integrity

At handoff, include only verified current state:

- source-of-truth identifiers and checksums where available;
- active locks and superseded decisions;
- completed work with evidence;
- current blockers and their smallest resolution;
- remaining work in dependency order;
- prohibited regressions;
- next exact action and the state to resume.

Mark claims as verified, inferred, pending, blocked, or stale. A continuation master must not upgrade an unverified statement into fact.
