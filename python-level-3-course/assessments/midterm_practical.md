# Mid-Course Practical Exam – Week 6

**Focus**: Advanced OOP (PCPP Sections 1.1–1.10)  
**Duration**: 2–3 hours  
**Weight**: 30% of course grade

## Exam Overview

This practical exam tests your understanding of advanced object-oriented programming concepts covered in Modules 1–6.

## Objectives Tested

- PCPP 1.1: OOP terminology and reflection
- PCPP 1.2: Magic methods
- PCPP 1.3: Inheritance, polymorphism, composition
- PCPP 1.4: Decorators and extended arguments
- PCPP 1.5: Static and class methods
- PCPP 1.6: Abstract classes
- PCPP 1.7: Encapsulation
- PCPP 1.8: Built-in subclassing
- PCPP 1.9: Advanced exceptions
- PCPP 1.10: Object copying

## Exam Format

You will be given a problem statement requiring you to:

1. Design a class hierarchy (30%)
2. Implement magic methods (25%)
3. Use decorators appropriately (15%)
4. Handle exceptions with chaining (15%)
5. Demonstrate proper code organization (15%)

## Sample Problem

**Domain**: E-commerce Product Management System

Design and implement a system for managing products in an e-commerce store:

1. **Base Class**: Create a `Product` abstract base class with:
   - Abstract methods: `calculate_price()`, `get_description()`
   - Instance variables: `product_id`, `name`, `base_price`
   - Class variable: `total_products` (counter)

2. **Subclasses**: Create at least 2 concrete product types:
   - `PhysicalProduct`: has `weight`, `shipping_cost`
   - `DigitalProduct`: has `file_size`, `download_link`

3. **Magic Methods**: Implement:
   - `__str__()` and `__repr__()`
   - `__eq__()` comparing by `product_id`
   - `__lt__()` comparing by `base_price`
   - `__hash__()` to make products hashable

4. **Decorators**: Create a decorator `@validate_price` that:
   - Ensures price is positive
   - Raises `ValueError` if invalid
   - Logs validation attempts

5. **Exception Handling**: Create custom exception hierarchy:
   - `ProductError` (base)
   - `InvalidPriceError` (chained from `ValueError`)
   - Use exception chaining in price validation

6. **Copying**: Demonstrate shallow vs deep copy:
   - Create a `ProductCatalog` class containing a list of products
   - Show difference between `copy.copy()` and `copy.deepcopy()`

## Evaluation Criteria

- **Core Correctness (30%)**: Code runs, implements requirements
- **Advanced OOP Concepts (25%)**: Proper use of magic methods, inheritance, abstract classes
- **Code Organization (20%)**: Clear structure, separation of concerns
- **Error Handling (15%)**: Exception chaining, proper error types
- **Code Quality (10%)**: PEP 8, docstrings, type hints

## Preparation

- Review Modules 1–6
- Practice implementing magic methods
- Review decorator patterns
- Practice exception chaining
- Review object copying concepts

## Resources Allowed

- Python documentation (online)
- Your course notes
- Module examples
- **Not allowed**: Pre-written code, communication with others

## Submission

Submit:
- All Python files (.py)
- README.md explaining your design decisions
- Test file demonstrating functionality

## Time Management

- **30 min**: Design and planning
- **90 min**: Implementation
- **30 min**: Testing and refinement

Good luck!
