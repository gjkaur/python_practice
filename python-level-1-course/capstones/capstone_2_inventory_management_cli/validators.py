"""
Input validation helpers for the Inventory Management CLI.
"""

from __future__ import annotations


def read_non_empty(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Value cannot be empty.")


def read_float_positive(prompt: str) -> float:
    while True:
        raw = input(prompt)
        try:
            value = float(raw)
        except ValueError:
            print("Please enter a valid number.")
            continue
        if value <= 0:
            print("Value must be positive.")
            continue
        return value


def read_int(prompt: str) -> int:
    while True:
        raw = input(prompt)
        try:
            return int(raw)
        except ValueError:
            print("Please enter a valid integer.")


