"""
JSON-based storage for expenses.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import List

from models import Expense

DATA_PATH = Path("data/expenses.json")


def load_expenses() -> List[Expense]:
    if not DATA_PATH.exists():
        return []
    try:
        text = DATA_PATH.read_text(encoding="utf-8")
        raw_list = json.loads(text)
    except (OSError, json.JSONDecodeError):
        print("Warning: failed to load expenses; starting with empty list.")
        return []

    expenses: List[Expense] = []
    for item in raw_list:
        try:
            expenses.append(
                Expense(
                    date=str(item["date"]),
                    category=str(item["category"]),
                    amount=float(item["amount"]),
                    description=str(item["description"]),
                )
            )
        except (KeyError, TypeError, ValueError):
            continue
    return expenses


def save_expenses(expenses: List[Expense]) -> None:
    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    raw_list = [
        {
            "date": e.date,
            "category": e.category,
            "amount": e.amount,
            "description": e.description,
        }
        for e in expenses
    ]
    DATA_PATH.write_text(json.dumps(raw_list, indent=2), encoding="utf-8")

