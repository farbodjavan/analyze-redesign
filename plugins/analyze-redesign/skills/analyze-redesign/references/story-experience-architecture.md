# Story, Product Promise, and Experience Architecture

Use this module when a product feels emotionally flat, slow to reach value, overloaded with setup, disconnected from its story, or when screens are being designed before the experience is coherent. “Story” includes narrative games, onboarding narratives, service promises, and the causal story a professional product tells through status and action.

## Experience thesis

Before screen design, write a compact thesis:

`For [audience] in [context], the product helps them move from [current tension] to [desired outcome] through [distinctive mechanism], while preserving [trust/agency constraint]. The first convincing proof arrives when [observable moment].`

Define anti-goals: what the product must not feel like or become. Anti-goals should describe consequences, not taste alone, for example “the tutorial must not delay first meaningful control” or “the dashboard must not imply that estimated data is verified.”

## Four connected architectures

1. **Value architecture:** promise, user contribution, returned value, proof, repeat value, and business exchange.
2. **Experience architecture:** trigger, anticipation, orientation, agency, challenge/work, reveal/result, recovery, return, and progression.
3. **Information architecture:** objects, terminology, hierarchy, navigation, search, filters, history, and result destinations.
4. **Delivery architecture:** people, systems, assets, data, permissions, latency, support, policy, and operational handoffs.

If these architectures disagree, repair the earliest disagreement before visual polish.

## Story and pacing map

For narrative or guided experiences, map:

`hook → promise → first agency → first competence → complication → meaningful choice → consequence → reveal → closure → next desire`

For each beat record:

- player/user knowledge and question;
- intended emotion or confidence;
- action and degree of agency;
- new information, reward, or proof;
- duration and skippability;
- failure/recovery and resume state;
- visual/audio/motion support;
- dependency on prior knowledge.

Avoid exposition that arrives before the user has a question, repeated explanation of visible facts, fake choices, reward without earned meaning, and interruption immediately before agency. Optional lore/help must remain discoverable later without blocking the primary loop.

## Time-to-value and friction budget

Measure the route from launch or entry to the first meaningful action and first credible result. Count surfaces, taps/clicks, mandatory reading, loads, permissions, account steps, and decisions.

Classify each step as:

- **essential prerequisite:** the task cannot safely or technically proceed without it;
- **value-building:** increases anticipation, comprehension, or commitment enough to justify its cost;
- **deferrable:** useful later but not before first value;
- **duplicate:** repeats known information or another control;
- **organizational leakage:** serves an internal structure rather than the user's job.

Reduce delay by deferring or merging steps, not by deleting necessary control, context, accessibility, or trust. For a game, first meaningful control matters more than arriving at a menu called “Play.” For enterprise software, first value may be seeing a trustworthy status or completing a real handoff.

## Core loop and return loop

Define the smallest repeatable loop that carries the product promise:

`motivation → action → system response → interpretation → progress/reward → next motivation`

Then define:

- moment-to-moment interaction loop;
- session loop;
- progression or lifecycle loop;
- return/resume loop;
- failure and recovery loop;
- social, operational, or monetization loop where applicable.

Every layer should reinforce rather than obscure the primary loop. A progression system that delays or replaces the enjoyable action is not a substitute for a strong core loop.

## PRD-to-experience contract

Translate each requirement into:

`requirement_id → user/job → trigger → rule → visible surface → states → permissions → success evidence → failure/recovery → metric → test`

Flag requirements that have no visible outcome, no owner, no error behavior, or no test. Flag screens or features that cannot be traced to an outcome or obligation.

Do not silently narrow an existing requirement for visual simplicity. Propose a deprecation or relocation decision with consequence, migration, evidence, and owner approval.

## Emotional and functional continuity

Check across adjacent steps:

- Does the user's question at one step receive an answer or meaningful escalation at the next?
- Does visual intensity match narrative or operational importance?
- Does audio/motion support rather than compete with control and comprehension?
- Are success, failure, and uncertainty emotionally honest?
- Is the user rewarded with agency, knowledge, mastery, utility, or connection—not only animation or points?
- Does the next call to action arise naturally from the achieved result?

For professional products, emotion still matters: confidence, control, orientation, momentum, and trust are experience outcomes even when the surface is utilitarian.

## Story-first redesign sequence

When the user rejects the product direction or says the experience became worse, stop local polishing and perform:

1. Reconstruct the intended promise from governing evidence.
2. Map current path and measure delay, repetition, and broken causality.
3. Identify where the user loses agency, question, or reward.
4. Rewrite the experience/story beats and core loop without screens.
5. Validate that every required capability and lock has a place.
6. Convert beats into journeys, states, and content.
7. Only then redesign visual structure and interaction.

Present the rewritten architecture for owner review when it materially changes pacing, narrative, capability placement, or the core loop.

## Acceptance signals

Examples, to be tailored:

- A first-time user can state the promise and next meaningful action after the intended opening.
- The path to first agency contains no unexplained mandatory detour.
- Every major beat changes knowledge, agency, risk, or progress.
- The core loop remains recognizable across onboarding, failure, return, and progression.
- Every screen and feature traces to a requirement, user job, story beat, trust obligation, or operating need.
- The result creates a clear reason to continue without deceptive urgency.
