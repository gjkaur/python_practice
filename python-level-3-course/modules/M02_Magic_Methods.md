# Module 2 – Magic Methods & Special Methods

**PCPP Objectives**: 1.2

## Learning Objectives

By the end of this module, students will be able to:

- Implement comparison magic methods (`__eq__`, `__lt__`, `__le__`, `__gt__`, `__ge__`, `__ne__`)
- Implement numeric magic methods (`__add__`, `__sub__`, `__mul__`, `__truediv__`, `__abs__`, etc.)
- Implement type conversion and introspection methods (`__str__`, `__repr__`, `__int__`, `__bool__`)
- Implement attribute access methods (`__getattr__`, `__setattr__`, `__getattribute__`)
- Implement container methods (`__getitem__`, `__setitem__`, `__len__`, `__contains__`, `__iter__`)
- Use `@functools.total_ordering` to reduce comparison boilerplate
- Understand when to return `NotImplemented` vs raising exceptions

## Topics Covered

### Lesson 2.1 – Comparison Magic Methods
- `__eq__`, `__ne__`, `__lt__`, `__le__`, `__gt__`, `__ge__`
- `@functools.total_ordering` decorator
- Rich comparison protocol
- Returning `NotImplemented` for unsupported comparisons

### Lesson 2.2 – Numeric Magic Methods
- Arithmetic: `__add__`, `__sub__`, `__mul__`, `__truediv__`, `__floordiv__`, `__mod__`, `__pow__`
- Unary: `__abs__`, `__neg__`, `__pos__`
- Right-hand operations: `__radd__`, `__rsub__`, etc.
- In-place operations: `__iadd__`, `__isub__`, etc.

### Lesson 2.3 – Type Conversion and Introspection Methods
- Type conversion: `__int__`, `__float__`, `__str__`, `__repr__`, `__bool__`, `__bytes__`
- Object representation: `__str__` vs `__repr__`
- Introspection: `__instancecheck__`, `__subclasscheck__`

### Lesson 2.4 – Attribute Access and Container Methods
- Attribute access: `__getattr__`, `__setattr__`, `__delattr__`, `__getattribute__`
- Container methods: `__getitem__`, `__setitem__`, `__delitem__`, `__len__`, `__contains__`
- Making objects iterable: `__iter__`, `__next__`

## Key Concepts

- **Magic Methods**: Special methods that Python calls automatically for built-in operations
- **Rich Comparison**: Implementing `__eq__` and one other enables all comparisons
- **NotImplemented**: Return this to allow Python to try right-hand methods
- **Container Protocol**: Make objects behave like lists/dicts using container methods

## Practice Exercises

See `practice/practice_02_magic_methods.py` for exercises covering:
- Comparison methods
- Numeric operations
- Type conversion
- Container behavior

## Examples

See `examples/magic_methods_demo.py` for:
- Complete examples of all magic method categories
- Real-world use cases
- Common patterns and best practices

## Common Mistakes

- Forgetting to return `NotImplemented` for unsupported types
- Not implementing `__hash__` when `__eq__` is defined
- Confusing `__str__` and `__repr__`
- Infinite recursion in `__setattr__` or `__getattribute__`
- Not handling `__getattr__` vs `__getattribute__` correctly

## Related Mini Project

**MP01 Part 2** – Add magic methods to your class hierarchy from Week 1.

## Next Module

**M03 – Decorators & Extended Arguments** (PCPP 1.4)

Building on magic methods (especially `__call__`), Module 3 covers decorators and extended function arguments.
