# Week 8 - Exceptions and Defensive Programming

**Module**: M07  
**Mini Project**: [mp08 Safe Calculator](../projects/mp08_safe_calculator/)

---

## Learning focus

- Exception hierarchy: BaseException, Exception, ValueError, TypeError, ZeroDivisionError, etc.
- `try/except` patterns; ordering except branches; propagation.
- Fail-fast vs graceful degradation; delegating error handling.

---

## Reading and notebooks

- [M07 - Exceptions and Defensive Programming](../modules/M07_Exceptions_and_Defensive_Programming.md)
- [M07 Concepts notebook](../modules/M07_Exceptions_and_Defensive_Programming/M07_Concepts.ipynb)
- Run M07 `examples/` and `practice/practice_07_*.py`.

---

## Concepts and practice

1. Write a function that converts a string to int; on invalid input catch ValueError and return None (or re-raise with a clearer message).
2. Use try/except so that division by zero in a calculator prints a friendly message instead of crashing.
3. From the module: complete at least 5 exercises from the M07 practice set.

---

## Mini project tasks

1. Read [mp08 README](../projects/mp08_safe_calculator/README.md).
2. Implement Safe Calculator: basic operations (+, -, *, /); prompt for two numbers and operator; handle invalid numbers and division by zero.
3. Use try/except; log or print failures clearly; no uncaught exceptions for normal invalid input.
4. Run README test cases including invalid input and divide-by-zero.

---

## Optional

- Use `logging` to record invalid attempts.
- Add power or modulo; handle negative exponents if you define behavior.

---

## Checklist

- [ ] Invalid numeric input handled
- [ ] Division by zero handled
- [ ] Invalid operator handled
- [ ] No unhandled exceptions for specified inputs
