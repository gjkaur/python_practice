## Teaching Notes – Python Level 1 Professional Course

These notes guide instructors (or self-paced learners acting as their own “coach”) on how to deliver the Level 1 course in a **job-focused, production-oriented** way while staying aligned with the **PCEP-30-02** syllabus.

---

### 1. Teaching Philosophy

- Treat learners as **junior developers in training**, not hobbyists.
- Make the connection to **real work** explicit in every module:
  - “This is how a production CLI would handle this.”
  - “This is the kind of bug you’ll see in tickets.”
- Emphasize **reading code** and **refactoring**, not just writing from scratch.

---

### 2. Lecture Flow per Module

For each module (M01–M08):

1. **Concept framing (10–20 min)**  
   - Connect PCEP objectives to real scenarios (e.g., lists for modeling students or inventory).
2. **Guided examples (20–30 min)**  
   - Live-code small, runnable snippets that demonstrate concepts.
   - Show both a naïve version and a more “production-ish” refactor.
3. **Hands-on practice (30–45 min)**  
   - Learners work on the curated exercise set.
   - Encourage pairing or small-group discussion.
4. **Mini-project integration (30–45 min)**  
   - Start or extend the module’s mini-project.
   - Focus on architecture and naming, not just making it run.
5. **Retrospective (10–15 min)**  
   - Discuss common mistakes and patterns noticed during practice.
   - Ask a few interview-style questions orally.

---

### 3. Typical Misconceptions to Address

- **M01–M02 (Foundations, Types, Operators)**
  - Treating Python like a calculator without understanding types.
  - Confusion between `=` and `==`.
  - Ignoring error messages instead of reading tracebacks.

- **M03 (Control Flow & Loops)**
  - Deeply nested `if` statements instead of guard clauses.
  - Off-by-one errors in loops.
  - Misunderstanding `for-else` and `while-else`.

- **M04–M05 (Collections & Strings)**
  - Using multiple parallel lists instead of dicts.
  - Misusing copying vs aliasing for lists.
  - Fragile string parsing without trimming or validation.

- **M06 (Functions & Design)**
  - Writing “god functions” that do everything.
  - Overusing `global` variables.
  - Forgetting to return values, leading to `None` where not expected.

- **M07 (Exceptions & Defensive Programming)**
  - Swallowing exceptions with `except: pass`.
  - Using exceptions for regular control flow instead of validation.
  - Catching `Exception` at very low levels and hiding real bugs.

- **M08 (File I/O & CLI Patterns)**
  - Mixing file I/O, CLI, and core logic in a single function.
  - Not handling missing or malformed files gracefully.

---

### 4. Pacing Suggestions (10-Week Format)

- Weeks 1–2: Move slower; ensure conceptual clarity on types, expressions, and simple scripts.
- Weeks 3–4: Spend extra time on **Boolean logic** and **loop patterns**; they underpin everything else.
- Weeks 5–6: Use real-life data modeling stories (students, inventory, expenses) for collections.
- Week 7–8: Focus on **design and robustness**; encourage refactoring earlier work.
- Weeks 9–10: Treat capstones like mini real-world projects; emphasize Git, documentation, and test plans.

If learners advance quickly, deepen exercises rather than moving to Level 2 topics prematurely.

---

### 5. Demo Ideas per Module

- **M01**: Show a broken script, read the traceback, and fix it together. Initialize Git and walk through commits.
- **M02**: Live-debug a bug caused by operator precedence and fix by adding parentheses.
- **M03**: Implement a small feature flag or access-check system using `if`/`elif` and loops.
- **M04**: Model a small dataset with lists vs dicts and discuss trade-offs.
- **M05**: Parse a small text log into structured data and print a summary.
- **M06**: Take a messy script and refactor into `main()`, `services.py`, and `validators.py`.
- **M07**: Show how a bare `except` hides a real bug, then refactor to specific exception types plus logging.
- **M08**: Build a tiny tool that reads config from JSON and prints a formatted report.

---

### 6. Code Review Guidance

Use the per-module **code review checklists** plus these global themes:

- **Naming & Readability**
  - Can someone new to the code understand it within minutes?
  - Are names meaningful and consistent?
- **Separation of Concerns**
  - Are UI, business logic, and persistence reasonably separated?
  - Is logic concentrated in functions or spread across top-level script code?
- **Defensive Thinking**
  - Where could this code break in production?
  - Are input validation and error messages adequate?

Encourage peer reviews in pairs or small groups using these checklists.

---

### 7. Git Workflow Suggestions

- Start each mini-project on a **feature branch**:
  - `feature/mp05-student-score-manager`
- Encourage:
  - Small, meaningful commits.
  - Descriptive messages: “Add statistics helpers” vs “fix stuff”.
- For capstones:
  - Require at least:
    - An **initial scaffolding commit** (structure only).
    - One or more **feature commits**.
    - A **cleanup/refactor commit** after initial implementation.

---

### 8. Assessment and Feedback Strategy

- **Midterm practical**:
  - Focus feedback on decomposition, data modeling, and correctness.
- **Final practical / capstones**:
  - Focus feedback on structure, robustness, and professional practices.
- Use rubric scores as a guide, but always include:
  - 2–3 clear strengths.
  - 2–3 concrete improvement suggestions.

Encourage learners to revise one mini-project or capstone after feedback as a growth exercise.

---

### 9. Preparing Learners for PCAP and Beyond

- Highlight how:
  - Collections and functions lead naturally into **classes** and **methods**.
  - Modules and packages here map onto PCAP’s module and package topics.
- Suggest next steps:
  - Introduce OOP for expense and inventory items.
  - Add richer testing with `unittest` or `pytest`.
  - Explore selected parts of the standard library (e.g., `datetime`, `argparse`).

