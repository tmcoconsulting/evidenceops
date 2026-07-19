# Cloudflare Worker Validation Record

**Date:** 2026-07-18

**Branch:** `codex/cloudflare-worker-runtime`

**Starting commit:** `ccec44bd674c761fe3e4b335c56442f6ef7be912`

**Human-reviewed Worker checkpoint:** `7683c69f9eaca9f67ec220de5fb9f1a19fe9b3df`

**Runtime hardening commit:** `f8994d9`

**Protected workflow support:** `925e0f8`

**Externally validated egress/runtime fix:** `cfd9975`

## Scope

This milestone adds and deploys the Worker/static-assets runtime selected after Phase 1 security
remediation. It does not complete Phase 1: live TMCO Intune validation and a successful generated
OpenAI narrative remain outstanding. Production intentionally serves the synthetic fixture after
the bounded OpenAI validation returned capacity unavailable.

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
         25 workerd contract tests, generated-binding check, and fixture/preview/production dry-runs

npm audit --audit-level=moderate
  PASS — 0 vulnerabilities

python -m ruff format --check .
  PASS — 40 Python files already formatted

python -m ruff check .
  PASS

python -m mypy
  PASS — no issues in 40 source files

python -m pytest
  PASS — 152 passed, 1 opt-in live test skipped, 91.13% branch-aware coverage

python -m bandit -r evidenceops scripts -c pyproject.toml
  PASS — no findings; 2,829 source lines scanned

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

The final documentation build initially failed closed when this record included a Cloudflare
version UUID. The operational identifier was removed from public content, the site was rebuilt,
and the complete public-artifact scan then passed.

Local HTTP smoke validation used `wrangler dev --local` in fixture mode. `GET /api/status` and
`GET /live-demo/` returned HTTP 200. Posting the tracked public package to `/api/narrative`
returned HTTP 200 with `ai_model_call_performed: false`, four typed claims accepted, fourteen
generated-prose entries quarantined, and human review required. The local process then shut down.

The workerd corpus verifies same-origin and method enforcement, browser-key rejection, native rate
handling, compression/content-length/byte bounds, shared credential patterns, unknown fields,
tampered fingerprints, fixture identity, one fixed OpenAI request, no silent fallback, exact
finding coverage, unknown claims, unsupported verdicts, and unrestricted-prose quarantine.

## External validation

- Verified the authenticated TMCO Consulting Cloudflare account and active `tmcoconsulting.com`
  zone without modifying unrelated Workers or DNS.
- Deployed credential-free preview `evidenceops-preview` and production Worker `evidenceops`.
- Attached `evidenceops.tmcoconsulting.com` as a Worker Custom Domain; public DNS, TLS hostname
  coverage, HTTPS, CSP, HSTS, static assets, and API status returned success.
- Verified same-origin, method, browser-key, authorization, media-type, compression, publication,
  fingerprint, verifier, and native-rate boundaries. A ten-request preview burst returned six 429s.
- Created one key under the exact OpenAI Platform EvidenceOps project and transferred it directly to
  the encrypted Worker secret `OPENAI_API_KEY`; no plaintext file remained.
- Confirmed the project key lists all three GPT-5.6 model identifiers and kept the fixed runtime pin
  at `gpt-5.6-terra` for balanced cost and capability.
- A bounded synthetic production request reached OpenAI and returned capacity unavailable. No model
  output was returned, accepted, logged, or published. Production was then returned to explicit
  fixture mode, where the verifier accepted four typed status claims and quarantined fourteen prose
  fields for human review.
- Disabled the legacy GitHub Pages site/environment. Created a branch-restricted GitHub production
  environment and nonsecret variables; Cloudflare deployment remains disabled pending a narrow
  environment token.

## External validation not performed

- No Microsoft Graph or Intune request was made because the Entra FIC/admin-consent state could not
  be configured without an authenticated Entra administrative session.
- OpenAI project budget alerts and per-model limits could not be inspected or changed because the
  Platform administrative UI required sign-in. A budget would be a soft alert, not a hard cap.
- A Cloudflare GitHub deployment token was not created because Wrangler OAuth cannot mint API
  tokens and the dashboard required sign-in.
- No production rollback was executed because earlier versions used live model mode; the CLI
  deployment history and rollback command were verified instead.
