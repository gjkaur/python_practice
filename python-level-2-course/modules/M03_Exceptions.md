## M03 – Exceptions

**PCAP Alignment**: Section 2 (2.1–2.2) – Python-defined and self-defined exceptions.  
**Professional Focus**: Defensive design, custom exception hierarchy, clear error handling.

---

### 1. Outcomes

By the end of this module you will:

- Use **except** variants: `except:`, `except Exception:`, `except E1, E2:`, `except E as e:`, and chained `except`/`else`.
- Understand the **exception hierarchy** (BaseException, Exception, concrete types).
- Use **raise** and **raise ex** to raise or re-raise.
- Use **assert** and know when to use it vs exceptions.
- Use **event classes** (concept: exceptions as events).
- Use the **arg** property (e.g. `e.args`) of exception instances.
- **Define and use** self-defined (custom) exception classes.

---

### 2. Core Concepts (PCAP 2.1–2.2)

#### 2.1 except variants (PCAP 2.1)

- `except:` catches all (avoid; catch `BaseException` or `Exception` explicitly).
- `except E1: except E2:` multiple handlers.
- `except E1, E2:` or `except (E1, E2):` catch either type.
- `except E as e:` bind instance to `e` for inspection.
- `try/except/else:` else runs if no exception.

#### 2.2 Hierarchy, raise, assert (PCAP 2.1)

- BaseException → Exception → built-in subclasses (ValueError, TypeError, etc.).
- `raise SomeError("message")`; `raise` (re-raise) inside except.
- `assert condition, "message"` raises AssertionError if condition is false; use for invariants, not control flow.

#### 2.3 Event classes and arg property (PCAP 2.1)

- Exceptions as “events” carrying data; `e.args` is the tuple of arguments (e.g. message).

#### 2.4 Self-defined exceptions (PCAP 2.2)

- Subclass `Exception` (or a built-in); define and raise; catch by type. Use for domain-specific errors.

---

### 2.5 Edge Cases and Pitfalls

- **Bare except:** Catching `except:` catches everything (including KeyboardInterrupt, SystemExit). Always catch at least `Exception` or a specific type.
- **Order of except clauses:** Put more specific exceptions first; the first matching handler runs. `except Exception` before `except ValueError` would make ValueError never run.
- **assert in production:** Assertions can be disabled with `python -O`. Do not use assert for validating user input or external data; use if/raise.

---

### 2.6 Built-in and Related

- **Exception.args**: Tuple of arguments passed to the constructor (e.g. raise ValueError("msg") → e.args == ("msg",)).
- **type(e)**: The exception class. **isinstance(e, ValueError)** for type checks.
- **traceback module**: For formatting stack traces (intro only at this level).

---

### 2.7 Production Notes

- Define a **small hierarchy** (e.g. ValidationError → RequiredError, FormatError) so callers can catch either the base or a specific type.
- **Re-raise** with bare `raise` when you log and want the exception to propagate.
- Use **custom exceptions** for domain failures; use built-ins (ValueError, TypeError) for invalid arguments.

---

### 3. Exercises (10+)

1. Write try/except that catches ValueError and prints the exception message.
2. Use `except TypeError as e:` and print `e.args`.
3. Chain two except handlers for ValueError and TypeError.
4. Use `else` with try/except: print "OK" only when no exception.
5. Raise ValueError with a message; catch and re-raise.
6. Use assert to check a precondition; trigger AssertionError.
7. Define `class ValidationError(Exception): pass`; raise and catch it.
8. Define a custom exception with a custom attribute (e.g. `code`).
9. Build a small hierarchy: BaseError → ValidationError, ParseError; catch base and subclass.
10. In except block, use `raise` with no arguments to re-raise.

---

### 4. Mini-Project – Validator Library with Exception Hierarchy

#### 4.1 Problem Statement

Build a small validator library that defines a **exception hierarchy** (e.g. **ValidationError** with **RequiredError**, **FormatError** subclasses). Raise these from validation functions and use them in a simple CLI or script.

#### 4.2 Requirements

- Define at least one base exception (e.g. **ValidationError**) and two subclasses (e.g. **RequiredError**, **FormatError**).
- Implement at least two validation functions that raise these exceptions (e.g. **require_non_empty(s)**, **require_int(s)**).
- In a small CLI or **main()**, call the validators and catch the base **ValidationError** (and optionally specific subclasses); print clear messages.
- Use **e.args** or a custom attribute (e.g. **code**) where helpful. Do not use bare **except:**; order except clauses from specific to general.
- **main()** entrypoint; PEP 8 and docstrings.

#### 4.3 Suggested Folder Structure

```text
mp03_validator/
  validator.py   # exception classes, require_* functions
  main.py        # CLI: read input, call validators, catch exceptions
  README.md
```

#### 4.4 Acceptance Tests (High-Level)

- Raising **RequiredError** or **FormatError** and catching **ValidationError** works (catch by base class).
- Catching **ValidationError** then **Exception** in that order; specific handler runs first.
- Assert is not used for user input validation; **if/raise** is used.

---

### 5. Code Review Checklist

- [ ] Except clauses are ordered from most to least specific.
- [ ] Custom exceptions subclass Exception and are used consistently.
- [ ] Assert used for invariants only; user-facing errors use exceptions.

---

### 6. Interview-Style Questions

1. What is the difference between `except:` and `except Exception:`?
2. How do you re-raise the current exception?
3. What does `e.args` contain?
4. When should you use assert vs raise?
5. How do you define a custom exception?
6. Why order except branches from specific to general?
7. What is the base class for most user-defined exceptions?
8. Explain except E as e and how you use e.
