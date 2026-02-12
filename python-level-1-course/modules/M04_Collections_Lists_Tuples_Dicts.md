## M04 – Collections: Lists, Tuples, Dictionaries

**PCEP Alignment**: Section 3.1, 3.2, 3.3 (lists, tuples, dictionaries)  
**Professional Focus**: Modeling real data in memory and performing CRUD operations cleanly.

---

### 1. Outcomes (Job-Skill Phrasing)

By the end of this module, a learner should be able to:

- Choose between **lists, tuples, and dictionaries** based on mutability and access patterns.
- Implement typical **CRUD operations** on in-memory data collections.
- Use **slicing, indexing, and comprehensions** safely and idiomatically.
- Understand **copying vs aliasing** and avoid accidental shared-state bugs.
- Iterate over collections in ways that are clear, efficient, and Pythonic.

---

### 2. Concept Explanations and Code Examples

#### 2.1 Lists (PCEP 3.1)

```python
students: list[str] = ["Alice", "Bob", "Charlie"]

students.append("Diana")
first_student = students[0]
last_two = students[-2:]
```

Methods to highlight:

- `append`, `insert`, `remove`, `pop`, `index`, `sort`, `reverse`, `copy`.

List comprehension:

```python
scores = [65, 80, 90, 72]
passing_scores = [s for s in scores if s >= 70]
```

Copy vs alias:

```python
list_a = [1, 2, 3]
list_b = list_a          # alias
list_c = list_a.copy()   # shallow copy
```

#### 2.2 Tuples (PCEP 3.2)

Tuples are **immutable sequences**, often modeling fixed “records”:

```python
User = tuple[str, str]  # (username, email)

user: User = ("alice", "alice@example.com")
username = user[0]
```

Compare:

- Use **tuples** when:
  - Structure is fixed-size and semantically ordered.
- Use **lists** when:
  - You plan to add/remove elements frequently.

#### 2.3 Dictionaries (PCEP 3.3)

```python
inventory: dict[str, int] = {
    "SKU123": 10,
    "SKU456": 3,
}

inventory["SKU789"] = 0
stock = inventory.get("SKU000", 0)
```

Iteration:

```python
for sku, qty in inventory.items():
    print(sku, qty)
```

Checking keys:

```python
if "SKU123" in inventory:
    print("Found")
```

CRUD:

- Create: `inventory["SKU999"] = 5`
- Read: `inventory["SKU123"]` or `get`
- Update: `inventory["SKU123"] = 15`
- Delete: `del inventory["SKU456"]`

---

### 3. Edge Cases and Common Mistakes

- Indexing out of range on lists/tuples → `IndexError`.
- Accessing missing dictionary keys → `KeyError` (unless using `get`).
- Modifying a list while iterating over it → skipped or duplicated work.
- Confusing shallow vs deep copy when collections contain other collections.

---

### 4. Production Notes

- When storing domain data:
  - Use **dicts with descriptive keys** rather than “parallel lists” of attributes.
- For frequently looked-up entities, prefer dicts over scanning lists.
- Avoid “magic index positions” in tuples; consider constants or named containers (later, dataclasses).
- Use comprehensions for readable transformation/filtering; avoid overly clever one-liners.

---

### 5. Practice Set (10–15 Exercises)

1. Create a list of student names and:
   - Append a new name.
   - Insert one at index 0.
   - Remove a specific name.
2. Given a list of integers, return a new list with only the even numbers using a comprehension.
3. Create a tuple `(course_name, level, is_active)` and access each element.
4. Convert a list of `(name, score)` tuples into a dict mapping names to scores.
5. Write a function that safely gets a dictionary value using `get` with a default.
6. Demonstrate the difference between aliasing and copying a list.
7. Write a script that counts how many times each word appears in a small list of words.
8. Implement a function that removes a student from an `inventory`-style dict, if present, without raising errors.
9. Iterate over a dictionary of students to print “PASS” or “FAIL” based on their scores.
10. Show how modifying a list while iterating can cause bugs; fix it by iterating over a copy or using comprehension.

---

### 6. Mini-Project – Student Score Manager v1

**Goal**: Build an in-memory student score management tool using lists, tuples, and/or dicts.

#### 6.1 Problem Statement

The tool should:

- Track student names and scores.
- Allow adding new students, updating scores, and viewing basic statistics.

#### 6.2 Requirements

- Store data in collections (choose appropriate combination of list/tuple/dict).
- Provide operations:
  - Add student.
  - Update score.
  - List all students and scores.
  - Show min, max, and average scores.

#### 6.3 Suggested Folder Structure

```text
mp05_student_score_manager_v1/
  main.py        # CLI and menu
  repository.py  # functions to manage in-memory data
  stats.py       # score statistics functions
  README.md
```

#### 6.4 Acceptance Tests (High-Level)

- Adding a new student does not overwrite existing ones.
- Updating a score affects statistics correctly.
- Listing students shows them in a predictable order (e.g., insertion order).
- No `KeyError` or `IndexError` during normal usage.

---

### 7. Code Review Checklist

- **Data Modeling**
  - [ ] Appropriate choice of list/tuple/dict for each task.
  - [ ] No unnecessary parallel arrays where a dict would be clearer.
- **Safety**
  - [ ] Dictionary accesses are guarded or use `get`.
  - [ ] List indices are validated before use or code structure guarantees correctness.
- **Readability**
  - [ ] Comprehensions are clear and not overly complex.
  - [ ] Variable names reflect what the data represents (e.g., `inventory_by_sku`).

---

### 8. Interview-Style Questions

1. Compare lists, tuples, and dictionaries. When would you choose each?
2. What happens if you access a list index that does not exist?
3. How do you safely access a key in a dictionary that might not be present?
4. What is the difference between `list_a = list_b` and `list_a = list_b.copy()`?
5. Give an example of when a tuple is more appropriate than a list.
6. How would you count the frequency of items in a list without using external libraries?
7. Explain why mutating a list while iterating over it can cause problems.
8. Show how to transform a dictionary of scores into a list of “name: score” strings using a comprehension.

