## Level 2 – Evaluation Rubrics

Rubrics for Level 2 assignments, mini projects, code reviews, and capstones. Aligned with PCAP-31-03.

---

### 1. Mini Project Rubric (0–3 per criterion)

**1.1 Correctness (0–9)**
- **0**: Code does not run or fails core scenarios.
- **3**: Runs but fails many cases or crashes often.
- **6**: Mostly correct; minor edge cases.
- **9**: Correct across requirements and common edge cases.

**1.2 PCAP Concept Alignment (0–6)**
- Target concepts (modules, exceptions, OOP, strings, comprehensions, I/O) used correctly.
- **0**: Concepts misused or ignored.
- **3**: Some misuse or anti-patterns.
- **6**: Concepts correctly and appropriately applied.

**1.3 Code Structure & Modularity (0–6)**
- Multi-module layout; clear separation of concerns.
- PEP 8 naming; docstrings where needed.
- **0**: Monolithic; poor structure.
- **3**: Some structure but long functions or duplication.
- **6**: Clear, modular; single-responsibility.

**1.4 Error Handling & Exceptions (0–3)**
- **0**: No validation; crashes on invalid input.
- **1**: Minimal checks.
- **2**: Handles common invalid inputs.
- **3**: Good coverage; clear messages; custom exceptions where appropriate.

**1.5 Git & Iterative Development (0–3)**
- **0**: No Git or single dump commit.
- **1**: Few commits; vague messages.
- **2**: Multiple commits; reasonable messages.
- **3**: Logical commits; clear messages.

**1.6 Testing (0–3)**
- **0**: No tests.
- **1**: Manual test cases in README.
- **2**: Basic automated tests or assert.
- **3**: Good coverage of success and failure paths.

---

### 2. Code Review Rubric (Pass / Needs Work)

**2.1 Readability & Style**
- PEP 8; consistent indentation; docstrings.
- Code understandable without running.

**2.2 Correctness & Edge Cases**
- Implements specified behavior; edge cases considered.
- No obvious logic flaws.

**2.3 Separation of Concerns**
- Business logic vs I/O.
- Module boundaries clear.
- Data access abstracted (capstones).

**2.4 Error Handling**
- Specific exceptions; no bare except.
- Clear messages; logging where helpful.

**2.5 Testability**
- Pure functions where possible.
- Tests meaningful and not trivial.

---

### 3. Capstone Rubric

Capstones use the same criteria as mini projects, with higher expectations:
- **Modularity**: At least 4–6 modules; clear package structure.
- **OOP**: At least 2–3 classes; inheritance where appropriate.
- **Exceptions**: Custom exception hierarchy; defensive validation.
- **I/O**: File persistence; with statement; errno handling.
- **Professional practices**: README, basic tests, Git history.

---

### 4. Practical Exams (Midterm / Final)

- **Scope**: Mix of PCAP objective codes; 1–2 hours.
- **Format**: Small programs; fill-in; trace output; debugging.
- **Criteria**: Correctness; PCAP alignment; code quality.

See `../python-level-2-course/assessments/` for exam materials.
