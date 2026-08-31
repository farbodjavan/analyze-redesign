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

## Agentic action contract

Use this contract when an AI system can plan across steps, invoke tools, delegate, retain memory, spend resources, or change an external system. A conversational surface alone does not make an experience safely agentic.

Model each run as:

`user-owned goal and scope → proposed plan → authority check → bounded execution → observable progress → result and action receipt → recovery or escalation`

- **Choose the least agency that delivers the value.** Inventory every tool and action by data scope, privilege, externality, cost, reversibility, and failure radius. Prefer read-only, preview, recommendation, or draft modes before autonomous mutation.
- **Keep intent separate from content.** Treat retrieved pages, documents, messages, tool results, memory, and peer-agent output as untrusted data. They may inform a plan but must not silently redefine the user's goal, authority, or policy.
- **Bind authority to the exact action.** Show the actor, target, consequential parameters, data leaving the boundary, cost or commitment, and reversible/irreversible effect before a high-impact action. Re-authorize when the goal, recipient, destination, privilege, or impact changes; a generic chat approval is not a permanent mandate.
- **Preview before commitment.** For consequential writes, provide a dry run, diff, recipient/target preview, or equivalent plan view. Approval must attach to the reviewed plan revision, expire when it changes materially, and never authorize hidden follow-on actions.
- **Constrain execution outside the model.** Use deterministic policy enforcement, least-privilege and short-lived credentials, allowlisted destinations, typed tool contracts, rate/cost/time budgets, idempotency, circuit breakers, and fail-closed resolution for ambiguous tools or identities. UI confirmation cannot substitute for service-side authorization.
- **Make delegation attributable.** Distinguish the user, orchestrator, sub-agent, tool, and external service; preserve scope through each handoff; prevent privilege inheritance by convenience; and expose the responsible actor for every consequential step.
- **Make progress truthful and interruptible.** Show current stage, completed and pending actions, resource use where material, partial success, and what pause/cancel can still prevent. Do not present a plan as executed or a queued action as complete.
- **Issue a usable receipt.** Record the approved goal and plan revision, action/target, authority source, material inputs and outputs, tool/service, status, time, cost where relevant, and recovery path without exposing secrets or unnecessary reasoning traces.
- **Design real recovery.** Specify safe retry, rollback or compensating action, revocation, correction, incident escalation, and residual effects. Do not label a cosmetic UI reversal as undo when the external action remains active.
- **Increase autonomy only from evidence.** Expand automation gradually when measured reliability, user control, and low failure consequence justify it; preserve an understandable manual path or human escalation for consequential work.

Threat-model at least indirect prompt injection, goal hijack, excessive agency, tool misuse, identity/privilege abuse, poisoned memory/context, compromised tool or agent supply chain, insecure delegation, runaway cost or loops, cascading partial failure, and human-agent trust exploitation. Redesign findings should identify the user-visible control and the required service/security control separately. This review is not a penetration test, security certification, or compliance decision; route consequential systems to qualified security review.

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
- agentic runs preserve the user's goal, use least agency, bind approval to an exact plan/action, expose progress and receipts, and provide bounded recovery;
- responsive, RTL/LTR, accessibility, performance, privacy, and telemetry are specified;
- no capability disappeared solely as a cosmetic simplification;
- acceptance criteria cover at least one full cross-role handoff and one costly failure/recovery journey.
