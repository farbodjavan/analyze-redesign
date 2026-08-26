# Accessibility, Inclusion, Trust, Privacy, and Ethics

Use this module from discovery through QA. Accessibility and trust are product requirements, not a final polish pass.

## Set the target

- Identify platform, jurisdiction, procurement or policy obligations, user populations, assistive technologies, and required conformance target.
- For web work, use WCAG 2.2 Level AA as a common product target unless a stricter or jurisdiction-specific requirement applies; do not equate that default with legal advice.
- Use WCAG-EM to define scope and representative sampling for formal evaluation.
- Record what was tested, by whom or by what tool, against which version, on which surfaces, and what remains untested.
- Never claim compliance or certification from a heuristic review or automated scan.

## Perceivable and adaptable

- Provide text alternatives according to the image's purpose; decorative media should not create noise.
- Preserve programmatic heading, landmark, list, table, form, status, and relationship semantics.
- Ensure text and meaningful UI contrast meet the applicable criterion across states and themes.
- Never rely only on color, position, shape, sound, hover, or animation to convey meaning.
- Support text resize, browser zoom, reflow, orientation, content spacing, high contrast, and reduced motion as applicable.
- Provide captions, transcripts, audio description, pause/stop, and non-audio alternatives where required.
- Make charts and canvases understandable through labels, summaries, data tables, or equivalent access paths.

## Operable

- Every function must work by keyboard or the platform's supported alternative input without traps.
- Focus order should follow task logic; focus must remain visible, stable, and restored after overlays or route changes.
- Controls need sufficient target size and separation; provide alternatives to precise drag, path, multipoint, or motion gestures.
- Avoid time limits where possible; otherwise warn, extend, preserve data, and explain exceptions.
- Give users control over autoplay, flashing, parallax, animation, sound, and repeated interruptions.
- Define skip, bypass, search, and navigation mechanisms for repeated or complex content.

## Understandable and robust

- Use familiar language, consistent names, visible instructions, and clear consequences.
- Labels, names, roles, values, states, errors, and status changes must be programmatically available.
- Prefer native elements. Use ARIA only when necessary and follow the relevant APG keyboard pattern.
- Error prevention is strongest for legal, financial, identity, health, public, and destructive actions: support review, correction, confirmation, and reversal where possible.
- Announce asynchronous changes without unexpectedly moving focus.
- Authentication should support password managers, paste, accessible challenges, and alternatives to memory or puzzle-heavy steps.

## Manual accessibility matrix

Automated checks catch only a subset. For representative journeys test:

| Mode | Check |
| --- | --- |
| Keyboard only | Complete tasks, overlays, menus, grids, drag alternatives, focus order, focus visibility, and escape behavior |
| Zoom and reflow | 200%/400% where applicable, small viewport, text spacing, no two-dimensional scrolling except legitimate content |
| Screen reader or semantic tree | Names, roles, values, landmarks, headings, reading order, errors, live status, tables, and dialogs |
| Visual modes | Contrast, forced colors/high contrast, dark mode, color-blind-safe meaning, focus, disabled/read-only distinction |
| Motion and media | Reduced motion, pause/stop, captions, transcript, flashing, autoplay, and time limits |
| Touch/switch/voice | Target size, gesture alternatives, accessible names matching visible labels, order, and dwell safety |

Test with disabled users when consequential and feasible. Their participation is research evidence, not a box to tick; recruit ethically and do not generalize one person's experience to a whole population.

## Inclusive-design stress cases

Evaluate permanent, temporary, and situational constraints:

- Vision: blind, low vision, color-vision difference, glare, cracked screen.
- Hearing: Deaf or hard of hearing, noisy space, muted device.
- Motor: tremor, limited reach, one hand, injury, switch or voice input.
- Cognitive and learning: memory, attention, language, numeracy, dyslexia, stress, fatigue.
- Speech: nonspeaking users, accent variation, privacy-sensitive environments.
- Connectivity and hardware: low bandwidth, old device, low battery, intermittent service.
- Culture and language: unfamiliar metaphors, name formats, script direction, calendar/number conventions, literacy.

Do not treat personas as evidence that these users succeeded. Use stress cases to generate testable risks and recruit actual participants when needed.

## Trust and meaningful control

- State what the product is doing, why, what data it uses, who can see the result, and what happens next.
- Make costs, recurring terms, limits, defaults, eligibility, ranking, sponsorship, and material consequences visible before commitment.
- Keep accept and decline choices comparable in clarity and effort. Cancellation and deletion should not be intentionally harder than joining.
- Distinguish recommendation, advertisement, notification, system status, and human communication.
- Provide history, status, provenance, edit, undo, export, appeal, escalation, and deletion where the context warrants them.
- Do not manufacture urgency, scarcity, social proof, shame, obstruction, disguised ads, hidden fees, or confirmshaming.
- Avoid coercive permission requests and repeated prompts after a clear refusal.

## Privacy and safety review

Map data from collection through use, sharing, inference, retention, export, and deletion. Minimize collection, default exposure, retention, and audience. Check secondary use, sensitive inference, re-identification, shared devices, screenshots, notification previews, logs, analytics, and support tooling.

For high-risk products, model misuse and abuse: actor, target, capability, entry point, harm, detection, prevention, response, appeal, and recovery. Design safe defaults, friction proportional to harm, rate limits, reporting, blocking, moderation status, evidence preservation, and human escalation as appropriate.

## Decision test

Before approving a pattern, ask:

1. Can the user understand the choice and consequence?
2. Can they freely refuse, change, undo, leave, or appeal?
3. Is the burden or risk distributed unfairly across a group?
4. Would the pattern remain acceptable if the conversion metric were removed?
5. What evidence would reveal harm after launch?

Log unresolved risks with severity, affected population, owner, mitigation, verification, and release decision.
