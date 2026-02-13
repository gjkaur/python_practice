# Module 7 – Serialization & Metaprogramming

**PCPP Objectives**: 1.11, 1.12

## Learning Objectives

- Serialize and deserialize objects using `pickle`
- Use `shelve` for dictionary-like persistent storage
- Understand metaclasses and their purpose
- Use `type()` for dynamic class creation
- Access special class attributes (`__name__`, `__bases__`, `__dict__`)

## Topics Covered

### Lesson 7.1 – Pickle Module
- `pickle.dumps()` / `pickle.loads()` for bytes
- `pickle.dump()` / `pickle.load()` for files
- Pickling various data types
- Security considerations

### Lesson 7.2 – Shelve Module
- Creating shelve databases
- Dictionary-like interface
- File modes and persistence

### Lesson 7.3 – Metaclasses Introduction
- Metaclass: class of a class
- `type()` function for dynamic class creation
- Custom metaclasses

### Lesson 7.4 – Special Attributes
- `__name__`, `__class__`, `__bases__`, `__dict__`
- Inspecting classes programmatically
- Metaclass operations

## Key Concepts

- **Serialization**: Converting objects to byte streams for storage/transmission
- **Metaclasses**: Classes that create classes
- **Dynamic Creation**: Creating classes at runtime using `type()`

## Practice Exercises

See `practice/practice_07_serialization.py`

## Examples

See `examples/serialization_demo.py`

## Related Mini Project

**MP06 – Object Persistence System** (Week 7)

## Next Module

**M08 – PEP Standards & Best Practices** (PCPP 2.1, 2.2, 2.3)
