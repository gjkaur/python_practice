## M07 – Exceptions and Defensive Programming

**PCEP Alignment**: Section 4.3, 4.4 (exception hierarchy, `try`/`except`, branch ordering, propagation, delegating handling)  
**Professional Focus**: Failing safely, validating inputs, and not hiding bugs.

---

### 1. Outcomes (Job-Skill Phrasing)

By the end of this module, a learner should be able to:

- Recognize and reason about the main **built-in exceptions** in Python.
- Use `try`/`except` blocks to **handle errors without crashing** the whole program.
- Decide when to **catch** an exception vs let it **propagate**.
- Write code that **validates inputs** and uses exceptions as a last resort.
- Log or surface errors in a way that helps with debugging in production.

---

### 2. Concept Explanations and Code Examples

#### 2.1 Exception Hierarchy (PCEP 4.3)

Key classes:

- `BaseException`
- `Exception`
- `ArithmeticError`, `ZeroDivisionError`
- `LookupError`, `IndexError`, `KeyError`
- `TypeError`, `ValueError`

Example:

```python
def get_item(values: list[int], index: int) -> int:
    return values[index]  # IndexError if out of range
```

#### 2.2 Basic `try` / `except` (PCEP 4.4)

```python
try:
    result = 10 / user_input
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

Order matters:

```python
try:
    risky_operation()
except ValueError:
    handle_value_error()
except Exception as exc:
    log_unexpected(exc)
```

Catch specific exceptions first.

#### 2.3 Propagation and Delegation

```python
def read_config(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    return parse_config(text)  # may raise ValueError

def main() -> None:
    try:
        config = read_config("config.ini")
    except (OSError, ValueError) as exc:
        print(f"Failed to load config: {exc}")
```

Let inner functions raise exceptions; catch at a **reasonable boundary**.

---

### 3. Edge Cases and Common Mistakes

- Using a bare `except:` which catches everything, including `KeyboardInterrupt`.
- Swallowing exceptions with empty `except` blocks (`except: pass`).
- Catching `Exception` too early and hiding programming errors (e.g., `TypeError` from a bug).
- Using exceptions for **normal control flow** instead of proper validation.

---

### 4. Production Notes

- Prefer **validation before operation**:

```python
def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("b must not be zero")
    return a / b
```

- Log unexpected exceptions with context instead of just printing.
- Only catch what you can **meaningfully handle** (e.g., show a friendly message, retry, or choose a safe default).

---

### 5. Practice Set (10–15 Exercises)

1. Intentionally trigger and examine `ZeroDivisionError`, `IndexError`, `KeyError`, and `ValueError`.
2. Wrap a risky division in `try`/`except` and show appropriate messages.
3. Write a function that reads an integer from input with both validation and exception handling.
4. Refactor a function that uses `except: pass` into one that logs and re-raises or returns an error.
5. Implement a `safe_get` for lists that returns `None` on out-of-range and does not raise.
6. Write a function that loads a configuration file and explain where you would catch errors.
7. Show how a broad `except Exception` can hide a bug, then fix it by catching specific exceptions.
8. Add error-handling to a previous mini-project (e.g., Unit Converter, Address Book) so that invalid operations never crash the whole program.
9. Implement a simple retry mechanism for a function that may temporarily fail.
10. Create a small library function that validates arguments and raises `ValueError` when invalid.

---

### 6. Mini-Project – Safe Calculator

**Goal**: Build a CLI calculator that never crashes on invalid input and reports errors clearly.

#### 6.1 Problem Statement

Users can choose operations (add, subtract, multiply, divide) and enter numbers.  
The program must:

- Handle non-numeric input.
- Prevent division by zero.
- Show meaningful error messages.

#### 6.2 Requirements

- Implement **pure calculation functions** and separate CLI interaction.
- Use `try`/`except` for:
  - Casting input to numbers.
  - Catching division by zero where appropriate.
- Optionally, log unexpected errors to a file using the `logging` module.

#### 6.3 Suggested Folder Structure

```text
mp08_safe_calculator/
  main.py        # CLI and menu
  operations.py  # add/subtract/multiply/divide functions
  io_utils.py    # input reading and validation helpers
  README.md
```

#### 6.4 Acceptance Tests (High-Level)

- Any invalid user input produces a readable error and returns to the menu.
- Division by zero is handled without a crash.
- Calculation results are correct given valid inputs.

---

### 7. Code Review Checklist

- **Safety**
  - [ ] No use of bare `except:`.
  - [ ] Only relevant exceptions are caught at each boundary.
- **Clarity**
  - [ ] Error messages are informative and user-friendly.
  - [ ] The flow of control on error vs success is easy to follow.
- **Design**
  - [ ] Validation and core logic are separated.
  - [ ] Exceptions are used to represent **exceptional** conditions, not normal control flow.

---

### 8. Interview-Style Questions

1. What is the difference between `BaseException` and `Exception`?
2. Name at least five built-in exception types and when they occur.
3. Why is it bad practice to write `except: pass`?
4. How do you ensure that only specific exceptions are caught in a `try` block?
5. What does it mean to “let an exception propagate”?
6. When should you raise an exception yourself vs return an error code?
7. How would you add basic logging to exception handling without overcomplicating the code?
8. Describe how you would implement error handling in a CLI application that reads from files and user input.

