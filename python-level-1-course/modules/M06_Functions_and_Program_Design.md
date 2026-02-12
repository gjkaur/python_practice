## M06 – Functions and Program Design

**PCEP Alignment**: Section 4.1, 4.2 (defining/invoking functions, return, `None`, parameters/arguments, defaults, scope, `global`)  
**Professional Focus**: Decomposition, reusable utilities, and clean interfaces.

---

### 1. Outcomes (Job-Skill Phrasing)

By the end of this module, a learner should be able to:

- Decompose a requirement into **small, focused functions** with clear responsibilities.
- Use **positional, keyword, and default arguments** correctly.
- Understand **scope rules** and avoid abusing `global`.
- Design **utility modules** that can be imported and reused across projects.
- Write functions that are **easy to test** and reason about.

---

### 2. Concept Explanations and Code Examples

#### 2.1 Defining and Calling Functions (PCEP 4.1)

```python
def calculate_tax(amount: float, rate: float) -> float:
    return amount * rate

total = calculate_tax(100.0, 0.2)
```

Explain:

- Functions encapsulate logic and can be reused.
- `return` ends the function and sends a value back.

#### 2.2 Parameters vs Arguments; Default Values

```python
def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"

greet("Alice")                 # uses default greeting
greet("Bob", greeting="Hi")    # keyword argument
```

Good practice:

- Use defaults for common cases.
- Avoid mutable default arguments (e.g., `def f(x, acc=[])`).

#### 2.3 Scope and `global`

```python
COUNTER = 0

def increment() -> None:
    global COUNTER   # use sparingly
    COUNTER += 1
```

Prefer explicit passing of values:

```python
def increment(value: int) -> int:
    return value + 1
```

---

### 3. Edge Cases and Common Mistakes

- Forgetting to **return** a value; getting `None` instead.
- Overusing `global` and making state hard to track.
- Writing “do everything” functions that are too long.
- Using mutable default parameters and seeing surprising shared state.

---

### 4. Production Notes

- Aim for functions that:
  - Do **one thing**.
  - Are **< 20–30 lines** where possible.
  - Have **clear names** and typed parameters/returns (even if not enforced).
- Group related functions into modules: `validators.py`, `services.py`, `storage.py`.
- Design function signatures so they are **easy to test** (pure where possible).

---

### 5. Practice Set (10–15 Exercises)

1. Write a pure function that calculates a discounted price given `amount` and `discount_rate`.
2. Implement a function that returns the greater of two numbers; then one for three numbers.
3. Write `format_user(name, age)` that returns a string summary.
4. Refactor any earlier script into at least three small functions and a `main()`.
5. Demonstrate the pitfall of using a list as a default parameter and fix it.
6. Implement a function with both positional and keyword-only arguments.
7. Write a function that validates that an integer is within a range and returns a boolean.
8. Show how scope affects variable values in nested functions (conceptual, simple example).
9. Create a module `math_utils.py` with at least three reusable helpers used by another script.
10. Design function signatures for reading, validating, and processing a single CLI command.

---

### 6. Mini-Project – Functional Refactor of a Previous Project

**Goal**: Take a previous mini-project (e.g., Unit Converter or Address Book) and refactor into cleanly designed functions and modules.

#### 6.1 Problem Statement

Given a working but monolithic script, refactor it such that:

- Logic is decomposed into small functions.
- I/O is separated from computation.

#### 6.2 Requirements

- No function should exceed ~25 lines unless clearly justified.
- All top-level logic should live inside `main()` or orchestrating functions.
- At least one module with reusable utility functions.

#### 6.3 Suggested Folder Structure

```text
mp07_functional_refactor/
  main.py        # orchestrates user flow
  services.py    # core business logic
  validators.py  # input validation
  utils.py       # shared helpers
  README.md
```

#### 6.4 Acceptance Tests (High-Level)

- Behavior matches the original version (same inputs → same outputs).
- New functions are small, well-named, and easy to test.
- There is no overuse of `global`; state flow is explicit.

---

### 7. Code Review Checklist

- **Design**
  - [ ] Functions have single, clear purposes.
  - [ ] No “god functions” that mix many unrelated concerns.
- **Signatures**
  - [ ] Parameter names are descriptive.
  - [ ] Default values are sensible and not mutable containers.
- **Reusability**
  - [ ] Common logic is extracted to shared helpers/modules.
  - [ ] Functions avoid unnecessary side effects.

---

### 8. Interview-Style Questions

1. Explain the difference between a parameter and an argument.
2. What is `None` in Python, and when does a function return it?
3. How does Python determine variable scope inside functions?
4. Why is using `global` generally discouraged in professional code?
5. What are the benefits of small, focused functions?
6. How would you design a function that is easy to test?
7. Give an example of a safe use of default parameters and an unsafe one.
8. How would you structure modules for a small CLI application?

