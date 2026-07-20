from pathlib import Path

from scripts.check_company_name import scan


def test_company_name_scanner_rejects_standalone_public_copy(tmp_path: Path) -> None:
    docs = tmp_path / "docs"
    docs.mkdir()
    (docs / "index.md").write_text("TMCO audit dashboard", encoding="utf-8")

    assert scan(tmp_path) == [(Path("docs/index.md"), 1)]


def test_company_name_scanner_accepts_full_name_and_lowercase_identifiers(
    tmp_path: Path,
) -> None:
    docs = tmp_path / "docs"
    docs.mkdir()
    (docs / "index.md").write_text(
        "TMCO Consulting operates tmcoconsulting/evidenceops.",
        encoding="utf-8",
    )

    assert scan(tmp_path) == []
