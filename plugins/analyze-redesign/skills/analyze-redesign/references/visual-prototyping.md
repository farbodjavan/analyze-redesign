# Visual Prototyping and Owner Review

Use this module when visuals are needed to decide, communicate, or verify a redesign. Select fidelity by the uncertainty being resolved, not by a desire to make every artifact look finished.

## Fidelity ladder

| Artifact | Best use | Must not be claimed as |
| --- | --- | --- |
| Evidence capture | Demonstrating observed current state | General behavior outside captured conditions |
| Flow/IA diagram | Route, hierarchy, state, or ownership decisions | Spatial screen specification |
| Structural wireframe | Priority, grouping, order, and responsive composition | Final visual design |
| Style tile / art-direction frame | Typography, color, imagery, material, mood, motion principles | Complete component system |
| High-fidelity screen | Exact composition and content for named states | Working interaction |
| Component/state sheet | Anatomy, variants, states, tokens, and behavior | End-to-end product proof |
| Clickable prototype | Task sequence and simulated transitions | Production data, performance, persistence, or accessibility |
| Rendered implementation | Actual coded/engine state | Verified behavior beyond the tested build and scenario |
| Concept art / generated scene | Exploration of atmosphere, character, object, or 3D direction | Exact UI geometry or implemented game scene |

Label the artifact and its limitations on the review surface or adjacent manifest.

## Choose the artifact by question

- “Where does this live?” → IA/object diagram.
- “What happens after this action?” → state or sequence flow.
- “What should command attention?” → structural wireframe with real content.
- “What should it feel like?” → art-direction frame or concept scene.
- “Is this layout, type, and spacing right?” → high-fidelity screen at target dimensions.
- “Does every state exist?” → component/state matrix.
- “Can the task be completed?” → interactive prototype or working build.
- “Did implementation match approval?” → controlled baseline/result captures and diff.

Do not generate a full visual pack before the product question and review decisions are known. Do not answer an interaction question with a static beauty shot.

## Review-frame contract

Every owner-review frame should identify:

`artifact_id · decision question · fidelity · baseline/reference · viewport/device · route/screen · role · state · locale/direction · theme · data/content condition · functional limitations · version/date`

Include only annotations that help decide: hierarchy, interaction, content, state, responsive change, lock, or implementation note. Avoid covering the artifact with commentary.

## Real content and stress states

Design with representative content, then stress with:

- shortest, longest, missing, duplicated, stale, partial, and erroneous content;
- large numbers, negative values, units, dates, currencies, code, URLs, and mixed scripts;
- low/high density, empty/loading/error/success, and permission-limited states;
- compact/medium/expanded widths, orientation, zoom/text scale, and virtual keyboard;
- LTR, RTL, and mixed-direction fields;
- light/dark/high-contrast or reduced-motion modes as supported.

Placeholder-perfect screens conceal system defects. Synthetic data must be minimal, authorized, clearly labeled, and must not resemble a real private record.

## Exact interface work

For high-fidelity UI specify:

- canvas/window and safe areas;
- grid, container, columns, gutters, alignment anchors, reading measure, and overflow;
- typography roles with script-aware family, weight, size, line height, truncation, and numeric behavior;
- semantic colors and every interactive/status state;
- component anatomy, hit target, focus, keyboard, semantics, and responsive change;
- content, localization, error, and permission rules;
- motion trigger, duration class, easing intent, interruption, and reduced-motion alternative.

Use vector, layout, or code-native tools for exact geometry. Raster generation can support illustration and mood, but text and precise controls should be authored in a controllable layout system.

## 3D, spatial, and game-scene review

Specify enough to make the concept implementable:

- world/scene scale, coordinate assumptions, camera, field of view, framing, and navigation boundary;
- object dimensions, placement rules, collision/interaction volumes, occlusion, and readable distance;
- lighting intent, key/fill/environment sources, shadow quality, exposure, and accessibility alternatives;
- material model, texture scale, level of detail, transparency, reflections, and asset provenance;
- 2D/3D interface relationship, depth ordering, safe UI zones, subtitles, prompts, and focus;
- animation/state transitions, input, interruption, performance tier, thermal/memory budget, and fallback;
- verification capture from the target engine/device where implementation is claimed.

A generated 3D-looking image may approve atmosphere and composition, but it does not verify geometry, navigation, scale, material response, frame stability, or object placement in the engine.

## Before/after protocol

Use the same role, route, state, content, viewport, locale, theme, zoom, font availability, animation time, and capture scale. State material differences that are intentional. If conditions cannot be matched, label the comparison illustrative rather than exact.

Show cause and effect, not merely two images: identify which root cause changed, which lock remained, and which acceptance criterion the new artifact is meant to satisfy.

## Staged visual review

When the owner asks to see each step:

1. Agree or infer the review unit: story beat, flow, screen family, component family, scene, or implementation slice.
2. Produce one complete review unit, including relevant states and responsive/locale variants.
3. Render it under named conditions.
4. Run a contradiction and craft check before presentation.
5. Present decision, preserved elements, changed elements, and known limits.
6. Stop for owner decision if that was the agreed boundary.
7. Lock the accepted unit and carry it into subsequent work.

Never advance by showing text-only descriptions when the requested gate is visual. Never reuse a stale capture to imply the latest build.

## Visual acceptance

A visual direction is ready for implementation only when:

- required hierarchy, content, actions, states, and return paths are represented;
- representative content and stress states do not break the system;
- responsive, locale, direction, theme, and accessibility behavior is specified;
- components and tokens can reproduce the screens without one-off values dominating;
- assets have purpose, rights/provenance, dimensions, and fallbacks;
- the owner decision and preserved locks are recorded;
- remaining unknowns are implementation questions rather than unresolved product architecture.
