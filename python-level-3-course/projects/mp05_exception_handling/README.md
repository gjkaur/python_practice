# MP05 – Exception Handling System

**PCPP Objectives**: 1.9, 1.10  
**Week**: 6  
**Related Modules**: M06

## Goal

Build a robust exception handling system with chained exceptions and traceback analysis.

## Requirements

- Define a custom exception hierarchy (at least 3 exception classes)
- Implement exception chaining:
  - At least one example of implicit chaining (`raise` in `except` block)
  - At least one example of explicit chaining (`raise NewException from OriginalException`)
- Create a function that analyzes exception tracebacks:
  - Extracts traceback information using `traceback` module
  - Logs formatted traceback to file
  - Returns structured error information
- Demonstrate shallow and deep copy:
  - Create a class with nested mutable attributes
  - Show difference between `copy.copy()` and `copy.deepcopy()`
  - Demonstrate when shallow copy causes bugs

## Acceptance Criteria

- Custom exception hierarchy is logical and follows inheritance
- Exception chaining preserves error context (visible in traceback)
- Traceback analysis function extracts and formats information correctly
- Copy operations demonstrate clear difference between shallow and deep
- All exceptions include meaningful error messages

## Suggested Extensions

- Implement a context manager that automatically logs exceptions with tracebacks
- Create a decorator that wraps functions with exception handling and chaining
- Implement custom `__copy__` and `__deepcopy__` methods for a class

## File Structure

```
mp05_exception_handling/
├── README.md
├── exceptions.py      # Exception hierarchy
├── traceback_utils.py # Traceback analysis functions
├── copying_demo.py    # Copy demonstration
└── demo.py            # Main demonstration
```

## Submission Checklist

- [ ] Exception hierarchy defined
- [ ] Exception chaining demonstrated
- [ ] Traceback analysis function implemented
- [ ] Shallow vs deep copy demonstrated
- [ ] Code tested and working
