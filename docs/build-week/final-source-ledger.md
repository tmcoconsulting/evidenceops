# Final Source Ledger

Accessed 2026-07-21. This ledger records the external claims used by the final-readiness review. It
does not copy restricted benchmark prose or private tenant data.

The OpenAI, Devpost, YouTube, Microsoft, and Cloudflare entries are live vendor documentation
without a repository-pinned revision; the recorded version is therefore “live page accessed
2026-07-21.” Provifact links to those pages and paraphrases only the bounded claim shown below; it
does not redistribute their prose. Copyright and documentation terms remain with each source
owner. The mSCP entry is the exception: its exact Git revision, hashes, and CC BY 4.0 attribution are
recorded below and in `NOTICE`.

| Owner | Authoritative source | Claim supported | Repository evidence |
| --- | --- | --- | --- |
| OpenAI / Devpost | [OpenAI Build Week official rules](https://openai.devpost.com/rules) | July 21, 2026, 5:00 PM PDT deadline; Codex and GPT-5.6 requirement; sub-three-minute public YouTube demonstration; repository, README, credential-free developer-tool test path, and private `/feedback` metadata; four equal judging criteria | [Final readiness](final-readiness-report.md), [Devpost packet](final-devpost-packet.md) |
| OpenAI | [Build Week overview](https://openai.com/build-week/) | Challenge purpose, categories, submission shape, and judge framing | [Final readiness](final-readiness-report.md) |
| OpenAI | [Introducing GPT-5.6](https://openai.com/index/gpt-5-6/) | GPT-5.6 Terra is the balanced, cost-conscious model variant used by the bounded explainer | [Architecture](../architecture.md) |
| Devpost | [Build Week dates](https://openai.devpost.com/details/dates) | Live submission close timestamp and phase | [Submission checklist](submission-checklist.md) |
| YouTube | [Create a channel](https://support.google.com/youtube/answer/1646861) | Business/Brand Account channel workflow | [YouTube runbook](youtube-publishing-runbook.md) |
| YouTube | [Manage channel branding](https://support.google.com/youtube/answer/10456525) | Profile and banner formats, dimensions, safe region, and size limits | [YouTube assets](../assets/brand/youtube/README.md) |
| YouTube | [Upload videos](https://support.google.com/youtube/answer/57407?co=GENIE.Platform%3DDesktop&hl=en) | Upload, title, description, visibility, processing, and audience-selection workflow | [YouTube runbook](youtube-publishing-runbook.md) |
| YouTube | [Verify a YouTube account](https://support.google.com/youtube/answer/171664) | Custom-thumbnail verification requirement | [YouTube runbook](youtube-publishing-runbook.md) |
| Microsoft | [Device configuration Graph API](https://learn.microsoft.com/graph/api/intune-deviceconfig-deviceconfiguration-list) | GET-only legacy configuration collection | [Live collection](../operations/live-collection.md) |
| Microsoft | [Configuration policies Graph API](https://learn.microsoft.com/graph/api/intune-deviceconfigv2-devicemanagementconfigurationpolicy-list) | GET-only Settings Catalog collection and documented beta dependency | [Live collection](../operations/live-collection.md) |
| Microsoft | [GitHub Actions OIDC with Azure](https://learn.microsoft.com/azure/developer/github/connect-from-azure-openid-connect) | Short-lived workload federation without a client secret | [Architecture](../architecture.md) |
| Cloudflare | [Workers Static Assets](https://developers.cloudflare.com/workers/static-assets/) | Static-site plus Worker API deployment model | [Worker runbook](../operations/cloudflare-worker.md) |
| NIST | [macOS Security Compliance Project](https://github.com/usnistgov/macos_security) | Source repository for the pinned public macOS technical-profile membership | [Approved baseline](../operations/approved-baseline.md) |
| NIST mSCP | [CC BY 4.0 license](https://github.com/usnistgov/macos_security/blob/main/LICENSE.md) | Attribution terms for the derived rule identifiers, titles, and profile membership | [Repository NOTICE](https://github.com/tmcoconsulting/provifact/blob/main/NOTICE) |

## Source discipline

- The repository pins mSCP revision `11b5896e4f12f43410686024f543792742562c91` and verifies both
  the source archive SHA-256
  `af9ef14ca568f17d3663e6e508c1f75971596fe43c6f185af27ca43451c240d2`, extracted 98-rule
  inventory SHA-256 `5cced0709c90885ede600f00a640a35b0679aed933cda456db80ee629ee54d41`,
  and public catalog fingerprint
  `sha256:2c30e3996b6070dc8a748aa84701689a3d813933682a66222b4afd1960b14e47`.
- CIS, DISA STIG, NIST, CMMC-oriented, CNSSI, HICP, NLLMAP, and CIS Controls columns are exact
  membership references from that pinned public source. They are not copied remediation text,
  framework scores, completed assessments, certifications, or control-satisfaction verdicts.
- Microsoft Graph permissions and endpoint families are machine-readable and test-validated in the
  repository. No claim relies on tenant display names or inferred API behavior.
- Official rules control if a host announcement or summary conflicts with them. A public YouTube
  video is the safest interpretation even though later host guidance allowed unlisted visibility.
