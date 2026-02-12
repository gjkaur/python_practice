"""CLI entrypoint (Level 2 capstone 1)."""
from storage import load_expenses, save_expenses
from services import add_expense, summary_by_category
from validators import validate_amount, validate_date
from exceptions import ValidationError

DATA_PATH = "data/expenses.json"

def main():
    expenses = load_expenses(DATA_PATH)
    while True:
        print("1) Add 2) List 3) Summary 0) Exit")
        choice = input("Choice: ").strip()
        if choice == "0":
            save_expenses(DATA_PATH, expenses)
            break
        if choice == "1":
            try:
                amt = validate_amount(input("Amount: "))
                cat = input("Category: ").strip() or "other"
                date = validate_date(input("Date (YYYY-MM-DD): "))
                desc = input("Description: ").strip()
                add_expense(expenses, amt, cat, date, desc)
                print("Added.")
            except ValidationError as e:
                print("Validation error:", e)
        elif choice == "2":
            for e in expenses:
                print(e)
        elif choice == "3":
            for cat, total in summary_by_category(expenses).items():
                print(f"  {cat}: {total:.2f}")
        else:
            print("Unknown option")

if __name__ == "__main__":
    main()
