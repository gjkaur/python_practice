## Level 1 – PCEP-30-02 Aligned Course Redesign

This redesign uses the official PCEP-30-02 exam syllabus (`Level_1.pdf`) as the primary source of truth.  
All modules, lessons, and projects explicitly map to **Sections 1–4** and their objective codes (1.1–4.4).

---

### 1. Direct Mapping to PCEP Sections & Objectives

PCEP defines four sections:

- **Section 1 – Computer Programming and Python Fundamentals (18%)**
- **Section 2 – Control Flow – Conditional Blocks and Loops (29%)**
- **Section 3 – Data Collections – Tuples, Dictionaries, and Lists (25%)**
- **Section 4 – Functions and Exceptions (28%)**

Below is a concise mapping of course topics to the official objective codes and bullets from `Level_1.pdf`.

#### 1.1 Section 1 – Fundamentals (PCEP-30-02 1.1–1.4)

- **PCEP-30-02 1.1 – Understand fundamental terms and definitions**
  - interpreting and the interpreter, compilation and the compiler  
  - lexis, syntax, and semantics  
  - **Course mapping**:
    - Module 0: Lessons 0.1–0.3 (interpreter vs compiler, REPL vs scripts).  
    - Module 1: Lesson 1.1 (syntax/semantics with concrete code examples).

- **PCEP-30-02 1.2 – Understand Python’s logic and structure**
  - keywords  
  - instructions  
  - indentation  
  - comments  
  - **Course mapping**:
    - Module 0: 0.3 (indentation, comments).  
    - Module 1: 1.1–1.3 (keywords in examples, statement forms).

- **PCEP-30-02 1.3 – Introduce literals and variables; numeral systems**
  - Boolean, integers, floating-point numbers, scientific notation  
  - strings  
  - binary, octal, decimal, hexadecimal numeral systems  
  - variables, naming conventions, implementing PEP 8 recommendations  
  - **Course mapping**:
    - Module 1: 1.1 (literals & variables, naming).  
    - Module 1: 1.2 (numeric types, scientific notation).  
    - Module 1: 1.5 (numeral systems & conversions).  
    - Module 0: 0.4 (PEP 8 emphasis).

- **PCEP-30-02 1.4 – Choose operators and data types adequate to the problem**
  - arithmetic, assignment, comparison, logical and bitwise operators  
  - priorities and binding  
  - simple input and output operations  
  - type casting  
  - **Course mapping**:
    - Module 1: 1.2 (arithmetic/comparison, precedence).  
    - Module 1: 1.3 (boolean logic basics).  
    - Module 1: 1.4 (input/output, casting).  
    - Projects: MP2 Unit Converter.

#### 1.2 Section 2 – Control Flow (PCEP-30-02 2.1–2.2)

- **PCEP-30-02 2.1 – Make decisions and branch the flow**
  - relational and equality operators  
  - building complex Boolean expressions  
  - conditional statements: `if`, `if-else`, `if-elif-else`  
  - nesting and indentation levels  
  - **Course mapping**:
    - Module 2: 2.1–2.2.  
    - Projects: MP3 Admission Eligibility Checker.

- **PCEP-30-02 2.2 – Perform different types of loops**
  - `while`, `for`, `range()`  
  - `break`, `continue`, `else` on loops  
  - iterating through sequences and simple numeric ranges  
  - **Course mapping**:
    - Module 2: 2.3–2.5.  
    - Projects: MP4 CLI Menu System, MP5/MP6 loop-based operations.

#### 1.3 Section 3 – Data Collections (PCEP-30-02 3.1–3.4)

- **PCEP-30-02 3.1 – Collect and process data using lists**
  - list creation, indexing, slicing  
  - `len()`, list methods (`append`, `insert`, `index`, etc.)  
  - `sorted()`, `del`, iterating with `for`  
  - `in` / `not in`, list comprehensions, copying/cloning, nested lists  
  - **Course mapping**:
    - Module 3: 3.1–3.2.  
    - Project: MP5 Student Score Manager v1.

- **PCEP-30-02 3.2 – Collect and process data using tuples**
  - tuple creation, indexing, slicing, immutability  
  - tuples vs lists; nesting tuples/lists  
  - **Course mapping**:
    - Module 3: 3.3.  
    - Projects: MP5 (list of tuples) and MP7 refactor.

- **PCEP-30-02 3.3 – Collect and process data using dictionaries**
  - building, indexing, adding/removing keys  
  - iterating through keys/values/items  
  - checking key existence; `keys()`, `items()`, `values()`  
  - **Course mapping**:
    - Module 3: 3.4.  
    - Project: MP6 Address Book CLI; Inventory capstone.

- **PCEP-30-02 3.4 – Operate with strings**
  - constructing strings; indexing, slicing, immutability  
  - escaping with `\`; quotes and apostrophes; multi-line strings  
  - basic string functions and methods  
  - **Course mapping**:
    - Module 3: 3.5.  
    - Used across projects: parsing config, logs, and CLI inputs.

#### 1.4 Section 4 – Functions and Exceptions (PCEP-30-02 4.1–4.4)

- **PCEP-30-02 4.1 – Decompose the code using functions**
  - defining and invoking user-defined functions  
  - the `return` keyword, results, `None`  
  - recursion (introduced conceptually only at Level 1)  
  - **Course mapping**:
    - Module 4: 4.1–4.2.  
    - MP7 Functional Refactor; all capstones.

- **PCEP-30-02 4.2 – Organize interaction between function and environment**
  - parameters vs arguments  
  - positional, keyword, mixed argument passing  
  - default parameter values  
  - name scopes, shadowing, `global`  
  - **Course mapping**:
    - Module 4: 4.2–4.3.  
    - Reinforced in Module 5 (testable, pure functions).

- **PCEP-30-02 4.3 – Python Built-In Exceptions Hierarchy**
  - `BaseException`, `Exception`, `SystemExit`, `KeyboardInterrupt`  
  - abstract exceptions (`ArithmeticError`, `LookupError`)  
  - specific exceptions: `IndexError`, `KeyError`, `TypeError`, `ValueError`  
  - **Course mapping**:
    - Module 4: 4.4 (exception types).  
    - Referenced in MP8 Safe Calculator & MP9/config loading.

- **PCEP-30-02 4.4 – Basics of Python Exception Handling**
  - `try-except` pattern  
  - ordering `except` branches  
  - propagating exceptions; delegating handling  
  - **Course mapping**:
    - Module 4: 4.5.  
    - Module 5: 5.2 & 5.3 (tests and logging), all capstones.

---

### 2. Redesigned Module & Week Structure (PCEP-First View)

This version rearranges the earlier roadmap so that each week foregrounds the **official objectives** and uses industry practices as supporting layers.

#### Week 1 – Fundamentals, Terminology, and Environment (1.1–1.3)

- **Objectives**:
  - PCEP 1.1 (terms: interpreter, compiler, lexis, syntax, semantics).
  - PCEP 1.2 (keywords, instructions, indentation, comments).
  - PCEP 1.3 (literals, variables, numeral systems basics).
- **Lessons**:
  - 0.1–0.3, 0.4, 1.1, partial 1.5 (decimal only).
- **Practice**:
  - Short exercises labelling code as syntax vs semantics issues.
  - Tiny REPL-to-script exercises.
- **Mini Project**:
  - MP1 Developer Setup Checker (plus a few questions explicitly referencing 1.1–1.3).

#### Week 2 – Data Types, Operators, and Console I/O (1.3–1.4)

- **Objectives**:
  - PCEP 1.3 (scientific notation, binary/octal/hex literal recognition).
  - PCEP 1.4 (operators, priorities, simple input/output, casting).
- **Lessons**:
  - 1.2, 1.3, 1.4, 1.5 (full numeral systems coverage).
- **Practice**:
  - Operator precedence puzzles; translating math formulas into Python.
  - Type casting exercises with invalid input analysis.
- **Mini Project**:
  - MP2 Unit Converter CLI – explicitly mention objectives 1.3, 1.4 at the top of the spec.

#### Week 3 – Decisions & Branching (2.1)

- **Objectives**:
  - PCEP 2.1 (relational/equality operators, complex Boolean expressions, conditional blocks).
- **Lessons**:
  - 2.1 & 2.2 (simple and nested conditionals, guard clauses).
- **Practice**:
  - Translate natural language rules into precise conditionals.
  - Debugging exercises where a single `>` vs `>=` changes outcomes.
- **Mini Project**:
  - MP3 Admission Eligibility Checker – annotated with PCEP 2.1 mapping.

#### Week 4 – Loops & Iteration Patterns (2.2)

- **Objectives**:
  - PCEP 2.2 (`while`, `for`, `range`, `break`, `continue`, `else`).
- **Lessons**:
  - 2.3–2.5 (input loops, iteration patterns, `for-else`).
- **Practice**:
  - Counting, searching, aggregation tasks with both `for` and `while`.
- **Mini Project**:
  - MP4 CLI Menu System – highlight 2.2 in the specification.

#### Week 5 – Lists & Tuples (3.1–3.2)

- **Objectives**:
  - PCEP 3.1 (lists: creation, indexing, slicing, methods, list comprehensions).
  - PCEP 3.2 (tuples: immutability, use vs lists).
- **Lessons**:
  - 3.1–3.3.
- **Practice**:
  - List transformation and filtering with and without comprehensions.
  - Converting between list of separate values and list of tuples.
- **Mini Project**:
  - MP5 Student Score Manager v1 (score list, list of tuples).

#### Week 6 – Dicts & Strings (3.3–3.4)

- **Objectives**:
  - PCEP 3.3 (dictionaries: build/index/update/delete, iterate keys/values/items, `in` checks).
  - PCEP 3.4 (strings: construction, slicing, escaping, multi-line, methods).
- **Lessons**:
  - 3.4 (dicts) and 3.5 (strings).
- **Practice**:
  - Build small JSON-like in-memory structures; write search functions.
  - String parsing for simple CSV-like lines.
- **Mini Project**:
  - MP6 Address Book CLI – explicit use of 3.3 and 3.4.

#### Week 7 – Functions & Decomposition (4.1–4.2)

- **Objectives**:
  - PCEP 4.1 (defining functions, `return`, `None`, basic recursion concept).
  - PCEP 4.2 (parameters vs arguments, positional/keyword, defaults, scope, `global`).
- **Lessons**:
  - 4.1–4.3.
- **Practice**:
  - Writing small functions with clear signatures.
  - Tracing variable scope in nested functions.
- **Mini Project**:
  - MP7 Functional Refactor – tag all refactors with which 4.1/4.2 subpoints they reinforce.

#### Week 8 – Exceptions & Robustness (4.3–4.4)

- **Objectives**:
  - PCEP 4.3 (built-in exceptions hierarchy).
  - PCEP 4.4 (basic exception handling, branch ordering, propagation).
- **Lessons**:
  - 4.4–4.5.
- **Practice**:
  - Creating tiny examples that intentionally raise each listed exception type.
  - Refactoring to delegate exception handling across function boundaries.
- **Mini Project**:
  - MP8 Safe Calculator – explicit tests for `ValueError` and `ZeroDivisionError`.

#### Week 9 – Integration: Testing, Logging, Config (Cross-Cutting)

- **Objectives**:
  - Uses knowledge from Sections 1–4; not additional PCEP content, but deepens exam readiness and professional skills.
- **Lessons**:
  - 5.1–5.4 (clean code, tests, logging, config).
- **Practice**:
  - Add logging and tests to prior mini projects.
  - Convert environment-sensitive values to config files.
- **Mini Project**:
  - MP9 Configurable Reminder CLI.

#### Week 10 – Capstones (Integrated Objectives 1.1–4.4)

- **Objectives**:
  - Apply all PCEP topics (1.1–4.4) in realistic projects with proper architecture.
- **Lessons**:
  - 6.1–6.4 (planning, architecture, implementation, documentation).
- **Capstones**:
  - Expense Tracker and Inventory App (or equivalent), built per the structure in the main plan.
- **Assessment**:
  - Final practical rubric directly referencing correct use of:
    - Lists/tuples/dicts/strings (Section 3).  
    - Conditionals/loops (Section 2).  
    - Functions/exceptions (Section 4).

---

### 3. Assessment & Quiz Design Directly from PDF Objectives

- **Concept Quizzes**:
  - Build question banks where each question is tagged with a **PCEP objective code** (e.g., `Q12 → 3.1 list comprehensions`).
  - Maintain coverage tables to ensure all 1.1–4.4 objectives are assessed multiple times.

- **Practical Exams (Mid & Final)**:
  - Each major requirement explicitly lists which PCEP objective it demonstrates.
  - Example: “Implement a function that calculates and returns statistics (Objectives: 3.1 lists, 4.1 functions, 4.2 parameters).”

- **Rubrics**:
  - The rubric in `LEVEL1_RUBRICS.md` can be extended with a column for “Primary PCEP objective(s) demonstrated”, ensuring traceability to the PDF.

---

### 4. How This Redesign Differs from the Initial Plan

- Keeps your previous **Module 0–6 structure**, but:
  - Makes **PCEP sections and objective codes explicit** in every week/module.
  - Ensures **every bullet from `Level_1.pdf`** (lists, tuples, dicts, strings, control flow, functions, exceptions) has an identified lesson and at least one project use.
  - Tightens assessment design so that quizzes and practicals can be audited against the official exam blueprint.

Use this file as the top-level, PCEP-facing plan; the other documents (`LEVEL1_MODULE_CONTENT.md`, `LEVEL1_PROJECT_SPECS.md`, `LEVEL1_RUBRICS.md`, `LEVEL1_TEACHING_ASSETS.md`) remain as implementation/detail layers beneath it.

