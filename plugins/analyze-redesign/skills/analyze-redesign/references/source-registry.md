# Authoritative UI/UX Source Registry

This registry routes decisions to primary standards, platform owners, research organizations, and mature public design systems. It is a starting map, not proof by association: open the relevant source, verify it is current, and cite the exact guidance that supports the decision.

## Contents

1. [Source discipline](#source-discipline)
2. [Standards, accessibility, and internationalization](#standards-accessibility-and-internationalization)
3. [Platform guidance](#platform-guidance)
4. [Mature design systems](#mature-design-systems)
5. [Research, service design, content, and metrics](#research-service-design-content-and-metrics)
6. [AI, trust, inclusive design, games, and data](#ai-trust-inclusive-design-games-and-data)
7. [Implementation and verification](#implementation-and-verification)
8. [Source pack selection](#source-pack-selection)

## Source discipline

Use this precedence for external evidence:

1. Normative standard, regulator, or platform owner for a claim within its authority.
2. Peer-reviewed or directly published research with transparent method.
3. Large evidence library applicable to the same task and population.
4. Mature design-system documentation for implementation patterns, not universal truth.
5. Expert heuristic, case study, or observed benchmark as a hypothesis.
6. Trend gallery or inspiration only for visual exploration, never as proof of usability.

For every material source, record publisher, title, URL, version or publication date, access date, applicable population/platform, and the exact decision it informs. Search live when information may have changed. Downgrade broken, undated, secondary, or context-mismatched sources. Do not turn company popularity into evidence.

## Standards, accessibility, and internationalization

| Source | Use it for |
| --- | --- |
| [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/) | Current testable web accessibility success criteria and conformance levels. |
| [W3C WCAG-EM](https://www.w3.org/WAI/test-evaluate/conformance/wcag-em/) | Defining scope, representative sampling, evaluation, and reporting. |
| [WAI-ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/) | Expected semantics and keyboard interaction for common widgets. |
| [ISO 9241-210](https://www.iso.org/standard/77520.html) | Human-centred design principles and lifecycle framing. |
| [ISO 9241-11](https://www.iso.org/standard/63500.html) | Usability as effectiveness, efficiency, and satisfaction in context. |
| [Unicode Bidirectional Algorithm](https://www.unicode.org/reports/tr9/) | Correct rendering and ordering of mixed-direction text. |
| [Unicode CLDR](https://cldr.unicode.org/) | Locale data for dates, numbers, units, names, and plural behavior. |
| [Unicode LDML](https://unicode.org/reports/tr35/) | Locale-data model and implementation details behind CLDR. |
| [W3C Arabic and Persian Layout Requirements](https://www.w3.org/International/alreq/) | Script-specific layout, typography, and bidi requirements. |
| [W3C Arabic Script Resources](https://w3c.github.io/alreq/arab/) | Practical Arabic-script layout and gap analysis. |
| [W3C Internationalization Techniques](https://www.w3.org/International/techniques/authoring-html) | Authoring choices for international-ready HTML and CSS. |
| [W3C Internationalization Quick Tips](https://www.w3.org/International/quicktips/) | Compact checks for encoding, language, layout, and local formats. |

## Platform guidance

| Source | Use it for |
| --- | --- |
| [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/) | Apple-platform layout, interaction, input, typography, motion, writing, and accessibility conventions. |
| [Material Design 3](https://m3.material.io/) | Android-oriented components, adaptive layout, color, type, motion, and interaction guidance. |
| [Android Adaptive App Quality](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality) | Quality expectations across window sizes, postures, and input devices. |
| [Android Adaptive Layout](https://developer.android.com/design/ui/mobile/guides/layout-and-content/adapt-layout) | Concrete responsive and adaptive layout behavior. |
| [Android Accessibility Principles](https://developer.android.com/guide/topics/ui/accessibility/principles) | Android semantics, focus, labels, actions, and testing principles. |
| [Microsoft Fluent 2](https://fluent2.microsoft.design/) | Microsoft-platform components, tokens, layout, accessibility, and content patterns. |
| [web.dev Learn Responsive Design](https://web.dev/learn/design) | Modern web layout, media, typography, and input adaptation. |
| [web.dev Learn Forms](https://web.dev/learn/forms/welcome) | Form semantics, labels, controls, validation, and usability. |
| [web.dev Learn Accessibility](https://web.dev/learn/accessibility) | Practical web accessibility implementation and testing. |

## Mature design systems

Study these systems comparatively. Borrow reasoning, architecture, state coverage, and governance patterns; do not assemble a product by mixing their visual surfaces.

| System | Strong reference area |
| --- | --- |
| [IBM Carbon](https://carbondesignsystem.com/) | Enterprise density, components, content, accessibility, and data visualization. |
| [Salesforce Lightning](https://www.lightningdesignsystem.com/) | Complex CRM workflows, enterprise components, and platform consistency. |
| [Shopify Polaris](https://shopify.dev/docs/api/polaris) | Merchant workflows, commerce patterns, and admin-product foundations. |
| [Atlassian Design System](https://atlassian.design/) | Collaboration-product components, tokens, content, and accessibility. |
| [GitHub Primer](https://primer.style/) | Developer-product UI, primitives, tokens, CSS, and component architecture. |
| [Adobe Spectrum](https://spectrum.adobe.com/) | Cross-platform components, color, typography, iconography, and contribution. |
| [GOV.UK Design System](https://design-system.service.gov.uk/) | Accessible public-service patterns supported by research and clear content. |
| [U.S. Web Design System](https://designsystem.digital.gov/) | Accessible government patterns, principles, components, and maturity guidance. |
| [SAP Design System and Fiori](https://www.sap.com/design-system/fiori-design-web) | Role-based enterprise applications and complex business processes. |
| [eBay Evo](https://playbook.ebay.com/) | Marketplace foundations, accessibility, content, and commerce components. |
| [Elastic EUI](https://eui.elastic.co/) | Search, observability, dense data, charts, and enterprise components. |
| [Zendesk Garden](https://garden.zendesk.com/) | Support-product patterns, components, and content-rich enterprise UI. |
| [Twilio Paste](https://paste.twilio.design/) | Token-based product UI and contribution/documentation patterns. |
| [Mozilla Protocol](https://protocol.mozilla.org/) | Content-rich responsive marketing and product surfaces. |
| [Uber Base Web](https://baseweb.design/) | Extensible component APIs, overrides, theming, and web implementation. |

## Research, service design, content, and metrics

| Source | Use it for |
| --- | --- |
| [Nielsen Norman Group: Ten Usability Heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/) | A baseline heuristic vocabulary; apply with context, not as user evidence. |
| [NN/g: Heuristic Evaluation](https://www.nngroup.com/articles/how-to-conduct-a-heuristic-evaluation/) | Planning, running, consolidating, and reporting heuristic reviews. |
| [NN/g: UX Research Methods](https://www.nngroup.com/articles/which-ux-research-methods/) | Selecting attitudinal/behavioral and qualitative/quantitative methods. |
| [NN/g: Complex Application Heuristics](https://www.nngroup.com/articles/usability-heuristics-complex-applications/) | Extending heuristic review for professional and complex tools. |
| [Google Research: HEART](https://research.google/pubs/measuring-the-user-experience-on-a-large-scale-user-centered-metrics-for-web-applications/) | Connecting experience goals to large-scale behavioral metrics. |
| [Kerry Rodden: HEART resources](https://kerryrodden.com/heart/) | Practical Goals–Signals–Metrics use and cautions. |
| [GOV.UK Service Manual](https://www.gov.uk/service-manual) | End-to-end public-service design, research, delivery, and measurement. |
| [GOV.UK Form Structure](https://www.gov.uk/service-manual/design/form-structure) | Question sequencing, branching, checking, and long-form completion. |
| [Baymard Checkout Research](https://baymard.com/research/checkout-usability) | Evidence-backed checkout and purchase-flow problem areas. |
| [Baymard Research Library](https://baymard.com/) | Large-scale ecommerce pattern research; verify access and relevance. |
| [Microsoft Writing Style Guide](https://learn.microsoft.com/en-us/style-guide/welcome/) | Clear software language, terminology, voice, and UI text patterns. |
| [GOV.UK Style Guide](https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/style-guides/a-to-z-style-guide/) | Plain, task-oriented public-facing content conventions. |
| [Australian Government Plain Language](https://www.stylemanual.gov.au/writing-and-designing-content/clear-language-and-writing-style/plain-language-and-word-choice) | Plain-language choices and content accessibility. |

## AI, trust, inclusive design, games, and data

| Source | Use it for |
| --- | --- |
| [Microsoft HAX Toolkit](https://www.microsoft.com/en-us/haxtoolkit/) | Human-AI product planning, interaction, and evaluation activities. |
| [Microsoft Guidelines for Human-AI Interaction](https://www.microsoft.com/en-us/haxtoolkit/ai-guidelines/) | Expectations, explanations, correction, control, and learning over time. |
| [Google PAIR Guidebook](https://pair.withgoogle.com/guidebook/) | People-centered AI product process and design patterns. |
| [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) | AI risk governance, mapping, measurement, and management. |
| [NIST Privacy Framework](https://www.nist.gov/privacy-framework) | Privacy risk identification and product/organizational controls. |
| [FTC: Bringing Dark Patterns to Light](https://www.ftc.gov/reports/bringing-dark-patterns-light) | Recognition of manipulative choice, consent, purchase, and cancellation flows. |
| [Microsoft Inclusive Design](https://inclusive.microsoft.design/) | Designing for permanent, temporary, and situational exclusion. |
| [Xbox Accessibility Guidelines](https://learn.microsoft.com/en-us/xbox/accessibility/guidelines) | Testable accessibility guidance for game features and input. |
| [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/) | Practical game accessibility coverage by impact and complexity. |
| [Tableau Visual Best Practices](https://help.tableau.com/current/blueprint/en-us/bp_visual_best_practices.htm) | Analytical hierarchy, chart choice, interaction, and dashboard clarity. |
| [Carbon Data Visualization](https://carbondesignsystem.com/data-visualization/getting-started/) | Data-viz tokens, chart patterns, color, and system integration. |
| [Massachusetts Data Visualization Accessibility](https://www.mass.gov/info-details/data-visualization-accessibility) | Accessible charts, alternatives, color, labeling, and interaction. |

## Implementation and verification

| Source | Use it for |
| --- | --- |
| [Design Tokens Community Group](https://www.designtokens.org/) | Interoperable design-token standards work and ecosystem context. |
| [DTCG Format Specification](https://www.designtokens.org/tr/drafts/format/) | Token file structure, types, aliases, groups, and interoperability. |
| [Figma Variables](https://help.figma.com/hc/en-us/articles/15339657135383-Guide-to-variables-in-Figma) | Modes, semantic values, component properties, and prototyping with variables. |
| [Figma Libraries](https://help.figma.com/hc/en-us/articles/360041051154-Guide-to-libraries-in-Figma) | Publishing, consuming, updating, and governing shared assets. |
| [Figma Design Systems](https://help.figma.com/hc/en-us/sections/14548397990423-Introduction-to-design-systems) | Foundations, components, variables, libraries, and adoption. |
| [Figma: Build Design Systems](https://help.figma.com/hc/en-us/sections/23536356509975-Build-design-systems) | Practical construction and maintenance workflows. |
| [Open UI](https://open-ui.org/) | Cross-browser research into native control and component behavior. |
| [Storybook Visual Tests](https://storybook.js.org/docs/writing-tests/visual-testing) | Component-state rendering and visual-regression workflows. |
| [Storybook Interaction Tests](https://storybook.js.org/docs/writing-tests/interaction-testing) | Exercising component behavior and assertions in stories. |
| [Playwright Accessibility Testing](https://playwright.dev/docs/accessibility-testing) | Automated axe checks within end-to-end journeys, with stated limits. |
| [axe-core](https://github.com/dequelabs/axe-core) | Automated accessibility rules and integration foundation. |
| [Chrome Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) | Repeatable audits for performance, accessibility, and web quality signals. |
| [web.dev Web Vitals](https://web.dev/articles/vitals) | User-centered loading, responsiveness, and visual-stability metrics. |
| [Google Search: Core Web Vitals](https://developers.google.com/search/docs/appearance/core-web-vitals) | Current Core Web Vitals definitions and measurement context. |

## Source pack selection

| Product signal | Minimum source pack |
| --- | --- |
| Any web product | WCAG, APG, target design system, responsive design, forms where relevant, Web Vitals, testing sources |
| iOS or Android | Target platform guidance, WCAG principles, platform accessibility, adaptive layouts, content/localization sources |
| Persian or Arabic | Unicode bidi, CLDR/LDML, ALReq, W3C i18n, target-platform typography and accessibility |
| Enterprise or admin | ISO usability, complex-app heuristics, Carbon/Fluent/SAP/Atlassian comparisons, performance and QA |
| Commerce or marketplace | Baymard, Polaris/eBay, trust/privacy, accessible forms, performance and measurement |
| AI experience | HAX, PAIR, NIST AI RMF, privacy, inclusive design, accessibility, human-control and evaluation sources |
| Game | Xbox and Game Accessibility Guidelines, platform conventions, input and motion coverage, telemetry and QA |
| Government or regulated service | Jurisdiction-specific law plus GOV.UK/USWDS patterns, WCAG/WCAG-EM, privacy, plain language, service design |

When a source pack disagrees with verified user evidence, first test whether context differs. Preserve the evidence and document the tradeoff; do not force a generic pattern onto a specialized task.
