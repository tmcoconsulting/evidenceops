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
    for line in content.splitlines():
        if "uses:" not in line:
            continue
        reference = line.split("uses:", maxsplit=1)[1].strip().split()[0]
        assert "@" in reference
        assert len(reference.rsplit("@", maxsplit=1)[1]) == 40
