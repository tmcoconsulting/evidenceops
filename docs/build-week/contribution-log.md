# Contribution Log

## Work location

The Phase 0 implementation occurred in the primary Codex thread. No supporting Codex thread or
subagent produced repository content during this phase.

## Milestones

| Date | Milestone | Primary contributor | Commit |
| --- | --- | --- | --- |
| 2026-07-18 | Secure project, evidence engine, and sanitizer foundation | Human-directed Codex implementation | `a5dbe3703e530297cfda165e69338791a419d403` |
| 2026-07-18 | Synthetic documentation and demo site | Human-directed Codex implementation | `b0a283b3848a523f80fd6501273872725d44161d` |
| 2026-07-18 | GitHub governance, CI, and Pages automation | Human-directed Codex implementation | `0a2dbc3906ae6274e2f9d4a79d2ce620ae417368` |
| 2026-07-18 | Validation evidence record | Human-directed Codex implementation | This document's follow-up commit |

## Commands and checks

The primary thread recorded and directly inspected environment commands including `pwd`, `uname
-a`, Git/GitHub CLI/Python versions, Git identity, GitHub authentication, actor identity,
organization membership and policy, repository conflicts, repository settings, and local
permissions.

Implementation validation commands and their final results are recorded here after the clean run:

```text
python -m ruff format --check .
  PASS — 18 Python files already formatted
python -m ruff check .
  PASS — all checks passed
python -m mypy
  PASS — no issues in 18 source files
python -m pytest
  PASS — 13 tests; 91.03% coverage
python -m bandit -r evidenceops scripts -c pyproject.toml
  PASS — no issues identified
python scripts/check_secrets.py
  PASS — secret scan passed
mkdocs build --strict
  PASS — site built; upstream Material/MkDocs 2.0 warning recorded in the decision log
python scripts/check_public_artifacts.py site
  PASS — public artifact scan passed
python -m pip_audit -r requirements-dev.txt
  PASS — no known vulnerabilities found
```

The dependency installation began in a newly created `.venv` using Python 3.14.6 and the exact
direct pins, after which the resolved transitive environment was captured in
`requirements-dev.txt`. CI independently installs that lock on Python 3.12.

## Pre-Build-Week material

No source history, code, tenant exports, or licensed baseline content from another repository was
incorporated in Phase 0. A previously referenced visual asset was not present with established
usage rights, so the site uses text and original CSS only.

## Rejected design choices

- Importing code or history from an existing endpoint-management repository
- Live Graph collection in a public workflow
- Any Microsoft Graph or Intune write operation
- Stored client secrets or committed pseudonymization keys
- Unclassified field pass-through
- Model-authored compliance verdicts
- A custom domain before separate access and rollback verification
