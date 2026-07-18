"""Shared high-confidence credential signatures for every repository egress gate."""

from __future__ import annotations

import re
from re import Pattern
from typing import Final

CredentialPattern = tuple[str, Pattern[str]]

# Keep this catalog intentionally high confidence.  Publication, repository scanning,
# generated-site scanning, and pre-model egress all import these exact compiled patterns.
CREDENTIAL_PATTERNS: Final[tuple[CredentialPattern, ...]] = (
    (
        "private key",
        re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    ),
    ("certificate material", re.compile(r"-----BEGIN " r"CERTIFICATE-----")),
    (
        "GitHub token",
        re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,})\b"),
    ),
    ("Slack token", re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b")),
    ("OpenAI API key", re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b")),
    (
        "JWT-like access token",
        re.compile(r"\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\b"),
    ),
    (
        "bearer credential",
        re.compile(r"\b(?:authorization\s*[:=]\s*)?Bearer\s+[A-Za-z0-9._~+/-]{20,}=*", re.I),
    ),
)
