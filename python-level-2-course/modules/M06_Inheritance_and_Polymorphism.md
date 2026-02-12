## M06 – Inheritance and Polymorphism

**PCAP Alignment**: Section 4 (4.5) – Build class hierarchy using inheritance.  
**Professional Focus**: Clean hierarchies, polymorphism, avoiding diamond issues.

---

### 1. Outcomes

By the end of this module you will:

- Use **single and multiple inheritance**.
- Use the **isinstance()** function.
- Use **overriding** (methods and attributes).
- Use operators **is**, **not is** (identity).
- Apply **polymorphism** (same interface, different types).
- Override **__str__()** for readable output.
- Understand **diamond** inheritance and method resolution order (MRO).

---

### 2. Core Concepts (PCAP 4.5)

#### 2.1 Single and multiple inheritance

- Subclass: `class B(A):`; multiple: `class C(A, B):`. Order matters for MRO.

#### 2.2 isinstance()

- `isinstance(obj, Class)` and `isinstance(obj, (A, B))` for type checks.

#### 2.3 Overriding

- Define method in subclass with same name; override __str__ for str(obj).

#### 2.4 is / not is

- Identity comparison (same object in memory), not value comparison.

#### 2.5 Polymorphism

- Different classes with same method name; caller uses same interface.

#### 2.6 __str__()

- Override to return readable string; used by str() and print().

#### 2.7 Diamonds

- A; B(A), C(A); D(B, C). MRO (e.g. `D.__mro__`) resolves method lookup.

---

### 3. Exercises (10+)

1. Define Animal and Dog(Animal); override a method in Dog.
2. Use isinstance(dog, Dog) and isinstance(dog, Animal).
3. Override __str__ in a class; print(instance) and str(instance).
4. Use is to compare two references to the same object vs ==.
5. Define two subclasses with same method name; call it polymorphically from a list.
6. Implement multiple inheritance: Mixin + Base; show MRO.
7. Build a diamond: A, B(A), C(A), D(B,C); print D.__mro__ and call a method.
8. In a subclass, call super().method() to invoke overridden method.
9. Override an attribute in subclass; access via self and via super().
10. Use not is to check that two equal-valued objects are not the same object.

---

### 4. Mini-Project – Extend Class Hierarchy with Polymorphism

#### 4.1 Problem Statement

Extend the M05 class hierarchy (e.g. Product/Order or your domain): add **subclasses** with **inheritance**, **override** **__str__** and at least one method, and demonstrate **polymorphism** and **isinstance()**.

#### 4.2 Requirements

- At least one superclass and two subclasses (e.g. **Product** → **DigitalProduct**, **PhysicalProduct**).
- Override **__str__** in subclasses (and optionally call **super().__str__()**); override at least one other method (e.g. **shipping_cost()**).
- In a demo, create a list of superclass-type instances (mixed subclasses), iterate and call the overridden method (polymorphism); use **isinstance(obj, SubClass)** where appropriate.
- **main()** entrypoint; PEP 8 and docstrings.

#### 4.3 Suggested Folder Structure

```text
mp06_inheritance_demo/
  main.py
  models.py   # base class and subclasses
  README.md
```

#### 4.4 Acceptance Tests (High-Level)

- **print(obj)** uses overridden **__str__** for each subclass.
- Code that accepts the base type works with all subclasses (polymorphism).
- **isinstance** is used for type-specific behavior where needed.

---

### 5. Code Review Checklist

- [ ] Inheritance models “is-a” relationship; composition where “has-a” fits better.
- [ ] __str__ overridden for user-facing classes.
- [ ] MRO understood when using multiple inheritance.

---

### 6. Interview-Style Questions

1. What is the difference between is and ==?
2. What does isinstance() return? When would you use it?
3. How do you override a method? How do you call the superclass implementation?
4. What is polymorphism? Give an example.
5. What is the purpose of __str__?
6. What is diamond inheritance? How does Python resolve it?
7. What is __mro__?
8. When is multiple inheritance appropriate?
