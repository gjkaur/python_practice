# MP05 – Class Hierarchy for a Domain

**PCAP**: 4.1–4.4, 4.6 (OOP foundations)

## Problem

Model a small **domain** (e.g. products, accounts, orders) with a **class hierarchy**: base class and at least one subclass. Use instance/class variables, __init__, methods, __dict__, hasattr.

## User Stories

- As a user I create objects and call methods; I see clear attribute and method design.
- As a learner I practice __init__, self, and optional class variables.

## Suggested Structure

- `models.py` – Product (name, price), maybe Order(Product, quantity) or Account (balance).
- `main.py` – create instances, print __dict__, call methods.

## Test Cases

1. Create Product("A", 10.0); print p.name, p.price; print p.__dict__.
2. hasattr(p, "name") is True.
3. Method (e.g. total_price or format_line) returns expected value.
