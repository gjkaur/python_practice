# MP02 – Decorator Library

**PCPP Objectives**: 1.4  
**Week**: 3  
**Related Modules**: M03

## Goal

Create a library of reusable decorators demonstrating advanced decorator patterns.

## Requirements

Implement at least 4 decorators:

1. **`@timer`**: Measures and logs function execution time
2. **`@retry(max_attempts)`**: Retries function on failure (decorator with arguments)
3. **`@validate_input(validator_func)`**: Validates function arguments before execution
4. **`@cache`**: Caches function results (simple dictionary-based cache)

Additional requirements:
- At least one decorator must accept arguments (three-level function pattern)
- At least one decorator must be implemented as a class (using `__call__`)
- Use `@functools.wraps` to preserve function metadata
- Demonstrate decorator stacking: `@timer @retry(3) def func(): ...`

## Acceptance Criteria

- All decorators work correctly and preserve function behavior
- Decorator with arguments works: `@retry(3)`
- Class-based decorator works: `@Logger('module')`
- Decorator stacking works without conflicts
- Functions retain their original names and docstrings (use `@wraps`)
- Code includes type hints and docstrings

## File Structure

```
mp02_decorator_library/
├── README.md
├── decorators.py      # Decorator implementations
├── demo.py            # Demonstration script
└── tests.py           # Unit tests (optional)
```

## Suggested Extensions

- Implement `@rate_limit(calls_per_second)` decorator
- Create a decorator that logs function calls with arguments and return values
- Implement `@deprecated(reason)` decorator that warns when deprecated function is called
- Add a decorator that measures memory usage

## Submission Checklist

- [ ] At least 4 decorators implemented
- [ ] Decorator with arguments works correctly
- [ ] Class-based decorator implemented
- [ ] Decorator stacking demonstrated
- [ ] `@functools.wraps` used appropriately
- [ ] PEP 8 compliant code
- [ ] Docstrings and type hints added
- [ ] Code tested and working
