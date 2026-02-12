## M07 – Comprehensions, Lambdas, and Closures

**PCAP Alignment**: Section 5 (5.1–5.3) – List comprehensions, lambdas, closures.  
**Professional Focus**: Readable functional-style code, map/filter, closure pitfalls.

---

### 1. Outcomes

By the end of this module you will:

- Build **list comprehensions** with the **if** operator and **nested** comprehensions.
- **Define and use** **lambda** functions.
- Write **self-defined functions** that take lambdas as arguments.
- Use **map()** and **filter()**.
- Understand **closures**: meaning and rationale; **defining and using** closures.

---

### 2. Core Concepts (PCAP 5.1–5.3)

#### 2.1 List comprehensions (PCAP 5.1)

- `[x*2 for x in range(5)]`; with condition: `[x for x in seq if x > 0]`.
- Nested: `[[i*j for j in range(3)] for i in range(2)]` or flatten patterns.

#### 2.2 Lambdas (PCAP 5.2)

- `lambda x: x + 1`; single expression; can be passed to map, filter, or custom functions.
- map(f, iterable); filter(predicate, iterable).

#### 2.3 Closures (PCAP 5.3)

- Closure: inner function that captures variables from enclosing scope. Rationale: factory functions, callbacks. Define: nested def; use: return inner or pass to callers.

---

### 2.4 Edge Cases and Production Notes

- **Lambda**: Can only be a single expression; no statements, no annotations. For anything non-trivial use a def.
- **Closure late binding**: In a loop, creating closures that reference the loop variable will all see the final value. Capture with default arg: `lambda x, i=i: ...`.
- **map/filter**: Return iterators in Python 3; use list() if you need a list. Often a list comprehension is clearer than map/filter for simple cases.

---

### 3. Exercises (10+)

1. Write a list comprehension that squares even numbers in range(10).
2. Use if in comprehension to keep only positive numbers from a list.
3. Write nested comprehension that builds a 3x3 matrix of i+j.
4. Define lambda that adds two arguments; use it in map().
5. Use filter(lambda x: x > 0, list) and compare to list comprehension.
6. Write a function apply_twice(f, x) that returns f(f(x)); call with lambda.
7. Define a closure: outer(a) returns inner(b) that returns a+b; call outer(1)(2).
8. Use closure to create a counter factory (each call returns next int).
9. Pass a lambda to sorted(seq, key=lambda x: x[1]).
10. Flatten a list of lists using a comprehension.

---

### 4. Mini-Project – Data Pipeline or Transformer

#### 4.1 Problem Statement

Build a small **data pipeline** or **transformer**: transform a list with **comprehensions**; use **map**/ **filter** and at least one custom function that takes a **lambda** (or callable); optional **closure** for configuration.

#### 4.2 Requirements

- At least one list (or dict/set) **comprehension** that transforms or filters data.
- Use **map** or **filter** with a **lambda** (e.g. normalize numbers, filter by threshold).
- At least one function that accepts a callable (e.g. **apply(f, data)**) and call it with a lambda.
- Optional: a **closure** (e.g. **make_filter(threshold)** returning a predicate) for configuration.
- **main()** entrypoint; PEP 8 and docstrings.

#### 4.3 Suggested Folder Structure

```text
mp07_pipeline/
  main.py
  transform.py   # comprehensions, map/filter, apply
  README.md
```

#### 4.4 Acceptance Tests (High-Level)

- Running the script transforms input (e.g. list of numbers or strings) and produces expected output.
- Comprehensions and map/filter are used; at least one lambda is passed to a function.
- Code is readable and avoids unnecessary side effects in lambdas/closures.

---

### 5. Code Review Checklist

- [ ] Comprehensions stay readable; complex logic extracted to functions.
- [ ] Lambdas used for one-off, short logic; named functions when reused.
- [ ] Closures not used to mutate outer state in confusing ways.

---

### 6. Interview-Style Questions

1. What is the syntax of a list comprehension with an if condition?
2. What can a lambda contain? What can it not contain?
3. What does map() return in Python 3? How do you get a list?
4. What is the difference between map and list comprehension for simple transforms?
5. What is a closure? When is it useful?
6. How do you write a nested list comprehension?
7. Can a lambda have multiple statements? Why or why not?
8. Give an example of a function that takes a lambda as an argument.
