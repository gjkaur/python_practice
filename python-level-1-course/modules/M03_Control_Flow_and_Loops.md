## M03 – Control Flow and Loops

**PCEP Alignment**: Section 2.1, 2.2 (conditional statements; loops with `while`, `for`, `range`, `in`, `break`, `continue`, `for-else`, `while-else`)  
**Professional Focus**: Translating business rules into clear branching and iteration without spaghetti code.

---

### 1. Outcomes (Job-Skill Phrasing)

By the end of this module, a learner should be able to:

- Implement **multi-branch business rules** using `if`/`elif`/`else` without deeply nested code.
- Design **loop-based workflows** (menus, searches, aggregations) with `for` and `while`.
- Use `break`, `continue`, and `else` on loops intentionally, not accidentally.
- Compose safe, readable **Boolean expressions** for non-trivial conditions.
- Combine control structures with **input validation** for robust CLIs.

---

### 2. Concept Explanations and Code Examples

#### 2.1 Boolean Expressions (PCEP 2.1)

```python
is_premium = True
has_coupon = False
cart_total = 120.0

eligible_for_discount = (is_premium or has_coupon) and cart_total >= 100
```

Explain:

- Group with parentheses to avoid ambiguity.
- Short-circuit behavior of `and`/`or`.

#### 2.2 `if` / `elif` / `else`

```python
def classify_score(score: int) -> str:
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
```

Show rewrite from nested `if` to `elif` chain for clarity.

#### 2.3 Guard Clauses

```python
def can_access_dashboard(is_active: bool, is_admin: bool) -> bool:
    if not is_active:
        return False  # guard clause
    return is_admin
```

Guard clauses reduce nesting and are common in production code.

#### 2.4 `while` and `for` Loops (PCEP 2.2)

Counting loop:

```python
for i in range(5):
    print(f"Attempt {i + 1}")
```

Menu loop:

```python
def main_menu() -> None:
    while True:
        print("1) View balance")
        print("2) Deposit")
        print("3) Exit")
        choice = input("Choose option: ")
        if choice == "1":
            view_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")
```

#### 2.5 `break`, `continue`, `for-else`, `while-else`

Search with `for-else`:

```python
def find_first_over_limit(values: list[int], limit: int) -> int | None:
    for value in values:
        if value > limit:
            return value
    else:
        return None
```

Explain that `else` executes if the loop wasn’t terminated by `break`.

---

### 3. Edge Cases and Common Mistakes

- Infinite loops from forgetting to update a loop variable in `while`.
- Using `=` instead of `==` inside conditions.
- Misusing `break`/`continue` so that logic becomes hard to follow.
- Complex nested `if` structures instead of refactoring to functions or guard clauses.

---

### 4. Production Notes

- Prefer **clear `elif` chains** and guard clauses to deep nesting.
- Extract complicated conditions into **well-named helper functions**:

```python
def is_eligible_for_free_shipping(is_premium: bool, cart_total: float) -> bool:
    return is_premium or cart_total >= 100
```

- Limit the size of loops; avoid hundreds of lines inside a single loop.
- Keep input reading and processing logic separated where possible.

---

### 5. Practice Set (10–15 Exercises)

1. Write a function that returns `"even"` or `"odd"` based on an integer input.
2. Implement a function `max_of_three(a, b, c)` using `if`/`elif`/`else`.
3. Write a script that asks for a password up to 3 times and locks out afterward.
4. Use a `for` loop to compute the sum of numbers from 1 to `n`.
5. Use a `while` loop to repeatedly ask for a positive integer; reject and retry on invalid input.
6. Implement a menu with at least 4 options and a clean exit path using `break`.
7. Write a function that searches a list for a target value and returns `True`/`False` using `for-else`.
8. Rewrite a nested `if` block into guard-clause style and compare readability.
9. Trace a piece of code with `continue` statements and explain which iterations are skipped.
10. Identify and fix an infinite loop example.

---

### 6. Mini-Project – CLI Menu System

**Goal**: Build a robust CLI menu framework that you can reuse in later projects.

#### 6.1 Problem Statement

Create a text-based menu system that provides options like:

- Show help.
- Perform a simple calculation.
- Display a list of available commands.
- Exit.

#### 6.2 Requirements

- Main menu loop implemented with `while True` and `break` to exit.
- Input validation for menu choices.
- Use **separate functions** for each action; the loop only orchestrates.

#### 6.3 Suggested Folder Structure

```text
mp04_cli_menu_system/
  main.py        # menu loop and CLI entrypoint
  actions.py     # functions implementing menu actions
  validators.py  # helpers for menu input validation
  README.md
```

#### 6.4 Acceptance Tests (High-Level)

- Entering an invalid option does not crash the program and shows a clear message.
- Choosing “Exit” ends the loop cleanly.
- Each menu option is implemented in its own function (no giant `main()`).

---

### 7. Code Review Checklist

- **Logic Clarity**
  - [ ] `if`/`elif`/`else` branches are easy to read and not deeply nested.
  - [ ] Long Boolean expressions are broken into smaller pieces or helper functions.
- **Loops**
  - [ ] Loops have clear termination conditions.
  - [ ] `break`/`continue` use is justified and documented if non-obvious.
- **Structure**
  - [ ] Menu actions are separated into dedicated functions or modules.
  - [ ] No business logic is buried directly in the loop when it could be in functions.

---

### 8. Interview-Style Questions

1. Explain the difference between `if` and `elif`. When would you use each?
2. How does `for-else` work in Python? Give a practical example.
3. What is a guard clause, and why might it be preferred over nested `if` statements?
4. Describe a scenario where `while` is more appropriate than `for`, and vice versa.
5. How can an infinite loop occur accidentally? How would you prevent it?
6. What does it mean that `and` and `or` are “short-circuiting” operators?
7. Show how you would implement a simple retry loop for user input.
8. How would you refactor a long function with many nested `if` blocks to improve readability?

