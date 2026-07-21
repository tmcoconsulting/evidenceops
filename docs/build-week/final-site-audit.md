# Final Site Audit

Audit date: 2026-07-21. Production target:
`https://provifact.tmcoconsulting.com/`. This was a read-only review; no model request, tenant
collection, deployment, or cloud configuration change was made.

## Result

The production site is materially functional and judge-ready in information architecture,
traceability, security messaging, and public evidence behavior. All 32 sitemap URLs and all 15
sampled authoritative external links returned HTTP success. TLS and browser security headers were
present. The current public package validated as live sanitized tenant data at audit time.

The submission remains **conditional** because production evidence will cross its 24-hour freshness
limit before the submission deadline unless refreshed, the displayed two-device aggregate does not
yet explain the expected three-device test fleet, and the fixes on this branch are not deployed.

## Page matrix

| Page | Judge question answered | Audit result |
| --- | --- | --- |
| Landing | What problem is solved, how does the chain work, and where do I start? | Pass; this branch removes an unsupported “continuous” cadence claim and improves skip/social semantics |
| Mission Control | What is approved, observed, drifting, missing, fresh, and traceable now? | Pass; 98 rules, four exact joins, deterministic findings, gaps, privacy, and Assistant are visible |
| Baseline Plan | What is implemented versus still to plan, and how does the company target compare to public references? | Pass; 17 profiles and 309 exact rule memberships, with no framework verdict |
| Judge Guide | Can I understand the product in three minutes? | Pass |
| Runtime Status | Is the Worker/model boundary real or fixture-based? | Pass with terminology clarification below |
| Getting Started | Can a judge run it without credentials? | Pass |
| Live Collection | Are Graph endpoints, permissions, OIDC, retention, and publication controls explicit? | Pass |
| Architecture / Security | Are authority and trust boundaries credible? | Pass |
| Video / Submission docs | Can the operator finish safely? | Replaced by the final dynamic-value recording and Devpost packet on this branch |

## Accessibility and responsive findings

This branch:

- gives Mission Control a real heading target for Material's skip link;
- makes large Mission Control tables focusable, labeled scroll regions;
- allows command actions to wrap on narrow screens;
- replaces tiny one-line horizontal Assistant suggestion cards with readable wrapping grid buttons;
- preserves the generated-analysis label and limitations when session history is restored; and
- emits a page-specific social title and description while retaining the approved social card.

The desktop information hierarchy, keyboard-operable native controls, unique titles, canonical
URLs, heading structure, alt text, and social image passed source/production inspection. Final
browser verification after deployment remains required for keyboard focus order, narrow breakpoints,
console output, and social-card fetch behavior.

## Production-state qualifications

### Freshness

The audited package was collected `2026-07-20T21:28:14Z` with a 24-hour maximum age. It reported
`current` during the audit but becomes stale at `2026-07-21T21:28:14Z`, before the 5:00 PM PDT
submission deadline. The site will fail closed to degraded/stale state. Run the protected refresh
after merge and before recording.

### Device aggregate

The public package reports two managed Apple devices: one macOS and one iOS. The expected test fleet
was described as one Mac, one iPhone, and one iPad. The audit did not inspect private device data and
does not infer why one device is absent. Validate enrollment, platform classification, Graph return,
and normalization privately during the protected refresh. Until explained, narrate only the public
aggregate actually displayed.

### Assistant modes

Production `/api/status` reports the active `/api/ask` runtime as OpenAI with fixed
`gpt-5.6-terra`. The Mission package retains `ai.mode: fixture` for its package-bundled offline
narrative metadata. Those fields describe separate boundaries: GPT does not build or change the
Mission package. The architecture now states that distinction explicitly.

### Baseline label

The human-approved record is named **TMCO Consulting macOS CIS Level 1 Demo Baseline**. UI controls
shorten this to **TMCO Consulting Approved**. Removing “Demo” from the canonical record would be a
new organization approval decision, not a cosmetic edit, so this branch documents the current truth
instead of rewriting approval history.

## Security observations

- GET-only Graph, fail-closed publication, credential catalogs, exact mapping review, immutable
  workflow pins, CodeQL, server-side OpenAI secret, no BYOK, rate limits, CSP, and typed-claim
  verification were present.
- No open CodeQL, secret-scanning, or Dependabot alert was reported by the repository audit.
- Material for MkDocs requires inline script/style allowances in the current CSP. Repository code
  renders evidence with safe DOM text APIs; moving to nonce/hash-only policy is post-submission
  hardening.
- CodeQL is green but is not a required branch-protection context. Signed commits are disabled, and
  production-environment administrators may bypass protection. These are recorded single-maintainer
  tradeoffs, not hidden as completed controls.

## Recording readiness

Do not record until:

1. this branch is reviewed, merged, and deployed through protected `main`;
2. a fresh protected audit explains or accurately preserves the device aggregate;
3. production status, package fingerprint, and security headers pass;
4. the Assistant succeeds once and keeps its generated/review-required boundary after reload; and
5. the final video checklist is complete.
