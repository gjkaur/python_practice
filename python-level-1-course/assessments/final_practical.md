## Final Practical – Level 1 Python Course

### 1. Purpose

Evaluate the learner’s ability to design, implement, and refine a **small, production-like CLI application** using all Level 1 skills:

- PCEP-aligned fundamentals (data types, control flow, collections, functions, exceptions).
- Basic file I/O and configuration.
- Clean code, modularity, basic testing, and Git usage.

---

### 2. Scenario

Learner completes and submits **two capstone projects**:

- Capstone 1 – CLI Expense Tracker.
- Capstone 2 – Inventory Management CLI.

The final practical focuses on:

- Code quality and structure.
- Correctness and robustness.
- Professional practices (logging, validation, Git).

---

### 3. Requirements

For each capstone:

- Must be runnable via a clear entry command, e.g.:

```bash
python main.py           # expense tracker
python cli.py            # inventory manager
```

- Includes:
  - A `README.md` describing usage and features.
  - Basic configuration and/or data file(s) (JSON/CSV).
  - Meaningful error handling and logging.

---

### 4. Grading Rubric (Per Capstone, 0–20)

**1. Correctness & Stability (0–6)**  
- 0–1: Crashes often; core features incomplete.  
- 2–3: Works for basic flows; some bugs for edge cases.  
- 4–5: Correct for most flows; minor edge issues only.  
- 6: Robust and correct for typical and edge scenarios.

**2. Code Quality & Style (0–4)**  
- 0–1: Inconsistent style; hard to read.  
- 2–3: Mostly PEP 8-compliant; reasonable naming and formatting.  
- 4: Clean, readable, and consistently styled.

**3. Design & Modularity (0–5)**  
- 0–1: Monolithic script; weak separation of concerns.  
- 2–3: Some separation between CLI, logic, and storage.  
- 4–5: Clear modules with focused responsibilities; good decomposition.

**4. Error Handling & Validation (0–3)**  
- 0: No validation; crashes on invalid input.  
- 1–2: Some validation and try/except blocks; a few holes.  
- 3: Consistent validation; well-placed exception handling; no silent failures.

**5. Professional Practices (0–2)**  
- 0: No Git or testing evidence.  
- 1: Basic Git usage (few commits) and manual test notes.  
- 2: Multiple meaningful commits, simple tests, or a clear manual test plan.

Total per capstone: **/20**  
Combined suggested total: **/40**

---

### 5. Evaluation Process

1. **Run** each capstone with a set of predefined test scenarios.
2. **Review** project structure and key modules.
3. **Inspect** Git history for:
   - Incremental progress.
   - Descriptive commit messages.
4. **Discuss** with learner (optional):
   - Design choices.
   - Trade-offs.
   - Possible improvements.

---

### 6. Suggested Test Scenarios

**Expense Tracker**

- Add multiple expenses across categories.
- Generate category summaries and verify totals.
- Restart and confirm data persistence.
- Trigger invalid inputs (negative amount, malformed date).

**Inventory Manager**

- Add products and adjust quantities via “restock” and “sale” operations.
- Generate low-stock report and verify correctness.
- Restart and confirm data persistence.
- Trigger invalid SKUs or negative quantity adjustments.

---

### 7. Instructor Notes

- Focus feedback on:
  - How well the learner **structures** their code.
  - How they use **exceptions and validation** to create robust flows.
  - How they use **logging** for observability.
- Encourage learners to:
  - Reflect on what they would change with more time.
  - Identify next steps for Level 2 (e.g., OOP, testing frameworks, more advanced modules).

