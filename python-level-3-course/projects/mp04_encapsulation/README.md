# MP04 – Encapsulated Class Design

**PCPP Objectives**: 1.7, 1.8  
**Week**: 5  
**Related Modules**: M05

## Goal

Implement classes with proper encapsulation using properties and subclass built-ins.

## Requirements

- Create at least 2 classes demonstrating encapsulation:
  - **Class 1**: Use `@property` with getter, setter, and deleter for at least one attribute
  - **Class 2**: Subclass a built-in class (e.g., `list`, `dict`, `str`) and extend/modify behavior
- Property setter must include validation (e.g., range checks, type checks)
- Property deleter must handle cleanup appropriately
- Subclass must override at least 2 methods from the parent built-in class
- Demonstrate that encapsulation prevents invalid states

## Acceptance Criteria

- Properties work correctly: `obj.attr = value` calls setter, `del obj.attr` calls deleter
- Validation in setters prevents invalid values (raises `ValueError` or similar)
- Subclass behaves like parent but with extended/modified functionality
- Code demonstrates "has a" vs "is a" relationships appropriately
- All classes have proper docstrings explaining encapsulation strategy

## Suggested Extensions

- Implement a custom `__setattr__` to enforce encapsulation rules
- Create a class that subclasses multiple built-ins (if conceptually valid)
- Add `__slots__` to optimize memory usage

## File Structure

```
mp04_encapsulation/
├── README.md
├── models.py          # Encapsulated classes
├── demo.py            # Demonstration
└── tests.py           # Unit tests
```

## Submission Checklist

- [ ] Property with getter, setter, deleter implemented
- [ ] Built-in class subclassed and extended
- [ ] Validation prevents invalid states
- [ ] Code tested and working
