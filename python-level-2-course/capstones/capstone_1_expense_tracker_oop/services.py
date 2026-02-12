"""Business logic: add, list, summary (PCAP 4.x)."""
from models import Expense

def add_expense(expenses: list[Expense], amount: float, category: str, date: str, description: str = "") -> None:
    expenses.append(Expense(amount, category, date, description))

def summary_by_category(expenses: list[Expense]) -> dict:
    result = {}
    for e in expenses:
        result[e.category] = result.get(e.category, 0) + e.amount
    return result
