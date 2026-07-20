# Final Live MVP Pre-Merge Validation

**Date:** 2026-07-20

**Branch:** `codex/build-week-final-live-mvp`

**Implementation commit:** `143f694f7183f1a2ce117a3a0867aad316f7a1ae`

**Human review:** required before merge

**External state:** no live collection or deployment was performed from this feature branch

## Validated scope

- Exact reviewed Microsoft Intune provider-definition mappings; no display-name or substring join
- Mission schema `2.1.0`, public-safe parent references, and current/prior live snapshot comparison
- Live-artifact-only production workflow with exact audit-run and snapshot provenance
- Action-first Mission Control, compact Settings detail, global provenance, and snapshot refresh
- Site-wide bounded Evidence Copilot with production `gpt-5.6-terra` and local/preview fixture mode
- Official owner-approved TMCO Consulting assets and standalone-company-name content gate
- Preserved GET-only Graph provider, fail-closed publication, deterministic authority, and no BYOK

## Clean environment

A new Python 3.14.6 virtual environment was created outside the repository. Exact locked
dependencies installed from `requirements-dev.txt`; the package installed with
`--no-build-isolation --no-deps`; `pip check` reported no broken requirements. Public CI remains
pinned to Python 3.12.

## Commands and results

```text
python -m ruff format --check .
  PASS — 60 files formatted
python -m ruff check .
  PASS
python -m mypy
  PASS — no issues in 60 source files
python -m pytest
  PASS — 228 passed, 1 skipped, 90.62% branch coverage
python -m bandit -r evidenceops scripts -c pyproject.toml
  PASS — no findings; 6,255 source lines scanned
python scripts/check_company_name.py
  PASS
python scripts/check_secrets.py
  PASS
python -m pip_audit -r requirements-dev.txt
  PASS — no known vulnerabilities
npm ci --ignore-scripts --no-audit --no-fund
  PASS — 89 exact-locked packages installed
npm audit --audit-level=moderate
  PASS — 0 vulnerabilities
npm run validate:worker
  PASS — Prettier, Oxlint, strict TypeScript, 54 Worker tests, generated bindings,
  and root/preview/production Wrangler dry-runs
python -m evidenceops run-mission-demo --output-dir <temporary-a>
python -m evidenceops run-mission-demo --output-dir <temporary-b>
diff -qr <temporary-a> <temporary-b>
  PASS — deterministic outputs identical
python -m evidenceops rebuild-static-demo
  PASS
mkdocs build --strict
  PASS — 128 static assets in the final production dry-run
python scripts/check_public_artifacts.py site
  PASS
npm run worker:dry-run:production
  PASS — production mode openai; model gpt-5.6-terra; no deployment
git diff --check
  PASS
```

The one skipped test is the opt-in live Microsoft Intune integration test. The protected audit may
run only after reviewed code reaches `main`; feature-branch execution is intentionally prohibited.

## Security review facts

- Provider-source inspection found no POST, PUT, PATCH, DELETE, create, update, apply, or remediation
  operation.
- Production deployment has no synthetic builder or optional artifact path.
- Public CI has no Microsoft, OpenAI, or Cloudflare credential.
- The GitHub production deployment window was independently re-read as disabled after validation.
- The staged repository/public scans found no credential, private evidence, or tenant-derived data.
- The tracked Mission package remains explicitly synthetic; production must replace it in-memory in
  the trusted workflow with one reviewed live sanitized artifact before building.

## Post-merge gates

The final external result requires a protected-main Intune audit with publication enabled, review of
the single sanitized artifact, exact-snapshot Cloudflare deployment, `/api/status` and Mission
identity verification, one bounded live Copilot request, and desktop/mobile browser checks. Those
run and deployment identifiers belong in the final operator report after direct verification.
