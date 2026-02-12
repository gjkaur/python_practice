## Level 1 Python – Curriculum Roadmap

**Course Name**: Python Level 1 – Professional Foundations  
**Primary Alignment**: PCEP-30-02 (Certified Entry-Level Python Programmer)  
**Secondary Goal**: Prepare for PCAP and entry-level professional Python roles.

---

### 1. High-Level Flow

The course is structured into **eight Level 1 modules**, delivered over approximately **10 weeks**:

- **M01 – Foundations and Tooling**  
  Environment, mindset, PEP 8, Git, and basic Python scripting.
- **M02 – Data Types and Operators (PCEP Section 1)**  
  Literals, variables, numeral systems, operators, and console I/O.
- **M03 – Control Flow and Loops (PCEP Section 2)**  
  Boolean logic, conditionals, loops, and iteration patterns.
- **M04 – Collections: Lists, Tuples, Dictionaries (PCEP Section 3)**  
  Core collection types and CRUD-style operations.
- **M05 – Strings and Text Processing (PCEP Section 3.4)**  
  String construction, slicing, escaping, and practical text handling.
- **M06 – Functions and Program Design (PCEP Section 4.1–4.2)**  
  Decomposition, parameters, scope, and reusable utilities.
- **M07 – Exceptions and Defensive Programming (PCEP Section 4.3–4.4)**  
  Exception hierarchy, try/except, and robust error-handling mindset.
- **M08 – Intro File I/O and Simple CLI Patterns**  
  Light, PCEP-adjacent topic that leverages course fundamentals to build small, production-like CLI tools.

Each module:

- Maps directly to one or more **PCEP objectives**.
- Contains **lesson-level outcomes**, **industry practices**, and **mini projects**.
- Builds toward one of the **two major capstone projects**.

See module-level details in `../modules/`.

---

### 2. Week-by-Week Progression

**Week 1 – Foundations and Tooling**  
_Modules_: M01 (core), M02 (preview)  
_Focus_:
- Setting up Python, editor/IDE, and virtual environments.
- Understanding interpreter vs compiler, syntax, semantics, indentation.
- Writing and running first scripts, using `print`, comments, and simple expressions.
- Introducing PEP 8, naming conventions, and Git basics.
- **Mini Project**: Developer Setup Checker (environment diagnostics script).

**Week 2 – Data Types, Operators, and Console I/O**  
_Module_: M02  
_Focus_:
- Boolean, integer, and floating-point types; scientific notation.
- Numeric, string, assignment, and comparison operators; precedence and binding.
- Numeral systems (binary, octal, decimal, hex) at the level needed for PCEP.
- `print()` and `input()`, advanced parameters (`sep`, `end`), `int()`, `float()`.
- **Mini Project**: Unit Converter CLI (with validation and meaningful error messages).

**Week 3 – Decisions and Branching**  
_Module_: M03 (conditionals)  
_Focus_:
- Boolean expressions, combining `and`/`or`/`not` safely.
- Conditional patterns: `if`, `if-else`, `if-elif-else`, nested `if` blocks.
- Guard clauses and avoiding excessive nesting (pyramid of doom).
- **Mini Project**: Admission Eligibility Checker (multi-criteria decision logic).

**Week 4 – Loops and Iteration Patterns**  
_Module_: M03 (loops)  
_Focus_:
- `while` and `for` loops, `range()`, `in` for iteration.
- Loop patterns for counting, aggregating, searching, and building menus.
- `break`, `continue`, `for-else`, `while-else` and when each is appropriate.
- **Mini Project**: CLI Menu System (robust interactive loop with validation).

**Week 5 – Lists and Tuples**  
_Module_: M04 (lists/tuples)  
_Focus_:
- Constructing lists; indexing, slicing, and negative indices.
- List operations and methods; shallow vs deep copying, cloning patterns.
- Tuples: creation, immutability, and their use for fixed-shape records/keys.
- **Mini Project**: Student Score Manager v1 (basic statistics using lists/tuples).

**Week 6 – Dictionaries and Strings**  
_Modules_: M04 (dicts), M05 (strings)  
_Focus_:
- Dictionaries for mapping keys to values; building, indexing, updating, deleting.
- Dictionary iteration, membership checks, `keys()`, `items()`, `values()`.
- Strings: literals, escaping, slicing, immutability, basic methods.
- **Mini Project**: Simple Address Book (CRUD operations over an in-memory dict).

**Week 7 – Functions and Decomposition**  
_Module_: M06  
_Focus_:
- Defining and invoking functions; parameters vs arguments; return values and `None`.
- Positional and keyword arguments, default values.
- Scope, name resolution, and when (not) to use `global`.
- **Mini Project**: Functional Refactor (refactor an earlier project into clean functions).

**Week 8 – Exceptions and Defensive Programming**  
_Module_: M07  
_Focus_:
- Python’s exception hierarchy (BaseException, Exception, and common concrete types).
- `try/except` patterns, branch ordering, and propagation through functions.
- Delegating responsibility for handling errors; fail-fast vs graceful-degradation.
- **Mini Project**: Safe Calculator (handles invalid input and arithmetic errors; logs failures).

**Week 9 – Strings, Text Processing, and Small Systems**  
_Modules_: M05 (deeper), M08 (intro CLI/file I/O)  
_Focus_:
- PEP 8 deep dive and common Python code smells.
- Using `logging` instead of `print` for operational insights.
- Basic testing (`unittest`-style, assertions) focused on business logic, not I/O.
- Simple configuration patterns (JSON/INI/.env-like) and structured CLI entry points.
- **Mini Project**: Configurable Reminder CLI (reads config, uses logging and tests key functions).

**Week 10 – Capstones and Professionalization**  
_Modules_: M06–M08 (integration)  
_Focus_:
- Building 2 capstone projects end-to-end (e.g., Expense Tracker and Inventory Manager).
- Applying modular architecture, logging, validation, and testing.
- Working with Git branches, pull requests, and code review checklists.
- Preparing a short architecture and demo-style walkthrough.

---

### 3. Alignment to PCEP Objectives

**Section 1 – Computer Programming and Python Fundamentals (18%)**

- Covered primarily in **M01** and **M02**:
  - Interpreting & interpreter vs compilation & compiler.
  - Lexis, syntax, semantics.
  - Literals (Boolean, integers, floats, strings) and numeral systems.
  - Variables, naming conventions, and PEP 8 recommendations.
  - Numeric, string, assignment, boolean, relational, and bitwise operators.
  - Floating-point accuracy caveats.
  - Console I/O via `print()` and `input()`, `int()` and `float()`.

**Section 2 – Control Flow: Conditional Blocks and Loops (29%)**

- Delivered in **M03**:
  - Conditional statements: `if`, `if-else`, `if-elif`, `if-elif-else`.
  - Multiple and nested conditionals; structuring decisions without confusion.
  - Loop constructs: `while`, `for`, `range()`, and `in`.
  - Loop patterns, nesting with conditionals, `break`, `continue`, `for-else`, `while-else`.

**Section 3 – Data Collections (25%)**

- Covered in **M04** and **M05**:
  - Lists: construction, indexing, slicing, methods, comprehensions, cloning, nested lists.
  - Tuples: structure, immutability, interactions with lists.
  - Dictionaries: building, indexing, insertion/removal, iteration, methods, key existence.
  - Strings: construction, indexing, slicing, escaping, quotes, multi-line strings, basic functions/methods.

**Section 4 – Functions and Exceptions (28%)**

- Implemented in **M06** and **M07**, with practical reinforcement in **M08**:
  - Defining and invoking functions; generators are conceptually mentioned but not emphasized at this level.
  - `return`, `None`, and function result patterns.
  - Parameters vs arguments; positional, keyword, and mixed calling conventions.
  - Default parameter values and their trade-offs.
  - Name scopes, shadowing, and `global`.
  - Built-in exception hierarchy (BaseException, Exception, ArithmeticError, LookupError, IndexError, KeyError, TypeError, ValueError, etc.).
  - `try/except` basics, ordering `except` branches, and exception propagation.

---

### 4. Skills Progression (Conceptual Stages)

- **Stage 1 – Foundations (Weeks 1–2)**
  - Syntax, semantics, data types, expressions, and simple I/O.
  - Students can read and write small scripts, interpret tracebacks, and modify code confidently.

- **Stage 2 – Control and Logic (Weeks 3–4)**
  - Translating rules into conditionals and loops.
  - Students can build interactive CLIs with clear branching and repetition patterns.

- **Stage 3 – Working with Data (Weeks 5–6)**
  - Using collections to model small datasets.
  - Students manage in-memory data for real use cases (scores, inventory, contacts).

- **Stage 4 – Abstraction and Robustness (Weeks 7–8)**
  - Decomposing into functions and handling errors intentionally.
  - Students create reusable utilities and start thinking in layers (validation, logic, I/O).

- **Stage 5 – Professionalization and Systems Thinking (Weeks 9–10)**
  - Applying clean code, testing, logging, and project structure to capstones.
  - Students operate in a workflow closer to professional teams (Git, reviews, small systems).

---

### 5. Bridge Toward PCAP and Professional Python

This Level 1 curriculum:

- **Exceeds PCEP** by embedding:
  - Git workflows.
  - Logging, basic testing, and configuration.
  - Modular design and separation of concerns.
- **Prepares for PCAP** by:
  - Establishing strong function design and error handling.
  - Building comfort with larger multi-file codebases.
  - Introducing patterns (e.g., services, validators, storage layers) that naturally extend to OOP and more advanced modules.

For detailed teaching plans and lesson structures, see the per-module documents under `../modules/`.

