"""
Validation and input helpers for the Admission Eligibility Checker.
"""

from __future__ import annotations


def read_int_in_range(prompt: str, min_value: int, max_value: int) -> int:
    """Prompt until an integer within [min_value, max_value] is provided."""
    while True:
        raw = input(prompt)
        try:
            value = int(raw)
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if value < min_value or value > max_value:
            print(f"Value must be between {min_value} and {max_value}.")
            continue
        return value


def read_non_negative_int(prompt: str) -> int:
    """Prompt until a non-negative integer is provided."""
    while True:
        raw = input(prompt)
        try:
            value = int(raw)
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if value < 0:
            print("Value must be non-negative.")
            continue
        return value

