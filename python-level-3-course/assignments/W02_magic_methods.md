# Week 2 Assignment – Magic Methods & Special Methods

**Module**: M02 – Magic Methods & Special Methods  
**PCPP Objectives**: 1.2  
**Mini Project**: MP01 (Part 2)

## Learning Objectives

- Implement comparison magic methods
- Implement numeric magic methods
- Implement type conversion methods
- Implement attribute access and container methods
- Use `@functools.total_ordering` to reduce boilerplate

## Reading

1. Review `modules/M02_Magic_Methods/M02_Magic_Methods.md`
2. Study examples in `modules/M02_Magic_Methods/examples/magic_methods_demo.py`
3. Complete practice exercises

## Exercises

### Exercise 1: Comparison Methods
Create a `Student` class with `name` and `grade` attributes. Implement `__eq__` (compare by name) and `__lt__` (compare by grade). Use `@total_ordering` to enable all comparisons.

### Exercise 2: Numeric Methods
Create a `Vector2D` class with `x` and `y` components. Implement `__add__`, `__mul__` (scalar multiplication), `__abs__` (magnitude), and `__rmul__` for right-hand multiplication.

### Exercise 3: Type Conversion
Create a `Fraction` class with `numerator` and `denominator`. Implement `__int__`, `__float__`, `__str__`, `__repr__`, and `__bool__`.

### Exercise 4: Container Methods
Create a `Deck` class that behaves like a list. Implement `__getitem__`, `__len__`, `__contains__`, and `__iter__` to make it subscriptable, sized, testable with `in`, and iterable.

## Mini Project Part 2

Continue **MP01 – OOP Class Hierarchy** by adding magic methods:

1. Add `__str__()` and `__repr__()` to all classes
2. Add `__eq__()` for comparison
3. Add `__lt__()` or `__gt__()` for ordering
4. Add `__len__()` or `__getitem__()` if applicable to your domain

## Submission

- Completed practice exercises
- MP01 Part 2: Magic methods added to class hierarchy

## Assessment Criteria

- Correctness (40%), Magic Methods Usage (30%), Code Quality (20%), Understanding (10%)
