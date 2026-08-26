# Evolution Log

This log records only public, release-level changes. It never includes user prompts, project examples, private evaluation artifacts, account data, or unpublished sources.

## 1.2.0 — 2026-08-26

- Made the installed personal skill the sole authority for skill content and the public GitHub repository a downstream distribution only.
- Prohibited every GitHub-to-personal-skill path, including imports from main, branches, pull requests, releases, marketplace updates, or workflow results.
- Added machine-validated `installed-to-github-only` direction metadata and a repository-import prohibition.
- Changed evolution order to author, validate, and save the personal skill first, then export an allowlisted public-safe snapshot to GitHub.

## 1.1.1 — 2026-08-26

- Added the proprietary Analyze & Redesign Source-Available No-Derivatives License 1.0.
- Allowed installation and use of exact unmodified official releases while prohibiting modification, derivative works, modified forks, patches, pull requests, redistribution, mirroring, sale, and hosting without prior written permission.
- Locked the license digest in the privacy and integrity gates so autonomous evolution cannot alter the legal terms.

## 1.1.0 — 2026-08-26

- Added a public-only evolution policy and a matching safety module inside the skill.
- Added explicit isolation from conversations, personal context, connected apps, private repositories, project files, and proprietary artifacts.
- Added a repository allowlist and a privacy gate for paths, file types, local identifiers, personal data indicators, and common secret formats.
- Added deterministic sync-manifest maintenance and scheduled repository validation.
- Defined branch, review, green-check, versioning, provenance, rollback, and public-to-installed synchronization gates.
