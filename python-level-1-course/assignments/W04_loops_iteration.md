# Week 4 – Loops and Iteration Patterns

**Module**: M03 (loops)  
**Mini Project**: [mp04 CLI Menu System](../projects/mp04_cli_menu_system/)

---

## Learning focus

- `while` and `for` loops; `range()`; iteration with `in`.
- Patterns: counting, aggregating, searching, menu loop.
- `break`, `continue`; when to use `for-else` / `while-else`.

---

## Reading and notebooks

- [M03 – Control Flow and Loops](../modules/M03_Control_Flow_and_Loops.md) (loops sections)
- [M03 Concepts notebook](../modules/M03_Control_Flow_and_Loops/M03_Concepts.ipynb)
- Run M03 `examples/` and `practice/practice_03_*.py` (loop parts).

---

## Concepts & practice

1. Write a loop that prints the first N positive even numbers (N from input). Use both a `while` and a `for` version.
2. Sum all integers from 1 to N (N from input); validate N > 0.
3. From the module: complete at least 5 loop exercises from the M03 practice set.

---

## Mini project tasks

1. Read [mp04 README](../projects/mp04_cli_menu_system/README.md).
2. Implement the CLI Menu System: main loop, menu options (e.g. 1–3 + Exit), prompt for choice, run the chosen action, repeat until Exit.
3. Validate menu choice (integer in range or 0 to quit); handle invalid input without crashing.
4. Run through all README test cases and note behavior for invalid input.

---

## Optional

- Add a "confirmation" step for a destructive-looking option.
- Use a `for` loop somewhere (e.g. list options by iterating a list of strings).

---

## Checklist

- [ ] Menu loop runs until user exits
- [ ] All options do something defined
- [ ] Invalid choice handled cleanly
- [ ] Code is readable and PEP 8
