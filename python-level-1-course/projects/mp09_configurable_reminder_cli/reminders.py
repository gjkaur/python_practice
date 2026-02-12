"""
Core reminder logic.
"""

from __future__ import annotations


def run_reminders(message: str, repeat: int) -> None:
    for _ in range(max(repeat, 0)):
        print(f"Reminder: {message}")

