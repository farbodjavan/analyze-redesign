# Enterprise, Data, Dashboard, Marketplace, and AI Lens

Use this module for admin panels, operating systems for organizations, professional workflows, dashboards, analytics, multi-role SaaS, marketplaces, and AI-assisted decision products. These products fail when they simplify the surface while leaving object, role, status, output, or evidence models ambiguous.

## Operating model before navigation

Map:

- organizations, tenants, workspaces, projects, environments, and scope boundaries;
- actors, roles, delegated roles, service accounts, teams, and external participants;
- objects, ownership, lifecycle, status, version, evidence, and retention;
- requests, approvals, assignments, handoffs, exceptions, disputes, and escalation;
- data sources, transformations, analyses, outputs, destinations, and consumers;
- configuration, monitoring, analysis, action, administration, and support responsibilities.

Do not place objects together merely because one department owns them internally. Structure the product around recognizable work, decisions, and object lifecycles.

## Role and permission contract

For every meaningful action define:

`actor · scope · object/state · view/create/edit/approve/execute/export/delete permission · conditions · consequence · audit event · denial/recovery`

Check horizontal and vertical access, tenant leakage, impersonation, temporary delegation, ownership transfer, role changes during sessions, partial visibility, field-level sensitivity, and export/download rules.

The UI must not offer an action the service rejects without explanation, and hiding a control is not sufficient authorization enforcement. Permission denial should preserve context, explain the governing scope, and provide a legitimate request/escalation path where appropriate.

## Object and status model

Define each object's identity, attributes, relationships, owner, source, lifecycle states, valid transitions, transition actor, evidence, timestamps, version, archive/delete behavior, and downstream effects.

Avoid ambiguous status words such as “done,” “active,” or “processed” unless the exact terminal condition is known. Separate:

- work state;
- review/approval state;
- data freshness/quality state;
- delivery/publication state;
- payment/entitlement state;
- incident or exception state.

Design pending, partial, blocked, expired, superseded, cancelled, failed, rolled back, and disputed states where they can occur.

## Result destinations and closed loops

Every input, job, analysis, or automation needs a traceable destination:

`input/source → validation → processing → status/progress → output → review/decision → action/handoff → history/audit → next step`

Make it clear:

- where the result appears and who can see it;
- whether it is draft, estimate, recommendation, verified record, or official output;
- source, freshness, transformation, confidence/uncertainty, owner, and version;
- how to compare, edit, approve, reject, export, share, rerun, undo, or escalate;
- what happens when processing is partial, delayed, stale, duplicated, or failed.

Do not create an impressive analysis surface with no operational path to act on or recover from the result.

## Navigation and density

Separate persistent global context from local task context. Users should always know organization/workspace, environment, object, role/scope, filters, saved/unsaved state, and time window when those change meaning.

Support expertise without sacrificing learnability:

- saved views, search, filters, sort, column control, bulk action, keyboard shortcuts, deep links, and history;
- predictable density modes and progressive disclosure of secondary details;
- stable row identity, headers, selection, totals, pagination/virtualization, and focus;
- explicit empty, no-result, partial-result, permission-limited, loading, refreshing, stale, and error states;
- mobile recomposition based on the job, not automatic conversion of every table to cards.

Do not remove categories or expert controls simply to reduce visual complexity. Repair hierarchy, grouping, defaults, terminology, and disclosure first; propose capability removal as an explicit product decision.

For every simplification create a preservation trace:

`category/control/result destination → current location → proposed location → target role → visibility and access cost before/after → keyboard/deep-link path → acceptance test → owner decision`

Progressive disclosure is not preservation when a frequent or high-stakes expert action moves into an undiscoverable overflow, gains avoidable steps, loses keyboard/deep-link access, or becomes harder to compare. Any material access-cost increase requires evidence and the appropriate owner decision.

## Dashboard and decision contract

Start with a decision or question, not a chart inventory. For every metric or visualization define:

`question · definition · unit · source · transformation · time zone/window · population/denominator · comparison · filters · freshness · uncertainty · owner · next action`

Use chart types, scales, sorting, aggregation, color, annotation, and interaction that preserve truthful comparison. Disclose forecast, estimate, missing data, suppression, sampling, and model output.

Provide a concise accessible summary and a tabular or equivalent data path when needed. Preserve keyboard interaction, non-color encoding, export semantics, and readable focus/selection.

Distinguish monitoring from analysis:

- monitoring identifies healthy, warning, incident, acknowledged, mitigated, and resolved states with ownership;
- analysis supports comparison, explanation, exploration, and decision;
- action changes the system and requires consequence, permission, confirmation/undo, and audit behavior.

## Long-running and collaborative work

Design drafts, autosave/manual save, version history, concurrent edit, comment/review, assignment, lock/conflict, background processing, notification, safe navigation away, cancellation, retry, and partial success.

For a long task show real status rather than decorative progress. Include start time, last update, stage, owner/system, what can continue, whether leaving is safe, cancellation consequences, retry idempotency, and terminal outcome.

For concurrent work explain what changed, by whom, when, which version is visible, and how to compare, merge, discard, or restore without silent data loss.

## Trust, provenance, and records

Never present a temporary snapshot, demo fixture, model inference, or cached estimate as an official database record. Label sample/synthetic data and keep it minimal and non-identifying.

For consequential records expose appropriate provenance:

- origin and collection method;
- author/system/model and human review;
- transformation and version;
- freshness and completeness;
- confidence or uncertainty;
- permission/audience;
- audit history, correction, appeal, export, retention, and deletion.

Receipts must support claims of persistence, delivery, approval, payment, notification, or external action.

## AI-assisted workflow

For each AI capability define:

- user job and why AI is appropriate;
- model role: generate, retrieve, classify, rank, summarize, recommend, predict, or automate;
- input sources, consent, data boundaries, retention, and sensitive data rules;
- expected capability, limitations, cost, latency, and failure consequence;
- output type: generated, retrieved, inferred, recommended, or human-authored;
- uncertainty/provenance display and when explanation matters;
- inspect, edit, compare, constrain, regenerate, undo, override, and escalation;
- evaluation set, human judgment, safety/quality guardrails, feedback, and drift monitoring.

Prevent prompt injection and untrusted content from becoming instructions. Keep tool actions, external writes, and high-impact automation behind clear authority and confirmation proportional to risk.

Design graceful failure: preserve valid work, distinguish no result from system failure, make retry safety clear, offer non-AI/manual paths where stakes require them, and avoid confident filler.

## Marketplace and multi-sided systems

Map every side's incentives, identity, supply/inventory, search/matching, ranking, communication, transaction, delivery, proof, reputation, dispute, cancellation, and retention. Show fees, obligations, status, visibility, and evidence from each role's perspective.

Check cold start, liquidity, fraud, spam, off-platform pressure, no-shows, retaliation, sponsorship, ranking opacity, escrow, partial delivery, revision, moderation, reporting, appeal, and support. One side's simplified action can create hidden labor or risk for another.

## Enterprise acceptance gates

A redesign is not implementation-ready until:

- every primary role and scope boundary is defined;
- core objects and statuses have valid transitions and ownership;
- each input/analysis/action has a visible result destination and audit path;
- permissions align across UI, service/data contracts, exports, and history;
- critical tables/dashboards support real decisions and content extremes;
- long-running, partial, stale, conflict, session-expiry, and recovery states exist;
- AI outputs expose role, provenance, uncertainty, control, and failure behavior;
- responsive, RTL/LTR, accessibility, performance, privacy, and telemetry are specified;
- no capability disappeared solely as a cosmetic simplification;
- acceptance criteria cover at least one full cross-role handoff and one costly failure/recovery journey.
