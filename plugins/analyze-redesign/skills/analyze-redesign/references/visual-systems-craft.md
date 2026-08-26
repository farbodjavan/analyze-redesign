# Visual Design, Systems, and Craft

Use this module after product structure and interaction are coherent. Visual quality should clarify priority, meaning, state, and brand—not conceal unresolved architecture.

## Art direction frame

Define the direction in operational terms:

- **Brand attributes:** three to five traits with explicit anti-traits.
- **Audience and context:** expertise, stakes, session length, device, environment, and cultural context.
- **Attention model:** what must be noticed first, compared, monitored, remembered, or ignored.
- **Expression levers:** typography, composition, color, shape, imagery, iconography, texture, motion, density, and voice.
- **Reference rationale:** extract transferable principles from references; do not copy distinctive layouts or brand assets.
- **Quality bar:** name observable criteria such as calm density, editorial hierarchy, precise states, or expressive motion.

Create two or three direction hypotheses only when a real strategic choice exists. Recommend one and state what it optimizes and sacrifices.

## Composition and hierarchy

- Begin with content priority and task sequence; assign visual weight afterward.
- Establish a stable grid, container strategy, reading measure, alignment logic, and spacing rhythm.
- Use proximity, alignment, repetition, contrast, and containment consistently; avoid nested cards as a substitute for hierarchy.
- Separate persistent chrome, context, primary work, supporting information, and transient feedback.
- Reserve strongest contrast and saturation for high-value or high-risk meaning.
- Make scan paths work with realistic content, not placeholder-perfect samples.
- Test extremes: sparse and dense data, long labels, large numbers, missing media, zoom, and localization expansion.

## Typography

Define roles before sizes: display, page title, section heading, body, compact body, label, metadata, code/data, and helper text. For each role specify family, weight, size, line height, tracking if appropriate, casing, color role, max width, truncation, and responsive behavior.

- Choose typefaces with complete glyph, numeral, punctuation, and weight support for required scripts.
- Tune hierarchy by size, weight, spacing, and placement; do not rely on color alone.
- Preserve readable line length and line height; dense UI may need different roles from editorial content.
- Avoid fake weights, overly light text, full justification in UI, and letter spacing that damages connected scripts.
- Align numeric columns deliberately; use tabular figures when comparison needs them.
- Test mixed scripts, acronyms, code, URLs, dates, currency, negative values, and ellipsis behavior.

## Color, theme, and elevation

Build semantic roles instead of component-specific hex values:

`surface · surface-raised · text-primary · text-secondary · border · focus · action · success · warning · danger · info · data-series`

- Define interaction and contrast across every state and theme, not just default light mode.
- Never encode status, category, selection, or chart meaning by hue alone.
- Separate brand color from semantic status roles.
- Test translucent layers against every allowed backdrop.
- Use elevation, border, or tonal shift according to a consistent depth model; avoid decorative shadows that imply false interactivity.
- Treat dark mode as a recalibrated system, not color inversion.

## Spacing, shape, iconography, imagery, and motion

- Use a documented spacing scale with intentional exceptions; optical adjustment must be named, not random.
- Map radius, border, and elevation to function and hierarchy rather than applying one card style everywhere.
- Icons need a shared grid, stroke/fill logic, optical weight, bounding box, label policy, and RTL behavior.
- Do not use an icon alone when meaning is unfamiliar, consequential, or culturally ambiguous.
- Define imagery purpose, crop, focal point, aspect ratio, loading, alt-text responsibility, empty fallback, and rights provenance.
- Motion must communicate relationship, state, orientation, or feedback. Specify trigger, duration class, easing intent, interruption, reduced-motion alternative, and performance budget.
- Avoid motion that delays repeated work, steals focus, causes vestibular discomfort, or masks latency.

## Token architecture

Use layers that preserve intent:

1. **Primitive:** raw palette, type, spacing, radius, elevation, duration.
2. **Semantic:** text, surface, border, action, feedback, focus, data, density.
3. **Component:** values used only when a component requires a stable exception.

Define token name, type, value or alias, modes, description, status, and owner. Prefer aliases from component to semantic to primitive. Avoid values whose names encode appearance when their purpose is semantic. Keep design and code naming mappable and use DTCG-compatible formats when interoperability matters.

## Component contract

Each component needs:

`purpose · anatomy · content rules · variants · sizes/density · states · behavior · keyboard · semantics · responsive rules · localization · theming · tokens · examples · anti-patterns · tests · version/status`

Build components from recurring product needs, not speculative completeness. Distinguish component, pattern, template, and one-off composition. Prefer composition APIs over variant explosions; prevent invalid combinations through documented constraints and code where possible.

## System governance

- Establish contribution, review, ownership, deprecation, migration, release, and support paths.
- Track adoption, duplication, exceptions, accessibility defects, change failure, and time-to-implement—not component count alone.
- Document decisions and rationale beside assets and code.
- Treat Figma libraries and coded components as linked implementations of one system, with an explicit synchronization process.
- Pilot new foundations on representative simple, dense, localized, and high-risk surfaces before broad rollout.
- Provide migration guidance and compatibility windows for breaking changes.

## Craft review

Inspect at actual device scale and common zoom, not only on a design canvas. Compare baseline and result across priority, alignment, rhythm, contrast, typography, optical balance, component states, real content, responsive behavior, RTL, and motion. A visual review passes only when the system remains coherent across representative states—not when one hero screen looks polished.
