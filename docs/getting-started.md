# Getting Started

Python 3.12 or later is required. Public CI and the demo use no tenant or OpenAI credential.

## Install from a clean environment

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python -m pip install --no-build-isolation --no-deps .
```

Dependencies are exactly pinned. The runtime evidence path uses the Python standard library;
`msal` is included only for attended live collection. The optional `ai` extra pins `certifi` for
Python installations that lack a usable platform CA bundle; the development lock already includes
it.

## Three-minute synthetic demonstration

```bash
python -m evidenceops run-demo --output-dir build/synthetic-demo
python scripts/check_public_artifacts.py build/synthetic-demo
mkdocs build --strict
python scripts/check_public_artifacts.py site
```

Open `site/live-demo/index.html`, then `site/evidence-dashboard/index.html`. The walkthrough shows
four deterministic outcomes, machine-verified typed status claims, generated prose quarantined for
human review, and an adversarial verdict rejected for an additional policy reason. The fixture
demonstrates the GPT contract but is clearly labeled as not originating from a live model call.

## Command boundary

```text
run-demo                 credential-free synthetic end-to-end flow
live-collect             GET-only Intune collection into ignored private storage
publish                  validate, sanitize, scan, and emit a selected public package
generate-narrative       optional GPT-5.6 call using only the public package
verify-narrative         deterministic acceptance or quarantine
rebuild-static-demo      regenerate tracked synthetic static-build data
```

There is deliberately no `apply`, remediation, assignment, profile, deployment, rollback, or
exception command. Live mode never falls back to synthetic mode.

## Optional live and GPT workflows

Live collection requires a separately approved Entra app and explicit authentication choice; see
[Live Collection](operations/live-collection.md). Publication requires a runtime-only
`EVIDENCEOPS_PSEUDONYM_KEY` of at least 32 bytes. Optional narrative generation reads
`OPENAI_API_KEY` and defaults to `gpt-5.6-sol`.

No successful paid model call is required or claimed by the static demo. The selected future
Cloudflare runtime will use a dedicated EvidenceOps Project service-account/project key stored only
as a Worker secret. This repository does not create that key or secret. BYOK is deferred pending a
separate browser-key threat model.

EvidenceOps does not load `.env` files. Environment-variable names appear in `.env.example`, but
operators must use a local process environment or managed secret store. Never add a real value to
the repository.

## Full validation

```bash
python -m ruff format --check .
python -m ruff check .
python -m mypy
python -m pytest
python -m bandit -r evidenceops scripts -c pyproject.toml
python scripts/check_secrets.py
python -m pip_audit -r requirements-dev.txt
mkdocs build --strict
python scripts/check_public_artifacts.py site
```

The test command enforces 90% branch-aware coverage. All public artifacts must pass the final scan.

## Static-build hosting compatibility

`mkdocs build --strict` produces `site/` with relative navigation and self-contained public assets.
That directory is suitable as the input to the selected future Cloudflare Workers Static Assets
milestone. There is currently no Wrangler configuration, Worker API, custom domain, DNS record,
deployment workflow, or production deployment.
