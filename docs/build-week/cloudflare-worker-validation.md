# Cloudflare Worker Validation Record

**Date:** 2026-07-18

**Branch:** `codex/cloudflare-worker-runtime`

**Starting commit:** `ccec44bd674c761fe3e4b335c56442f6ef7be912`

**Review commit:** pending human review

## Scope

This milestone adds the locally testable Worker/static-assets runtime selected after Phase 1
security remediation. It does not complete Phase 1: live TMCO Intune validation and an operational
OpenAI call remain outstanding. It also does not create Cloudflare resources, DNS, secrets, a
production deployment, or a deployment workflow.

Implemented runtime controls include:

- selective Worker-first `/api/*` routing with scanned `site/` static assets;
- explicit fixture and OpenAI modes with no silent fallback;
- same-origin, exact-method, JSON/content-encoding, request-size, rate, timeout, and response bounds;
- repeated publication/credential scanning before model egress;
- strict public-package and structured-output contracts;
- deterministic exact-coverage narrative verification and unrestricted-prose quarantine;
- allowlisted structured logging and static CSP/security headers; and
- exact-pinned Node tooling, workerd tests, binding drift checks, dry-run bundle, and credential-free CI.

## Local validation

The final credential-free run produced:

```text
npm ci --ignore-scripts --no-audit --no-fund
  PASS — 89 exact-lock packages installed

npm run validate:worker
  PASS — Prettier, type-aware Oxlint, strict runtime/test TypeScript,
         18 workerd contract tests, generated-binding check, and fixture/production dry-runs

npm audit --audit-level=moderate
  PASS — 0 vulnerabilities

python -m ruff format --check .
  PASS — 40 Python files already formatted

python -m ruff check .
  PASS

python -m mypy
  PASS — no issues in 40 source files

python -m pytest
  PASS — 151 passed, 1 opt-in live test skipped, 91.13% branch-aware coverage

python -m bandit -r evidenceops scripts -c pyproject.toml
  PASS — no findings; 2,803 source lines scanned

python scripts/check_secrets.py
  PASS

python -m pip_audit -r requirements-dev.txt
  PASS — no known vulnerabilities

python -m evidenceops rebuild-static-demo
git diff --exit-code -- docs/assets/data
  PASS — synthetic data rebuilt byte-for-byte

python -m evidenceops run-demo --output-dir <clean-temporary-directory>/output
python scripts/check_public_artifacts.py <clean-temporary-directory>/output
  PASS — complete synthetic evidence flow and output scan

mkdocs build --strict
python scripts/check_public_artifacts.py site
  PASS — static artifact and Worker frontend built and scanned

python -m pip wheel --no-deps --no-build-isolation .
  PASS — wheel contains all three shared JSON policy/schema catalogs

git diff --check
  PASS
```

Local HTTP smoke validation used `wrangler dev --local` in fixture mode. `GET /api/status` and
`GET /live-demo/` returned HTTP 200. Posting the tracked public package to `/api/narrative`
returned HTTP 200 with `ai_model_call_performed: false`, four typed claims accepted, fourteen
generated-prose entries quarantined, and human review required. The local process then shut down.

The workerd corpus verifies same-origin and method enforcement, browser-key rejection, native rate
handling, compression/content-length/byte bounds, shared credential patterns, unknown fields,
tampered fingerprints, fixture identity, one fixed OpenAI request, no silent fallback, exact
finding coverage, unknown claims, unsupported verdicts, and unrestricted-prose quarantine.

## External validation intentionally not performed

- No Microsoft Graph or Intune request was made.
- No OpenAI API request or paid model call was made; transport tests use a local mock response.
- No Cloudflare account/resource, Worker secret, DNS record, custom domain, or deployment was created.
- No GitHub workflow deployed code or received a Cloudflare/OpenAI credential.

## Outstanding production gates

Human review, provider budget/abuse controls, Cloudflare actor/zone verification, secret creation,
manual preview/production deployment, external TLS/header/route checks, and rollback validation are
required before GitHub deployment orchestration is considered.
