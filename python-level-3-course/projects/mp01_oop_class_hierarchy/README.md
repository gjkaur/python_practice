# MP01 – OOP Class Hierarchy with Magic Methods

**PCPP Objectives**: 1.1, 1.2, 1.3  
**Weeks**: 1–2  
**Related Modules**: M01, M02

## Goal

Design a class hierarchy demonstrating inheritance, polymorphism, and magic methods. This project spans two weeks as it covers both OOP foundations (M01) and magic methods (M02).

## Requirements

### Part 1 (Week 1 – M01): Class Hierarchy

- Design a class hierarchy with at least 3 levels (e.g., `Vehicle` → `Car` → `ElectricCar`).
- Use `isinstance()` and `issubclass()` in at least one function.
- Demonstrate polymorphism: function that works with any object in the hierarchy.
- Include both instance variables and class variables.
- Use `super()` to call parent class methods.

### Part 2 (Week 2 – M02): Magic Methods

- Implement at least 5 magic methods:
  - `__init__()`: proper initialization with instance and class variables.
  - `__str__()` and `__repr__()`: user-friendly and developer-friendly representations.
  - `__eq__()`: comparison based on meaningful attributes.
  - `__lt__()` or `__gt__()`: ordering (e.g., by price, year, or ID).
  - `__len__()` or `__getitem__()`: make objects behave like containers if appropriate.

## Acceptance Criteria

- All classes properly initialized with `__init__()`.
- Magic methods work correctly: `str(obj)`, `obj1 == obj2`, `obj1 < obj2`, etc.
- `isinstance()` and `issubclass()` used correctly.
- Polymorphic function demonstrates duck typing or inheritance-based polymorphism.
- Code follows PEP 8 and includes docstrings (PEP 257).
- Type hints (PEP 484) added to all methods.

## Suggested Domain Examples

- **Vehicles**: `Vehicle` → `Car` → `ElectricCar`, `Motorcycle` → `SportBike`
- **Animals**: `Animal` → `Mammal` → `Dog`, `Cat`
- **Products**: `Product` → `Electronics` → `Smartphone`, `Laptop`
- **Employees**: `Employee` → `Manager` → `SeniorManager`, `Developer` → `SeniorDeveloper`

## File Structure

```
mp01_oop_class_hierarchy/
├── README.md
├── models.py          # Class definitions
├── demo.py            # Demonstration script
└── tests.py           # Unit tests (optional but encouraged)
```

## Suggested Extensions

- Add `@functools.total_ordering` to reduce comparison method boilerplate.
- Implement `__hash__()` to make objects hashable (if `__eq__` is defined).
- Add `__add__()` or other numeric magic methods if applicable to the domain.
- Create a factory function using `@classmethod` to create instances.

## Submission Checklist

- [ ] Class hierarchy with at least 3 levels
- [ ] At least 5 magic methods implemented
- [ ] `isinstance()` and `issubclass()` used
- [ ] Polymorphic function demonstrated
- [ ] PEP 8 compliant code
- [ ] Docstrings for all classes and methods
- [ ] Type hints added
- [ ] Code tested and working
