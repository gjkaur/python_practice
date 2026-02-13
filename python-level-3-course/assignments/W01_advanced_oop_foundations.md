# Week 1 Assignment – Advanced OOP Foundations

**Module**: M01 – Advanced OOP Foundations  
**PCPP Objectives**: 1.1, 1.3  
**Mini Project**: MP01 (Part 1)

## Learning Objectives

By completing this assignment, you will:

- Understand essential OOP terminology and concepts
- Use reflection functions (`isinstance()`, `issubclass()`) to inspect objects
- Design class hierarchies with inheritance
- Understand Method Resolution Order (MRO)
- Apply polymorphism in your code

## Reading

1. Review `modules/M01_Advanced_OOP_Foundations/M01_Advanced_OOP_Foundations.md`
2. Study the examples in `modules/M01_Advanced_OOP_Foundations/examples/oop_foundations_demo.py`
3. Complete practice exercises in `modules/M01_Advanced_OOP_Foundations/practice/practice_01_oop_foundations.py`

## Exercises

### Exercise 1: Class Variables vs Instance Variables

Create a `BankAccount` class with:
- Class variable `total_accounts` (counter)
- Instance variables: `account_number`, `balance`
- `__init__` method that increments `total_accounts` and initializes instance variables
- Method `deposit(amount)` that adds to balance
- Method `withdraw(amount)` that subtracts from balance (with validation)

Demonstrate that `total_accounts` is shared across all instances.

### Exercise 2: Inheritance Hierarchy

Create a class hierarchy for a library system:
- Base class: `LibraryItem` with `title`, `author`, `item_id`
- Subclass: `Book` with `isbn`, `pages`
- Subclass: `DVD` with `duration`, `rating`
- Subclass: `Magazine` with `issue_number`, `publication_date`

Each subclass should have appropriate methods (e.g., `Book` has `read()`, `DVD` has `play()`).

### Exercise 3: Reflection Functions

Write a function `analyze_object(obj)` that:
- Uses `isinstance()` to check the object's type
- Uses `issubclass()` to check class relationships
- Prints the object's class name and MRO
- Returns a dictionary with this information

### Exercise 4: Polymorphism

Create a function `process_items(items: list[LibraryItem])` that:
- Iterates through a list of `LibraryItem` objects (or subclasses)
- Calls a method that exists in all items (demonstrating polymorphism)
- Handles different item types appropriately

### Exercise 5: Composition vs Inheritance

Design a `Computer` class that:
- Uses composition for components (CPU, RAM, Storage)
- Each component is a separate class
- Demonstrates "has a" relationship instead of "is a"

## Mini Project Part 1

Begin working on **MP01 – OOP Class Hierarchy** (Part 1):

1. Choose a domain (vehicles, animals, products, employees, etc.)
2. Design your class hierarchy (at least 3 levels)
3. Implement base class and subclasses
4. Add class variables and instance variables
5. Use `isinstance()` and `issubclass()` in your code
6. Create a polymorphic function

**Deliverable**: Submit your `models.py` file with the class hierarchy implemented.

## Submission

Submit the following:

1. Completed practice exercises (`practice_01_oop_foundations.py`)
2. Solutions to Exercises 1–5 (create separate files or add to practice file)
3. MP01 Part 1: Class hierarchy implementation (`mp01_oop_class_hierarchy/models.py`)

## Assessment Criteria

- **Correctness** (40%): Code runs without errors, implements requirements correctly
- **OOP Design** (30%): Proper use of inheritance, class/instance variables, reflection
- **Code Quality** (20%): PEP 8 compliance, docstrings, type hints
- **Understanding** (10%): Demonstrates understanding of concepts through comments and design choices

## Resources

- Python Documentation: [Classes](https://docs.python.org/3/tutorial/classes.html)
- `isinstance()`: https://docs.python.org/3/library/functions.html#isinstance
- `issubclass()`: https://docs.python.org/3/library/functions.html#issubclass
- MRO: https://www.python.org/download/releases/2.3/mro/

## Next Week

Next week (Week 2), you'll add magic methods to your MP01 class hierarchy (Part 2).
