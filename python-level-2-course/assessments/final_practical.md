## Final Practical – Level 2 Python Course

### 1. Purpose

Assess end-of-course ability to build a **multi-module, OOP, exception-aware** CLI application with **file persistence**, aligned with PCAP-31-03.

---

### 2. Scenario Options

**Option A – Expense Tracker**  
Implement (or extend) the Capstone 1 spec: add/list/summary expenses, custom exceptions for validation, Expense model(s), JSON persistence. Handle missing file (errno).

**Option B – Inventory**  
Implement (or extend) Capstone 2: add/list/update quantity, Item model, custom exceptions, JSON persistence. Handle missing file.

**Option C – Own design**  
Design a small CLI that uses: at least two modules, at least one class with __init__ and methods, at least one custom exception, and file I/O (read/write). Must be approved by instructor.

---

### 3. Requirements (All Options)

- **Modules**: At least two .py modules with clear responsibility (e.g. models, storage, services, validators).
- **OOP**: At least one class with instance attributes and methods; optional inheritance.
- **Exceptions**: At least one custom exception type; raised in validation or business logic and caught in CLI.
- **I/O**: Save and load data (e.g. JSON); handle missing file without crash (try/except OSError or errno).
- **CLI**: Menu-driven; add, list, and at least one more action; exit saves data.

---

### 4. Grading Rubric (0–40)

**Correctness (0–12)**  
- Program runs; add/list/persist work; no uncaught crashes for normal use.

**Module and OOP design (0–10)**  
- Clear module split; class(es) with __init__ and methods; appropriate use of instance data.

**Exceptions and I/O (0–10)**  
- Custom exception defined and used; file load/save work; missing file handled.

**Style and robustness (0–8)**  
- PEP 8; validation and user messages; code review checklist applied.

---

### 5. Deliverables

- Full codebase (multiple files).
- Short README: how to run, which PCAP objectives the solution demonstrates.
- Self-assessment using assessments/code_review_rubric.md (optional but recommended).
