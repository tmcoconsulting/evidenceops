# Cloudflare Worker Runtime

## Current state

The Worker runtime is deployed at `https://evidenceops.tmcoconsulting.com/` in explicit fixture
mode. The credential-free preview is available at
`https://evidenceops-preview.tmco-consulting.workers.dev/`. The custom domain/TLS, Static Assets,
dual native rate limiters, and encrypted `OPENAI_API_KEY` binding are active. Fixture mode does not
call OpenAI.

Cloudflare Workers Static Assets serves the scanned MkDocs `site/` directory. The
[`run_worker_first`](https://developers.cloudflare.com/workers/static-assets/binding/#run_worker_first)
configuration sends only `/api/*` through Worker code before static-asset handling.

## Local fixture validation

Node.js 22 or later and Python 3.12 or later are required.

```bash
npm ci --ignore-scripts --no-audit --no-fund
python -m evidenceops rebuild-static-demo
mkdocs build --strict
python scripts/check_public_artifacts.py site
npm run validate:worker
npm run dev
```

The development script disables Wrangler `.env` and `.dev.vars` loading. Visit the local URL
printed by Wrangler and open **Live Demo**. The status panel must show `Fixture runtime ready`.
Running the narrative produces the tracked fixture and reports `Model call performed: no`.

## Same-origin API contract

| Route | Method | Public behavior |
| --- | --- | --- |
| `/api/status` | `GET` | Returns mode, model name, synthetic/public boundary, and safety flags; never a secret |
| `/api/narrative` | `POST` | Accepts one sanitized public package; returns narrative plus deterministic verification |

The narrative route enforces, in order:

1. exact method and same-origin `Origin`/`Sec-Fetch-Site` checks;
2. rejection of browser `Authorization` and `X-OpenAI-Key` headers;
3. client-keyed and global native rate limits; the one-way client digest is never logged;
4. JSON-only, identity-encoded input with a 64 KiB limit and strict UTF-8;
5. the explicit publication-field policy and shared credential/public-value catalog;
6. strict public-package schema and evidence-reference validation;
7. exact fixture identity in fixture mode, or one bounded Responses API request in OpenAI mode;
8. strict model-output schema, repeated egress scan, and deterministic verifier; and
9. a human-review-required response with generated prose quarantined.

OpenAI mode pins `gpt-5.6-terra`, uses `store: false`, exposes no tools, makes no retry, times out
after 20 seconds, caps output at 1,600 tokens, and reads at most 256 KiB of response JSON. It never
falls back to fixture output.
The public production deployment remains in explicit fixture mode while the OpenAI project returns
capacity unavailable. A bounded production request proved that the Worker reached OpenAI, but no
model output was returned or accepted. Fixture mode makes no OpenAI request and does not silently
fall back from a failed live call.

## Secret and logging boundary

The project-scoped runtime key belongs only in the encrypted
[Worker secret](https://developers.cloudflare.com/workers/configuration/secrets/). It must not be a
Wrangler plain-text variable, GitHub public-CI secret, browser value, repository file, build
argument, or log field. The Worker logs only event code, request ID, method, route, and status. It
does not log client IPs, headers, packages, prompts, model responses, or error bodies.

The `global_fetch_strictly_public` compatibility flag forces the fixed OpenAI hostname through its
public route rather than treating it as an implicit Worker-to-Worker service binding. No arbitrary
egress target is accepted from a request.

Browser BYOK is deliberately unsupported. It would make EvidenceOps a credential processor and
requires its own browser storage, transit, redaction, support, exfiltration, and abuse design.

## Production validation and remaining gates

Completed: account/zone verification, preview and production deployment, custom-domain/TLS checks,
static/API/header tests, fixture verification, rate-limit proof, and secure Worker-secret transfer.
The bounded live request reached OpenAI and returned capacity unavailable; no output was accepted.

Remaining:

1. sign in to **OpenAI Platform → EvidenceOps project → Limits**; set a small `$5` monthly soft
   budget with 50%, 80%, and 100% alerts, allow only `gpt-5.6-terra`, and start with at most 5 RPM
   and 25,000 TPM (or the lowest supported values that still allow the bounded demo); this budget
   is an alert threshold and does not stop spending;
2. if the project UI permits, create service account `evidenceops-cloudflare-runtime`, transfer its
   replacement project key directly to the existing Worker secret, validate once in synthetic mode,
   and then revoke the current user-owned project key;
3. in **Cloudflare → My Profile → API Tokens**, create `evidenceops-github-deploy` restricted to the
   TMCO Consulting account and `tmcoconsulting.com` zone with Account `Workers Scripts Edit` and
   `Account Settings Read`, Zone `Workers Routes Edit`, and User `User Details Read` plus
   `Memberships Read`; do not add KV, R2, DNS, billing, or unrelated-account access;
4. store the one-time value only as the protected GitHub environment secret
   `CLOUDFLARE_API_TOKEN`, then change `CLOUDFLARE_DEPLOY_ENABLED` to `true` after review;
5. review Cloudflare observability/alert retention in the dashboard;
6. use `wrangler deployments list --env production` and
   `wrangler rollback <known-good-version> --env production` for rollback; and
7. enable OpenAI mode only after a single bounded request succeeds and the dashboard label is
   revalidated.

Cloudflare documents [Worker secrets](https://developers.cloudflare.com/workers/configuration/secrets/),
[custom domains](https://developers.cloudflare.com/workers/configuration/routing/custom-domains/),
and [rollbacks](https://developers.cloudflare.com/workers/configuration/versions-and-deployments/rollbacks/).
