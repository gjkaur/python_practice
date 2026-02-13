# Module 5 – Encapsulation & Built-in Subclassing

**PCPP Objectives**: 1.7, 1.8

## Learning Objectives

- Implement getters, setters, and deleters using `@property`
- Understand attribute encapsulation and validation
- Subclass built-in classes (`list`, `dict`, `str`) to extend functionality
- Choose between composition and inheritance appropriately

## Topics Covered

### Lesson 5.1 – Attribute Encapsulation (Properties)
- `@property` decorator for getters
- `@property_name.setter` for setters
- `@property_name.deleter` for deleters
- Private attributes: `_attr` (convention) and `__attr` (name mangling)

### Lesson 5.2 – Subclassing Built-in Classes
- Inheriting from `list`, `dict`, `str`, etc.
- Overriding built-in methods
- Extending functionality
- Calling parent methods with `super()`

## Key Concepts

- **Encapsulation**: Controlling access to attributes through properties
- **Name Mangling**: `__attr` makes attributes harder to access
- **Built-in Subclassing**: Extending Python's built-in types

## Practice Exercises

See `practice/practice_05_encapsulation.py`

## Examples

See `examples/encapsulation_demo.py`

## Related Mini Project

**MP04 – Encapsulated Class Design** (Week 5)

## Next Module

**M06 – Advanced Exceptions & Object Copying** (PCPP 1.9, 1.10)
