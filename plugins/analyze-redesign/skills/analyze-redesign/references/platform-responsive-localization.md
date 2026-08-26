# Platform, Responsive, Localization, Persian, and RTL

Use this module whenever behavior spans devices, operating systems, input modes, locales, or writing directions.

## Platform decision rule

Start with the target platform's current guidance, then adapt only when verified product evidence or a cross-platform requirement justifies it. Preserve conceptual consistency across platforms while allowing native interaction, navigation, typography, permissions, and system-integration behavior to differ.

| Context | Prioritize |
| --- | --- |
| Web | URLs/deep links, browser history, keyboard, pointer and touch, zoom/reflow, semantics, responsive layout, loading and network variability |
| iOS/iPadOS | Native navigation and presentation, safe areas, Dynamic Type, system gestures, platform controls, pointer/keyboard on iPad |
| Android | System back behavior, adaptive layouts, edge-to-edge, dynamic type/font scaling, platform permissions, varied device and input classes |
| Desktop/pro tools | Window resizing, density, selection, context menus, shortcuts, multicolumn work, drag alternatives, persistence, multi-window behavior |

Do not force mobile navigation onto desktop, hover-only behavior onto touch, or a web convention onto a native platform without examining consequences.

## Responsive and adaptive model

Design around content and task breakpoints rather than named devices.

1. Inventory layout regions, minimum viable widths, preferred widths, collapse priority, and overflow behavior.
2. Decide for each region whether it reflows, wraps, stacks, scrolls, condenses, moves, becomes an overlay, or disappears with an equivalent access path.
3. Define compact, medium, and expanded behavior only when the transitions reflect actual content needs.
4. Test resize continuously between target widths; breakpoint screenshots alone miss unstable ranges.
5. Preserve task order and information priority when columns rearrange.
6. Avoid hiding essential actions or information to make a narrow screenshot look clean.

## Responsive stress matrix

- Narrow phone, large phone, tablet portrait/landscape, small laptop, wide desktop, and split-window/multitasking where applicable.
- Browser zoom and OS text scaling, including reflow and enlarged controls.
- Touch, coarse pointer, precise pointer, keyboard, switch, voice, and stylus where relevant.
- On-screen keyboard, safe areas, browser chrome, notches, fold/hinge, and orientation changes.
- Short and long content, dense data, localization expansion, mixed scripts, empty/error/loading states.
- Slow network, offline transition, image failure, cached/stale data, and interrupted work.

## Dense tables and professional layouts

- Preserve column meaning and comparison before compressing decoration.
- Provide column priority, resize, reorder, pin, sort, filter, and horizontal-scroll behavior only where the task needs them.
- Keep row identity and headers available during scrolling; maintain semantic table relationships.
- On narrow screens, choose among responsive columns, horizontal table, detail drill-in, or purpose-built card/list based on the task. Do not automatically turn every table into cards.
- Make bulk selection, totals, pagination, loading, empty, partial, and permission states explicit.

## Internationalization foundation

- Store and render Unicode correctly; separate content from layout and avoid string concatenation for translated sentences.
- Set document and component language and direction explicitly. Use language metadata for pronunciation, hyphenation, fonts, and assistive technology.
- Use locale-aware formatting for names, addresses, dates, calendars, time, numbers, decimals, grouping, currency, units, plural categories, and sorting.
- Support text expansion/contraction, variable word order, line wrapping, and fonts with complete glyph coverage.
- Avoid text baked into images, fixed-width controls, and direction encoded in asset filenames or DOM order.
- Pseudo-localize early; test real priority locales before release.
- Define fallback behavior for missing translation, font, locale data, and unsupported format.

## RTL layout rules

- Prefer logical layout properties and start/end terminology over left/right in tokens, CSS, specs, and component APIs.
- Set direction at the correct container; isolate embedded opposite-direction content instead of manually reordering characters.
- Use bidi-safe markup such as appropriate `dir`, `lang`, and isolation (`bdi` or equivalent) for user names, URLs, IDs, code, phone numbers, and dynamic fragments.
- Mirror spatial navigation, progression, drawers, chevrons, and directional motion when their meaning follows reading direction.
- Do not blindly mirror universal or intrinsic-direction content such as media timelines, clocks, charts with fixed axes, maps, brand marks, mathematical notation, code, or a direction explicitly chosen by the user.
- Keep DOM, reading, focus, and visual order coherent. CSS reversal that only looks correct can break keyboard and screen-reader use.
- Test overlays, carousels, breadcrumbs, pagination, tables, mixed-direction inputs, truncation, copy/paste, and punctuation.

## Persian-specific review

- Choose a Persian-capable typeface and verify all required weights, joining behavior, diacritics, punctuation, digits, Latin fallback, and bold/italic substitutes.
- Avoid positive tracking on connected Persian text. Tune line height and vertical alignment for Persian glyph proportions rather than inheriting Latin values blindly.
- Decide Persian versus Latin digit policy by task and user expectation; apply it consistently while preserving machine-readable values.
- Make calendar system explicit. Do not infer Gregorian versus Solar Hijri solely from language; clarify product and user requirements.
- Validate date order, weekday names, time format, decimal/group separators, currency placement, percent sign, units, and negative values with locale-aware formatters.
- Treat Iranian names, addresses, national identifiers, phone numbers, postal codes, bank/card values, and search normalization as separate domain rules; never invent validation rules.
- Test Persian plus English product names, URLs, email, hashtags, mentions, version numbers, formulas, parentheses, slashes, and ellipses in the same line.
- Check search for Arabic/Persian character variants and optional diacritics only when the product domain supports normalization; preserve original user content.
- Verify cursor movement, selection, deletion, placeholder direction, error placement, and copy/paste in mixed-direction fields.
- Translate meaning and tone, not word order. Maintain a glossary for product terms and avoid unnecessary English when a clear established Persian term exists.

## Localization content contract

For every string or content field, define owner, context note, audience, variables, plural/gender behavior if relevant, character constraints, markup, fallback, translation status, and screenshot/context availability. Do not split sentences into fragments that translators cannot reorder.

## Verification evidence

Record platform/version, device or emulator, viewport/window, pixel density where relevant, input mode, font/text scale, locale, direction, theme, route, role, state, and build. Screenshots alone do not verify focus, reading order, gestures, back behavior, copy/paste, or bidi correctness; exercise those interactions directly.
