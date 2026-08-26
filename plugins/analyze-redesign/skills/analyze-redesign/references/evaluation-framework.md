# Evidence-Based Evaluation Framework

Use this framework for deep audits and prioritized redesign decisions. Adjust emphasis to the product's actual users and jobs.

## Contents

1. Evidence classes
2. Finding record
3. Severity rubric
4. Evaluation dimensions
5. Scoring rules
6. Root-cause clustering
7. Prioritization and coverage
8. Contradiction review

## Evidence classes

Prefer evidence in this order while retaining all relevant sources:

1. Reproducible behavior in the exact build or live environment
2. Source code, data contracts, logs, tests, and measured analytics
3. Supplied acceptance criteria and explicit user approvals
4. Annotated screenshots or recordings with known route and state
5. Research with traceable authoritative sources
6. Heuristic inference or synthetic scenario, explicitly labeled

Never use a lower-confidence source to overwrite a higher-confidence verified fact without explaining the conflict.

## Finding record

Record material findings with these fields:

| Field | Meaning |
|---|---|
| ID | Stable identifier |
| Surface | Product, role, route, screen, component, viewport, and state |
| Evidence | Reproduction steps or artifact reference |
| Evidence grade | Direct/strong, corroborated, indicative, or assumed |
| Observation | What demonstrably happens |
| Impact | User and business consequence |
| Root cause | Systemic or local cause |
| Severity | Blocker, critical, major, or minor |
| Confidence | Confirmed, high, medium, or low |
| Reach/frequency | Affected users, roles, tasks, and recurrence |
| Council lenses | Roles that surfaced or challenged the finding |
| Recommendation | Smallest coherent repair |
| Acceptance | Observable pass condition |
| Verification | Test, research, analytics, or review method |
| Dependency/owner | Prerequisite and accountable role |
| Lock impact | Approved element affected or preserved |

## Severity rubric

- **Blocker:** Prevents a primary task, causes data loss, crashes, locks the user in, creates a serious safety/security issue, or makes verification impossible.
- **Critical:** Causes frequent failure, severe confusion, wrong permissions/data, major accessibility exclusion, or a broken cross-screen system.
- **Major:** Meaningfully slows tasks, harms comprehension or trust, produces strong inconsistency, or breaks an important responsive/state case.
- **Minor:** Local polish, small inconsistency, or low-impact friction with a clear workaround.

Consider reach, frequency, persistence, reversibility, and dependency. A visually small issue can be critical if it blocks navigation or trust.

## Evaluation dimensions

Evaluate only dimensions that apply, but never omit a relevant structural dimension merely because the visual layer is prominent.

| Dimension | Core questions |
|---|---|
| Product fit | Does the experience support the promised user job and business outcome? |
| Information architecture | Can users predict where things live and where outputs appear? |
| Journey integrity | Can users enter, complete, recover, return, and exit every primary flow? |
| Interaction | Are actions discoverable, reversible where appropriate, and acknowledged? |
| Content | Is language concise, specific, consistent, localized, and action-oriented? |
| Visual hierarchy | Do composition, contrast, grouping, and emphasis guide attention? |
| Typography | Are family, size, weight, line height, measure, numerals, and RTL/LTR behavior coherent? |
| Layout system | Are grid, spacing, alignment, density, and component geometry systematic? |
| Design system | Are tokens, components, icons, imagery, and motion consistent and reusable? |
| States | Are loading, empty, error, success, disabled, focus, offline, and permission states designed? |
| Responsive behavior | Does each viewport recompose intentionally rather than merely shrink? |
| Accessibility | Can users perceive, navigate, understand, and operate the experience with relevant assistive modes? |
| Trust and safety | Are identity, provenance, permissions, destructive actions, privacy, and system status clear? |
| Performance | Does perceived and measured performance support the task? |

## Scoring rules

Use scoring only if the user asks for it or comparison benefits from it.

- Score each applicable dimension from 0 to 4: 0 broken, 1 poor, 2 fragile, 3 solid, 4 excellent.
- Attach at least one finding to every score below 3.
- Mark untested dimensions as `NT`; do not treat them as zero.
- Weight dimensions by the primary job before calculating an aggregate.
- Show the rubric, weights, evidence coverage, and uncertainty beside any total.
- Do not use a single score to hide a blocker.

## Root-cause clustering

Cluster repeated findings under causes such as:

- unclear product model or ownership
- fragmented information architecture
- missing navigation and state model
- inconsistent layout primitives or tokens
- typography or localization architecture
- duplicated components
- incomplete data and permission contracts
- responsive behavior implemented as scaling instead of recomposition
- missing acceptance criteria or visual regression coverage

Repair the shared cause first, then verify each symptom.

## Prioritization and coverage

Do not use a single arithmetic formula as the decision. Build a priority view from:

- severity of user, accessibility, trust, safety, privacy, and business harm
- reach and frequency across users, roles, locales, journeys, and states
- persistence and reversibility of the harm
- confidence and evidence quality
- dependency value: whether the repair unlocks or prevents other work
- urgency, contractual or regulatory deadlines, and operational exposure
- implementation effort, migration risk, and ability to validate safely

Classify work as `must fix`, `should fix`, `experiment`, `explore`, or `won't do now`. Low-confidence severe risks belong in rapid validation or risk mitigation, not silently at the bottom of a backlog.

Track audit coverage separately from quality. Use a matrix of journeys × roles × states × viewports/platforms × locales/input modes. Report the percentage or count only when the denominator is explicitly defined. Never describe sampled coverage as exhaustive.

## Contradiction review

Before finalizing, search for:

- the same action with different names, locations, or consequences
- states that have visuals but no transition or recovery path
- component variants that violate token, accessibility, or content rules
- desktop, mobile, LTR, and RTL versions that change task meaning
- permissions shown in UI but not supported by the underlying data contract
- success metrics that reward behavior the trust or accessibility review rejects
- recommendations that conflict with preserve locks or the verified baseline
- acceptance criteria that cannot be observed or tested

Record unresolved contradictions as explicit decisions or blockers; do not smooth them away in prose.
