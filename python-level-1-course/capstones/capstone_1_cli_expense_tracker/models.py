"""
Data structures for the Expense Tracker.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Expense:
    date: str
    category: str
    amount: float
    description: str

