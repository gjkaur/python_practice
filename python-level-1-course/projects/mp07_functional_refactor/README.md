## MP07 – Functional Refactor

### 1. Problem Statement

You already have a working mini-project (e.g., Unit Converter, Address Book, or Student Score Manager) that was written in a more “script-like” style.  
Now you will **refactor** it into a clean, function-based design with:

- Clear separation between I/O and business logic.
- Small, testable functions.
- Simple modules with single responsibilities.

This simulates real-world refactoring of legacy scripts into maintainable code.

---

### 2. User Stories

- **As a maintainer**, I want the code to be easy to read and change without fear.
- **As a developer**, I want to see how to move from “works” to “clean and modular”.
- **As a reviewer**, I want a clear diff showing improved structure with preserved behavior.

---

### 3. Inputs and Outputs

Inputs/outputs are inherited from the chosen original mini-project.  
The key change is **how** the code is structured, not what it does.

---

### 4. Constraints and Refactoring Rules

- No new features; behavior should remain the same (same inputs → same outputs).
- Introduce:
  - `main()` entrypoint.
  - At least 3–5 non-trivial helper functions.
  - At least 2 modules beyond `main.py` (e.g., `services.py`, `validators.py`).
- No new global variables beyond obvious constants.

---

### 5. Suggested Architecture

```text
mp07_functional_refactor/
  main.py        # CLI flow and orchestration
  services.py    # core business logic functions
  validators.py  # input validation helpers
  utils.py       # any small shared helpers
  README.md
```

Process:

1. Copy the original script into this folder as a starting point.
2. Identify **logical chunks** and extract them into functions.
3. Move related functions into modules (`services`, `validators`, etc.).
4. Keep a test plan to ensure you haven’t changed behavior.

---

### 6. Test Cases (At Least 8)

Design tests based on your original project:

1. **Functional equivalence** – run original and refactored versions with same inputs; compare outputs.
2. **Boundary inputs** – ensure edge cases still behave correctly.
3. **Invalid inputs** – ensure error handling remains correct or is improved.
4. **Module imports** – importing `services` or `validators` in a REPL works without side effects.
5. **Function-level tests** – call key functions directly with representative arguments.
6. **No global state leaks** – running functions multiple times yields expected results.
7. **Entry point** – `python main.py` still starts the program correctly.
8. **Code size check** – no single function exceeds your agreed size threshold unnecessarily.

---

### 7. Level-Up Extensions

- Introduce simple **unit tests** using `unittest` or plain assertions in a `tests/` folder.
- Add basic **type hints** to all functions and run a type checker (later level).
- Document your refactoring decisions in a short `REFactor_NOTES.md` (optional).

