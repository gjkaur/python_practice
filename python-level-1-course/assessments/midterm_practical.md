## Midterm Practical – Level 1 Python Course

### 1. Purpose

Assess learners’ ability to apply **PCEP-aligned fundamentals** (data types, operators, control flow, collections, basic functions) in a small, time-boxed coding task with professional expectations:

- Clean code.
- Basic validation and error handling.
- Simple modular design.

---

### 2. Scenario

Implement a **Student Result Processor v1** as a standalone script or small multi-file mini-app.

Requirements (high-level):

- Read a small, hard-coded list of students and scores (in code).
- Compute:
  - Average score.
  - Highest and lowest score.
  - Simple pass/fail classification (threshold, e.g., 60).
- Provide a CLI to:
  - Show all students and scores.
  - Show summary statistics.
  - Show only passing students.

Timebox: ~90 minutes.

---

### 3. Functional Requirements

- Use built-in types and operators only (no external libraries).
- Implement at least:
  - One function for computing stats (min, max, average).
  - One function for filtering passing students.
- Must not crash for normal usage.

---

### 4. Non-Functional Requirements

- Code style:
  - PEP 8 indentation and naming.
  - No excessively long functions.
- Structure:
  - At minimum, a `main()` function.
  - Prefer 2–3 helper functions where appropriate.
- Error handling:
  - Basic guard against empty score lists (e.g., no division by zero).

---

### 5. Grading Rubric (0–20)

**1. Correctness (0–6)**  
- 0–1: Frequent errors; does not run end-to-end.  
- 2–3: Partially correct; some statistics incorrect or unstable.  
- 4–5: Mostly correct; minor edge-case issues.  
- 6: All functional requirements met; correct for typical and edge inputs.

**2. Code Quality & PEP 8 (0–4)**  
- 0–1: Poor naming, inconsistent formatting, unclear flow.  
- 2–3: Generally clean; minor style issues.  
- 4: Very clean; good names; formatting aligns with PEP 8.

**3. Design & Modularity (0–5)**  
- 0–1: All logic in one big block.  
- 2–3: Some decomposition into functions; `main()` present.  
- 4–5: Functions are focused; decomposition supports readability and reuse.

**4. Error Handling & Validation (0–3)**  
- 0: No consideration of edge cases or errors.  
- 1–2: Some guards (e.g., empty list, invalid threshold).  
- 3: Clear, consistent defensive checks where appropriate.

**5. Professional Practices (0–2)**  
- 0: No comments or explanation; no Git usage.  
- 1: Basic comments; a couple of meaningful commits.  
- 2: Clear commit history, brief notes on design decisions.

Total: **/20**

---

### 6. Suggested Deliverables

- Source file(s) (`.py`).
- Short `README` or comment block describing:
  - How to run the script.
  - What it does.
- Optional: `git log` output or link to repository branch.

---

### 7. Instructor Notes

- Observe how learners:
  - Interpret requirements.
  - Decompose the problem.
  - Name functions and variables.
- Provide written or verbal feedback focusing on:
  - Decomposition.
  - Data modeling (lists/dicts).
  - Edge case handling.

