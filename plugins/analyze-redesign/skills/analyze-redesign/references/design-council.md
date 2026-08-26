# Virtual Design Council

Use this council to obtain multidisciplinary coverage without pretending that real people participated. Each role is an analytical lens applied in a separate pass to the same evidence ledger.

## Council roster

| Lane | Specialist lenses | Primary question |
| --- | --- | --- |
| Direction | Product strategy, business model, service strategy | What outcome and operating model must the experience support? |
| Evidence | UX research, behavioral science, analytics, experimentation | What is known, how strong is it, and what must be learned? |
| Structure | Service design, information architecture, content modeling | How should the journey, channels, objects, and hierarchy fit together? |
| Interaction | Task analysis, interaction design, prototyping, error recovery | Can people understand, complete, undo, and resume the work? |
| Content | Content design, UX writing, terminology, conversational design | Does language help users predict and act? |
| Surface | Visual design, art direction, typography, color, iconography, motion | Is attention guided with a coherent, legible, distinctive expression? |
| System | Design systems, tokens, component architecture, governance | Can the solution remain consistent and scale across teams and code? |
| Inclusion | Accessibility, inclusive design, localization, RTL, low-literacy | Who is excluded by the current assumptions or implementation? |
| Context | Web, iOS, Android, desktop, responsive and adaptive design | Does behavior fit the platform, device, input, and environment? |
| Trust | Privacy, security UX, safety, ethics, policy | Can users understand consequences and retain meaningful control? |
| Domain | Enterprise, commerce, marketplace, data, AI, game, learning | Which domain constraints change otherwise-valid advice? |
| Delivery | UX engineering, performance, QA, metrics, design operations | Can the result be built, verified, measured, maintained, and evolved? |

## Activation rules

Always activate product outcome, user task, interaction, content, accessibility, visual hierarchy, and QA. Add other lenses when a task signal exists:

- Multiple roles, departments, or channels: service design and enterprise.
- Large navigation or object model: information architecture and content modeling.
- Forms, onboarding, checkout, or destructive actions: behavioral science, trust, content, and recovery.
- Dense tables, monitoring, or analysis: data visualization, enterprise, responsive density, and performance.
- AI generation, ranking, recommendations, or automation: AI UX, trust, safety, evaluation, and human control.
- Persian, Arabic, mixed-direction content, or multiple locales: localization, typography, RTL, and content.
- Children, health, finance, identity, employment, public services, or regulated domains: deep trust, inclusion, privacy, safety, and jurisdiction-specific review.
- Games: game UX, input remapping, sensory and cognitive accessibility, onboarding, and telemetry.
- Implementation: design systems, UX engineering, accessibility testing, performance, and regression QA.

## Stage gates

Do not advance a deep redesign while a blocking gate is unresolved.

| Gate | Required output | Blocking condition |
| --- | --- | --- |
| 1. Context | Outcome, users, jobs, constraints, preserve locks, risks | No stable target or baseline |
| 2. Evidence | Evidence ledger, source quality, unknowns, research needs | Core claims rely only on guesses |
| 3. Structure | Journey, roles, IA, content model, state inventory | Key task has no coherent path or owner |
| 4. Interaction and content | Task flow, actions, feedback, recovery, language | Critical action, error, or consequence is ambiguous |
| 5. Visual and system | Composition, hierarchy, tokens, components, responsive rules | Direction cannot scale across required surfaces |
| 6. Inclusion and trust | Accessibility, localization, privacy, safety review | Known severe exclusion or harmful pattern remains |
| 7. Delivery and measurement | Acceptance criteria, test matrix, instrumentation, rollout | Result cannot be verified or success cannot be judged |

## Shared evidence ledger

Every lens must use the same record:

`claim_id · observation · evidence_type · source/location · user/job · surface/state · interpretation · confidence · risk · open_question`

Keep separate ledgers for observed evidence and proposed decisions. Link each decision back to one or more claims.

## Conflict adjudication

Do not average or majority-vote incompatible advice. Decide in this order:

1. Non-waivable safety, security, privacy, legal, and accessibility requirements.
2. Explicit user goal, accepted scope, and preserve locks that do not conflict with item 1.
3. Verified project evidence: actual research, analytics, support data, code, and reproducible behavior.
4. Target-platform conventions and domain constraints.
5. High-quality external research and standards applicable to the same population and task.
6. Internal design-system consistency and delivery constraints.
7. General heuristics and cognitive principles.
8. Aesthetic preference and current trends.

If two priorities remain valid, record the decision, rejected alternative, tradeoff, evidence gap, owner, and reversal trigger.

## Synthesis protocol

1. Cluster duplicate findings by root cause, not by reviewer role.
2. Separate must-fix, should-fix, experiment, and exploration work.
3. Build a dependency order; structural fixes precede local polish.
4. Recommend one coherent direction and show at most two meaningful alternatives.
5. Attach acceptance criteria and verification to every high-priority decision.
6. Run a final contradiction scan across journeys, components, breakpoints, locales, permissions, and states.

## Adversarial review pass

For deep or high-risk work, perform a separate pass that tries to disprove the recommendation. Probe edge cases, misuse, failure recovery, low connectivity, assistive technology, mixed directionality, role escalation, stale data, cancellation, destructive actions, and metric gaming. This is a structured self-critique, not independent validation.

## Honesty boundary

Never claim a headcount, panel consensus, user study, expert review, compliance certification, statistical result, or production outcome that did not occur. Synthetic personas and scenario walkthroughs may reveal hypotheses; label them as simulations and validate consequential claims with real evidence.
