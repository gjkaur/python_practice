# MP03 – Abstract Base Class Framework

**PCPP Objectives**: 1.5, 1.6  
**Week**: 4  
**Related Modules**: M04

## Goal

Design and implement an abstract base class system with multiple inheritance.

## Requirements

- Define at least 2 abstract base classes (using `abc.ABC`):
  - Each ABC must have at least 2 abstract methods
  - Example: `Drawable` (with `draw()`, `get_area()`), `Movable` (with `move()`, `get_position()`)
- Create at least 3 concrete classes implementing these ABCs:
  - At least one class implements multiple ABCs (multiple inheritance)
  - All abstract methods must be implemented
- Use `@classmethod` for at least one factory method (alternative constructor)
- Use `@staticmethod` for at least one utility method
- Demonstrate that abstract classes cannot be instantiated directly

## Acceptance Criteria

- Abstract classes cannot be instantiated (raises `TypeError`)
- All concrete classes successfully implement all abstract methods
- Multiple inheritance works correctly (MRO resolves methods properly)
- Factory methods create instances correctly
- Code uses proper type hints and docstrings

## Suggested Extensions

- Add abstract properties using `@property` with `@abstractmethod`
- Implement a registry pattern where all concrete classes are automatically registered
- Create a mixin class that provides common functionality to multiple ABCs

## File Structure

```
mp03_abstract_base_class/
├── README.md
├── shapes.py          # Abstract base classes and implementations
├── demo.py            # Demonstration script
└── tests.py           # Unit tests
```

## Submission Checklist

- [ ] At least 2 abstract base classes defined
- [ ] At least 3 concrete implementations
- [ ] Multiple inheritance demonstrated
- [ ] Factory methods implemented
- [ ] Static methods implemented
- [ ] Code tested and working
