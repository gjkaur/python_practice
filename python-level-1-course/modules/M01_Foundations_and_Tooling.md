## M01 – Foundations and Tooling

**PCEP Alignment**: Section 1 (intro to interpreter, syntax, semantics, basic instructions, indentation, comments)  
**Professional Focus**: Environment, Git, PEP 8, debugging mindset.

---

### 1. Outcomes (Job-Skill Phrasing)

By the end of this module, a learner should be able to:

- Set up a **professional Python development environment** using virtual environments and a code editor/IDE.
- Create, run, and debug **Python scripts** from the command line and IDE.
- Apply **PEP 8** and consistent **naming conventions** to all new code.
- Use **Git** to version-control code (init, status, add, commit, basic branching).
- Read and interpret **tracebacks** to locate and fix errors.
- Explain, in plain language, **what a Python interpreter does** and how it differs from a compiler.

---

### 2. Core Concepts and Explanations

#### 2.1 Interpreter vs Compiler (PCEP 1.1)

- A **compiler** translates source code into a separate executable before running it.  
- An **interpreter** (like CPython) reads and executes code line by line (internally there is compilation to bytecode, but conceptually it’s interactive).

Key ideas:

- Python code is run by the **Python interpreter** (`python` / `python3` command).
- You can run Python:
  - In the **REPL** (interactive prompt) for quick experiments.
  - As **scripts** (`.py` files) for reusable programs.

#### 2.2 Lexis, Syntax, Semantics (PCEP 1.1)

- **Lexis**: the “vocabulary” (keywords, identifiers, literals, operators).
- **Syntax**: how tokens can be combined (grammatical rules).
- **Semantics**: what those valid combinations actually *do*.

Example:

```python
message = "Hello"
print(message)
```

- Lexis: `message`, `"Hello"`, `print`, `=`, `()`.
- Syntax: assignment statement + function call.
- Semantics: binds name `message` to the string `"Hello"` and prints it.

If syntax is wrong:

```python
print "Hello"  # SyntaxError in Python 3
```

You get a **SyntaxError**, and the interpreter will show a traceback.

#### 2.3 Indentation and Instructions (PCEP 1.2)

Python uses **indentation** instead of braces to mark blocks:

```python
value = 10

if value > 5:
    print("Greater than five")
```

- The **indent** after `if` is part of the syntax.
- Inconsistent indentation leads to **IndentationError**.

#### 2.4 Comments and Script Structure

Use `#` for single-line comments:

```python
# This script prints a greeting
print("Hello, developer!")
```

Early introduction to a **script entrypoint**:

```python
def main() -> None:
    print("Hello from main()")


if __name__ == "__main__":
    main()
```

This pattern prepares students for larger programs.

#### 2.5 Environment, Virtualenv, and Tooling

- Use `python -m venv .venv` to create a virtual environment.
- Activate it before installing packages.
- Configure the IDE (e.g., VS Code/Cursor) to use the `.venv` interpreter.

This ensures reproducible environments similar to professional workflows.

#### 2.6 Git Basics

Essential commands:

```bash
git init
git status
git add .
git commit -m "Initial commit"
```

Teach:

- **Small, focused commits**.
- Meaningful messages (“Add basic CLI skeleton” vs “changes”).

---

### 3. Edge Cases and Common Mistakes

- Mixing tabs and spaces → **IndentationError**.  
  - Configure the editor to use spaces only (4 spaces per indent).
- Forgetting to save before run → script appears unchanged.  
  - Habit: *save → run* cycle.
- Running Python with a different interpreter than the one configured in the project environment.
- Ignoring error messages; closing the terminal instead of reading the traceback.

---

### 4. Production Notes (PEP 8, Naming, Modularity, Validation)

- **PEP 8**:
  - 4 spaces per indentation level.
  - `snake_case` for functions and variables; `UPPER_SNAKE_CASE` for constants.
  - `lowercase_with_underscores` for file names.
- From this module onward:
  - No anonymous, single-letter variable names except for obvious counters (`i`, `j`) in tiny loops.
  - All new scripts should have a **`main()` function** and `if __name__ == "__main__":` guard.
- Start thinking in **modules**:
  - Even if a file is small, keep logic, configuration, and test code separate where practical.

---

### 5. Practice Set (10–15 Exercises)

1. Install Python and create a **virtual environment** for this course.  
   - Verify using `python -V` and `which python` / `where python`.
2. Write a script `hello_env.py` that prints:
   - Python version.
   - Current working directory.
   - Active virtual environment path (if any).
3. Intentionally introduce a syntax error and capture the **traceback**.  
   - Identify: error type, file name, line number.
4. Fix the error from exercise 3 and refactor into a `main()` function.
5. Configure your editor to use **4 spaces** and show **invisible characters**; take note of where whitespace matters.
6. Create `m01_notes.py` with several commented lines describing:
   - What the interpreter does.
   - Difference between syntax and semantics.
7. Create a new Git repo for your Level 1 work:
   - `.gitignore` should exclude `.venv` and editor-specific folders.
   - Make at least **two meaningful commits**.
8. Write a script that intentionally produces an **IndentationError**; then fix it while preserving logic.
9. Rewrite any previous script to use **PEP 8 naming** for variables and functions.
10. Use `git diff` to review the changes you made in exercise 9 and summarize them in a commit message.

---

### 6. Mini-Project – Developer Setup Checker

**Goal**: Build a small, professional-looking CLI script that reports the developer’s environment state.

#### 6.1 Problem Statement

Create a CLI tool that prints a short “environment report”:

- Python version.
- OS/platform.
- Current working directory.
- Whether a virtual environment appears to be active.

#### 6.2 Requirements

- Implement a `main()` function as the entrypoint.
- Use **clear function names** and docstrings.
- Print a readable, labeled report.
- Handle failure cases gracefully (e.g., when environment variables are missing).

#### 6.3 Suggested Folder Structure

```text
mp01_developer_setup_checker/
  env_report.py        # main CLI script with main()
  utils_system.py      # helper functions for querying environment
  README.md            # project spec (see projects/ folder)
```

#### 6.4 Acceptance Tests (High-Level)

- Running `python env_report.py` should:
  - Exit without exceptions.
  - Print a section for Python version, OS, CWD, and venv status.
- Code should:
  - Use PEP 8 naming.
  - Contain a `main()` function.
- Git history should show:
  - Initial commit with skeleton.
  - Subsequent commit(s) adding functionality and improvements.

---

### 7. Code Review Checklist (Module-Specific)

When reviewing Module 1 code:

- **Structure**
  - [ ] Does each script have a clear `main()` entrypoint?
  - [ ] Is logic inside functions rather than at top-level where reasonable?
- **Style**
  - [ ] PEP 8 indentation (4 spaces) and no tab usage.
  - [ ] File, variable, and function names are descriptive and follow `snake_case`.
  - [ ] Comments explain *why* something is done, not restate the obvious.
- **Git**
  - [ ] Commits are small and purposeful.
  - [ ] Commit messages describe intent (e.g., “Add environment reporting helper”).
- **Error Handling Mindset**
  - [ ] Learner reads and responds to tracebacks instead of ignoring them.

---

### 8. Interview-Style Questions (8–12)

1. Explain the difference between a **compiler** and an **interpreter**. Where does Python fit?
2. What is a **SyntaxError**? Give a minimal example that triggers it.
3. What is the role of **indentation** in Python, and what happens if it’s inconsistent?
4. Define **lexis**, **syntax**, and **semantics** in the context of Python.
5. Why is using a **virtual environment** considered a best practice?
6. What is the purpose of the pattern `if __name__ == "__main__":`?
7. What information do you normally find in a Python **traceback**, and how do you use it?
8. Why is version control (Git) important even for a solo developer?
9. How would you configure your editor to reduce the chance of indentation-related bugs?
10. What makes a **good commit message** in a professional codebase?

