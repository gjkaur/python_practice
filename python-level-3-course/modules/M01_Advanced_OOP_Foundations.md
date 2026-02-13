# Module 1 – Advanced OOP Foundations

**PCPP Objectives**: 1.1, 1.3

## Learning Objectives

By the end of this module, students will be able to:

- Understand and explain essential OOP terminology (class, instance, object, attribute, method, type, instance/class variables, superclasses/subclasses)
- Use reflection functions (`isinstance()`, `issubclass()`) to inspect objects and classes
- Design and implement class hierarchies with single and multiple inheritance
- Understand Method Resolution Order (MRO) and how Python resolves method calls
- Apply polymorphism through inheritance and duck typing
- Choose between inheritance and composition using "is a" vs "has a" relationships

## Topics Covered

### Lesson 1.1 – OOP Terminology and Reflection
- Essential terminology: class, instance, object, attribute, method, type
- Instance variables vs class variables
- Superclasses and subclasses
- Reflection: `isinstance()`, `issubclass()`
- The `__init__()` method

### Lesson 1.2 – Class Variables vs Instance Variables
- When to use class variables
- Mutable class variables and shared state pitfalls
- Accessing class variables: `ClassName.var` vs `instance.var`

### Lesson 1.3 – Inheritance and Class Hierarchies
- Single inheritance
- Multiple inheritance
- Method Resolution Order (MRO)
- Viewing MRO: `ClassName.__mro__` or `ClassName.mro()`
- Calling parent methods: `super()`

### Lesson 1.4 – Polymorphism and Composition
- Polymorphism through inheritance
- Duck typing
- Inheritance vs composition
- "Is a" vs "has a" relationships

## Key Concepts

- **Reflection**: Using `isinstance()` and `issubclass()` to inspect object types and inheritance relationships
- **MRO**: Understanding how Python resolves method calls in inheritance chains, especially with multiple inheritance
- **Polymorphism**: Same interface, different implementations
- **Composition**: Using "has a" relationships instead of inheritance when appropriate

## Practice Exercises

See `practice/practice_01_oop_foundations.py` for exercises covering:
- Creating class hierarchies
- Using `isinstance()` and `issubclass()`
- Understanding MRO
- Implementing polymorphism

## Examples

See `examples/oop_foundations_demo.py` for:
- Class hierarchy examples
- Reflection function usage
- MRO demonstrations
- Polymorphism examples

## Common Mistakes

- Confusing instance variables with class variables (shared vs per-instance)
- Misunderstanding MRO in multiple inheritance scenarios
- Overusing inheritance when composition is more appropriate
- Incorrect use of `super()` in multiple inheritance

## Related Mini Project

**MP01 – OOP Class Hierarchy with Magic Methods** (Weeks 1–2)

This project builds on Module 1 concepts by creating a class hierarchy and adding magic methods (covered in Module 2).

## Next Module

**M02 – Magic Methods & Special Methods** (PCPP 1.2)

Building on the OOP foundations, Module 2 covers Python's magic methods for comparison, numeric operations, type conversion, and container behavior.
