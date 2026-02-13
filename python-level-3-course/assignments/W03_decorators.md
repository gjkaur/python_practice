# Week 3 Assignment – Decorators & Extended Arguments

**Module**: M03 – Decorators & Extended Arguments  
**PCPP Objectives**: 1.4  
**Mini Project**: MP02 – Decorator Library

## Learning Objectives

- Use `*args` and `**kwargs` for flexible function signatures
- Understand closures and create function factories
- Create and use function decorators
- Create decorators with arguments
- Implement class-based decorators

## Reading

1. Review `modules/M03_Decorators/M03_Decorators.md`
2. Study examples in `modules/M03_Decorators/examples/decorators_demo.py`
3. Complete practice exercises

## Exercises

### Exercise 1: Extended Arguments
Create a function `calculate_total(*prices, discount=0.0, tax_rate=0.0)` that calculates total with discount and tax applied.

### Exercise 2: Closures
Create a function factory `make_counter()` that returns a counter function. Each call increments and returns the count.

### Exercise 3: Simple Decorator
Create a `@log_calls` decorator that prints function name and arguments before calling, and return value after.

### Exercise 4: Decorator with Arguments
Create a `@repeat(n)` decorator that calls the function `n` times and returns the last result.

### Exercise 5: Class Decorator
Create a `Cache` class decorator that caches function results based on arguments.

## Mini Project

**MP02 – Decorator Library**: Implement all required decorators according to project specification.

## Submission

- Completed practice exercises
- MP02: Complete decorator library

## Assessment Criteria

- Correctness (40%), Decorator Patterns (30%), Code Quality (20%), Understanding (10%)
