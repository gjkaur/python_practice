## M05 – Object-Oriented Programming Foundations

**PCAP Alignment**: Section 4 (4.1–4.4, 4.6) – OOP notions, properties, methods, introspection, constructors.  
**Professional Focus**: Class design, encapsulation, clear APIs.

---

### 1. Outcomes

By the end of this module you will:

- Understand **class**, **object**, **property**, **method**, **encapsulation**, **inheritance**, **superclass**, **subclass** (identifying class components).
- Use **instance vs class variables** (declarations and initializations).
- Use the **__dict__** property (objects vs classes).
- Use **private components** (convention and name mangling for instances vs classes).
- **Declare and use methods**; understand the **self** parameter.
- Use **introspection** and **hasattr()** (objects vs classes).
- Use **__name__**, **__module__**, **__bases__** on classes.
- **Declare and invoke constructors** (e.g. `__init__`).

---

### 2. Core Concepts (PCAP 4.1–4.4, 4.6)

#### 2.1 OOP approach (PCAP 4.1)

- **Class**: blueprint for objects. **Object**: instance of a class. **Property**: data (attribute). **Method**: behavior (function attached to the class). **Encapsulation**: bundling data and behavior in one unit. **Inheritance**: superclass/subclass (see M06).

Example:

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def format_line(self):
        return f"{self.name}: {self.price:.2f}"
p = Product("Widget", 9.99)
print(p.format_line())
```

#### 2.2 Class and object properties (PCAP 4.2)

- Instance variables: per object (e.g. in `__init__`); class variables: shared (defined on class).
- `obj.__dict__` vs `Klass.__dict__`; private: single `_` (convention) or `__` (name mangling).

#### 2.3 Methods and self (PCAP 4.3)

- Methods take `self` as first parameter; call as `obj.method()`.

#### 2.4 Class structure (PCAP 4.4)

- `hasattr(obj, "name")`; `hasattr(Klass, "name")`. Class attributes: `__name__`, `__module__`, `__bases__`.

#### 2.5 Constructors (PCAP 4.6)

- `__init__(self, ...)` for initialization; called when object is created.

---

### 2.6 Edge Cases and Pitfalls

- **Class vs instance variables**: Mutating a class variable (e.g. `MyClass.list.append(1)`) affects all instances; rebinding (`MyClass.list = []`) affects the class attribute. Prefer instance data unless you truly need shared state.
- **Forgetting self**: Instance methods must take `self` as first parameter; calling `obj.method()` passes `obj` as `self` automatically.
- **__init__ return value**: Must not return anything other than `None`; Python ignores it. Use `__new__` only for advanced cases (immutables, singletons).

---

### 2.7 Built-in and Related Functions

- **hasattr(obj, name)**: True if object has that attribute (inherited included).
- **getattr(obj, name [, default])**: Get attribute by string; default if missing.
- **setattr(obj, name, value)**: Set attribute dynamically.
- **vars(obj)**: Like obj.__dict__ for instances with a __dict__.
- **type(obj)**: The class of the object. **isinstance(obj, Class)**: Type check (see M06).

---

### 2.8 Production Notes

- Use **instance variables** for per-object state; **class variables** for constants or shared counters only.
- Prefer **composition** (object has another object) over deep inheritance when "has-a" fits.
- Keep **__init__** focused on assignment and light validation; defer heavy work to methods or factories.

---

### 3. Practice Set (10–15 Exercises)

1. Define a class with **__init__** and two instance attributes; create two instances and print their attributes.
2. Add a class variable (e.g. **count**); increment it in **__init__** and print it after creating two instances.
3. Print **obj.__dict__** and **Class.__dict__** (e.g. first 5 keys) and explain the difference.
4. Define a method that uses **self** to return a formatted string (e.g. name and value).
5. Use **hasattr(obj, "attr")** before and after setting an attribute; print both results.
6. Print **MyClass.__name__**, **__module__**, **__bases__** for a class you define.
7. Define a "private" instance attribute with **_prefix** and one with **__double**; show **__dict__** for the instance (note name mangling for __).
8. Write a constructor that validates input (e.g. positive number) and raises **ValueError** if invalid.
9. Add a **@classmethod** or **@staticmethod** and call it from the class (e.g. factory or utility).
10. Create an object, modify an instance attribute, and show **__dict__** changed.
11. Use **getattr(obj, "attrname")** and **setattr(obj, "attrname", value)** and print the result.
12. Use **type(obj)** and **isinstance(obj, MyClass)** and explain the output.

---

### 4. Mini-Project – Class Hierarchy (e.g. Product / Order)

#### 4.1 Problem Statement

Build a small class hierarchy for a domain (e.g. **Product** with name and price, **Order** with a list of products and total). Use **__init__**, instance and optionally class variables, and demonstrate introspection (e.g. **hasattr**, **__dict__**, **__name__**).

#### 4.2 Requirements

- At least two classes (e.g. **Product** and **Order**); **Order** may contain or reference **Product** instances.
- Each class has **__init__** and at least one method that uses **self** (e.g. **format_line**, **total**).
- Use at least one class variable (e.g. counter or constant) and show it in **Class.__dict__** or via **hasattr**.
- In a small demo script, create instances, call methods, and use **hasattr** or **getattr**; print **__name__** and **__bases__** for one class.
- **main()** entrypoint; PEP 8 and docstrings for public methods.

#### 4.3 Suggested Folder Structure

```text
mp05_product_order/
  main.py      # create Product/Order instances, demo introspection
  models.py    # class Product, class Order
  README.md    # short project description
```

#### 4.4 Acceptance Tests (High-Level)

- Running **main.py** creates at least one **Product** and one **Order**, prints formatted output, and shows introspection (e.g. **hasattr(order, "total")**, **Order.__name__**).
- Code uses **self** consistently in instance methods; **__init__** does not return a value.
- A reviewer can confirm class vs instance variables are used intentionally.

---

### 5. Code Review Checklist (Module-Specific)

When reviewing Module 5 code:

- **Constructors**: [ ] **__init__** used for initialization; no mandatory logic in **__new__** unless needed. [ ] **__init__** does not return a value (other than None).
- **Methods**: [ ] **self** used consistently as the first parameter of instance methods.
- **Data**: [ ] Class vs instance variables chosen intentionally; no accidental shared mutable state.
- **Introspection**: [ ] **hasattr** / **getattr** used correctly when attribute names are dynamic.

---

### 6. Interview-Style Questions (8–12)

1. What is the difference between a **class** and an **object**?
2. What is **self**? Why is it the first parameter of instance methods?
3. What is the difference between **instance** and **class** variables? Give an example where a class variable is shared.
4. What does **__dict__** contain for an object? For a class?
5. What is **name mangling**? When does it occur (e.g. which prefix)?
6. What does **hasattr()** do? Give an example with an object and with a class.
7. What are **__name__**, **__module__**, **__bases__** on a class?
8. When is **__init__** called? Can it return a value?
9. What is **getattr(obj, "name", default)**? When would you use it?
10. Why might mutating a class variable (e.g. list.append) affect all instances?
