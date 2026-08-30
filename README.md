# Analyze & Redesign

A stage-controlled, evidence-led product design operating system for ChatGPT and Codex.

It connects product strategy, story and experience architecture, UX research, IA, interaction and content design, visual craft, design systems, accessibility, localization and RTL, games and spatial experiences, enterprise/data/AI workflows, implementation fidelity, recovery, measurement, and design QA.

## What is included

- A virtual multidisciplinary council applied as separate evidence-led passes—not a claim of real independent experts
- Ten controlled states: FRAME, EVIDENCE, EXPERIENCE, STRUCTURE, INTERACTION, VISUAL SYSTEM, PROTOTYPE, IMPLEMENTATION, VERIFICATION, and OWNER DECISION
- Hard phase caps so audit, pre-design, design, implementation, and external-action authority cannot silently expand
- A project control plane for baseline identity, evidence, locks, decisions, coverage, review, and continuation
- A curated registry of 95 authoritative sources with stable, draft, preview, jurisdiction, and platform status
- Deep support for Persian, Arabic-script typography, mixed-direction content, and RTL/LTR products
- Deep modules for story/experience, games and spatial/audio systems, enterprise/data/AI, visual prototyping, design-to-code fidelity, recovery, and multi-skill collaboration
- Deliverable contracts for audits, experience architecture, redesign specifications, visual packs, implementations, QA evidence, owner review, and continuation masters
- 19 behavioral scenarios across 16 domains, pinned safety cases, independent forward testing, semantic provenance, privacy self-tests, and exact Git-head distribution reconciliation

The council is a structured multi-pass AI workflow. It does not claim that real designers, researchers, users, or independent reviewers participated.

## Repository layout

The installable plugin lives at:

```text
plugins/analyze-redesign/
├── .codex-plugin/plugin.json
└── skills/analyze-redesign/
    ├── SKILL.md
    ├── VERSION
    ├── agents/openai.yaml
    ├── assets/icon.svg
    ├── config/
    ├── evals/
    ├── references/
    └── scripts/
```

The downstream public skill directory is:

```text
plugins/analyze-redesign/skills/analyze-redesign
```

The canonical directory contains `PUBLIC_SNAPSHOT_MANIFEST.json`, generated only after the personal source passes release, privacy, and integrity gates. `SYNC_MANIFEST.json` binds that snapshot to plugin packaging. `PUBLIC_SYNC_ALLOWLIST.json` and the repository privacy gate restrict what can be published.

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
@analyze-redesign Run a Deep Pass. Establish the source of truth and phase cap, repair story and experience before screens, and produce reviewable visual evidence, acceptance criteria, and QA.
```

In Codex:

```text
$analyze-redesign Run a Deep Pass on this product and implement only the explicitly approved redesign scope.
```

The skill can also activate implicitly when a request clearly asks for UX/UI analysis, audit, critique, repair, or redesign.

## فارسی

این مخزن نسخهٔ قابل‌نصب اسکیل `analyze-redesign` را نگه می‌دارد. نسخهٔ ۲ آن یک سیستم‌عامل طراحی مرحله‌ای است: ابتدا منبع حقیقت، Story و معماری تجربه را روشن می‌کند؛ سپس فقط تا سقف مجاز وارد ساختار، تعامل، ویژوال، پروتوتایپ، پیاده‌سازی و QA می‌شود. برای نصب در یک حساب دیگر، پوشهٔ اصلی اسکیل را دانلود و در ChatGPT Work همراه با `@skill-creator` نصب کنید. برای استفادهٔ تیمی و نسخه‌بندی‌شده، مخزن را به‌عنوان Plugin Marketplace به Codex اضافه کنید. چرخهٔ رشد فقط از منابع عمومی معتبر استفاده می‌کند و حق خواندن یا انتشار گفتگوها، فایل‌های شخصی، پروژه‌های خصوصی، اسکرین‌شات‌ها، داده‌های تحلیلی یا اطلاعات ورود را ندارد.

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

A scheduled maintainer periodically checks independent public primary and authoritative sources for genuinely reusable improvements. It updates, forward-tests, semantically reviews, validates, and saves the personal skill first; then it builds an allowlisted public-safe snapshot through a reviewable branch. It derives the complete candidate and published trees from exact Git heads, preserves locked legal/governance files by hash, and publishes only after every check succeeds. It never imports repository content into the personal skill. If there is no material improvement, it creates no release.

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
- canonical file modes and the generated snapshot manifest
- an immutable SHA-256 lock for the repository license
- machine-checked one-way authority metadata that forbids GitHub-to-personal-skill imports
- a strict public-path and file-type allowlist
- absence of credentials, credential assignments, local paths, personal-data indicators, and account-specific identifiers
- real behavioral and semantic-provenance attestations
- exact Git-head reconciliation plus public-history incident and rollback rules
