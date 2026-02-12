"""
CLI entrypoint for the Password Strength Checker.
"""

from __future__ import annotations

from formatting import format_reasons
from rules import evaluate_password


def main() -> None:
    password = input("Enter password: ")
    strength, reasons = evaluate_password(password)
    print(f"Strength: {strength}")
    print(format_reasons(reasons))


if __name__ == "__main__":
    main()

