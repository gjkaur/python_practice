"""
Business logic for the Expense Tracker.
"""

from __future__ import annotations

from collections import defaultdict
from typing import Dict, List

from models import Expense


def add_expense(
    expenses: List[Expense],
    date: str,
    category: str,
    amount: float,
    description: str,
) -> None:
    expenses.append(Expense(date=date, category=category, amount=amount, description=description))


def list_expenses(expenses: List[Expense]) -> List[Expense]:
    return list(expenses)


def filter_by_category(expenses: List[Expense], category: str) -> List[Expense]:
    category_lower = category.lower()
    return [e for e in expenses if e.category.lower() == category_lower]


def total_amount(expenses: List[Expense]) -> float:
    return sum(e.amount for e in expenses)


def totals_by_category(expenses: List[Expense]) -> Dict[str, float]:
    totals: Dict[str, float] = defaultdict(float)
    for e in expenses:
        totals[e.category] += e.amount
    return dict(totals)

