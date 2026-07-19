import json
import re
from pathlib import Path

REPOSITORY_ROOT = Path(__file__).parents[1]
WORKFLOWS = REPOSITORY_ROOT / ".github" / "workflows"


def test_executable_workflows_have_no_privileged_pages_chain() -> None:
    workflow_files = sorted((*WORKFLOWS.glob("*.yml"), *WORKFLOWS.glob("*.yaml")))
    assert [path.name for path in workflow_files] == ["ci.yml"]
    content = workflow_files[0].read_text(encoding="utf-8")
    for prohibited in (
        "workflow_run:",
        "pages: write",
        "id-token: write",
        "cloudflare/wrangler-action",
        "wrangler deploy --env",
        "actions/deploy-pages",
        "actions/upload-pages-artifact",
        "actions/configure-pages",
    ):
        assert prohibited not in content


def test_executable_workflow_actions_are_immutable_and_least_privilege() -> None:
    content = (WORKFLOWS / "ci.yml").read_text(encoding="utf-8")
    assert "permissions:\n  contents: read" in content
    assert "${{ secrets." not in content
    assert "OPENAI_API_KEY" not in content
    assert "AZURE_" not in content
    assert "EVIDENCEOPS_GRAPH_ACCESS_TOKEN" not in content
    assert "npm run worker:dry-run" in content
    assert "npm run worker:dry-run:production" in content
    assert "npm run test:worker" in content
    for line in content.splitlines():
        if "uses:" not in line:
            continue
        reference = line.split("uses:", maxsplit=1)[1].strip().split()[0]
        assert "@" in reference
        assert len(reference.rsplit("@", maxsplit=1)[1]) == 40


def test_worker_static_assets_and_modes_are_explicit() -> None:
    source = (REPOSITORY_ROOT / "wrangler.jsonc").read_text(encoding="utf-8")
    configuration = json.loads(re.sub(r",(?=\s*[}\]])", "", source))
    assert configuration["assets"] == {
        "directory": "./site",
        "binding": "ASSETS",
        "html_handling": "auto-trailing-slash",
        "not_found_handling": "404-page",
        "run_worker_first": ["/api/*"],
    }
    assert configuration["workers_dev"] is False
    assert configuration["vars"]["EVIDENCEOPS_MODE"] == "fixture"
    production = configuration["env"]["production"]
    assert production["workers_dev"] is False
    assert production["vars"]["EVIDENCEOPS_MODE"] == "openai"
    assert production["secrets"]["required"] == ["OPENAI_API_KEY"]
    assert production["routes"] == [
        {
            "pattern": "evidenceops.tmcoconsulting.com",
            "custom_domain": True,
        }
    ]


def test_worker_toolchain_is_exact_pinned_and_private() -> None:
    package = json.loads((REPOSITORY_ROOT / "package.json").read_text(encoding="utf-8"))
    assert package["private"] is True
    for version in package["devDependencies"].values():
        assert version[0].isdigit()
        assert not any(marker in version for marker in ("^", "~", "*", ">", "<"))


def test_browser_boundary_does_not_store_or_accept_byok() -> None:
    browser = (REPOSITORY_ROOT / "docs/assets/javascripts/evidenceops-api.js").read_text(
        encoding="utf-8"
    )
    router = (REPOSITORY_ROOT / "worker/src/security.ts").read_text(encoding="utf-8")
    for prohibited in ("localStorage", "sessionStorage", "innerHTML", "X-OpenAI-Key"):
        assert prohibited not in browser
    assert 'request.headers.has("X-OpenAI-Key")' in router
    assert 'request.headers.has("Authorization")' in router


def test_static_asset_headers_set_core_browser_controls() -> None:
    headers = (REPOSITORY_ROOT / "docs/_headers").read_text(encoding="utf-8")
    for expected in (
        "Content-Security-Policy:",
        "frame-ancestors 'none'",
        "Permissions-Policy:",
        "Referrer-Policy: no-referrer",
        "X-Content-Type-Options: nosniff",
        "X-Frame-Options: DENY",
    ):
        assert expected in headers
