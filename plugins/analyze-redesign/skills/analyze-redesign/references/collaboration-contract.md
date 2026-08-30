# Cross-Discipline Collaboration Contract

Use this module only when the user invokes or the task genuinely requires product, research, content, architecture, engineering, security, legal, accessibility, or QC capabilities alongside this skill. It prevents overlapping skills from inventing different products or overwriting one another's evidence.

## Shared control plane

All contributors use the same:

- project objective and non-goals;
- baseline and artifact inventory;
- surface/object/role/state vocabulary;
- evidence and decision ledgers;
- preserve locks and authority boundaries;
- acceptance criteria and coverage matrix.

Do not let each discipline create its own unlinked requirement set. New evidence enters once, receives a grade, and links to affected decisions.

## Responsibility boundaries

| Discipline | Leads | Must provide to others |
| --- | --- | --- |
| Product | Outcome, audience, value, scope, prioritization, success/guardrails | Accepted requirements, product decisions, metrics, constraints |
| Research | Questions, method, participants/data, analysis, limitations | Evidence-grade findings and decisions they can change |
| Design | Experience architecture, IA, interaction, content, visual/system, prototype | Screen/state contracts, assets/tokens, rationale, acceptance criteria |
| Architecture/engineering | Feasibility, system/data/API/state architecture, performance, implementation | Constraints, code/data map, build evidence, deviations, rollback |
| Accessibility/trust/security/legal | Risk and applicable requirements within expertise | Requirements, severity, affected users, verification, unresolved decisions |
| QC/QA | Test strategy, traceability, execution evidence, regression and release readiness | Reproducible results, coverage, blockers, known risks |
| Owner | Product authority, lock acceptance, risk exceptions, external actions | Explicit accept/reject/revise/hold decisions |

This is coordination, not a claim that separate humans participated. When one agent applies multiple skills, label them as lenses or workflows.

## Handoff packets

Each discipline hands off:

`input evidence · decisions made · decisions requested · artifacts · assumptions · dependencies · acceptance criteria · verification · risks · owner/status`

Design should not hand engineering only screenshots. Engineering should not hand QA only a commit. QA should not hand the owner only a score. Every handoff must preserve traceability.

## Conflict resolution

Resolve conflicts using:

1. safety, security, privacy, legal, accessibility, and data-integrity obligations within verified scope;
2. current owner instruction and accepted locks that do not violate item 1;
3. reproducible project evidence;
4. product promise and primary user outcome;
5. platform/domain constraints and feasibility;
6. applicable authoritative research/standards;
7. system consistency and delivery cost;
8. heuristic or aesthetic preference.

Record the rejected alternative, tradeoff, owner, and reversal trigger. A technical constraint is evidence only when demonstrated; a design preference is not a requirement merely because it appears in a mockup.

## Parallel and sequential work

Parallel work is safe when tasks have independent outputs and the shared baseline is stable, for example current-state inventory, source verification, or separate platform test capture. Sequence work when one output changes another's premise, such as story before flow, object/permission model before screens, accepted design before implementation, and implementation before runtime QA.

Do not create concurrency merely to imitate a large team. Merge results through one evidence and decision ledger.

## Owner-decision boundaries

Escalate when a choice:

- changes the user promise, core loop, business rule, role, permission, capability, data meaning, or result destination;
- breaks or challenges a preserve lock;
- creates material safety, privacy, legal, accessibility, security, financial, or reputational risk;
- requires destructive migration, publication, deployment, purchase, or external communication;
- cannot be validated with available evidence and has high reversal cost.

Routine implementation choices within an accepted contract do not require repeated owner approval unless the user requested every-step review.

## Integrated final review

Before handoff confirm:

- product requirement, story, design, architecture, code behavior, test, and metric use the same terms and state model;
- every high-priority finding became a decision, experiment, accepted risk, or explicit non-goal;
- no discipline silently removed another's required capability;
- implementation deviations returned to design/product review;
- QA tested the accepted behavior, not a stale specification;
- owner approval is attached to the exact artifact/build, not inferred from adjacent praise.
