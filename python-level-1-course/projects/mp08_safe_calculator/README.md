## MP08 – Safe Calculator

### 1. Problem Statement

You are building a CLI **calculator** that supports basic operations:

- Addition
- Subtraction
- Multiplication
- Division

The calculator must never crash on invalid input and must clearly communicate errors, demonstrating good exception handling and defensive programming practices.

---

### 2. User Stories

- **As a user**, I want to perform simple calculations from the command line without crashes.
- **As a developer**, I want clear separation between core operations and input handling.
- **As a maintainer**, I want errors to be handled in a consistent, predictable way.

---

### 3. Inputs and Outputs

**Inputs**

- Operation choice: `+`, `-`, `*`, `/`, or menu-based selection.
- Two operands (floats).

**Outputs**

- For valid input: result of the operation.
- For invalid input: descriptive error, no traceback, prompt to try again.

Example:

```text
Operation (+, -, *, /): /
First number: 10
Second number: 0
Error: Cannot divide by zero. Please try again.
```

---

### 4. Constraints and Validation Rules

- Division by zero must be explicitly caught and handled.
- Non-numeric input for operands must trigger a retry with a clear message.
- Only the operations specified are supported; others should be rejected.

---

### 5. Suggested Architecture

```text
mp08_safe_calculator/
  main.py        # CLI and menu
  operations.py  # arithmetic functions
  io_utils.py    # input reading and validation
  README.md
```

Responsibilities:

- `operations.py`
  - `add(a, b)`, `subtract(a, b)`, `multiply(a, b)`, `divide(a, b)` → raise `ValueError` on invalid cases, e.g., division by zero.
- `io_utils.py`
  - `read_float(prompt: str) -> float` using try/except.
  - `read_operation(prompt: str) -> str` validating `+ - * /`.
- `main.py`
  - Menu loop calling `io_utils` and `operations`; prints results and errors.

---

### 6. CLI Usage Examples

```bash
python main.py
```

Example interaction:

```text
Safe Calculator
---------------
Operation (+, -, *, /) or q to quit: +
First number: 10
Second number: 5
Result: 15.0

Operation (+, -, *, /) or q to quit: /
First number: 10
Second number: 0
Error: Cannot divide by zero. Please try again.
```

---

### 7. Test Cases (At Least 8)

1. **Addition** – various positive/negative inputs.
2. **Subtraction** – including negative results.
3. **Multiplication** – zero and negative cases.
4. **Valid division** – simple fractions and larger numbers.
5. **Division by zero** – triggers friendly error, no crash.
6. **Non-numeric operand** – error + re-prompt.
7. **Invalid operation symbol** – error + re-prompt.
8. **Quit path** – user can exit cleanly with `q` or similar.

---

### 8. Level-Up Extensions

- Add support for **power** and **modulo** operations.
- Introduce a **history** of previous calculations.
- Log operations and errors to a file for debugging.
- Add very simple expression parsing (e.g., `2 + 3 * 4`) as a stretch goal.

