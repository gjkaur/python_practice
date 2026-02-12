# MP06 – Extend Hierarchy with Inheritance and Polymorphism

**PCAP**: 4.5 (inheritance, isinstance, overriding, __str__)

## Problem

**Extend** the MP05 (or a fresh) class hierarchy with **inheritance**: subclasses that override methods, use **isinstance()**, and **polymorphism**. Override **__str__()** where appropriate.

## User Stories

- As a user I work with a list of different types (e.g. Product, DiscountedProduct) and call the same method polymorphically.
- As a learner I see single inheritance, override, and isinstance().

## Suggested Structure

- `models.py` – Product; DiscountedProduct(Product) with overridden price or method; use __str__.
- `main.py` – list of products (mixed); loop and call method; use isinstance() to branch.

## Test Cases

1. DiscountedProduct("B", 10, 0.1).price or total reflects discount.
2. isinstance(disc_product, Product) is True.
3. for p in [p1, p2]: print(p) uses __str__.
