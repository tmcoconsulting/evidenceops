# Approved Baseline Operations

This runbook governs the organization-owned desired state. Baseline approval changes deterministic
evidence scope, so it is a human decision recorded through Git review—not a model action.

## Current canonical record

The active Build Week target is defined by two reviewed repository layers:

1. `baselines/tmco-macos-cis-level1-demo-approval.json` is the machine-readable internal approval
   record. It identifies the 98-rule inventory, pinned mSCP revision, source and extracted hashes,
   approval date, approving organization, scope, and limitations.
2. `evidenceops/baselines/mscp.py` contains the organization-owned desired values and exact provider
   mappings for the implemented slice. Four mappings are reviewed and may enter deterministic
   evaluation. One remains explicitly unreviewed and may not produce a finding.

The approval JSON is the canonical baseline-selection record. The Python mapping table is a current
Phase 1 implementation limitation: it is reviewed and test-protected, but it is not yet a separate
data-only override manifest. Moving it into a versioned organization override is future work and
must preserve schema and fingerprint compatibility.

## What the baseline means

Approval means TMCO Consulting, LLC selected a technical desired-state inventory for Provifact
drift evaluation. It does **not** mean CIS certified, CMMC compliant, a control is satisfied, a
practice is MET, or an assessor reached a conclusion. Public reference profiles support comparison
and planning only.

## Safe update procedure

1. Create a feature branch from current protected `main`.
2. Verify the proposed source revision, license, source-artifact hash, and extracted-inventory hash.
3. Review every added or removed rule ID and record why the organization target changes.
4. Update the approval record. A human approver must set the approval metadata; generated analysis
   cannot approve a baseline.
5. Add or change desired values only when the target is technically explicit and testable.
6. Add a provider mapping only after the exact provider definition ID and normalized value shape
   are confirmed from official documentation and/or a private read-only observation. Never match a
   tenant display name, substring, or guessed setting path.
7. Keep unimplemented rules visible as planning work. Do not turn absence of a reviewed mapping
   into a drift or failed-control verdict.
8. Run the full repository suite, catalog fingerprint tests, synthetic deterministic comparison,
   and public-artifact scan.
9. Open a pull request showing inventory delta, mapping delta, expected denominator change, source
   citations, and limitations.
10. Require explicit human review before merge. Then use the protected refresh workflow; do not
    hand-edit a production Mission package.

## A. Select or replace the approved reference profile

1. Pin the upstream repository, commit, profile path, license, archive SHA-256, and extracted
   inventory SHA-256 in `evidenceops/baselines/mscp.py` and
   `baselines/tmco-macos-cis-level1-demo-approval.json`.
2. Update the ordered rule inventory and title allowlist from the pinned source only. Do not copy
   Apple-authored descriptions or restricted benchmark prose.
3. Record approver role, date, rationale, scope, limitations, superseded record, selected rule
   count, platform, and intended provider in the approval record and matching typed constant.
4. Rebuild the comparison catalog from a verified upstream archive into a temporary path before
   replacing the tracked file:

   ```bash
   python scripts/build_baseline_catalog.py \
     --source-tar <verified-pinned-mscp-archive.tar.gz> \
     --output <temporary-directory>/baseline-catalog.json
   python scripts/check_public_artifacts.py <temporary-directory>
   ```

5. Review the exact rule/profile delta, update the catalog fingerprint expected by the frontend,
   and merge only after the tests below pass. The resulting reviewed Git revision becomes the
   desired-state commit recorded in new evidence; loading the profile alone never activates it.

## B. Modify one approved target value

The current organization-owned target layer is the `expected_value`, assignment requirement, and
closed transform in `evidenceops/baselines/intune.py`; it is not generated from upstream. Change the
smallest typed value, preserve the exact provider ID, add below/equal/above or true/false fixtures as
appropriate, explain the rationale in the pull request, and run the full gate. A Git revert restores
the prior intent definition only; it does not touch Intune.

Concrete example: changing the approved FileVault target requires a reviewed edit to
`system_settings_filevault_enforce`, fixtures proving the `FILEVAULT_ENABLE_CHOICE` transform, and
an expected finding delta. Do not edit `docs/assets/data/mission-control.json` by hand.

## C. Add a selected rule that already exists upstream

1. Confirm the rule ID belongs to the pinned source/profile and add it to the approved ordered
   inventory if it is not already selected.
2. Choose an explicit management/evidence path: Settings Catalog, custom profile, script/agent, or
   alternate evidence.
3. Add a `ProviderRuleMapping` only after an exact provider definition and closed value transform
   are established. Leave `review_status` as `NOT_REVIEWED` until that review is complete.
4. Add normalizer, provider-contract, mapping, adversarial, mission, sanitizer, and UI tests. An
   unreviewed mapping must remain implementation work and cannot become drift.

## D. Add an organization-specific rule

Phase 1 has no active organization-extension rule, so this requires a schema-reviewed pull request;
it is not a data-entry shortcut. Use a stable namespace such as `tmco.macos.<descriptive_id>`, add
source/rationale, type and closed allowed values, scope, approval metadata, and an explicit empty
cross-reference set unless authoritative reviewed references exist. Extend the baseline verifier,
catalog builder, sanitizer classification, mapping registry, synthetic fixtures, public UI, and
tests together. Never invent a framework crosswalk.

## E. Compare another profile without adopting it

Add the pinned profile to `PROFILE_SPECS` in `scripts/build_baseline_catalog.py`, rebuild from the
verified archive, and review exact rule membership and source hashes. The selector may then show
overlap, company omissions, conflicts, and implementation candidates. It must remain
`public technical comparison profile`; only a separate approval-record change can make it the
organization target.

## Focused verification

```bash
python -m pytest -o addopts='' \
  tests/test_baseline_catalog.py \
  tests/test_mission.py \
  tests/test_apple_provider.py \
  tests/test_workflows.py
python -m provifact rebuild-static-demo
git diff --exit-code -- docs/assets/data
mkdocs build --strict
python scripts/check_public_artifacts.py site
```

Review and stage the intended generated-data delta before the final rebuild/diff check; the check
then proves regeneration introduces no second, unexplained change. Run the complete repository gate
from `AGENTS.md`. Source drift, hash mismatch, unexpected fields, unapproved profile selection, and
unreviewed mappings must fail closed.

## Pull-request checklist

- [ ] Source revision and license are authoritative and recorded.
- [ ] Source archive and extracted inventory hashes reproduce.
- [ ] Rule-set additions/removals are reviewed as an exact set.
- [ ] Desired targets are typed and vendor-neutral.
- [ ] Provider IDs and normalizers are exact, documented, and fixture-tested.
- [ ] Unknown/unreviewed mappings remain outside the denominator.
- [ ] Public reference profiles are not described as company approval or compliance results.
- [ ] Synthetic and public scans pass.
- [ ] A named human reviewer approves the organization decision.

## Rollback

Revert the baseline pull request and rebuild evidence from the restored Git revision. This restores
Provifact's desired-state history; it does **not** change or roll back Intune. Any endpoint change
requires a separate authorized administrator workflow outside Provifact.
