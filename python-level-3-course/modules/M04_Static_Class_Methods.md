# Module 4 – Static/Class Methods & Abstract Classes

**PCPP Objectives**: 1.5, 1.6

## Learning Objectives

By the end of this module, students will be able to:

- Design and use `@staticmethod` and `@classmethod` appropriately
- Understand when to use static vs class methods
- Define abstract base classes using the `abc` module
- Implement abstract methods that must be overridden by subclasses
- Use multiple inheritance with abstract classes
- Create factory methods using `@classmethod`

## Topics Covered

### Lesson 4.1 – Static and Class Methods
- Static methods: `@staticmethod`, no `self` or `cls`
- Class methods: `@classmethod`, receives `cls` parameter
- When to use: static for utilities, class for alternative constructors
- Factory methods: creating instances using `@classmethod`

### Lesson 4.2 – Abstract Base Classes (ABC)
- Abstract base class: cannot be instantiated directly
- `abc.ABC` base class or `metaclass=abc.ABCMeta`
- Abstract methods: `@abc.abstractmethod`
- Enforcing interface contracts

### Lesson 4.3 – Multiple Inheritance with Abstract Classes
- Multiple inheritance from ABCs
- Implementing all abstract methods from all parents
- MRO with abstract classes

## Key Concepts

- **Static Methods**: Utility functions related to class, no access to instance/class state
- **Class Methods**: Access to class state, can create instances, receives `cls`
- **Abstract Classes**: Define interfaces that subclasses must implement
- **Factory Methods**: Alternative constructors using `@classmethod`

## Practice Exercises

See `practice/practice_04_static_class_methods.py` for exercises.

## Examples

See `examples/static_class_methods_demo.py` for complete examples.

## Common Mistakes

- Using `@staticmethod` when `@classmethod` is needed
- Forgetting to implement abstract methods in subclasses
- Mixing abstract and concrete methods incorrectly

## Related Mini Project

**MP03 – Abstract Base Class Framework** (Week 4)

## Next Module

**M05 – Encapsulation & Built-in Subclassing** (PCPP 1.7, 1.8)
