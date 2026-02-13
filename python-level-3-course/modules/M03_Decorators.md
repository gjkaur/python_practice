# Module 3 – Decorators & Extended Arguments

**PCPP Objectives**: 1.4

## Learning Objectives

By the end of this module, students will be able to:

- Use `*args` and `**kwargs` for flexible function signatures
- Understand closures and use them to create function factories
- Create and use function decorators to modify function behavior
- Create decorators that accept arguments (three-level function pattern)
- Implement class-based decorators using `__call__`
- Understand decorator stacking and execution order
- Use `@functools.wraps` to preserve function metadata

## Topics Covered

### Lesson 3.1 – Extended Function Arguments (`*args`, `**kwargs`)
- `*args`: variable positional arguments (tuple)
- `**kwargs`: variable keyword arguments (dict)
- Combining positional, keyword, `*args`, and `**kwargs`
- Forwarding arguments: `func(*args, **kwargs)`

### Lesson 3.2 – Closures
- Closure: inner function that captures variables from enclosing scope
- Lexical scoping: inner functions access outer function's variables
- Common use cases: function factories, decorators, callbacks
- Late binding and `nonlocal` keyword

### Lesson 3.3 – Function Decorators
- Decorator syntax: `@decorator` above function definition
- Decorator as function: `@decorator` is syntactic sugar for `func = decorator(func)`
- Simple decorator: function that takes a function and returns a function
- Preserving metadata: `@functools.wraps(func)`

### Lesson 3.4 – Decorators with Arguments and Class Decorators
- Decorator with arguments: three-level function pattern
- Class decorators: class with `__call__` method
- Decorating functions with classes: class instance used as decorator

## Key Concepts

- **Extended Arguments**: `*args` and `**kwargs` enable flexible function signatures
- **Closures**: Functions that "remember" their enclosing scope
- **Decorators**: Functions that modify or enhance other functions
- **Decorator Pattern**: Three-level function for decorators with arguments
- **Syntactic Sugar**: `@decorator` is equivalent to `func = decorator(func)`

## Practice Exercises

See `practice/practice_03_decorators.py` for exercises covering:
- `*args` and `**kwargs` usage
- Closure creation
- Simple decorators
- Decorators with arguments
- Class decorators

## Examples

See `examples/decorators_demo.py` for:
- Complete examples of all decorator patterns
- Real-world use cases (timing, retry, validation, caching)
- Common patterns and best practices

## Common Mistakes

- Confusing decorator execution time (definition vs call)
- Forgetting `@functools.wraps` (loses function metadata)
- Incorrect three-level function pattern for decorators with arguments
- Late binding in closures (capturing variable references, not values)
- Decorator stacking order confusion

## Related Mini Project

**MP02 – Decorator Library** (Week 3)

Create a library of reusable decorators demonstrating all decorator patterns.

## Next Module

**M04 – Static/Class Methods & Abstract Classes** (PCPP 1.5, 1.6)

Building on decorators, Module 4 covers `@staticmethod`, `@classmethod`, and abstract base classes.
