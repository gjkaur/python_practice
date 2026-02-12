## Level 1 – Lesson-Level Module Content

This document details lesson-level content for each module in the Level 1 Professional Python course, aligned with the PCEP-30-02 syllabus and the high-level plan.

---

### Module 0 – Environment, Mindset, and Professional Practices

**Lesson 0.1 – Setting Up Python and the IDE**
- **Goal**: Install Python and an editor; run the first script like a real developer.
- **Content**:
  - Install Python; verify with `python --version` or `py --version`.
  - Install VS Code/Cursor, Python extension, configure interpreter.
  - Create project folder and first `.py` file.
  - Run script from IDE and from terminal (`python main.py`).
- **Examples**:
  - `hello_world.py` with `print("Hello, Python!")`.
  - Deliberate typo (`pritn`) to show `NameError` and how to read it.
- **Edge cases / misconceptions**:
  - Multiple Python versions (`python` vs `py` vs `python3`).
  - Forgetting to save the file before running.
- **Refactoring / demo**:
  - Start with top-level `print`, later refactor to `def main(): ...` and `if __name__ == "__main__": main()`.

**Lesson 0.2 – Virtual Environments & Project Structure**
- **Goal**: Understand basic environment isolation and folder layout.
- **Content**:
  - Why virtual environments matter.
  - `python -m venv .venv`, activation, `pip install`.
  - Simple project layout: `.venv/`, `src/` or root scripts, `README.md`.
- **Examples**:
  - Compare `pip list` before/after installing a package inside venv.
- **Edge cases / misconceptions**:
  - Installing packages globally by forgetting to activate the venv.
  - Deleting `.venv` and rebuilding it.
- **Refactoring / demo**:
  - Later show moving scripts into a `src/` folder while keeping run configs working.

**Lesson 0.3 – REPL vs Scripts, Basic Syntax & Layout**
- **Goal**: Differentiate REPL and scripts; understand indentation and comments.
- **Content**:
  - Start Python REPL, run simple expressions.
  - Indentation and blocks; comments, docstrings.
  - Script layout with `main()` entry point.
- **Examples**:
  - REPL: `2 + 3`, `print("Hi")`, variable assignments.
  - Script: “setup checker” printing `sys.version` and platform.
- **Edge cases / misconceptions**:
  - Mixing tabs and spaces.
  - Thinking REPL variables automatically exist in scripts.
- **Refactoring / demo**:
  - Convert a REPL experiment into a saved script with `main()`.

**Lesson 0.4 – PEP 8 Intro and Naming Conventions**
- **Goal**: Learn that style matters from day one.
- **Content**:
  - Naming: `snake_case` for functions/variables, `PascalCase` for classes, `UPPER_CASE` for constants.
  - Spacing, line length, blank lines.
- **Examples**:
  - “Messy” script refactored into PEP 8–compliant version.
- **Edge cases / misconceptions**:
  - Overusing comments instead of improving names.
- **Refactoring / demo**:
  - Pure style refactor of a small script: same behavior, better readability.

**Lesson 0.5 – Git Basics and Debugging Mindset**
- **Goal**: Initialize a repo, commit changes, and interpret Python tracebacks.
- **Content**:
  - `git init`, `git status`, `git add`, `git commit -m`.
  - `.gitignore` for `.venv`, `.pyc`, etc.
  - Anatomy of a traceback; “most recent call last”.
- **Examples**:
  - Introduce bug, run, read traceback, fix, commit.
- **Edge cases / misconceptions**:
  - Accidentally committing `.venv/`.
  - Reading the top of the traceback instead of the bottom.
- **Refactoring / demo**:
  - Compare history before/after a bug fix; show meaningful commit messages.

---

### Module 1 – Python & Programming Fundamentals

**Lesson 1.1 – Literals and Variables**
- **Goal**: Understand fundamental data values and variable binding.
- **Content**:
  - Literals: integers, floats, strings, booleans.
  - Assignment, reassignment, `type()` function.
- **Examples**:
  - `age = 30`, `pi = 3.14`, `is_student = True`, `name = "Alex"`.
  - Print values and their types.
- **Edge cases / misconceptions**:
  - Believing variables “contain” values vs “label” references.
  - Reusing names with incompatible meanings.
- **Refactoring / demo**:
  - Replace duplicated literals with constants (e.g., `TAX_RATE = 0.2`).

**Lesson 1.2 – Numeric Types and Operators**
- **Goal**: Use arithmetic and comparison operators correctly.
- **Content**:
  - Arithmetic: `+`, `-`, `*`, `/`, `//`, `%`, `**`.
  - Comparisons: `==`, `!=`, `<`, `<=`, `>`, `>=`.
  - Operator precedence and associativity.
- **Examples**:
  - BMI calculator and compound expressions.
  - Float demo: `0.1 + 0.2` vs `0.3`.
- **Edge cases / misconceptions**:
  - Confusing `/` and `//` (`5 / 2` vs `5 // 2`).
  - Expecting exact decimal behavior from floating-point.
- **Refactoring / demo**:
  - Introduce intermediate variables to clarify complex expressions.

**Lesson 1.3 – Boolean Logic and Truthiness**
- **Goal**: Build boolean expressions for decisions.
- **Content**:
  - Boolean literals; `and`, `or`, `not`.
  - Truthy/falsey values (empty strings, zero, empty lists).
- **Examples**:
  - Eligibility conditions: `(age >= 18 and has_id) or has_parent`.
  - `if user_input:` vs `if len(user_input) > 0:`.
- **Edge cases / misconceptions**:
  - Mistaking `=` for `==`.
  - Misunderstanding precedence of `and`/`or`.
- **Refactoring / demo**:
  - Extract complex conditions into named booleans for readability.

**Lesson 1.4 – Console Input and Output**
- **Goal**: Interact with the user via the console.
- **Content**:
  - `input(prompt)`, `print()` with `sep`, `end`.
  - f-strings and basic type conversions (`int`, `float`, `str`).
- **Examples**:
  - Ask for name and age, then print a formatted greeting.
  - Convert a simple unit with user-provided value.
- **Edge cases / misconceptions**:
  - Handling invalid numeric input (`ValueError`).
  - Trailing spaces and `.strip()`.
- **Refactoring / demo**:
  - Replace string concatenation with f-strings for clarity.

**Lesson 1.5 – Numeral Systems**
- **Goal**: Recognize binary, octal, decimal, and hex in Python.
- **Content**:
  - Literals: `0b1010`, `0o12`, `0xA`.
  - Built-ins: `bin()`, `oct()`, `hex()`.
- **Examples**:
  - Convert small integers to different bases and print them.
- **Edge cases / misconceptions**:
  - Thinking each representation is a different underlying number.
- **Refactoring / demo**:
  - Use hex constants in a small demo, explaining readability.

---

### Module 2 – Control Flow: Decisions and Loops

**Lesson 2.1 – Simple and Nested Conditionals**
- **Goal**: Use `if`, `elif`, `else` for branching logic.
- **Content**:
  - Syntax and indentation rules.
  - Chained conditionals (grade classification, etc.).
  - Nested `if` statements.
- **Examples**:
  - Number sign check (positive/negative/zero).
  - Simple grading scheme with `if-elif-else`.
- **Edge cases / misconceptions**:
  - Forgetting `:` or mis-indenting `elif` / `else`.
  - Writing “pyramids of doom”.
- **Refactoring / demo**:
  - Show deeply nested conditions and flatten with guard clauses.

**Lesson 2.2 – Guard Clauses & Defensive Conditionals**
- **Goal**: Reduce nesting and improve clarity with early returns.
- **Content**:
  - Pattern: `if invalid: return` early.
  - Separate validation from business logic.
- **Examples**:
  - `calculate_discounted_price` with early checks for invalid price.
- **Edge cases / misconceptions**:
  - Belief that functions should have a single `return` only.
- **Refactoring / demo**:
  - Take a nested function and gradually introduce guard clauses.

**Lesson 2.3 – While Loops and Input Loops**
- **Goal**: Use `while` loops for unknown-length repetition.
- **Content**:
  - Basic `while` syntax and `break` conditions.
  - Sentinel values and user-driven termination.
- **Examples**:
  - Prompt until user types `"quit"`.
  - Simple validation loop for numeric input.
- **Edge cases / misconceptions**:
  - Infinite loops from forgotten updates.
  - Off-by-one errors in counting.
- **Refactoring / demo**:
  - Replace repeated input blocks with a single `while` loop.

**Lesson 2.4 – For Loops, Range, and Iteration Patterns**
- **Goal**: Iterate safely over sequences and ranges.
- **Content**:
  - `for item in collection`.
  - `range(start, stop, step)` and its semantics.
  - Counting, searching, and aggregation patterns.
- **Examples**:
  - Summing numbers in a list.
  - Searching for a value and stopping at first match.
- **Edge cases / misconceptions**:
  - Misunderstanding that `range` stop is exclusive.
- **Refactoring / demo**:
  - Replace manual index loops with item-based loops (and vice versa when needed).

**Lesson 2.5 – Break, Continue, and Loop Else**
- **Goal**: Control loop behavior with `break`, `continue`, and `else`.
- **Content**:
  - Breaking out early vs skipping an iteration.
  - `for-else` and `while-else` basics.
- **Examples**:
  - Search loop with `else` used for “not found” message.
- **Edge cases / misconceptions**:
  - Misinterpreting `else` on loops as “run when condition was true”.
- **Refactoring / demo**:
  - Replace a manual “found flag” with a `for-else` structure.

---

### Module 3 – Core Data Collections

**Lesson 3.1 – Lists: Creation, Indexing, and Mutation**
- **Goal**: Use lists to store and manipulate ordered data.
- **Content**:
  - List literals, indexing, slicing (`lst[start:stop:step]`).
  - Mutating methods: `append`, `insert`, `remove`, `pop`, `sort`, `reverse`.
- **Examples**:
  - Maintain a list of student scores; add, update, remove.
- **Edge cases / misconceptions**:
  - Index out of range errors.
  - Sorting in-place vs using `sorted`.
- **Refactoring / demo**:
  - Replace many standalone variables (`score1`, `score2`, …) with one list.

**Lesson 3.2 – Copies, Aliasing, and List Comprehensions**
- **Goal**: Avoid aliasing bugs and write concise list transformations.
- **Content**:
  - Aliasing via `b = a`.
  - Safe copies via `a.copy()`, `a[:]`, `list(a)`.
  - Basic list comprehensions with simple conditionals.
- **Examples**:
  - Show aliasing effect by changing one variable and observing both.
  - Filter positive numbers and double them with comprehension.
- **Edge cases / misconceptions**:
  - Believing `b = a` creates a copy.
- **Refactoring / demo**:
  - Replace manual build loop with an equivalent comprehension and discuss trade-offs.

**Lesson 3.3 – Tuples and Basic Records**
- **Goal**: Use tuples for fixed-size records and unpacking.
- **Content**:
  - Creating tuples with and without parentheses.
  - Tuple unpacking (`name, score = student`).
  - Using tuples as immutable records or dictionary keys.
- **Examples**:
  - Represent `(name, score)` as a tuple; unpack for printing.
- **Edge cases / misconceptions**:
  - Attempting to assign to an element of a tuple.
- **Refactoring / demo**:
  - Replace two parallel lists with a list of tuples.

**Lesson 3.4 – Dictionaries and CRUD Operations**
- **Goal**: Store structured data in key-value pairs.
- **Content**:
  - Creating dicts; reading, updating, deleting keys.
  - Iterating through `keys()`, `values()`, `items()`.
- **Examples**:
  - Address book mapping names to phone numbers.
- **Edge cases / misconceptions**:
  - `KeyError` when accessing absent keys.
  - Using mutable objects as keys accidentally.
- **Refactoring / demo**:
  - Replace index-based mapping with a dict keyed by email or id.

**Lesson 3.5 – Strings and Simple Parsing**
- **Goal**: Manipulate and parse text input.
- **Content**:
  - Indexing, slicing strings.
  - Methods: `.upper()`, `.lower()`, `.strip()`, `.split()`, `.join()`.
  - Parsing comma-separated data.
- **Examples**:
  - Parsing `"Alice,85"` into `("Alice", 85)`.
- **Edge cases / misconceptions**:
  - Empty strings and whitespace-only input.
  - Incorrect assumptions about input format.
- **Refactoring / demo**:
  - Replace manual substring logic with `.split()` and `.join()`.

---

### Module 4 – Functions, Decomposition, and Exceptions

**Lesson 4.1 – Defining and Calling Functions**
- **Goal**: Encapsulate logic in reusable functions.
- **Content**:
  - `def` syntax; parameters and return values.
  - Distinguish `return` vs `print`.
  - Returning multiple values via tuples.
- **Examples**:
  - `def calculate_bmi(weight, height): ... return bmi`.
- **Edge cases / misconceptions**:
  - Forgetting `return` and getting `None`.
  - Printing instead of returning inside library functions.
- **Refactoring / demo**:
  - Extract repeated logic from a script into named functions.

**Lesson 4.2 – Parameters, Defaults, and Keyword Arguments**
- **Goal**: Design flexible function interfaces.
- **Content**:
  - Positional vs keyword arguments.
  - Default parameters and their use cases.
  - (Light) warning about mutable default arguments.
- **Examples**:
  - `def greet(name, greeting="Hello")`.
- **Edge cases / misconceptions**:
  - Mixing positional and keyword incorrectly.
  - Expecting defaults to re-evaluate every call.
- **Refactoring / demo**:
  - Replace multiple nearly identical functions with one function using parameters/defaults.

**Lesson 4.3 – Scope and Lifetime**
- **Goal**: Understand variable visibility in functions and modules.
- **Content**:
  - Local vs global scope and lifetime.
  - Module-level constants and configuration values.
  - Basic `global` usage (and why to avoid it).
- **Examples**:
  - Show variable defined in function not accessible outside.
  - `UnboundLocalError` from trying to assign to a global without `global`.
- **Edge cases / misconceptions**:
  - Assuming every variable is global unless declared otherwise.
- **Refactoring / demo**:
  - Replace global usage with passing parameters and returns.

**Lesson 4.4 – Built-in Exceptions and Error Thinking**
- **Goal**: Recognize and reason about common error types.
- **Content**:
  - Overview of `Exception` hierarchy.
  - Demonstrations of `ValueError`, `TypeError`, `ZeroDivisionError`, `IndexError`, `KeyError`.
  - When to fix the bug vs when to handle the exception.
- **Examples**:
  - Short snippets that intentionally raise each exception type.
- **Edge cases / misconceptions**:
  - Catching broad exceptions to “hide” bugs.
- **Refactoring / demo**:
  - Replace `except Exception:` with targeted exceptions.

**Lesson 4.5 – Try/Except and Graceful Failure**
- **Goal**: Handle predictable failures without crashing.
- **Content**:
  - `try/except` syntax; multiple `except` clauses.
  - Usage of `else` and `finally`.
  - Propagating exceptions vs handling locally.
- **Examples**:
  - Safe division function that catches `ZeroDivisionError`.
  - Simple file-read function handling `FileNotFoundError`.
- **Edge cases / misconceptions**:
  - Doing full business logic in `except` instead of small recovery.
  - Overusing try/except instead of validating inputs where appropriate.
- **Refactoring / demo**:
  - Replace nested `if` checks with clean `try/except` where exceptions are the natural model.

---

### Module 5 – Clean Code, Testing, and Small Systems

**Lesson 5.1 – PEP 8 Deep Dive and Code Smells**
- **Goal**: Recognize and improve unclean Python code.
- **Content**:
  - Deeper PEP 8 guidelines: layout, imports, docstrings.
  - Code smells: long functions, deeply nested conditionals, duplication, magic numbers.
- **Examples**:
  - “Bad code” file refactored in class step by step.
- **Edge cases / misconceptions**:
  - Over-commenting vs using clearer names and structure.
- **Refactoring / demo**:
  - Break one large, monolithic function into small single-responsibility functions.

**Lesson 5.2 – Intro to Testing**
- **Goal**: Write simple automated tests or checks.
- **Content**:
  - Concept of red/green/refactor.
  - Using `assert` for basic checks.
  - Introduce `unittest` or pytest-style test functions.
- **Examples**:
  - Tests for pure functions (e.g., `calculate_bmi`, `convert_temperature`).
- **Edge cases / misconceptions**:
  - Confusing manual console testing with automatable tests.
- **Refactoring / demo**:
  - Refactor to pure functions specifically to make testing easier.

**Lesson 5.3 – Logging vs Print**
- **Goal**: Use the `logging` module for diagnostics.
- **Content**:
  - `logging.basicConfig` and log levels (DEBUG, INFO, WARNING, ERROR).
  - Difference between user messages and logs.
- **Examples**:
  - Add logging calls to Safe Calculator for invalid inputs and errors.
- **Edge cases / misconceptions**:
  - Logging overly noisy debug info in production-like settings.
- **Refactoring / demo**:
  - Replace scattered debug `print` calls with logging at appropriate levels.

**Lesson 5.4 – Config Files and Simple Project Structure**
- **Goal**: Parameterize applications with configuration files and organize modules.
- **Content**:
  - Simple JSON/INI config format; loading with `json` or `configparser`.
  - Distinguish CLI entry point from library modules.
- **Examples**:
  - Configurable reminder CLI reading message and interval from a config file.
- **Edge cases / misconceptions**:
  - Hardcoding configuration values in multiple places.
- **Refactoring / demo**:
  - Move magic constants into config and create a loader function.

---

### Module 6 – Capstones and Professionalization

**Lesson 6.1 – Project Planning and Requirements**
- **Goal**: Translate an idea into clear requirements and tasks.
- **Content**:
  - User stories, acceptance criteria, constraints.
  - Sketching CLI flows and data model.
- **Examples**:
  - Expense Tracker: draft user stories for “add expense”, “list expenses”, “summarize by category”.
- **Refactoring / demo**:
  - Start with vague description, refine into concrete requirements.

**Lesson 6.2 – Architecture and Folder Structure**
- **Goal**: Apply the course’s architecture pattern to real projects.
- **Content**:
  - CLI entrypoint, validator layer, services layer, storage layer, logger.
  - Mapping the mermaid diagram to concrete files.
- **Examples**:
  - Walk through a skeleton `expense_tracker/` package with empty functions.
- **Refactoring / demo**:
  - Take a “flat” prototype script and reorganize it into modules.

**Lesson 6.3 – Implementation, Logging, and Tests**
- **Goal**: Implement features iteratively with logging and tests.
- **Content**:
  - Break capstone into small tasks; commit incrementally.
  - Add logging and basic tests for core services.
- **Refactoring / demo**:
  - Mid-project refactor that improves separation of concerns.

**Lesson 6.4 – Documentation and Final Polishing**
- **Goal**: Prepare portfolio-ready projects.
- **Content**:
  - Writing a clear README: problem, features, usage, limitations, future work.
  - Removing dead code and debugging artifacts.
- **Refactoring / demo**:
  - Before/after README and small code cleanups to show final polish.

