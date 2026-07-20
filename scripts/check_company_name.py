#!/usr/bin/env python3
"""Reject standalone user-facing uses of the abbreviated company name."""

from __future__ import annotations

import argparse
import re
from collections.abc import Iterator
from pathlib import Path
from typing import Final

_PUBLIC_ROOT_FILES: Final = (
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "NOTICE",
    "README.md",
    "SECURITY.md",
    "SUPPORT.md",
    "mkdocs.yml",
)
_PUBLIC_SUFFIXES: Final = {
    ".css",
    ".html",
    ".js",
    ".json",
    ".md",
    ".svg",
    ".txt",
    ".xml",
    ".yml",
    ".yaml",
}
_STANDALONE_TMCO: Final = re.compile(r"(?<![\w-])TMCO(?! Consulting\b)")
_PUBLIC_SOURCE_DIRECTORIES: Final = ("baselines", "docs", "evidenceops", "fixtures")


def _iter_public_sources(root: Path) -> Iterator[Path]:
    for relative in _PUBLIC_ROOT_FILES:
        path = root / relative
        if path.is_file():
            yield path
    for directory in _PUBLIC_SOURCE_DIRECTORIES:
        source_root = root / directory
        if not source_root.is_dir():
            continue
        for path in source_root.rglob("*"):
            if path.is_file() and path.suffix.lower() in _PUBLIC_SUFFIXES:
                yield path


def scan(root: Path) -> list[tuple[Path, int]]:
    """Return public source locations with standalone ``TMCO`` copy."""
    findings: list[tuple[Path, int]] = []
    for path in _iter_public_sources(root):
        content = path.read_text(encoding="utf-8")
        for match in _STANDALONE_TMCO.finditer(content):
            line = content.count("\n", 0, match.start()) + 1
            findings.append((path.relative_to(root), line))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", type=Path, default=Path.cwd())
    args = parser.parse_args()
    root = args.root.resolve()
    if not root.is_dir():
        parser.error(f"repository directory does not exist: {root}")
    findings = scan(root)
    if findings:
        for path, line in findings:
            print(f"{path}:{line}: use 'TMCO Consulting' in user-facing copy")
        return 1
    print("company-name content check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
