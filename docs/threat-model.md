# Threat Model

This Phase 1 model covers the public repository, unprivileged CI, local static build, live read-only
adapter, private evidence writer, sanitizer, OpenAI boundary, deterministic verifier, and
synthetic demo, and the locally validated Cloudflare Worker/static-assets runtime. Cloudflare
resources, DNS, production secrets, and external production behavior remain outside the validated
state because nothing has been deployed.

## Assets

- Desired configuration and approval history
- Private normalized Intune evidence and source trace identifiers
- Sanitized packages, evidence IDs, and fingerprints
- Graph/OpenAI credentials and pseudonymization key material
- Future workload identity and repository administration rights
- Generated narratives, verifier results, and human decisions

## Trust boundaries

| Boundary | Untrusted or private side | Validated side |
| --- | --- | --- |
| Pull request | Contributor code and fixtures | Protected `main` |
| Graph | Tenant response and bearer token | GET-only normalizer |
| Private storage | Traceable normalized evidence | Ignored restrictive directory |
| Publication | Private package and runtime key | Sanitized public package |
| OpenAI | External service and generated object | Deterministic verifier |
| Static build | Repository content | Scanned local `site/` artifact |
| Cloudflare runtime | Browser request and future Worker secret | Same-origin bounded API, publication gate, rate limiter, verifier |

## Primary threats and controls

| Threat | Impact | Phase 1 control | Residual/deferred control |
| --- | --- | --- | --- |
| Credential committed | Account compromise | Ignore rules and location-only secret scan | Organization incident drill |
| Private package reaches static/public assets | Re-identification | Separate writer, MkDocs exclusion, path/content scan | Signed publication manifest |
| Graph adds a sensitive field | Silent disclosure | Explicit normalization and unknown-field publication failure | Live canary contract monitoring |
| Fork obtains collection credential | Tenant disclosure | No public live workflow or credentials | OIDC subject/environment policy in private repo |
| Graph permission or verb expands | Endpoint mutation | One read permission and GET-only transport/tests | Dedicated manifest/AST policy gate |
| Narrative omits/duplicates evidence | Audit error | Exact unique finding-ID set equality | Broader evaluation corpus |
| Narrative reverses status in prose | Audit error | Typed claims only; all prose quarantined | Explicit human approval workflow |
| OpenAI receives private data | Tenant disclosure | Validated public shape plus repeated shared content/credential scan; size bound; no tools | Worker egress policy |
| Device-code token persists | Tenant access | In-memory MSAL cache; no token logging | Managed workstation controls |
| Pseudonym correlation leaks identity | Re-identification | Runtime-only key and content scans | Key rotation/mapping governance |
| Action dependency compromised | Build compromise | Immutable action SHAs and least privilege | Organization dependency review |
| Browser submits a key or cross-site request | Key exposure or spend abuse | BYOK/authorization headers rejected; strict Origin/Sec-Fetch-Site | Revisit only under a dedicated BYOK threat model |
| Public client floods narrative route | Cost or availability loss | Native rate binding, request bound, one attempt, timeout | Account budget alerts, WAF/abuse telemetry, authenticated tier if needed |
| Model or upstream returns oversized/hostile JSON | Resource exhaustion or false evidence | Response bound, strict schema, shared scanner, deterministic verifier | Production alerting and evaluation corpus |
| Logs disclose input or secret | Data or credential exposure | Structured allowlisted metadata only; no body/header logging | Verify Cloudflare log sinks and retention before deployment |

## Abuse cases covered by tests

- A contributor disguises a fake domain, email, serial, IP, GUID, token, or key as allowed text.
- A response nests an unclassified field under a private/dropped object.
- Graph returns a malformed page, hostile `nextLink`, unsupported policy type, or wrong field type.
- A narrative duplicates, omits, or invents a finding ID; changes a typed status; uses contradictory
  synonyms in prose; or declares compliance.
- A static artifact contains a `private`, `raw`, `exports`, or `artifacts` path.
- Any supported GitHub token family appears in publication, repository, static, or model-egress
  content.
- An operator chooses a nonignored private directory or attempts to overwrite an artifact.

## Assumptions and exclusions

The model assumes GitHub, Entra, and OpenAI administrative accounts are separately protected and
that an operator does not deliberately publish private files outside EvidenceOps. Endpoint
compromise, assessment-framework interpretation, remediation, tenant rollback, and external
service availability are outside this proof.

## Review triggers

Update this model before expanding Graph endpoints/settings/permissions, adding a provider,
creating a credentialed workflow, changing retention, accepting model tools, adding authentication,
adding Worker/API routes or BYOK, changing rate/spend controls, provisioning a secret or custom
domain, deploying tenant-specific infrastructure, or introducing a new public field.
