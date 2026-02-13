# Week 7 Assignment – Serialization & Metaprogramming

**Module**: M07 – Serialization & Metaprogramming  
**PCPP Objectives**: 1.11, 1.12  
**Mini Project**: MP06 – Object Persistence System

## Learning Objectives

- Serialize objects using `pickle`
- Use `shelve` for persistent storage
- Understand metaclasses and their purpose
- Create classes dynamically using `type()`
- Access special class attributes

## Reading

1. Review `modules/M07_Serialization/M07_Serialization.md`
2. Study examples
3. Complete practice exercises

## Exercises

### Exercise 1: Pickle
Create a class with nested objects. Serialize to file and deserialize, verifying all data is restored.

### Exercise 2: Shelve
Create a simple database using `shelve` with `save()`, `load()`, and `delete()` functions.

### Exercise 3: Dynamic Class Creation
Use `type()` to create a `Calculator` class dynamically with methods `add`, `subtract`, `multiply`, `divide`.

### Exercise 4: Metaclass
Create a metaclass that adds a `created_at` timestamp to all classes using it.

### Exercise 5: Class Inspection
Write a function that inspects a class and prints `__name__`, `__bases__`, `__dict__`, and `__mro__`.

## Mini Project

**MP06 – Object Persistence System**: Implement according to specification.

## Submission

- Completed practice exercises
- MP06: Object persistence system

## Assessment Criteria

- Correctness (40%), Serialization (30%), Code Quality (20%), Understanding (10%)
