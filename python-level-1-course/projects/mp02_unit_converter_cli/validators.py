"""
Input validation helpers for the Unit Converter CLI.
"""

from __future__ import annotations


def read_float(prompt: str) -> float:
    """Prompt until the user enters a valid float, then return it."""
    while True:
        raw = input(prompt)
        try:
            return float(raw)
        except ValueError:
            print("Invalid number. Please try again.")

