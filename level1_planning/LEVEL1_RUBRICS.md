## Level 1 – Evaluation Rubrics

This document defines rubrics for:
- Weekly assignments and mini projects.
- Code reviews (peer or instructor).
- Quizzes (conceptual understanding).
- Mid-course practical exam.
- Final practical capstones.

Rubrics are aligned with PCEP-30-02 objectives and professional coding standards.

---

### 1. Weekly Assignment & Mini Project Rubric

Use a 0–3 scale per criterion (0 = Not met, 1 = Partially, 2 = Mostly, 3 = Fully). You can adjust weights, but a /30 score is a good default.

**1.1 Correctness (0–9)**
- **0**: Code does not run or fails basic scenarios; key requirements unmet.
- **3**: Code runs but fails many core scenarios or crashes on common input.
- **6**: Mostly correct; minor logic errors or unhandled edge cases remain.
- **9**: Correct behavior across specified requirements and common edge cases.

**1.2 PCEP Concept Alignment (0–6)**
- Checks use of concepts targeted that week (e.g., variables/operators, control flow, collections, functions, exceptions).
- **0**: Target concepts misused or largely ignored.
- **3**: Concepts used but with notable misunderstandings or anti-patterns.
- **6**: Concepts correctly and appropriately applied to solve the problem.

**1.3 Code Structure & Readability (0–6)**
- Naming (PEP 8), function decomposition, comments/docstrings, line length.
- **0**: Unstructured, confusing code; poor naming; no comments where needed.
- **3**: Some structure and reasonable naming, but still long functions or duplication.
- **6**: Clear, modular structure with single-responsibility functions and readable names.

**1.4 Error Handling & Validation (0–3)**
- **0**: No validation; program easily crashes on invalid input.
- **1**: Minimal checks; only some invalid inputs handled.
- **2**: Handles common invalid inputs with sensible messages.
- **3**: Good coverage of likely invalid inputs; clear, user-friendly error messages.

**1.5 Git Usage & Iterative Development (0–3)**
- **0**: No Git usage or a single large “dump” commit.
- **1**: Few commits or vague messages; large, mixed changes.
- **2**: Multiple commits with reasonably descriptive messages.
- **3**: Regular, logical commits with clear messages describing the change.

**1.6 Testing Effort (0–3)**
- **0**: No tests or documented checks.
- **1**: Some manual test cases described in comments or README.
- **2**: At least basic automated tests or `assert` statements for core logic.
- **3**: Good coverage of success and failure paths with automated tests.

---

### 2. Code Review Rubric (Peer or Instructor)

Each category can be rated as **Pass** / **Needs Work**, with 1–2 sentences of feedback.

**2.1 Readability & Style**
- Uses PEP 8 naming, consistent indentation, appropriate comments/docstrings.
- Code is understandable without running it.

**2.2 Correctness & Edge Cases**
- Implements specified behavior; considers typical edge cases.
- No obvious logic flaws in core flows.

**2.3 Separation of Concerns**
- Business logic separated from I/O (e.g., pure functions vs CLI).
- Data access abstracted where appropriate (especially in capstones).

**2.4 Error Handling & Logging**
- Uses specific exceptions instead of bare `except`.
- Logs or explains important failures in a way that aids debugging.

**2.5 Testability & Tests**
- Presence of pure functions that can be tested.
- Tests (if present) are meaningful and not trivial or redundant.

---

### 3. Quiz Rubric (Conceptual)

Quizzes are usually multiple-choice and short answer questions.

**3.1 Multiple-Choice Questions**
- Typically 1 point per question.
- Focused on:
  - Operator precedence and semantics.
  - Flow control behavior (`for-else`, `while-else`, `break`, `continue`).
  - Data types and literals (e.g., differences between list/tuple).
  - Function semantics (parameters, defaults, return values, scope).
  - Exceptions and error types.

**3.2 Short Answer / Explanation Questions**
- Scored 0–2:
  - **0**: Incorrect or missing explanation.
  - **1**: Partially correct but vague or incomplete reasoning.
  - **2**: Accurate explanation using correct terminology and examples.

Examples:
- Conceptual: “Explain the difference between a list and a tuple and when to use each.”
- Debugging: “Why does this snippet raise an `IndexError`? How can you fix it?”

---

### 4. Mid-Course Practical Exam Rubric

Suitable for Week 5–6 practical focused on fundamentals, control flow, and basic collections/functions. Suggested /100 weighting:

**4.1 Core Correctness (30)**
- Implements the required features correctly (e.g., data operations and control flow).
- Handles basic specified scenarios without errors.

**4.2 Use of Required Constructs (20)**
- Appropriately uses constructs emphasized so far:
  - Variables and operators.
  - Conditional logic and loops.
  - Lists/tuples/dicts and simple string operations.
  - Functions with parameters and returns.

**4.3 Code Organization & Readability (20)**
- Code is broken into well-named, coherent functions.
- Avoids large monolithic sections and excessive duplication.
- Follows PEP 8 conventions reasonably well.

**4.4 Defensive Programming & Error Handling (15)**
- Validates user input or external data where reasonable.
- Deals gracefully with predictable errors (e.g., empty data, invalid choices).
- Does not rely on bare `except` or silent failure.

**4.5 Git & Project Hygiene (10)**
- Project has a clean tree:
  - No `.venv`, large binaries, or compiled artifacts committed.
  - `.gitignore` configured appropriately.
- Commit history shows incremental progress with meaningful messages.

**4.6 Tests or Systematic Checking (5)**
- At least a minimum level of automated or semi-automated checks:
  - Simple test functions.
  - Assertions with explanation.

**Score Bands**
- **0–49**: Fail – Major requirements missing or unstable program.
- **50–79**: Pass – Meets core requirements with acceptable structure.
- **80–100**: Strong Pass – Robust, well-structured solution with clear code quality.

---

### 5. Final Practical / Capstone Rubric

Used to evaluate capstone projects in Week 10. Suggested /100 weighting:

**5.1 Functionality vs Requirements (30)**
- Implements required features (e.g., add/list/summarize for Expense Tracker or core inventory operations).
- Key user flows work correctly and are demonstrable.

**5.2 Architecture & Separation of Concerns (25)**
- Follows the recommended architecture:
  - CLI entry module.
  - Validation layer.
  - Service/business-logic layer.
  - Storage layer.
  - Logging separated from user output where possible.
- Modules have clear, single responsibilities.

**5.3 Code Quality & Professionalism (20)**
- Consistent naming and formatting; minimal dead code.
- Clear docstrings and comments where needed.
- Project is structured in a way a teammate could reasonably understand.

**5.4 Error Handling, Validation, and Logging (10)**
- Common invalid inputs are handled gracefully (no unexpected tracebacks).
- Exceptions are used properly (specific types and sensible handling).
- Logging captures important events and failures.

**5.5 Testing (10)**
- Automated tests exist for core logic functions:
  - For example, summary calculations or inventory operations.
- Tests are meaningful (cover typical and edge cases) and pass reliably.

**5.6 Git History & Documentation (5)**
- README clearly documents:
  - Project purpose.
  - How to install and run.
  - Example usages or scenarios.
- Git history shows iterative development instead of last-minute dump.

**Score Bands**
- **90–100**: Excellent – Near “junior developer ready” level; minor polish needed.
- **75–89**: Strong – Solid understanding and implementation; a few improvements needed.
- **60–74**: Adequate – Meets course outcomes but with notable weaknesses.
- **<60**: Incomplete or significantly flawed; major rework needed.

---

### 6. Portfolio & Capstone Review Guidelines

In addition to numeric rubrics, use a brief qualitative review:

- **Problem Statement Clarity**
  - Can the student clearly describe what their project does and for whom?
- **Architecture Explanation**
  - Can they explain how modules interact (CLI, validators, services, storage, logging)?
- **Key Design Decisions**
  - Can they justify choices like data structures, error handling strategies, and configuration method?
- **Reflection & Next Steps**
  - Can they identify at least one area for improvement or an extension they would add in a “Level 2” version?

These narrative elements help students practice professional communication about their code alongside the more formal, numeric evaluation.

