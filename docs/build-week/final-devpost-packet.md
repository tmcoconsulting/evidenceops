# Final Devpost Packet

Copy from this page into Devpost only after checking the current form and official rules. Bracketed
items require TJ's private or external action. Never replace the `/feedback` placeholder in Git.

## Core fields

**Project title**

> Provifact™ by TMCO Consulting

**Tagline**

> From approved change to audit-ready proof.

**Category**

> Developer Tools

**Project URL**

> https://provifact.tmcoconsulting.com/

**Repository URL**

> https://github.com/tmcoconsulting/provifact

**Video URL**

> `[HUMAN: PUBLIC_YOUTUBE_URL]`

**Private `/feedback` Session ID**

> `[HUMAN: RUN /feedback IN THE PRIMARY CODEX TASK AND ENTER THE RETURNED ID DIRECTLY IN DEVPOST — NEVER COMMIT IT]`

**Submitter type / country**

> `[HUMAN: SELECT THE ACCURATE LEGAL/PERSONAL ANSWERS IN DEVPOST]`

## Submission description

### Inspiration

Regulated endpoint teams can make hundreds of configuration changes and still spend weeks before an
audit reconstructing what was approved, what the MDM actually held, what drifted, and which evidence
supports the conclusion. The problem is not another compliance score. It is the missing chain of
custody from approved change to reviewable proof.

### What it does

Provifact connects a Git-approved macOS baseline to read-only Microsoft Intune collection,
deterministic drift, a fail-closed sanitized evidence package, a Cloudflare-hosted Mission Control,
and bounded GPT-5.6 Terra explanation.

The current Build Week slice exposes all 98 rules in the approved demo inventory. Four exact,
reviewed Intune setting mappings enter the deterministic denominator; the remaining 94 stay visible
as implementation work. Missing collection, unsupported shapes, unreviewed mappings, and planning
work remain separate from technical drift. Public reference profiles—including CIS Level 2, DISA
STIG, NIST, and CMMC-oriented mSCP profiles—support comparison, not a framework score or
certification claim.

Mission Control lets an engineer or auditor open a finding and trace desired state, normalized
observation, assignment evidence, exact provider definition, stable evidence IDs, fingerprints,
freshness, and read-only guidance. Provifact Assistant answers a closed set of evidence questions
from a small sanitized context. Deterministic typed claims and evidence references are verified;
free prose is labeled AI-generated and remains subject to human review.

### How we built it

The Python core defines provider-neutral, versioned desired-state, observation, finding, evidence,
publication, narrative, and verification contracts. The Microsoft provider uses only documented
Graph GET endpoints, pagination, bounded retry, `Retry-After`, timeouts, strict response validation,
and per-resource collection gaps. GitHub Actions obtains a short-lived Entra token through
environment-scoped OIDC; no client secret exists.

A private normalized package is ephemeral and never becomes a raw public export. Publication
reconstructs an allowlisted package, pseudonymizes the minimum correlation fields, validates its
canonical fingerprint, and scans it for credentials and tenant-specific values. Cloudflare Workers
Static Assets serves the dashboard and same-origin API. The Worker pins `gpt-5.6-terra`, uses the
OpenAI Responses API with structured output, `store: false`, no tools, rate limits, input/output
bounds, and a deterministic verifier. Production cannot fall back to synthetic evidence.

Codex was the primary implementation collaborator for architecture inspection, typed boundaries,
provider and Worker code, adversarial tests, documentation, UI iteration, security remediation,
and validation. TJ Olnhausen retained product, security, baseline-approval, external-account,
review, and merge decisions. GPT-5.6 Terra is the runtime explainer only; it never determines drift
or compliance.

### Challenges

The hardest challenge was remaining useful without becoming misleading. Intune resource families
have materially different shapes, Settings Catalog requires an isolated beta dependency, and public
evidence cannot expose policy or assignment identities. Exact provider IDs replaced display-name or
substring matching. Unknown fields fail closed. A collection gap stays visible instead of becoming
a guessed failure.

The second challenge was constraining AI. Model prose can sound authoritative even when evidence is
incomplete, so Provifact makes the deterministic package authoritative, sends only intent-specific
sanitized context, attaches typed claims and references, rejects unsupported verdict language, and
quarantines every free-form explanation.

### Accomplishments

- Protected-main GET-only live collection with short-lived GitHub/Entra federation.
- A hash-pinned 98-rule macOS inventory and a 17-profile, 309-rule catalog: one approved company
  target plus 16 public technical comparison profiles.
- Exact deterministic mappings, evidence IDs, fingerprints, freshness, current/prior comparison,
  and honest coverage gaps.
- A public live sanitized dashboard with no tenant, user, device, policy, group, assignment, or
  credential identities.
- A fixed GPT-5.6 Terra Assistant whose typed claims and evidence references must match the package.
- Immutable workflow pins, CodeQL, branch-aware tests, dependency audits, secret scans, public
  artifact scans, CSP/security headers, rate limits, and no Intune write implementation.

### What we learned

Evidence completeness and control coverage are different questions. A useful tool must preserve
that distinction in its schemas and UI. Provider-neutrality also belongs at the normalized contract,
not in a promise that every vendor works without a new adapter. Most importantly, generative AI is
more credible when the product visibly limits what it can claim.

### What's next

The next work is to reduce the visible 94-rule implementation backlog through reviewed exact
mappings and approved alternate-evidence paths; investigate the current managed-device aggregate;
add authenticated sanitized history and approval records after retention design; and implement Jamf
or Omnissa Workspace ONE through the existing provider contract. Intune writes, automatic
exceptions, and AI compliance verdicts remain out of scope.

## Built with

- Codex
- GPT-5.6 Terra and the OpenAI Responses API
- Python 3.12+
- TypeScript
- Microsoft Graph and Microsoft Intune
- Microsoft Entra workload identity federation
- GitHub Actions and GitHub OIDC
- Cloudflare Workers and Static Assets
- Material for MkDocs

## Developer-tool testing instructions

**Fastest credential-free judge path**

1. Open https://provifact.tmcoconsulting.com/evidence-dashboard/.
2. Check evidence mode, freshness, 98-rule inventory, four exact joins, drift, backlog, and gaps.
3. Open a finding and trace desired/observed state, evidence IDs, fingerprint, and guidance.
4. Open https://provifact.tmcoconsulting.com/settings-matrix/ and compare company-approved inventory
   with reference-profile membership.
5. Ask Provifact Assistant “What requires my attention?” and inspect the generated/review-required
   label, evidence links, limitations, and verifier language.
6. Read https://provifact.tmcoconsulting.com/judge-guide/ for the three-minute path.

No tenant, Microsoft, OpenAI, Cloudflare, or GitHub credential is required. Supported judge
platforms are current desktop and mobile browsers with JavaScript enabled.

**Local deterministic path**

```bash
git clone https://github.com/tmcoconsulting/provifact.git
cd provifact
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python -m pip install --no-build-isolation --no-deps .
npm ci --ignore-scripts --no-audit --no-fund
python -m provifact run-mission-demo --output-dir build/mission-demo
python -m provifact rebuild-static-demo
mkdocs build --strict
npm run validate:worker
```

Local and preview builds are visibly synthetic/fixture mode. They do not contact Microsoft Graph or
OpenAI. Provifact has no apply command or Intune write path.

## Acknowledgments and licensing

Provifact™ is a trademark of TMCO Consulting, LLC. Source code is Apache-2.0 licensed. The pinned
baseline inventory and profile membership are derived from the NIST macOS Security Compliance
Project under its upstream CC BY 4.0 terms; attribution and hashes are recorded in `NOTICE` and the
repository manifest. Apple-authored vendor descriptions and restricted benchmark prose are not
copied into the public catalog.

## Final human gates

- [ ] Add the public YouTube URL and confirm signed-out playback.
- [ ] Enter accurate submitter type and country.
- [ ] Confirm category is Developer Tools.
- [ ] Confirm repository, project, and testing URLs.
- [ ] Run `/feedback` and enter the private Session ID directly in Devpost.
- [ ] Save every required answer.
- [ ] Submit and verify Devpost shows green **Submitted**, not draft, before July 21, 2026,
      5:00 PM PDT.
