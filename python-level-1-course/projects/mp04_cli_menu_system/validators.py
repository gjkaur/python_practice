"""
Input validation helpers for the CLI Menu System.
"""

from __future__ import annotations


def read_menu_choice(prompt: str, valid_choices: list[str]) -> str:
    """Prompt until the user enters one of the valid menu choices."""
    while True:
        raw = input(prompt).strip()
        if raw in valid_choices:
            return raw
        print(f"Invalid choice. Valid options: {', '.join(valid_choices)}")

