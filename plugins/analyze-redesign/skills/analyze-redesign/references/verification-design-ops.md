# Verification, Design QA, Performance, and Design Operations

Use this module to convert the redesign into reproducible evidence and a maintainable delivery process.

## Contents

1. Traceability matrix
2. Test layers and representative coverage
3. Visual and accessibility QA
4. Performance and telemetry
5. Release gates and design operations
6. Evidence pack

## Traceability matrix

Link each important decision through delivery:

`evidence/finding → design decision → specification → implementation location → acceptance criterion → test/evidence → release status → metric`

No high-priority recommendation is complete without an owner, dependency, acceptance criterion, and verification method. Mark checks as passed, failed, blocked, or not run; never collapse unknown into passed.

## Test layers

| Layer | Verify |
| --- | --- |
| Static and token | Invalid values, naming, aliases, contrast pairs, lint, type/schema, translation keys |
| Component | Anatomy, variants, every state, semantics, keyboard, content extremes, themes, locales, RTL |
| Pattern/integration | Forms, dialogs, navigation, tables, permissions, asynchronous state, focus restoration |
| Journey/end to end | Critical tasks, role transitions, payment/identity, failure, retry, resume, undo, cancellation |
| Visual regression | Stable representative states across viewport, theme, density, locale, and platform |
| Accessibility | Automated rules plus keyboard, zoom/reflow, semantics/screen reader, visual modes, motion |
| Performance | Real-user and lab loading, interaction, visual stability, long tasks, assets, degraded network |
| Resilience/security UX | Offline/stale/conflict behavior, safe errors, session expiry, permission denial, abuse paths |
| Analytics | Event semantics, deduplication, consent, exposure, success/failure, segment and guardrail coverage |

Automate stable, repeatable checks. Keep judgment-heavy and assistive-technology checks manual or human-supported. An automated tool's “zero violations” is not an accessibility pass.

## Representative coverage

Build the smallest matrix that spans risk:

- Critical and common journeys plus one high-cost failure/recovery journey.
- New, returning, expert, and permission-limited users where behavior differs.
- Short/long/empty/error/loading/stale/offline/conflict content states.
- Compact/medium/expanded layouts and unstable breakpoint edges.
- Keyboard/touch/pointer and relevant assistive technologies.
- Light/dark/high-contrast or forced-color modes as supported.
- Primary LTR and RTL locales, mixed-direction content, text expansion, date/number extremes.
- Supported browser/OS/device versions, including the lowest supported capability tier.

Use WCAG-EM sampling logic for formal accessibility evaluation. Sample selection never excuses untested templates, components, or critical processes.

## Visual QA protocol

1. Capture a named baseline with build/commit, route, role, state, viewport, locale, theme, and data fixture.
2. Compare at the same rendering conditions; stabilize fonts, animation, time, random data, and network where possible.
3. Use image diff to find change, then human review to decide whether the change is correct.
4. Review hierarchy, alignment, rhythm, typography, contrast, clipping, overlap, focus, loading, and transition behavior.
5. Confirm the fix at neighboring widths and states; a screenshot-specific patch is not complete.
6. Update baselines only after the change is reviewed and explained.

## Accessibility QA protocol

1. Run semantic and automated rule checks in representative rendered states, including opened overlays and validation errors.
2. Complete critical tasks keyboard-only and verify focus entry, containment, escape, restoration, and visibility.
3. Test zoom/reflow, text scaling, content spacing, contrast modes, reduced motion, and target sizes.
4. Inspect accessible names, roles, values, reading order, live regions, tables, errors, and dynamic status with a semantic tree or screen reader.
5. Test real assistive-technology/user combinations when stakes warrant; document coverage and limits.
6. Retest regressions after every relevant fix.

## Performance experience budget

Treat performance as interaction design. Define budgets for critical web-vital targets, route/data latency, image and font payload, animation frame stability, main-thread work, memory where relevant, and slow-device/network behavior. Use current Web Vitals definitions and measure both lab and real-user data when available.

Design the waiting experience by latency class:

- Immediate: direct feedback without fake loaders.
- Short: preserve context and prevent duplicate action.
- Noticeable: progress or skeleton only when it represents real structure.
- Long/background: status, safe navigation away, notification or return path, cancellation when feasible.
- Failed/partial/stale: explain data integrity, what was preserved, retry safety, and alternatives.

Do not let decorative animation, unoptimized media, font swapping, or layout shift damage the primary task.

## Telemetry and post-release evaluation

- Define events from the user/job model, not from DOM clicks alone.
- Capture start, meaningful progress, success, failure reason, recovery, abandonment, and relevant context without collecting unnecessary personal data.
- Validate event names, properties, identity/session rules, consent, sampling, deduplication, and dashboard definitions before launch.
- Pair primary outcomes with guardrails for errors, accessibility, complaints, cancellation, support demand, latency, and vulnerable segments.
- Set review windows and reversal triggers. A successful launch metric does not erase qualitative harm.

## Release gates

A material redesign is ready only when:

- Scope and preserve locks are satisfied or deviations are approved.
- Critical journeys and states pass the agreed matrix.
- No unresolved blocker-level accessibility, safety, security, privacy, or data-integrity issue remains.
- Required browsers, devices, roles, locales, themes, and input modes are covered.
- Performance and telemetry meet agreed thresholds or have an explicit exception owner.
- Rollback, support, monitoring, and incident ownership are clear.
- Known issues are visible, prioritized, and accepted by the authorized owner.

## Design operations

- Maintain a decision log, source registry, research repository, glossary, token/component ownership, and release notes.
- Use intake and triage criteria that distinguish product problems from component requests.
- Establish critique goals and roles: framing, evidence, coherence, craft, risk, and delivery. Avoid opinion-round-robin reviews.
- Track design-system adoption, duplication, exception causes, accessibility defects, rework, cycle time, and outcome—not output volume.
- Define contribution, review, deprecation, migration, and support service levels.
- Run periodic audits against real products, not only library files.

## Evidence pack

Deliver: scope and environment; traceability matrix; test matrix; commands/tools and versions; baseline and result captures; passed/failed/blocked/not-run results; accessibility coverage; performance evidence; known issues; deviations; metric plan; and exact reproduction steps. Clearly distinguish direct evidence, tool output, human judgment, and simulation.
