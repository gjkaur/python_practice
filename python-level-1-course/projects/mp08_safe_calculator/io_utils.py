"""
Input and validation helpers for the Safe Calculator.
"""

from __future__ import annotations


def read_float(prompt: str) -> float:
    while True:
        raw = input(prompt)
        try:
            return float(raw)
        except ValueError:
            print("Invalid number. Please try again.")


def read_operation(prompt: str) -> str:
    valid = {"+", "-", "*", "/"}
    while True:
        op = input(prompt).strip()
        if op.lower() == "q":
            return "q"
        if op in valid:
            return op
        print("Invalid operation. Use +, -, *, / or q to quit.")

