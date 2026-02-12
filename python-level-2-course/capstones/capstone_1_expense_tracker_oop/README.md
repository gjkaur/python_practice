# Capstone 1 – Expense Tracker (OOP + Modules + Persistence)

## Overview

CLI Expense Tracker using **multiple modules**, **OOP** (Expense, ExpenseStore classes), **custom exceptions** for validation, and **file I/O** for persistence. Aligns with PCAP: modules (1.x), exceptions (2.x), OOP (4.x), I/O (5.4–5.5).

## Requirements

- **Models**: Expense class (amount, category, date, description); optional ExpenseStore class to hold list and provide add/list/summary.
- **Exceptions**: ValidationError (and subclasses) for invalid amount, date, or category.
- **Storage**: save/load to JSON file; use open(), read/write, handle errno.
- **CLI**: add, list, summary, exit; input validation with custom exceptions.

## Milestones

- **MVP**: Add expense, list all, save/load to file.
- **v2**: Summary by category; filter by category.
- **v3**: Optional logging; config file for data path.

## Suggested Structure

- main.py, models.py, services.py, storage.py, validators.py, exceptions.py
- data/ for JSON (create at runtime or .gitkeep)
