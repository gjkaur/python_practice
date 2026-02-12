## Midterm Practical – Level 2 Python Course

### 1. Purpose

Assess learners’ ability to apply **PCAP-aligned** topics: modules, exceptions, OOP (classes, __init__, methods), and basic design in a time-boxed task.

- Clean multi-module layout.
- Custom exception(s) for validation.
- At least one class with instance data and methods.

---

### 2. Scenario

Implement a **Product Catalog** (in-memory) as a small multi-file application.

Requirements:

- **Module layout**: at least two modules (e.g. models.py, catalog.py or services.py) plus main.py.
- **Models**: Product class with name, price, optional id; constructor and at least one method (e.g. format_line or __str__).
- **Exceptions**: Define a custom exception (e.g. ValidationError or DuplicateError); raise it when price is negative or duplicate id.
- **CLI**: Add product (name, price), list all products, exit. No persistence required for midterm.

Timebox: ~90 minutes.

---

### 3. Functional Requirements

- Use only standard library.
- At least one **class** with __init__ and one method.
- At least one **custom exception** raised and caught.
- **Import** from your own modules (not everything in main.py).
- No crash on invalid input (negative price, empty name handled via exception or validation).

---

### 4. Grading Rubric (0–20)

**Correctness (0–6)**  
- 0–1: Does not run or major logic errors.  
- 2–3: Partially correct; add/list work but exceptions or class usage weak.  
- 4–5: Correct add/list; custom exception and class used correctly.  
- 6: Fully correct; edge cases handled.

**Structure and modules (0–5)**  
- Separate modules; clear responsibility; main imports from them.  
- Class and exception defined in appropriate modules.

**OOP and exceptions (0–5)**  
- Class has __init__ and at least one method; custom exception defined and used.  
- Catch exception in CLI and show message.

**Style and robustness (0–4)**  
- PEP 8; no crash on invalid input; clear messages.

---

### 5. Deliverables

- Code (main.py + at least one other module).
- Short note on which PCAP objectives the solution demonstrates (e.g. 1.5 modules, 2.2 custom exceptions, 4.x OOP).
