## Capstone 2 – Inventory Management CLI

### 1. Overview

Build a CLI **Inventory Management Tool** that manages products and stock levels.  
This capstone emphasizes dictionary-heavy logic, input validation, and clean separation of concerns.

---

### 2. Problem Statement and User Stories

**Problem**  
Small shops and internal teams need a simple way to track inventory without full-blown ERP software.

**User Stories**

- **As a store manager**, I want to:
  - Add products with SKU, name, and price.
  - Adjust stock levels (incoming and outgoing).
  - View low-stock items.
- **As a developer**, I want inventory operations to live in testable functions.
- **As a maintainer**, I want clear module boundaries and basic error logging.

---

### 3. Functional Requirements

Core features:

- Add a new product:
  - Fields: SKU (string), name, price, initial quantity.
- Update quantity:
  - Increase (restock) or decrease (sale/usage).
- List inventory:
  - All products with current quantity.
- Low-stock report:
  - Products where quantity < configurable threshold (e.g., 5).

Persistence:

- Store inventory in a JSON or CSV file.

---

### 4. Non-Functional Requirements

- No crashes on invalid input or missing data files.
- Consistent use of PEP 8 and clear naming.
- Simple logging for errors (e.g., invalid quantity updates).

---

### 5. Suggested Folder Structure

```text
capstone_2_inventory_management_cli/
  cli.py          # user interaction and commands
  inventory.py    # core inventory operations
  validators.py   # input validation
  storage.py      # persistence layer
  config.py       # low-stock threshold and data file path
  logging_config.py
  tests/
  README.md
  data/
    inventory.json
```

---

### 6. Milestones (MVP → v2 → v3)

**MVP**

- In-memory inventory with:
  - `add`, `list`, `update` operations.
- Simple CLI with menu.

**v2**

- Persist inventory to JSON or CSV.
- Add low-stock reporting based on threshold.
- Basic logging for operations and errors.

**v3**

- Add simple price calculations for stock value.
- Add basic search by SKU or name.
- Improve error messages and validation.

---

### 7. Data Persistence Approach

Use JSON structure like:

```json
{
  "SKU001": { "name": "Widget A", "price": 9.99, "quantity": 10 },
  "SKU002": { "name": "Widget B", "price": 12.50, "quantity": 3 }
}
```

- `storage.py`:
  - `load_inventory(path: str) -> dict[str, dict]`
  - `save_inventory(path: str, inventory: dict[str, dict]) -> None`

Handle I/O errors gracefully and log them.

---

### 8. Logging

- Configure logging with `logging_config.py`:
  - Log file e.g., `data/inventory.log`.
  - Record:
    - Errors (e.g., negative stock updates, missing SKU).
    - Significant operations (adds, adjustments).

---

### 9. Rubric (Quality, Correctness, Design, Testing)

Use the same 0–5 scale as Capstone 1, adjusted for inventory context:

- **Quality**: style, readability, PEP 8.
- **Correctness**: correct quantities and reports.
- **Design**: modular code and separation of concerns.
- **Testing**: documented manual tests or simple automated tests.

Total: /20

---

### 10. Example Manual Test Plan

- Add several products with varying quantities.
- Simulate sales and restocks; verify final quantities.
- Verify low-stock report shows only items below threshold.
- Restart tool and confirm data persistence.
- Intentionally corrupt data file and verify graceful recovery or clear error.

---

### 11. Level-Up Roadmap Toward Level 2

- Add command-line arguments for batch operations (e.g., import CSV of updates).
- Introduce a **transaction log** for all inventory changes.
- Move from JSON to a small SQLite database.
- Add more sophisticated search and filtering options.

