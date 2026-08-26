# Interaction, Content, Information Architecture, and Service Design

Use this module to turn the product model into understandable journeys, screens, language, and recovery behavior.

## Model the experience before screens

Create four connected maps:

1. **Object model:** core entities, attributes, relationships, states, permissions, and lifecycle.
2. **Journey model:** trigger, entry, orientation, work, decision, confirmation, follow-up, recovery, and exit.
3. **Navigation model:** global, local, contextual, utility, search, history, and deep-link paths.
4. **Service model:** user actions, frontstage UI, backstage people/systems, policies, dependencies, evidence, and failure points.

A screen should have one primary purpose, a clear owner or audience, and an obvious next or return path. Fix ambiguous objects and ownership before polishing cards or navigation labels.

## Information architecture checks

- Use user-recognizable concepts rather than internal departments, database tables, or implementation vocabulary.
- Keep labels mutually distinguishable, predictable, concise, and consistent across navigation, headings, search, and actions.
- Separate browse, search, filter, sort, compare, save, and history according to the job; do not overload one control.
- Preserve orientation with location, selected scope, applied filters, result counts, breadcrumbs where useful, and clear exits.
- Design cross-links and related actions around the object's lifecycle, not arbitrary page adjacency.
- Test findability with realistic tasks; tree testing and search-log review reveal problems that visual review cannot.
- Define no-result, partial-result, stale-result, permission-limited, and failed-search behavior.
- Keep URL/deep-link and back-button behavior coherent on the web.

## Task and interaction model

For every critical task, specify:

`trigger → prerequisite → entry → steps → system feedback → success evidence → undo/recovery → resume/exit`

Check that:

- Primary actions are visible at the moment of decision and named by outcome.
- System status, scope, saved state, progress, latency, and ownership are perceptible.
- Selection behavior, bulk actions, keyboard behavior, and focus are consistent.
- Destructive, irreversible, costly, or public actions reveal consequences before commitment.
- Confirmation is proportional to risk; prefer undo for low-risk reversible actions.
- Long operations support progress, backgrounding, cancellation where feasible, and safe retry.
- Interrupted work can resume without reconstructing context.
- Optimistic UI never implies completion before the system can honor it; reconcile failures explicitly.
- Cross-device and multi-user conflicts explain what changed and how to recover.

## State contract

Specify relevant states for each component and surface:

- Default, hover, focus-visible, active/pressed, selected, visited, disabled, read-only, and permission-limited.
- Initial, loading, progressive loading, refreshing, stale, offline, empty, no results, partial, error, success, and conflict.
- First-use, returning, draft, scheduled, processing, completed, archived, expired, and deleted where the object lifecycle requires them.
- Short/long content, missing media, large values, localization expansion, zoom/reflow, and mixed-direction text.

Every state needs a visual distinction, semantic meaning, permitted actions, content rule, transition, and test.

## Forms and data entry

- Ask only for information needed now; explain unusual or sensitive requests before input.
- Use one concept per field, persistent labels, appropriate input types, autocomplete, units, examples, and forgiving formats.
- Sequence questions by user logic and dependency. Reveal branches without losing previous answers.
- Prefer field-level validation after a meaningful pause or on blur; preserve input after failure.
- Error summaries should link to fields; messages state what happened and how to fix it without blame.
- Distinguish optional, required, unavailable, and not applicable values.
- Review or confirmation pages should emphasize consequential data and allow targeted edits.
- Save drafts for long or high-stakes forms and expose save status.
- Never disable paste in passwords, codes, identifiers, or payment fields without a defensible security reason.

## Content design

Build a content hierarchy for each surface:

1. Orientation: where am I and what is this?
2. Value or status: what matters now?
3. Action: what can or should I do?
4. Consequence: what will happen?
5. Support: what if I am unsure or something fails?

Write with concrete verbs, familiar nouns, short front-loaded sentences, and consistent terminology. Button text should describe the result, not the UI mechanism. Avoid vague actions such as “Submit,” “Continue,” or “Yes” when a more specific outcome fits.

Content patterns must define title, summary, label, helper text, placeholder use, empty state, success, warning, error, destructive confirmation, permission explanation, notification, and recovery message. Preserve legal accuracy while translating policy language into usable layers.

## Error and recovery language

An effective error answers: what happened, what was preserved, what the user can do now, whether retry is safe, and where to get help. Do not expose raw codes as the only explanation; keep a support reference when useful. Never blame the user or promise a resolution time the service cannot guarantee.

## Service continuity

Inspect emails, notifications, support, identity verification, payment, fulfillment, moderation, human review, and offline steps—not only the interface. Clarify handoffs, status ownership, expected time, escalation, evidence, cancellation, and appeal. A beautiful frontstage flow fails if backstage policy or operations cannot deliver the promise.

## Acceptance criteria examples

- A first-time user can identify the primary action and consequence without opening help.
- Back, refresh, retry, and resume preserve data according to the state contract.
- Every validation error is programmatically associated, described in plain language, and recoverable without re-entry of valid data.
- Every asynchronous task exposes status, last update, ownership, safe next actions, and terminal outcomes.
- Navigation labels and object names remain consistent across UI, URL, messages, support, and analytics.
