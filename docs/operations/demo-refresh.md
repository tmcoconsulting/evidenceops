# Protected Demo Refresh

Use this runbook when production evidence is stale, a mapped Intune observation changed, or the
approved baseline changed. The refresh is two gated workflows: read-only collection, then exact
artifact deployment. There is no synthetic production fallback.

## Preconditions

- The intended source revision is merged to protected `main` and CI is green.
- The `production` environment remains protected.
- Entra workload federation trusts only the Provifact production environment.
- The four permission-manifest application families remain read-only and admin-consented:
  `DeviceManagementApps.Read.All`, `DeviceManagementConfiguration.Read.All`,
  `DeviceManagementManagedDevices.Read.All`, and `DeviceManagementServiceConfig.Read.All`.
  Provider requests remain GET-only.
- `CLOUDFLARE_DEPLOY_ENABLED` is `true` only for an authorized deployment window.
- You have an optional prior successful audit run ID only when an exact current/prior comparison is
  intended.

## 1. Dispatch the protected audit

From GitHub, open **Actions → Read-only Intune audit → Run workflow** on `main`. Leave all tenant
responses private. If using the CLI, preview the command and confirm the repository and branch
before executing:

```bash
gh workflow run intune-audit.yml \
  --repo tmcoconsulting/provifact \
  --ref main \
  -f prepare_publication=true \
  -f prior_sanitized_audit_run_id="<optional successful run ID>"
```

Omit the prior-run input when no exact current/prior comparison is required. To find candidates,
inspect only trusted-main run metadata and choose deliberately; never auto-select a run:

```bash
gh run list \
  --repo tmcoconsulting/provifact \
  --workflow intune-audit.yml \
  --branch main \
  --event workflow_dispatch \
  --status success \
  --limit 10
```

Watch it without printing private artifacts:

```bash
gh run watch <audit-run-id> --repo tmcoconsulting/provifact --exit-status
```

Accept only a successful trusted-main run whose logs show OIDC authentication, approved endpoint
families, GET-only enforcement, publication-policy validation, public scanning, and ephemeral
private cleanup. The scanned public artifact is retained for only one day. Record the run ID and
review it promptly; no raw or private package is uploaded.

## 2. Review the sanitized artifact

The audit uploads exactly one scanned `mission-control.json` artifact for one day. Review only its
public-safe aggregate fields:

- `data_mode` is `LIVE SANITIZED TENANT DATA`;
- fingerprint and snapshot ID validate;
- freshness timestamp is current;
- approved baseline revision and hash match Git;
- evaluated denominator, drift, gaps, and device aggregates are plausible;
- no tenant, policy, group, assignment, user, device, or credential identity is present;
- the public-artifact scanner passed.

If the expected three-device test fleet is not reflected in the aggregate, stop and investigate
enrollment, platform classification, Graph collection, or normalization privately. Do not add a
device or infer its platform in public data.

Download only the named sanitized artifact to a temporary directory outside the repository, then
re-run the public scanner and fingerprint/schema promotion check:

```bash
gh run download <audit-run-id> \
  --repo tmcoconsulting/provifact \
  --name evidenceops-sanitized-mission-<audit-run-id> \
  --dir <temporary-directory>
python scripts/check_public_artifacts.py <temporary-directory>
python scripts/promote_live_mission.py \
  <temporary-directory>/mission-control.json \
  --destination <temporary-directory>/validated-mission-control.json
jq -r '.snapshot_id' <temporary-directory>/validated-mission-control.json
```

The printed snapshot ID is public-safe; do not print the whole artifact. Remove the temporary
directory after the deployment decision.

## 3. Dispatch exact-artifact deployment

Open **Actions → Deploy Cloudflare production → Run workflow** on `main`. Supply the successful audit
run ID and exact snapshot ID from the reviewed artifact. If using the CLI, open the deployment gate
immediately before dispatch:

```bash
gh variable set CLOUDFLARE_DEPLOY_ENABLED \
  --repo tmcoconsulting/provifact \
  --env production \
  --body true
```

Then dispatch the exact reviewed handoff:

```bash
gh workflow run deploy-cloudflare.yml \
  --repo tmcoconsulting/provifact \
  --ref main \
  -f confirm_production_deploy=true \
  -f sanitized_audit_run_id="<successful audit run ID>" \
  -f expected_source_snapshot_id="<reviewed mission snapshot ID>"
```

The workflow must validate source provenance, rebuild deterministic assets, scan the staged site,
deploy the exact artifact, and verify production. Never dispatch from a feature branch. Enable
`CLOUDFLARE_DEPLOY_ENABLED=true` only for this reviewed window, and return it to `false` after the
run regardless of success:

```bash
gh variable set CLOUDFLARE_DEPLOY_ENABLED \
  --repo tmcoconsulting/provifact \
  --env production \
  --body false
gh variable list --repo tmcoconsulting/provifact --env production
```

## 4. Post-deploy verification

Verify, without making an Assistant model request:

```bash
curl -fsS https://provifact.tmcoconsulting.com/api/status
curl -fsS https://provifact.tmcoconsulting.com/api/health
curl -fsS https://provifact.tmcoconsulting.com/api/ready
curl -fsSI https://provifact.tmcoconsulting.com/
curl -fsSI https://provifact.tmcoconsulting.com/evidence-dashboard/
```

Confirm HTTPS, CSP/security headers, `LIVE SANITIZED TENANT DATA`, current freshness, exact snapshot
identity, `gpt-5.6-terra` runtime configuration, and no synthetic fallback. Open Mission Control in
a clean browser and check the console, keyboard navigation, mobile layout, finding drilldown, and
the evidence links. One chargeable Assistant call is optional and separately bounded.

## Failure and rollback

- Audit failure: deploy nothing. Fix the collector/mapping through a reviewed pull request or retry
  a documented transient failure once.
- Scan/fingerprint/provenance failure: reject the artifact. Never weaken the gate.
- Deployment failure before promotion: the existing production version remains authoritative.
- Bad promoted version: use the documented Cloudflare version rollback, then verify the former
  snapshot and status. Follow [Cloudflare Worker rollback](cloudflare-worker.md#operations-and-rollback) and do
  not substitute the tracked synthetic package.
- Stale evidence: the site must show degraded/stale state until a new protected audit succeeds.

## Common failures

- **Graph has not propagated the policy:** wait for the documented provider API to return the new
  state, then run one new audit. Do not weaken a mapping or edit a public artifact.
- **OIDC or consent failure:** verify the environment-scoped federated credential and the single
  approved application permission. Do not create a client secret.
- **Prior artifact expired:** run without current/prior comparison or select another explicitly
  reviewed successful run; do not fabricate history.
- **Sanitizer, fingerprint, or public scan failure:** retain no output and fix the classified schema
  or mapping through a pull request.
- **Deployment gate disabled:** this is the safe default. Enable it only for the reviewed artifact
  and return it to `false` afterward.

## One-page operator checklist

- [ ] Reviewed source is merged to protected `main`; CI is green and the worktree is clean.
- [ ] Current approved baseline revision, hashes, and mapping denominator are understood.
- [ ] Optional prior run is an explicitly selected successful trusted-main audit.
- [ ] Audit is dispatched with `prepare_publication=true`; no private output is downloaded.
- [ ] Named one-day sanitized artifact passes schema, fingerprint, and public scans.
- [ ] Snapshot ID and aggregate counts are reviewed; unexpected device counts are investigated
      privately.
- [ ] Deployment gate is enabled only for the exact reviewed run and snapshot.
- [ ] Deployment succeeds; status, health, readiness, headers, pages, and browser behavior pass.
- [ ] Deployment gate is restored to `false` even after failure.
- [ ] Temporary sanitized artifact is deleted and the prior Worker version is recorded for rollback.
- [ ] Do not record Actions, Intune, Entra, Cloudflare, OpenAI, terminals, raw JSON, or private
      evidence screens.

This runbook intentionally provides no one-click helper. Printed commands plus the protected
environment and exact-artifact human gate make the two external state changes explicit.
