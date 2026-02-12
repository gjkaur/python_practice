## Capstone 1 – CLI Expense Tracker

### 1. Overview

A production-style **CLI Expense Tracker** that allows users to:

- Record expenses (amount, category, date, description).
- List and filter expenses.
- View simple reports (totals per category, totals per period).

This capstone consolidates:

- Data types and operators.
- Control flow and loops.
- Collections (lists, dicts).
- Functions and exceptions.
- Basic file I/O and JSON/CSV persistence.
- Logging and simple configuration.

---

### 2. Problem Statement and User Stories

**Problem**  
Individuals and small teams often track expenses manually or in spreadsheets.  
You will implement a CLI tool that makes this tracking easier while staying simple enough for Level 1.

**User Stories**

- **As a user**, I want to quickly add expenses with category, amount, and description.
- **As a user**, I want to see how much I’ve spent per category in a given period.
- **As a user**, I want the tool to handle invalid input without crashing.
- **As a maintainer**, I want the code organized into modules with clear responsibilities.

---

### 3. Functional Requirements

- Add new expense:
  - Fields: date (string or simple YYYY-MM-DD), category, amount, description.
- List expenses:
  - All, or filtered by category.
- Show summary:
  - Total spent overall.
  - Total per category.
- Persist data:
  - JSON or CSV file in the project directory.

Non-goals for Level 1:

- No authentication.
- No complex date parsing; treat dates as simple strings with minimal validation.

---

### 4. Non-Functional Requirements

- Code must follow **PEP 8** and be logically modular.
- Program must **not crash** on invalid input or missing data files.
- Logging for unexpected errors and key operations.

---

### 5. Suggested Folder Structure

```text
capstone_1_cli_expense_tracker/
  main.py          # CLI entrypoint and command routing
  models.py        # expense data structures
  services.py      # business logic (add, list, summaries)
  storage.py       # JSON/CSV file I/O
  validators.py    # input validation utilities
  config.py        # configuration loading (e.g., data file path)
  logging_config.py# basic logging setup
  tests/           # simple test scripts (optional at Level 1)
  README.md
  data/
    expenses.json  # or expenses.csv (created at runtime)
```

---

### 6. Milestones (MVP → v2 → v3)

**MVP**

- In-memory list of expenses.
- Commands:
  - `add` – add an expense.
  - `list` – list all expenses.
  - `summary` – total spent overall.
- Basic input validation and exception handling.

**v2**

- Persist expenses to a JSON or CSV file.
- Add category-based summary.
- Introduce basic logging (e.g., log file under `data/`).

**v3**

- Add date field and simple date validation (string-based).
- Add filtering by category and/or date range (simple, string-based).
- Improve error messages and user guidance.

---

### 7. Data Persistence Approach

Start with **JSON** for readability:

- Each expense stored as a dict:

```json
{
  "date": "2026-02-11",
  "category": "food",
  "amount": 12.50,
  "description": "Lunch"
}
```

- `storage.py` handles:
  - `load_expenses(path: str) -> list[dict]`
  - `save_expenses(path: str, expenses: list[dict]) -> None`

Use try/except around file I/O and JSON parsing; log errors and fall back to empty lists when appropriate.

---

### 8. Logging

Use the standard `logging` module:

- Configure at startup in `logging_config.py`:
  - Log to a file such as `data/expense_tracker.log`.
  - At least log errors and unexpected exceptions.
- Avoid printing stack traces to users; log details instead, show clear messages on CLI.

---

### 9. Rubric (Quality, Correctness, Design, Testing)

**Quality (0–5)**

- 0–1: Inconsistent style and naming; no structure.
- 2–3: Reasonable style; some modularity; occasional naming issues.
- 4–5: Strong adherence to PEP 8; clear naming; small, focused functions.

**Correctness (0–5)**

- 0–1: Frequent crashes; incorrect calculations.
- 2–3: Mostly correct, minor bugs under edge cases.
- 4–5: Correct behavior across expected cases, including edge cases.

**Design (0–5)**

- 0–1: All logic in one file or function.
- 2–3: Basic separation between CLI, logic, and storage.
- 4–5: Clear separation of concerns; modules follow single responsibility.

**Testing (0–5)**

- 0: No tests or manual plan.
- 2–3: Manual testing documented; some functions tested individually.
- 4–5: Basic automated tests or a thorough manual test checklist.

Total: /20

---

### 10. Example Manual Test Plan

- Add multiple expenses with different categories.
- Restart the program; verify expenses are persisted.
- Check that summaries match expected totals.
- Intentionally corrupt the data file; verify the program fails gracefully and logs errors.

---

### 11. Level-Up Roadmap Toward Level 2

- Introduce **argparse** for richer CLI options.
- Migrate from JSON to **SQLite** using a small database layer.
- Add more sophisticated reporting (e.g., monthly summaries).
- Consider introducing **OOP** models for expenses and repositories (Level 2+).

