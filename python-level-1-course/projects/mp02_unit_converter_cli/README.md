## MP02 – Unit Converter CLI

### 1. Problem Statement

You need a robust CLI tool that performs common unit conversions for end users, such as:

- Temperature: Celsius ↔ Fahrenheit.
- Distance: Kilometers ↔ Miles.

The tool must handle invalid input gracefully and demonstrate clean separation between:

- User interface (CLI).
- Conversion logic (pure functions).
- Input validation.

---

### 2. User Stories

- **As a user**, I want to convert units quickly without memorizing formulas.
- **As a junior developer**, I want to practice writing pure functions and reusable utilities.
- **As a reviewer**, I want the code structure to make conversion logic easy to test.

---

### 3. Inputs and Outputs

**Inputs**

- User menu choice:
  - `1` – Celsius to Fahrenheit.
  - `2` – Fahrenheit to Celsius.
  - `3` – Kilometers to Miles.
  - `4` – Miles to Kilometers.
  - `0` – Exit.
- Numeric input for the chosen value (e.g., temperature or distance).

**Outputs**

- Converted numeric values with labels, e.g.:

```text
Enter value in Celsius: 0
Result: 32.0 °F
```

Invalid input:

```text
Enter value in Celsius: hello
Invalid number. Please try again.
```

---

### 4. Constraints and Validation Rules

- Numeric input must be validated:
  - Reject non-numeric values with clear messages.
- No crashes on invalid input; the menu loop continues.
- Do not rely on floating-point equality; minor rounding differences are acceptable.
- Use only the Python standard library.

---

### 5. Suggested Architecture

```text
mp02_unit_converter_cli/
  main.py        # CLI loop, user prompts, and printing
  converters.py  # pure conversion functions
  validators.py  # input validation helpers
  README.md
```

**Module responsibilities**

- `converters.py`
  - `c_to_f(celsius: float) -> float`
  - `f_to_c(fahrenheit: float) -> float`
  - `km_to_miles(km: float) -> float`
  - `miles_to_km(miles: float) -> float`
- `validators.py`
  - `read_float(prompt: str) -> float` with safe retry loop.
- `main.py`
  - `main()` orchestrates menu, calls converters, and prints results.

---

### 6. CLI Usage Examples

```bash
python main.py
```

Example interaction:

```text
Unit Converter
--------------
1) Celsius to Fahrenheit
2) Fahrenheit to Celsius
3) Kilometers to Miles
4) Miles to Kilometers
0) Exit

Choose an option: 1
Enter value in Celsius: 100
Result: 212.0 °F
```

---

### 7. Test Cases (At Least 8)

1. **Celsius to Fahrenheit**  
   - Input: `0°C` → Expected: `32°F`.
2. **Fahrenheit to Celsius**  
   - Input: `32°F` → Expected: `0°C`.
3. **Kilometers to Miles**  
   - Input: `1 km` → Approx result: `0.6213... miles`.
4. **Miles to Kilometers**  
   - Input: `1 mile` → Approx result: `1.609... km`.
5. **Invalid numeric input**  
   - Input: `"abc"` for temperature.  
   - Expect: error message, no crash, and re-prompt.
6. **Menu exit**  
   - Choose `0` from main menu.  
   - Expect: program terminates cleanly.
7. **Edge case: negative values**  
   - Convert `-40°C` and `-40°F`; results should match (they intersect).
8. **Multiple consecutive conversions**  
   - Run 3–4 conversions in the same session.  
   - Expect: state does not leak between runs; each calculation is independent.

---

### 8. Level-Up Extensions

- Add support for:
  - Weight conversions (kg ↔ lb).
  - Time conversions (hours ↔ minutes).
- Allow conversions via **command-line arguments** (e.g., `--type c2f --value 100`).
- Implement a **simple history** of last N conversions.
- Introduce basic **logging** of conversions to a file for audit or debugging.

