# MP07 – Code Quality Refactor

**PCPP Objectives**: 2.1, 2.2, 2.3  
**Week**: 8  
**Related Modules**: M08

## Goal

Refactor existing code to meet PEP 8, PEP 257, and type hint standards.

## Requirements

- Select a previous mini project (MP01–MP06) or use provided "messy" code
- Apply PEP 8 guidelines:
  - Fix indentation, line length, imports, naming conventions
  - Use automated tools: `black`, `flake8`, or `autopep8`
- Add PEP 257 docstrings:
  - Module-level docstring
  - Class docstrings (one-line or multi-line as appropriate)
  - Function/method docstrings with parameter and return descriptions
- Add type hints (PEP 484):
  - Function parameters and return types
  - Use `typing` module for complex types (`List`, `Dict`, `Optional`, `Union`)
  - Run `mypy` to check type hints (optional but encouraged)
- Document the refactoring process:
  - List of changes made
  - Before/after code snippets for key improvements

## Acceptance Criteria

- Code passes `flake8` (or equivalent) with no errors (warnings acceptable if justified)
- All public functions, classes, and modules have docstrings
- Type hints added to all function signatures
- Code is more readable and maintainable after refactoring
- Refactoring document explains improvements clearly

## File Structure

```
mp07_code_quality/
├── README.md
├── before/            # Original code
├── after/             # Refactored code
└── REFACTORING.md     # Documentation of changes
```

## Submission Checklist

- [ ] Code refactored to PEP 8 standards
- [ ] Docstrings added (PEP 257)
- [ ] Type hints added (PEP 484)
- [ ] Refactoring documented
- [ ] Code quality tools used
