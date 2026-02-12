## M05 – Strings and Text Processing

**PCEP Alignment**: Section 3.4 (strings: construction, indexing, slicing, escaping, quotes, multi-line strings, basic functions/methods)  
**Professional Focus**: Practical CLI text handling, simple parsing, and formatting.

---

### 1. Outcomes (Job-Skill Phrasing)

By the end of this module, a learner should be able to:

- Construct and manipulate **strings** using indexing, slicing, and concatenation.
- Use essential string **methods** for searching, replacing, and formatting.
- Handle **escaping** and multi-line strings correctly.
- Implement basic **text parsing** for simple data formats (e.g., comma-separated values).
- Write user-facing messages that are **clear and consistent**.

---

### 2. Concept Explanations and Code Examples

#### 2.1 String Creation and Immutability

```python
message = "Welcome"
quote = "He said, \"Hello\""
multiline = """Line 1
Line 2"""
```

Strings are **immutable**:

```python
text = "python"
uppercased = text.upper()
# text is still "python"
```

#### 2.2 Indexing and Slicing

```python
name = "Alice"
first_letter = name[0]    # "A"
last_two = name[-2:]      # "ce"
middle = name[1:4]        # "lic"
```

Slicing is safe even if indices overshoot (no IndexError).

#### 2.3 Common String Methods

- Case conversion: `.lower()`, `.upper()`, `.title()`.
- Search: `.find()`, `.startswith()`, `.endswith()`.
- Replacement: `.replace(old, new)`.
- Splitting and joining:

```python
line = "alice,bob,charlie"
names = line.split(",")
joined = ", ".join(names)
```

#### 2.4 Basic Text Parsing

Example: parsing a “name:score” format:

```python
def parse_score(line: str) -> tuple[str, int]:
    name_part, score_part = line.split(":")
    return name_part.strip(), int(score_part.strip())
```

---

### 3. Edge Cases and Common Mistakes

- Off-by-one errors in slicing.
- Assuming `.split()` will always produce the same number of elements.
- Not trimming whitespace (`strip`) before comparisons.
- Case-sensitive comparisons when case-insensitive is needed.

---

### 4. Production Notes

- Normalize user input early (`strip`, `lower`) where appropriate.
- Use **f-strings** for readable formatting:

```python
user = "alice"
print(f"Hello, {user}!")
```

- Avoid hard-coded message fragments scattered across the code; centralize common messages where feasible.

---

### 5. Practice Set (10–15 Exercises)

1. Create a string with quotes and backslashes using proper escaping.
2. Extract the domain from an email address (text before `@`).
3. Given a full name `"First Last"`, split into first and last names.
4. Normalize input so that “YES”, “Yes”, and “ yes ” are treated the same.
5. Parse a line `"id, name, age"` into three variables and trim whitespace.
6. Implement a function that masks all but the last 4 digits of a string (e.g., card number).
7. Write a function that counts how many times a substring appears in a string.
8. Given a multiline string, split it into lines and number them when printing.
9. Format a simple report using f-strings with aligned columns.
10. Implement a small “slugify” function that turns `"Hello World!"` into `"hello-world"`.

---

### 6. Mini-Project – Simple Address Book (Text-Focused)

**Goal**: Extend dictionary-based address book with robust string handling.

#### 6.1 Problem Statement

The address book should:

- Store contacts by **name** with associated **phone** and **email**.
- Allow adding, updating, and searching by partial name.

#### 6.2 Requirements

- Use **normalized keys** (e.g., lowercased names) internally.
- Support a search command that finds all contacts containing a query substring.
- Format output cleanly using f-strings.

#### 6.3 Suggested Folder Structure

```text
mp06_address_book_cli/
  main.py        # CLI and input handling
  contacts.py    # add/update/search logic
  formatting.py  # string formatting helpers
  README.md
```

#### 6.4 Acceptance Tests (High-Level)

- Search is case-insensitive and ignores leading/trailing spaces.
- Adding a contact with a name that already exists updates it instead of duplicating.
- Errors and confirmations are expressed with clear text messages.

---

### 7. Code Review Checklist

- **Correctness**
  - [ ] No reliance on exact-case matching where case-insensitive logic is intended.
  - [ ] Slicing and indexing are safe and intentional.
- **Usability**
  - [ ] Messages to the user are clear, consistent, and free of jargon.
  - [ ] Output is formatted for readability (spacing, alignment where needed).
- **Structure**
  - [ ] Text parsing and formatting are factored into helpers instead of duplicated inline.

---

### 8. Interview-Style Questions

1. Explain string immutability and its implications for performance and design.
2. How would you reverse a string in Python?
3. What is the difference between `split` and `partition`? (Conceptual preview.)
4. How can you make a case-insensitive comparison between two strings?
5. Give an example of using `.join()` effectively.
6. How do you safely parse a colon-separated string into components?
7. Why is `.strip()` often called before comparing user input?
8. Show how to build a multi-line string that represents a simple text table.

