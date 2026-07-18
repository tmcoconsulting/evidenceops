# Roadmap

Roadmap items describe intent, not operational capability or delivery commitments.

## Phase 0 — complete foundation

- Public Apache-2.0 repository, governance, CI, and protected main
- Historical GitHub Pages foundation (deployment path retired during Phase 1 security review)
- Provider-neutral domain, deterministic drift, fail-closed sanitizer, and synthetic demo
- Security/data-handling boundaries and Build Week evidence

## Phase 1 — narrow proof on this branch

- Ten versioned schema-v1 objects with tamper-evident IDs/fingerprints
- GET-only Graph v1.0 Intune adapter for two macOS general-configuration fields
- Exact read-permission manifest and in-memory attended authentication
- Private package writer, explicit retention, and fail-closed public publication
- Four-state vendor-neutral desired/observed demonstration
- Optional GPT-5.6 structured narrative plus typed-claim/prose-quarantine verifier
- Credential-free end-to-end CLI and polished local synthetic static walkthrough
- Shared credential detection across publication, repository/static scans, and model egress

Live TMCO validation remains pending until approved Entra client/tenant configuration or a
short-lived Graph token is available. Public CI never performs live collection.

## Selected next milestone: Cloudflare runtime (not implemented)

- Add an exact-pinned Cloudflare Workers toolchain and Static Assets configuration for `site/`
- Implement same-origin `/api/status` and `/api/narrative` with strict method/body/rate limits
- Store a dedicated EvidenceOps Project OpenAI key only as a Cloudflare Worker secret
- Preserve fixture mode when API credits or the service key are unavailable
- Add Worker tests, log redaction, CSP/security headers, spend controls, and abuse protections
- Configure `evidenceops.tmcoconsulting.com`, rollback, and least-privilege GitHub deployment only
  after the runtime passes independent review

## Later application scope

- Privately validate the two documented Graph endpoints and record only sanitized metadata
- Add an independent reviewer for the permission/normalization contract
- Evaluate Settings Catalog support only after confirming a supported v1.0 contract
- Add a signed public-package manifest and broader narrative evaluation corpus
- Design explicit exception ownership/expiry without automatic exception grants
- Explore Jamf and Workspace ONE adapters against the same schema contract
- Reassess request-scoped BYOK only after a browser-key, logging, and abuse threat model

## Explicitly deferred or rejected

- Intune/Graph writes, automatic remediation, assignment, or rollback
- Generic raw-tenant data lake or managed-device identity inventory
- Scheduled live workflow in the public repository
- Directory-wide or managed-device permissions for convenience
- Model tools, autonomous publication, exceptions, or compliance verdicts
- Browser-persisted API keys or public-CI OpenAI credentials
- Claims of complete CIS/STIG/NIST/CMMC coverage
- Code/history imports from unrelated endpoint-management repositories
