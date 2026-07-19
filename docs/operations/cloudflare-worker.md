# Cloudflare Worker Runtime

## Current state

The Worker runtime is implemented and validated locally. It is **not deployed**. No Cloudflare
resource, DNS record, custom-domain attachment, production secret, or deployment workflow has been
created. The default configuration is fixture mode and does not call OpenAI.

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
3. native rate limiting keyed by a one-way request-origin/client digest that is never logged;
4. JSON-only, identity-encoded input with a 256 KiB limit and strict UTF-8;
5. the explicit publication-field policy and shared credential/public-value catalog;
6. strict public-package schema and evidence-reference validation;
7. exact fixture identity in fixture mode, or one bounded Responses API request in OpenAI mode;
8. strict model-output schema, repeated egress scan, and deterministic verifier; and
9. a human-review-required response with generated prose quarantined.

OpenAI mode pins `gpt-5.6-sol`, uses `store: false`, exposes no tools, makes no retry, times out
after 30 seconds, and reads at most 1 MiB of response JSON. It never falls back to fixture output.
The model call is mocked in tests; no paid request is claimed.

## Secret and logging boundary

The future service key belongs only in an encrypted
[Worker secret](https://developers.cloudflare.com/workers/configuration/secrets/). It must not be a
Wrangler plain-text variable, GitHub public-CI secret, browser value, repository file, build
argument, or log field. The Worker logs only event code, request ID, method, route, and status. It
does not log client IPs, headers, packages, prompts, model responses, or error bodies.

Browser BYOK is deliberately unsupported. It would make EvidenceOps a credential processor and
requires its own browser storage, transit, redaction, support, exfiltration, and abuse design.

## Production-change checklist (not yet executed)

Before any production command:

1. Review `wrangler.jsonc`, the Worker diff, dependency audit, dry-run bundle, and threat model.
2. Verify the Cloudflare account/zone actor and authorization for `tmcoconsulting.com`.
3. Establish OpenAI project budget limits/alerts and Cloudflare abuse/rate monitoring.
4. Confirm log destinations and retention do not exceed the documented allowlist.
5. Create the Worker secret interactively for the `production` environment; never echo it.
6. Deploy manually to a preview or controlled production target and capture the version ID.
7. Verify `/api/status`, static navigation/assets, CSP/security headers, API rejection paths, TLS,
   and `evidenceops.tmcoconsulting.com` from outside the operator workstation.
8. Exercise Cloudflare version rollback before adding automated deployment.
9. Add GitHub orchestration only with a protected environment and the minimum Cloudflare
   deployment credential or supported short-lived mechanism.

Cloudflare documents [Worker secrets](https://developers.cloudflare.com/workers/configuration/secrets/),
[custom domains](https://developers.cloudflare.com/workers/configuration/routing/custom-domains/),
and [rollbacks](https://developers.cloudflare.com/workers/configuration/versions-and-deployments/rollbacks/).
