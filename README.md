# Analyze & Redesign

A reusable, evidence-based, multidisciplinary UX/UI analysis and redesign skill for ChatGPT and Codex.

It combines product strategy, UX research, information architecture, interaction design, content design, visual craft, design systems, accessibility, inclusive design, localization and RTL, privacy and trust, AI UX, data visualization, ecommerce, enterprise workflows, games, performance, measurement, and design QA.

## What is included

- A virtual design council with more than 50 specialist lenses
- Seven stage gates from context and evidence through delivery and measurement
- A curated registry of 75 authoritative sources
- Deep support for Persian, Arabic-script typography, mixed-direction content, and RTL/LTR products
- Domain lenses for enterprise, dashboards, ecommerce, marketplaces, government, regulated services, AI, games, learning, social products, developer tools, and publishing
- Deliverable contracts for audits, redesign specifications, visual packs, implementations, QA evidence, and continuation masters
- Explicit evidence grading, conflict adjudication, adversarial review, accessibility QA, performance checks, and release gates

The council is a structured multi-pass AI workflow. It does not claim that real designers, researchers, users, or independent reviewers participated.

## Repository layout

The installable plugin lives at:

```text
plugins/analyze-redesign/
├── .codex-plugin/plugin.json
└── skills/analyze-redesign/
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── assets/icon.svg
    └── references/
```

The canonical skill directory is:

```text
plugins/analyze-redesign/skills/analyze-redesign
```

`SYNC_MANIFEST.json` records the SHA-256 digest of every canonical skill file.

## Install with Codex

Add this repository as a plugin marketplace:

```bash
codex plugin marketplace add farbodjavan/analyze-redesign
```

Then open the Plugins Directory in the ChatGPT desktop app, choose **Analyze & Redesign**, and install it.

For a direct standalone skill installation, ask `$skill-installer` to install:

```text
https://github.com/farbodjavan/analyze-redesign/tree/main/plugins/analyze-redesign/skills/analyze-redesign
```

## Install in another ChatGPT account

1. Download this repository as a ZIP.
2. Extract or separately ZIP `plugins/analyze-redesign/skills/analyze-redesign`.
3. In ChatGPT Work, upload that skill folder or ZIP.
4. Ask `@skill-creator` to install the uploaded `analyze-redesign` skill.
5. Refresh the Skills page if it does not appear immediately.

## Use

In ChatGPT:

```text
@analyze-redesign Run a Deep Pass on this product. Identify root causes and produce an implementation-ready redesign with acceptance criteria and a QA plan.
```

In Codex:

```text
$analyze-redesign Run a Deep Pass on this product and implement the approved redesign.
```

The skill can also activate implicitly when a request clearly asks for UX/UI analysis, audit, critique, repair, or redesign.

## فارسی

این مخزن نسخهٔ قابل‌نصب اسکیل `analyze-redesign` را نگه می‌دارد. برای نصب در یک حساب دیگر، پوشهٔ اصلی اسکیل را دانلود و در ChatGPT Work همراه با `@skill-creator` نصب کنید. برای استفادهٔ تیمی و نسخه‌بندی‌شده، مخزن را به‌عنوان Plugin Marketplace به Codex اضافه کنید.

## Integrity

The distributed skill is copied from the validated personal skill and is checked for:

- valid `SKILL.md` frontmatter
- required files and local reference routing
- valid plugin and marketplace JSON
- exact SHA-256 digests for every canonical skill file
- absence of credentials and account-specific identifiers
