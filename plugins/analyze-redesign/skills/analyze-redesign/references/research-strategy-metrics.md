# Research, Strategy, Behavior, and Metrics

Use this module to convert business intent into testable user outcomes and to prevent heuristic opinion from masquerading as research.

## Product frame

Write a one-page frame before proposing a large redesign:

- **Outcome:** the change in user or business reality, not the feature being shipped.
- **Audience and context:** primary and excluded users, frequency, stakes, device, environment, and constraints.
- **Jobs and moments:** trigger, desired progress, current workaround, anxiety, and success state.
- **Value exchange:** what the user gives, gets, risks, and must trust.
- **Operating model:** roles, permissions, service dependencies, support, policy, and commercial constraints.
- **Success and guardrails:** leading indicators, lagging outcomes, counter-metrics, and unacceptable harm.
- **Assumptions:** desirability, usability, feasibility, viability, accessibility, trust, and adoption assumptions.

Turn each uncertain assumption into a learning question with a decision it will change.

## Match method to question

| Question | Useful methods | Output |
| --- | --- | --- |
| What problem exists in context? | Contextual inquiry, field study, diary study, interviews, support-log review | Behaviors, environment, workarounds, unmet needs |
| How is the domain organized mentally? | Open/closed card sorting, tree testing, concept mapping, terminology testing | Taxonomy and findability evidence |
| Can people complete the task? | Moderated or unmoderated usability test, cognitive walkthrough, accessibility evaluation | Task breakdowns, errors, recovery, comprehension |
| What happens at scale? | Product analytics, funnel/cohort analysis, search logs, operational data | Frequency, sequence, retention, drop-off, segment differences |
| Why did a metric move? | Follow-up interviews, session evidence with consent, survey, support review | Explanations and competing hypotheses |
| Which direction communicates better? | Concept test, preference-plus-reasoning test, comprehension test | Mental model and value-proposition evidence |
| Did the change cause an outcome? | Controlled experiment where ethical and feasible, phased rollout, interrupted time series | Causal or quasi-causal evidence with limits |
| Is the service viable end to end? | Service blueprint, backstage observation, failure-demand analysis | Frontstage/backstage gaps and ownership |

Do not use preference voting to decide task performance, five interviews to estimate prevalence, analytics to infer motive, or an A/B test to decide an unethical pattern.

## Research quality checks

- Define population, recruiting criteria, sample rationale, scenario, environment, moderator role, and analysis method.
- Separate participants' behavior from what they say; report both when they diverge.
- Avoid leading tasks, teaching the interface, prototype dead ends, confirmation questions, and convenience-sample generalization.
- Include relevant assistive-technology, language, literacy, device, experience, and edge-case populations.
- Record saturation or recurring patterns without claiming statistical representativeness.
- Protect consent, privacy, compensation fairness, data minimization, retention, and participant safety.
- Triangulate consequential decisions with at least two fit-for-purpose evidence types when practical.
- Store clips or quotes only with permission and enough context to avoid misrepresentation.

## Evidence grades

| Grade | Meaning | Allowed language |
| --- | --- | --- |
| A | Direct, reproducible project evidence or rigorous applicable research | “Evidence shows…” with scope |
| B | Multiple credible signals with some contextual gap | “Evidence suggests…” |
| C | One credible signal, benchmark, or expert review | “A likely issue/hypothesis…” |
| D | Assumption, synthetic scenario, or aesthetic judgment | “Assumption to test…” |

The grade describes confidence, not priority. A plausible severe risk can be urgent even with weak evidence; label both independently.

## Behavioral design checks

Use cognitive principles as diagnostic prompts, not universal laws:

- Reduce memory burden through recognition, visible state, history, and meaningful defaults.
- Match choices and information density to decision complexity; do not remove necessary control in the name of simplicity.
- Place targets, feedback, and recovery close to the action while preserving safe separation for destructive actions.
- Use progressive disclosure when secondary complexity can wait without hiding consequences or commitments.
- Preserve spatial and conceptual consistency; distinguish elements only when their behavior or priority differs.
- Design interruption, resumption, undo, and error prevention for real work rather than ideal linear flows.
- Treat defaults, urgency, social proof, scarcity, and friction as power. Use them to support informed goals, not extraction.
- Avoid optimizing a proxy in ways that degrade comprehension, trust, accessibility, or long-term value.

## Goals–signals–metrics map

For each outcome, define:

`goal → user-visible signal → measurable metric → segment → time window → data source → guardrail → decision threshold`

Balance the HEART families where relevant: happiness, engagement, adoption, retention, and task success. Add service and business measures without treating activity as value.

Core usability measures may include task completion, critical error rate, time on task, recovery success, assistance required, comprehension, and satisfaction. Product measures may include activation, repeat value, retention, successful handoff, support demand, trust or complaint signals, and quality outcomes. Always segment by role, locale, device, accessibility need, and experience level when sample and privacy allow.

## Experiment and rollout discipline

1. State hypothesis, mechanism, target segment, primary metric, guardrails, minimum detectable effect or practical threshold, and stopping rule before launch.
2. Validate instrumentation, exposure, assignment, sample-ratio integrity, and event semantics.
3. Do not ship accessibility, safety, privacy, or deceptive variants merely to test whether harm improves conversion.
4. Examine novelty, seasonality, network effects, survivorship, and segment reversals.
5. Pair metric outcomes with qualitative evidence when the mechanism or unintended effects remain unclear.
6. Record the decision and what evidence would reverse it.

## Research handoff

Deliver a decision-oriented summary: questions, methods, participants/data, limitations, evidence-grade findings, opportunity areas, rejected interpretations, design implications, next decisions, and the smallest research that reduces remaining risk. Never fabricate participants, quotes, statistics, or study results.
