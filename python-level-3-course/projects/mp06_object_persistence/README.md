# MP06 – Object Persistence System

**PCPP Objectives**: 1.11, 1.12  
**Week**: 7  
**Related Modules**: M07

## Goal

Implement object serialization using pickle and shelve, and explore metaprogramming.

## Requirements

- Create a class that can be pickled and unpickled:
  - Class with instance variables, including nested objects (lists, dicts, other custom objects)
  - Demonstrate `pickle.dumps()`/`loads()` and `pickle.dump()`/`load()`
  - Handle pickling errors gracefully
- Implement a simple database using `shelve`:
  - Store and retrieve objects by key
  - Implement at least 3 operations: `save(key, obj)`, `load(key)`, `delete(key)`
  - Handle missing keys appropriately
- Create a simple metaclass example:
  - Metaclass that adds a method or attribute to all classes that use it
  - At least one class uses this metaclass
  - Demonstrate accessing `__name__`, `__bases__`, `__dict__` programmatically

## Acceptance Criteria

- Objects can be pickled and unpickled successfully (round-trip works)
- Shelve database stores and retrieves objects correctly
- Missing keys handled with appropriate exceptions or default values
- Metaclass modifies class creation as intended
- Special attributes (`__name__`, `__bases__`, `__dict__`) accessed correctly
- Code includes error handling for serialization failures

## File Structure

```
mp06_object_persistence/
├── README.md
├── models.py          # Classes for pickling
├── storage.py         # Shelve database implementation
├── metaclass_demo.py  # Metaclass examples
└── demo.py            # Demonstration script
```

## Suggested Extensions

- Implement custom `__getstate__` and `__setstate__` for complex pickling
- Create a registry metaclass that automatically registers all subclasses
- Build a simple ORM-like system using shelve with query methods

## Submission Checklist

- [ ] Pickle serialization works
- [ ] Shelve database implemented
- [ ] Metaclass example created
- [ ] Special attributes accessed
- [ ] Error handling implemented
