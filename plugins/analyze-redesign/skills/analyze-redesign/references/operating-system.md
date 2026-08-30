# Analyze–Redesign Operating System

Use this module for standard, deep, implementation, staged-owner-review, and recovery work. It converts a broad design request into a controlled state machine with observable exits.

## State contract

| State | Required work | Exit evidence | Re-enter when |
| --- | --- | --- | --- |
| FRAME | Define outcome, audience, job, scope, authority, platform, locale, risk, constraints, and deliverable | Project frame plus action contract | Goal, scope, owner, or authority changes |
| EVIDENCE | Inventory and grade artifacts; reproduce current behavior; identify unknowns and conflicts | Baseline candidate, evidence ledger, coverage map | New artifact contradicts a material fact |
| EXPERIENCE | Define promise, story or service thesis, intended emotional/functional arc, time-to-value, and success/guardrails | Experience thesis and measurable success definition | Proposed flow no longer serves the promise |
| STRUCTURE | Model objects, roles, permissions, lifecycle, service handoffs, IA, routes, and result destinations | Object/role/state maps and coherent navigation model | Screen work exposes missing ownership or object rules |
| INTERACTION | Specify tasks, transitions, feedback, errors, recovery, resume, cancellation, return, and content | Journey/state contracts and task flows | Prototype reveals misunderstood action or consequence |
| VISUAL SYSTEM | Define art direction, hierarchy, type, grid, color roles, components, tokens, imagery, motion, and density | System spec that covers representative surfaces/states | The direction fails real content, locale, or platform stress |
| PROTOTYPE | Create the smallest artifact that answers the current decision | Labeled, rendered prototype with review questions | Owner rejects direction or evidence invalidates it |
| IMPLEMENTATION | Map accepted decisions to code/assets/data and apply authorized changes | Reproducible build plus change trace | Build reveals architectural or design inconsistency |
| VERIFICATION | Exercise acceptance criteria and adjacent risks; collect evidence | Test ledger, visual evidence, known gaps, rollback state | Any required check fails or remains blocked |
| OWNER DECISION | Present exactly what changed, what is locked, and the next decision | Explicit accept/reject/revise/hold outcome | The owner requests revision or scope changes |

Do not use the states as a waterfall. Advance in dependency order, but loop back immediately when later evidence disproves an earlier decision.

## Entry and exit rules

At each state record:

`state_id · objective · entry evidence · active lenses · artifacts · decisions · locks touched · unknowns · exit criteria · phase_cap · status · next state`

Statuses are `READY`, `IN_PROGRESS`, `BLOCKED`, `OWNER_REVIEW`, `ACCEPTED`, `REJECTED`, or `SUPERSEDED`. Never report a state as accepted merely because its artifact exists.

An exit criterion must be observable. “Looks polished,” “fully checked,” or “better UX” is not an exit criterion. Useful forms include:

- the primary task has one named entry and one visible outcome;
- every role can identify scope, ownership, and permitted actions;
- a representative long Persian label fits at specified widths without clipping;
- platform Back returns to the documented prior state without losing accepted progress;
- the rendered build matches the accepted component/state sheet under controlled capture conditions.

## Phase caps

A phase cap is a hard authorization boundary, not a suggested stopping point.

- `ANALYSIS_ONLY`: investigate and report; create no proposed design artifact unless requested.
- `EXPERIENCE`: define promise, story/service arc, pacing, loop, success, and guardrails; stop before screen/interaction design.
- `STRUCTURE`: add objects, roles, IA, routes, and state ownership; stop before detailed interaction/visual design.
- `DESIGN`: interaction, content, visual system, and review prototypes are allowed; no executable product changes.
- `IMPLEMENTATION`: authorized code/asset/data changes are allowed within scope; no external publication by implication.
- `EXTERNAL_ACTION`: only explicitly named deploy/merge/publish/production actions are allowed.

The user's limiting phrase wins over the default mode. Reaching the cap produces an owner-review or handoff artifact, never silent continuation.

## Blocking conditions

Stop the affected branch of work when:

- baseline identity is unresolved and a wrong choice could overwrite approved work;
- current instruction conflicts with a locked decision and no owner ruling exists;
- a critical journey has no defined outcome, owner, or recovery path;
- a visual direction cannot represent required content or states;
- implementation would require deleting, migrating, publishing, or expanding scope without authority;
- severe accessibility, privacy, security, safety, or data-integrity risk remains unowned;
- requested verification cannot be run or reproduced.

Continue unaffected read-only investigation when it can reduce the blocker without expanding authority.

## Owner-review protocol

Use owner review when the user requests staged visibility, when a decision has high reversal cost, or when multiple valid directions remain.

1. State the decision being reviewed in one sentence.
2. Show the smallest real artifact that makes the decision visible.
3. Label fidelity and non-functional elements.
4. Show what is preserved and what changed.
5. Ask or infer only the decision needed now: accept, revise, reject, or hold.
6. On acceptance, create or update the lock record before advancing.
7. On revision, supersede the artifact without erasing its history or rationale.

If the owner delegates full direction, continue through low-reversal-cost states while still surfacing any decision that changes the product promise, removes a capability, creates legal/safety exposure, or commits production.

## Batch sizing

Choose the smallest batch that produces a meaningful review unit:

- one root-cause cluster rather than one cosmetic symptom;
- one coherent journey rather than disconnected screens;
- one component family with all relevant states rather than one default specimen;
- one implementation slice that can be built, captured, and rolled back;
- one evidence package that can prove or disprove acceptance.

Avoid batches so small that they create inconsistent intermediate systems or so large that the owner cannot identify which decision caused a regression.

## Contradiction and re-entry scan

Before every owner review or handoff, ask:

- Did the solution change the original promise, first-use path, core loop, or result destination?
- Did simplification remove a capability, role, category, state, or evidence source?
- Do story, screen copy, visual hierarchy, interaction, code behavior, and analytics describe the same product?
- Do desktop/mobile and RTL/LTR preserve task meaning and permission consequences?
- Does every accepted visual have an implementation/state contract, and does every implementation claim have evidence?
- Did a later decision invalidate an earlier lock or acceptance criterion?

Re-enter the earliest affected state. Do not conceal contradiction with additional polish.
