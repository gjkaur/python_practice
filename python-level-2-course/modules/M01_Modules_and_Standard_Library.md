## M01 – Modules and the Standard Library

**PCAP Alignment**: Section 1 (1.1–1.4) – Import and use modules; math, random, platform.  
**Professional Focus**: Multi-file programs, standard library, discoverability.

---

### 1. Outcomes

By the end of this module you will:

- Import modules using `import`, `from ... import`, `import ... as`, and `import *` (and know when to avoid `*`).
- Use `dir()` to discover names in a module and qualify nested modules.
- Understand and optionally modify `sys.path` for import resolution.
- Use the **math** module: `ceil()`, `floor()`, `trunc()`, `factorial()`, `hypot()`, `sqrt()`.
- Use the **random** module: `random()`, `seed()`, `choice()`, `sample()`.
- Use the **platform** module: `platform()`, `machine()`, `processor()`, `system()`, `version()`, `python_implementation()`, `python_version_tuple()`.

---

### 2. Core Concepts (PCAP 1.1–1.4)

#### 2.1 Import variants (PCAP 1.1)

- **import math** → use `math.sqrt(4)`; the module name is the namespace.
- **from math import sqrt** → use `sqrt(4)`; the name is bound in the current scope.
- **from math import sqrt as sq** → use `sq(4)`; alias avoids name clashes.
- **from package import *** → brings all public names (avoid in production for clarity and tooling).
- Nested packages: `from pkg.subpkg import mod` then use `mod` (or import specific names from `mod`).

Example:

```python
import math
from math import floor, ceil
from math import sqrt as sq
print(math.sqrt(16), floor(3.7), ceil(3.2), sq(9))
```

#### 2.2 dir() and sys.path (PCAP 1.1)

- **dir(obj)** returns a list of attribute names of the object (e.g. `dir(math)` lists what the math module exports).
- **dir()** with no arguments, in a module or REPL, lists names in the current scope.
- **sys.path** is a list of directory strings searched for modules; the first match wins. You can append or insert paths for custom package roots.

Example:

```python
import sys
print("dir(math)[:6] =", dir(math)[:6])
print("sys.path[0] =", sys.path[0])
```

#### 2.3 math module (PCAP 1.2)

- `ceil`, `floor`, `trunc`, `factorial`, `hypot`, `sqrt` – use for numeric evaluations.

#### 2.4 random module (PCAP 1.3)

- `random()` → [0, 1); `seed(x)` for reproducibility; `choice(seq)`, `sample(seq, k)`.

#### 2.5 platform module (PCAP 1.4)

- Discover host: `platform()`, `machine()`, `processor()`, `system()`, `version()`, `python_implementation()`, `python_version_tuple()`.

---

### 2.6 Edge Cases and Pitfalls

- **math.sqrt(x)**: Raises `ValueError` if x < 0. Use non-negative inputs or catch.
- **math.factorial(n)**: n must be a non-negative integer; otherwise `ValueError` or `OverflowError`.
- **random.choice(seq)**: seq must be non-empty; otherwise `IndexError`.
- **random.sample(seq, k)**: k must be ≤ len(seq); otherwise `ValueError`.
- **import \***: Pollutes namespace; can shadow your own names or future additions to the module. Avoid in production.

---

### 2.7 Built-in and Related Functions

- **dir([object])**: List of names in current scope (no arg) or object's attributes (e.g. `dir(math)`).
- **hasattr(obj, name)**: Returns True if obj has attribute name.
- **getattr(obj, name [, default])**: Get attribute by string; optional default if missing.
- **sys.path**: List of strings (directories); modify with append/insert for custom import roots.

---

### 2.8 Production Notes

- Prefer **explicit imports** (`from math import sqrt`) over `import *` for clarity and tooling.
- Use **random.seed()** in tests or demos when you need reproducible output.
- Use **platform** for environment reports and OS-specific paths (e.g. Windows vs Linux).
- Keep **sys.path** modifications minimal; prefer proper package layout and `PYTHONPATH` when possible.

---

### 3. Practice Set (10–15 Exercises)

1. Import **math** and compute **floor** and **ceil** of 3.7; print both values.
2. Use **random.seed(42)** then **random.choice(["a","b","c"])** twice. Run the script again and confirm you get the same two values; explain why.
3. Use **platform.python_version_tuple()** and print the result; then format it as a string like `"3.10.0"` using `".".join(...)`.
4. Use **dir(math)** and list all names that start with the letter `'f'` (e.g. with a list comprehension).
5. Write a script that uses **math.hypot(x, y)** for three (x, y) pairs of your choice and prints each distance.
6. Use **random.sample(range(10), 3)** and explain the return value (type and meaning). What happens if you use k=15?
7. Print **sys.path** and explain what the first entry usually represents. Append `"."` to sys.path and print again.
8. In a script, use **from math import *** and call **sqrt(9)**; then comment that out and use only **import math** and call **math.sqrt(9)**. Compare the two styles.
9. Use **platform.system()** and write conditional logic that prints different messages for "Windows", "Linux", and "Darwin" (macOS).
10. Combine **math** and **random**: e.g. generate a random angle in [0, 2π) with **random.random() * 2 * math.pi**, then compute and print **math.cos(angle)** and **math.sin(angle)**.
11. Use **getattr(math, "sqrt")(16)** to call **math.sqrt** by name; then use **hasattr(math, "sqr")** and **hasattr(math, "sqrt")** and print the results.
12. Write a one-liner that builds a short "environment report" string using **platform.system()**, **platform.machine()**, and **platform.python_version_tuple()**, and print it.

---

### 4. Mini-Project – Multi-Module Environment Reporter

#### 4.1 Problem Statement

Build a small CLI that reports environment information (OS, machine, Python version) and demonstrates use of **math**, **random**, and **platform**. The program should be split into at least two files: a main script and a small helper module.

#### 4.2 Requirements

- Implement a **main()** function as the entrypoint in the main script.
- Use the **platform** module to print: system name, machine, Python implementation, and version.
- Use the **math** module (e.g. hypot or sqrt) for at least one calculation (e.g. distance or rounding).
- Use the **random** module with a fixed **seed** to pick one option from a list and print it (e.g. "Random tip: ...").
- The main script must **import** from a local helper module that provides at least one function (e.g. format_version or get_tips).
- Use clear names and docstrings; follow PEP 8.

#### 4.3 Suggested Folder Structure

```text
mp01_environment_reporter/
  main.py           # entrypoint: main(), imports from utils_report
  utils_report.py   # e.g. get_platform_summary(), get_random_tip()
  README.md         # short project description
```

#### 4.4 Acceptance Tests (High-Level)

- Running `python main.py` exits without exceptions and prints: platform info, one math-based result, and one random tip (same tip every run if seed is fixed).
- Code uses **import** / **from ... import** (no bare **import *** in the main script).
- A code reviewer can see that **dir()** or the module’s public names are discoverable.

---

### 5. Code Review Checklist (Module-Specific)

When reviewing Module 1 code:

- **Imports**
  - [ ] Import style is consistent; no bare **import *** in production code unless justified.
  - [ ] Nested packages use clear qualification (e.g. `from pkg.subpkg import mod`).
- **Standard library**
  - [ ] **math** / **random** / **platform** are used where appropriate; no reinvention of sqrt or random choice.
  - [ ] **random.seed()** is used when reproducibility is required (e.g. tests, demos).
- **Naming and scope**
  - [ ] No shadowing of standard names (e.g. do not name a variable **math** or **random**).
- **Discoverability**
  - [ ] Public functions have docstrings; **dir(module)** or module docs make the API clear.

---

### 6. Interview-Style Questions (8–12)

1. What is the difference between **import math** and **from math import sqrt**? When would you use each?
2. What does **dir()** return when called with no arguments in a module? What about **dir(math)**?
3. What is **sys.path** and when would you modify it? What is usually in **sys.path[0]**?
4. When would you use **random.seed()**? Is it suitable for security-sensitive randomness?
5. Name three functions from the **math** module and their purpose. What happens if you call **math.sqrt(-1)**?
6. What does **platform.python_version_tuple()** return? How would you get a string like `"3.10.0"`?
7. Why is **import *** generally discouraged in production code?
8. How do you qualify a name from a nested package (e.g. **pkg.subpkg.mod**)?
9. What is **getattr(math, "sqrt")** and when might you use it?
10. What exceptions can **random.choice(seq)** and **random.sample(seq, k)** raise, and under what conditions?
