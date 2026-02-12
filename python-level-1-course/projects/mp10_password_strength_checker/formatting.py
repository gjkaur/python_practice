"""
Formatting helpers for password strength output.
"""

from __future__ import annotations

from typing import Iterable


def format_reasons(reasons: Iterable[str]) -> str:
    lines = ["Reasons :"]
    lines.extend(f"- {reason}" for reason in reasons)
    return "\n".join(lines)

