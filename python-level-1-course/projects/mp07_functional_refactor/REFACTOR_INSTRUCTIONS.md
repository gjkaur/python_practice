# MP07 – Refactor Instructions

Use this with [README.md](README.md). Your goal is to turn the **monolithic** `starter_script.py` into a **modular** design without changing behavior.

---

## Step 1: Run the starter

```bash
python starter_script.py
```

Try each menu option (1–4) with valid and invalid input; try option 0 and an invalid choice. Note the exact prompts and messages. Your refactored version must produce the same output for the same inputs.

---

## Step 2: Target structure

After refactoring you should have:

- **main.py** – Entrypoint with `main()`. A loop that prints the menu, reads choice, calls a handler, and exits when user chooses 0.
- **services.py** (or **converters.py**) – Pure conversion functions: `c_to_f`, `f_to_c`, `km_to_miles`, `miles_to_km`. No `input()` or `print()` here.
- **validators.py** – At least one helper that prompts for a number and retries on invalid input (e.g. `read_float(prompt)` returning a float).

No new features; same menu text, same conversions, same error messages.

---

## Step 3: Refactoring checklist

1. Extract the four conversion formulas into functions in a separate module.
2. Extract “prompt until valid float” into a function in validators.
3. In main.py: implement `print_menu()`, `handle_choice(choice)`, and `main()` with the menu loop.
4. Run `starter_script.py` and your `main.py` with the same inputs and compare output.
5. Keep `starter_script.py` in the repo for comparison; do not delete it.

---

## Step 4: Test cases (from README)

1. Choose 1, enter a number → correct Celsius to Fahrenheit result.
2. Choose 2, enter a number → correct Fahrenheit to Celsius result.
3. Choose 3, enter a number → correct km to miles result.
4. Choose 4, enter a number → correct miles to km result.
5. Choose 1, enter non-numeric → “Invalid number. Please try again.” (or equivalent).
6. Choose 0 → program exits with goodbye message.
7. Choose 99 or empty → “Invalid choice. Please try again.”
8. Run `python main.py` and complete one full conversion → no errors, same output as starter.

---

## Optional

- Add a short `REFACTOR_NOTES.md` describing what you extracted and why.
- Add a small test script that imports your conversion functions and asserts known values (e.g. 0°C → 32°F).
