# Week 6 – Dictionaries and Strings

**Module**: M04 (dicts), M05 (strings)  
**Mini Project**: [mp06 Address Book CLI](../projects/mp06_address_book_cli/)

---

## Learning focus

- Dictionaries: building, indexing, updating, deleting; iteration, `keys()`, `values()`, `items()`.
- Strings: literals, escaping, slicing, immutability; common methods (e.g. strip, split, join, format).
- When to use dict vs list; key existence checks.

---

## Reading and notebooks

- [M04 – Collections](../modules/M04_Collections_Lists_Tuples_Dictionaries.md) (dictionaries)
- [M05 – Strings and Text Processing](../modules/M05_Strings_and_Text_Processing.md)
- [M04](../modules/M04_Collections_Lists_Tuples_Dictionaries/M04_Concepts.ipynb) and [M05](../modules/M05_Strings_and_Text_Processing/M05_Concepts.ipynb) notebooks
- Run `examples/` and `practice/` for both modules.

---

## Concepts & practice

1. Build a dict mapping 3 names to phone numbers; add one, update one, look up one; iterate and print "name: number."
2. Given a string, print it in uppercase, then with spaces replaced by `-`; use `.split()` and `" ".join()` to normalize spacing.
3. From the module: complete at least 5 exercises from M04 (dict) and M05 (strings) practice sets.

---

## Mini project tasks

1. Read [mp06 README](../projects/mp06_address_book_cli/README.md).
2. Implement Address Book CLI: add, search (by name), list all, exit; store contacts in a dict (e.g. name → phone or name → {phone, email}).
3. Validate input (non-empty name, valid phone format if you define one); print clear errors.
4. Run README test cases; document how you handle duplicate names (overwrite vs reject).

---

## Optional

- Add "delete contact."
- Format output in columns (e.g. name width 20, phone width 15).

---

## Checklist

- [ ] Add, search, list work correctly
- [ ] Dict used appropriately; key handling clear
- [ ] String formatting readable
- [ ] Input validation and error messages
