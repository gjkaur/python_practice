# Week 7 - Functions and Refactoring

**Module**: M06  
**Mini Project**: [mp07 Functional Refactor](../projects/mp07_functional_refactor/)

## Learning focus

- Defining and calling functions; parameters vs arguments; return values and None.
- Positional and keyword arguments; default values.
- Scope and name resolution; when not to use global.
- Refactoring: extract functions, separate I/O from logic, small modules.

## Reading and notebooks

- M06 Functions and Program Design
- M06 Concepts notebook and examples, practice/practice_06_*.py

## Concepts and practice

1. Write clamp(value, low, high) that returns value if in range, else low or high. Add a docstring.
2. Write a function that takes a list of numbers and returns min, max, mean; handle empty list.
3. Complete at least 5 exercises from the M06 practice set.

## Mini project tasks

1. Read mp07 README and REFACTOR_INSTRUCTIONS.md in that folder.
2. Start from starter_script.py. Refactor into main.py, services.py, validators.py.
3. Introduce main() and at least 3 to 5 helper functions; same behavior.
4. Run original and refactored with same inputs; compare outputs.
5. Optionally add REFACTOR_NOTES.md with your decisions.

## Checklist

- [ ] Same behavior before and after refactor
- [ ] main() and 3-5 helpers; at least 2 modules beyond main.py
- [ ] No new globals (except constants)
- [ ] Code review checklist from module applied
