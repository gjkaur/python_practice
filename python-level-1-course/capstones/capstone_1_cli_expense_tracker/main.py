"""
CLI entrypoint for the Expense Tracker capstone.
"""

from __future__ import annotations

from models import Expense
from services import add_expense, filter_by_category, list_expenses, total_amount, totals_by_category
from storage import load_expenses, save_expenses
from validators import read_float_positive, read_non_empty


def print_menu() -> None:
    print("Expense Tracker")
    print("---------------")
    print("1) Add expense")
    print("2) List expenses")
    print("3) List expenses by category")
    print("4) Show summary")
    print("0) Exit")


def print_expenses(expenses: list[Expense]) -> None:
    if not expenses:
        print("No expenses recorded.")
        return
    for e in expenses:
        print(f"{e.date} | {e.category} | {e.amount:.2f} | {e.description}")


def show_summary(expenses: list[Expense]) -> None:
    if not expenses:
        print("No expenses recorded.")
        return
    print(f"Total amount: {total_amount(expenses):.2f}")
    by_cat = totals_by_category(expenses)
    for cat, total in by_cat.items():
        print(f"- {cat}: {total:.2f}")


def main() -> None:
    expenses = load_expenses()

    while True:
        print_menu()
        choice = input("Choose: ").strip()

        if choice == "1":
            date = read_non_empty("Date (YYYY-MM-DD): ")
            category = read_non_empty("Category: ")
            amount = read_float_positive("Amount: ")
            description = input("Description: ").strip()
            add_expense(expenses, date=date, category=category, amount=amount, description=description)
            save_expenses(expenses)
            print("Expense added.")

        elif choice == "2":
            print_expenses(list_expenses(expenses))

        elif choice == "3":
            category = read_non_empty("Category: ")
            print_expenses(filter_by_category(expenses, category))

        elif choice == "4":
            show_summary(expenses)

        elif choice == "0":
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()

