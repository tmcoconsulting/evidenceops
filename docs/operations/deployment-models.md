# Deployment Models

Phase 1 currently implements only the credential-free local build and the Python application core.
The remaining models document selected or possible deployment boundaries; they do not create
tenant infrastructure, Cloudflare resources, DNS, secrets, or credentialed workflows.

## 1. Current local synthetic static artifact

Public CI uses no tenant or OpenAI credential. It regenerates tracked synthetic data, builds
`site/` with MkDocs, and scans that directory. Operators can serve the result locally. `site/` is a
build artifact, not evidence that a hosting platform or production API is operational.

## 2. Selected next milestone: Cloudflare Workers Static Assets

The planned public runtime is a Worker at `evidenceops.tmcoconsulting.com` serving the scanned
`site/` directory as static assets. Only `/api/*` should run Worker code first; the initial
same-origin endpoints are `/api/status` and `/api/narrative`. Cloudflare documents selective
[`run_worker_first`](https://developers.cloudflare.com/workers/static-assets/binding/#run_worker_first)
routing and encrypted [Worker secrets](https://developers.cloudflare.com/workers/configuration/secrets/).

The next milestone must add, review, and test:

1. an exact-pinned Wrangler toolchain and configuration whose assets directory is `site/`;
2. a small typed Worker with explicit method, origin, body-size, timeout, and response limits;
3. `/api/status` with no sensitive operational metadata;
4. `/api/narrative` accepting only a bounded sanitized evidence package and preserving the existing
   typed output and deterministic verification contract;
5. the EvidenceOps Project service-account/project key as a Cloudflare Worker secret only;
6. rate, spend, abuse, logging-redaction, CSP, and human-approval controls;
7. custom-domain and rollback verification; and
8. a least-privilege GitHub deployment workflow only after the runtime is independently validated.

OpenAI recommends keeping API keys out of code/public repositories and exposing them through a
secret manager. It also recommends human review for high-stakes output:
[production practices](https://developers.openai.com/api/docs/guides/production-best-practices) and
[safety practices](https://developers.openai.com/api/docs/guides/safety-best-practices).

Fixture mode must remain available when credits or the runtime key are unavailable. Browser BYOK
is deferred: a browser-supplied key would cross the Worker, logging, support, and abuse boundaries.
If later approved, it must be request-scoped, never persisted or logged, never written to browser
storage, and clearly separated from the TMCO-funded service-account path.

## 3. Later private collection and sanitized publication

Where GitHub plan and policy support the design, keep collection in a private repository and use a
protected environment for publication. Authenticate GitHub Actions to Entra with OIDC/workload
identity federation, constrain the federated subject to the repository, branch/tag, and protected
environment, and grant only application `DeviceManagementConfiguration.Read.All`.

The private workflow should:

1. request `id-token: write` only in the collection job;
2. exchange the GitHub OIDC token for a short-lived Entra token;
3. collect to ephemeral restricted storage without logging responses;
4. sanitize and run policy/content tests before any artifact upload;
5. upload only the sanitized package with minimal retention;
6. require protected-environment approval before any sanitized package or deployment crosses its
   intended trust boundary; and
7. deny secrets and privileged jobs to fork-originated pull requests.

GitHub explains that OIDC avoids duplicated long-lived cloud secrets and yields job-scoped,
short-lived credentials in its [OIDC security guide](https://docs.github.com/actions/concepts/security/openid-connect).
Microsoft documents the corresponding
[workload identity federation](https://learn.microsoft.com/entra/workload-id/workload-identity-federation)
trust model.

The repository includes a deliberately non-executable
[`examples/private-repository/intune-oidc.yml`](https://github.com/tmcoconsulting/evidenceops/blob/main/examples/private-repository/intune-oidc.yml)
reference. It is outside `.github/workflows`, pins actions to commit SHAs, collects with a
process-scoped Graph token, and uploads nothing. Copy it only after reviewing the Entra subject,
audience, tenant/application IDs, environment protection, retention, and publication topology.

## 4. Private corporate or enterprise presentation

A private repository may orchestrate the same collection and sanitization controls and present the
application through an access-controlled Worker or another approved internal platform. Repository
privacy does not weaken the private/public package boundary, OIDC restriction, retention,
sanitizer, verifier, or human approval gates, and it is never a reason to publish raw Graph
responses.
