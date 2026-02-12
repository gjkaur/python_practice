## M02 – Data Types and Operators

**PCEP Alignment**: Section 1.3, 1.4, 1.5 (literals, variables, numeral systems, operators, basic I/O)  
**Professional Focus**: Precise numeric logic, predictable expressions, early validation.

---

### 1. Outcomes (Job-Skill Phrasing)

By the end of this module, a learner should be able to:

- Use **Boolean, integer, and floating-point types** correctly in business logic.
- Work confidently with **numeric, string, assignment, comparison, and boolean operators**.
- Understand and safely handle **floating-point accuracy issues**.
- Convert between `str`, `int`, and `float` using **input validation**.
- Use **binary, octal, decimal, and hexadecimal literals** where appropriate.
- Read and write simple **console I/O** that doesn’t crash on invalid input.

---

### 2. Concept Explanations and Code Examples

#### 2.1 Core Built-in Types (PCEP 1.3)

- `bool`: `True`, `False`.
- `int`: arbitrary-precision integers.
- `float`: double-precision floating-point numbers (approximate).
- `str`: text data.

Example:

```python
is_active = True
user_count = 120
discount_rate = 0.15
welcome_message = "Welcome to the system"
```

#### 2.2 Literals and Numeral Systems

```python
binary_mask = 0b1010      # 10 in decimal
octal_value = 0o12        # 10 in decimal
hex_color = 0xFF          # 255 in decimal
scientific = 1.5e3        # 1500.0
```

Explain:

- These are **just different ways of writing numbers**; they evaluate to `int` or `float`.

#### 2.3 Operators (PCEP 1.4)

- Arithmetic: `+`, `-`, `*`, `/`, `//`, `%`, `**`.
- Assignment and augmented assignment: `=`, `+=`, `-=`, `*=`, etc.
- Comparison: `==`, `!=`, `<`, `<=`, `>`, `>=`.
- Boolean: `and`, `or`, `not`.
- Bitwise: `&`, `|`, `^`, `~`, `<<`, `>>`.

Example – basic pricing rule:

```python
BASE_PRICE = 100.0
DISCOUNT_RATE = 0.15

def calculate_final_price(quantity: int) -> float:
    raw = BASE_PRICE * quantity
    discount = raw * DISCOUNT_RATE if quantity >= 5 else 0.0
    return raw - discount
```

#### 2.4 Operator Precedence and Binding

Show that parentheses clarify intent:

```python
result1 = 1 + 2 * 3      # 7
result2 = (1 + 2) * 3    # 9
```

Emphasize:

- In production, **use parentheses** instead of relying on memory of precedence.

#### 2.5 Floating-Point Accuracy

```python
print(0.1 + 0.2)  # 0.30000000000000004
```

Professional handling:

- When comparing floats, use a **tolerance**:

```python
def is_close(a: float, b: float, eps: float = 1e-9) -> bool:
    return abs(a - b) < eps
```

#### 2.6 Console I/O and Casting (PCEP 1.5)

Naive version:

```python
age_str = input("Enter age: ")
age = int(age_str)
```

Defensive version:

```python
def read_int(prompt: str) -> int:
    while True:
        raw = input(prompt)
        try:
            return int(raw)
        except ValueError:
            print("Please enter a valid integer.")
```

---

### 3. Edge Cases and Common Mistakes

- **Division by zero** with `/` or `//`.
- Using `==` to compare floats for equality.
- Confusing `=` (assignment) with `==` (comparison).
- Forgetting to cast input, e.g., `"5" + "5"` → `"55"` rather than `10`.
- Overflow is not typical in Python `int`, but for `float` extremely large values can lead to `inf`.

---

### 4. Production Notes

- Avoid **magic numbers**; prefer named constants.
- Wrap input parsing in **utility functions** (`read_int`, `read_float`).
- For boolean flags, use clear names: `is_admin`, `has_access`.
- For complex expressions, extract into **named helper functions** for readability.

---

### 5. Practice Set (10–15 Exercises)

1. Declare variables representing:
   - A feature flag.
   - A count of active users.
   - A tax rate.
2. Write an expression that computes total cost with quantity, unit price, and tax.
3. Convert between binary, octal, decimal, and hex literals that all represent the number `16`.
4. Write a function that checks if a number is even using both `%` and bitwise `&`.
5. Demonstrate a floating-point comparison that fails and then fix it using a tolerance.
6. Implement `read_float(prompt: str) -> float` with validation loop.
7. Create a script that asks for two integers and prints:
   - Sum, difference, product, integer division, remainder.
8. Write a short snippet using `and`/`or`/`not` to determine if a user may access a resource.
9. Use augmented assignment operators to update a running total based on three inputs.
10. Trace what happens in code where `score = score + 1` is accidentally replaced with `score == score + 1`.

---

### 6. Mini-Project – Unit Converter CLI

**Goal**: Build a robust unit conversion CLI (e.g., temperature and distance).

#### 6.1 Problem Statement

Users should be able to:

- Convert temperatures between Celsius and Fahrenheit.
- Convert distances between kilometers and miles.

#### 6.2 Requirements

- Menu-driven CLI (user chooses conversion type).
- Input is validated; invalid inputs do not crash the program.
- Computations use clear formulas and named constants where appropriate.

#### 6.3 Suggested Folder Structure

```text
mp02_unit_converter_cli/
  main.py            # CLI and user interaction
  converters.py      # pure conversion functions
  validators.py      # input validation helpers
  README.md
```

#### 6.4 Acceptance Tests (High-Level)

- `converters.py`:
  - Pure functions: `c_to_f`, `f_to_c`, `km_to_miles`, `miles_to_km`.
  - Tested with known values (`0°C -> 32°F`, `1km -> 0.62137...`).
- `main.py`:
  - Does not crash on invalid numeric input.
  - Loops until user chooses to exit.

---

### 7. Code Review Checklist

- **Correctness**
  - [ ] No reliance on float equality without tolerance.
  - [ ] Division by zero handled or impossible by design.
- **API Design**
  - [ ] Conversion logic is in pure functions, not mixed into the CLI.
  - [ ] Naming clearly describes purpose and units.
- **Validation**
  - [ ] All user input is validated before casting.
  - [ ] Error messages are clear and actionable.

---

### 8. Interview-Style Questions

1. Explain the difference between `==` and `is` in Python (conceptual preview).
2. Why is `0.1 + 0.2` not exactly `0.3` in binary floating-point?
3. When would you choose integer division `//` over `/`?
4. Show how to guard against division by zero in a function.
5. Explain operator precedence and why parentheses are still recommended.
6. What is the difference between `and` and `&`? When is it appropriate to use each?
7. How does Python represent boolean values under the hood with integers?
8. Given a function that takes a string input, how would you robustly convert it to an int?

