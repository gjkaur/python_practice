# Module 6 – Advanced Exceptions & Object Copying

**PCPP Objectives**: 1.9, 1.10

## Learning Objectives

- Use exception chaining to preserve error context
- Analyze exception traceback objects
- Understand shallow vs deep copy operations
- Use `copy` and `deepcopy` appropriately
- Understand object identity vs value

## Topics Covered

### Lesson 6.1 – Chained Exceptions
- Implicit chaining: `__context__` attribute
- Explicit chaining: `raise NewException from OriginalException`
- `raise ... from None` to suppress context

### Lesson 6.2 – Traceback Objects
- `__traceback__` attribute
- `traceback` module functions
- Custom traceback formatting

### Lesson 6.3 – Shallow and Deep Copy
- `copy.copy()` vs `copy.deepcopy()`
- Object identity: `id()` and `is` operator
- When to use shallow vs deep copy

## Key Concepts

- **Exception Chaining**: Linking exceptions to show error propagation
- **Traceback Analysis**: Extracting information from exception tracebacks
- **Object Copying**: Understanding reference vs value copying

## Practice Exercises

See `practice/practice_06_exceptions.py`

## Examples

See `examples/exceptions_demo.py`

## Related Mini Project

**MP05 – Exception Handling System** (Week 6)

## Next Module

**M07 – Serialization & Metaprogramming** (PCPP 1.11, 1.12)
