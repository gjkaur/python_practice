"""
Password strength evaluation rules.
"""

from __future__ import annotations

from typing import List, Tuple


def evaluate_password(password: str) -> Tuple[str, List[str]]:
    """
    Return (strength, reasons).

    Strength is one of: WEAK, MEDIUM, STRONG.
    """
    reasons: List[str] = []
    length = len(password)

    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    special_chars = "!@#$%^&*"
    has_special = any(c in special_chars for c in password)

    if length < 8:
        reasons.append("Too short (minimum length is 8).")
    if not has_lower:
        reasons.append("Does not contain lowercase letters.")
    if not has_upper:
        reasons.append("Does not contain uppercase letters.")
    if not has_digit:
        reasons.append("Does not contain digits.")
    if not has_special:
        reasons.append("Does not contain special characters.")

    types_count = sum([has_lower, has_upper, has_digit, has_special])

    if length >= 12 and types_count == 4:
        strength = "STRONG"
    elif length >= 8 and types_count >= 2:
        strength = "MEDIUM"
    else:
        strength = "WEAK"

    if not reasons:
        reasons.append("Meets all basic criteria.")

    return strength, reasons

