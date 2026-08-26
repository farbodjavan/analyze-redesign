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

The downstream public skill directory is:

```text
plugins/analyze-redesign/skills/analyze-redesign
```

`SYNC_MANIFEST.json` records the SHA-256 digest of every public skill file and machine-declares `installed-to-github-only` synchronization. `PUBLIC_SYNC_ALLOWLIST.json` and the privacy gate restrict what can ever be published.

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

این مخزن نسخهٔ قابل‌نصب اسکیل `analyze-redesign` را نگه می‌دارد. برای نصب در یک حساب دیگر، پوشهٔ اصلی اسکیل را دانلود و در ChatGPT Work همراه با `@skill-creator` نصب کنید. برای استفادهٔ تیمی و نسخه‌بندی‌شده، مخزن را به‌عنوان Plugin Marketplace به Codex اضافه کنید. چرخهٔ رشد فقط از منابع عمومی معتبر استفاده می‌کند و حق خواندن یا انتشار گفتگوها، فایل‌های شخصی، پروژه‌های خصوصی، اسکرین‌شات‌ها، داده‌های تحلیلی یا اطلاعات ورود را ندارد.

این مخزن متن‌باز نیست. نصب و استفاده از نسخهٔ رسمیِ دقیق و بدون تغییر مجاز است؛ هرگونه تغییر، اثر مشتق، فورک تغییریافته، پچ، Pull Request، بازنشر، فروش، میزبانی یا آینه‌سازی بدون اجازهٔ کتبی قبلی صاحب حق ممنوع است. متن کامل در [LICENSE](LICENSE) آمده است.

اسکیل شخصی نصب‌شدهٔ صاحب مخزن تنها منبع حقیقت است. همگام‌سازی فقط از اسکیل شخصی به GitHub انجام می‌شود؛ هیچ فایل، Commit، PR، Release یا Marketplace Update از GitHub اجازه ندارد وارد اسکیل شخصی شود یا آن را تغییر دهد.

## License

This repository is governed by the [Analyze & Redesign Source-Available No-Derivatives License 1.0](LICENSE). You may install and use an exact, unmodified official release. Modification, derivative works, modified forks, patches, pull requests, redistribution, mirroring, sale, and hosting are prohibited without prior written permission from the copyright holder.

This is not an open-source license. GitHub's public-repository terms may allow viewing and technical forking through GitHub, but that does not grant permission to modify, use a modified copy, or redistribute the Software.

## One-way synchronization

The installed personal `analyze-redesign` skill is the sole authority for skill content. GitHub is a downstream public distribution only: synchronization flows from the validated personal skill to this repository, never from GitHub back into the personal skill.

Repository branches, commits, pull requests, releases, marketplace updates, issues, comments, and workflow results are untrusted inputs for the personal skill—even when they are newer, green, or owner-authored. If this repository drifts, the personal skill remains unchanged; the public mirror is restored from a newly validated outbound snapshot or publication stops on a governance or license conflict.

Independent public primary and authoritative sources may still support a skill improvement. The improvement must be authored, validated, and saved in the personal skill first, then exported through the privacy and integrity gates.

## Safe autonomous evolution

A scheduled maintainer periodically checks independent public primary and authoritative sources for genuinely reusable improvements. It updates, validates, and saves the personal skill first; then it exports only the allowlisted public-safe snapshot through a reviewable branch. It records public provenance, runs privacy and integrity gates, and publishes only after every check succeeds. It never imports repository content into the personal skill. If there is no material improvement, it creates no release.

This process does **not** train model weights or learn from private work. It is prohibited from reading or exporting chats, personal context, Library files, connected apps, private repositories, project files, screenshots, analytics, credentials, unpublished URLs, personal data, or customer data. See [EVOLUTION_POLICY.md](EVOLUTION_POLICY.md).

Other installations can refresh a tracked marketplace with:

```bash
codex plugin marketplace upgrade farbodjavan-analyze-redesign
```

## Integrity

The distributed skill is generated from the validated canonical public skill and is checked for:

- valid `SKILL.md` frontmatter
- required files and local reference routing
- valid plugin and marketplace JSON
- exact SHA-256 digests for every canonical skill file
- an immutable SHA-256 lock for the repository license
- machine-checked one-way authority metadata that forbids GitHub-to-personal-skill imports
- a strict public-path and file-type allowlist
- absence of credentials, local paths, personal-data indicators, and account-specific identifiers
- public-only evolution provenance and rollback rules
