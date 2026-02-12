## MP05 – Student Score Manager v1

### 1. Problem Statement

You are building a small tool to manage students and their scores for a course.  
The tool should allow a user (instructor or TA) to:

- Add new students with scores.
- Update existing scores.
- View all students and scores.
- View basic statistics (min, max, average).

This is an in-memory system in Level 1, focusing on list/tuple/dict usage and control flow.

---

### 2. User Stories

- **As an instructor**, I want a quick overview of class performance.
- **As a TA**, I want to update scores without editing code.
- **As a developer**, I want the data representation to be clear and extendable.

---

### 3. Inputs and Outputs

**Inputs**

- Student name (string).
- Score (integer 0–100).
- Menu choices for operations:
  - `1` – Add/Update student.
  - `2` – List students and scores.
  - `3` – Show statistics.
  - `0` – Exit.

**Outputs**

- Confirmation messages after add/update.
- List of students and scores.
- Statistics summary, e.g.:

```text
Students: 3
Min score: 65
Max score: 92
Average : 78.0
```

---

### 4. Constraints and Validation Rules

- Score must be between 0 and 100.
- Student names should be non-empty after trimming whitespace.
- Duplicate student names should **update** the existing record, not create a duplicate.
- No crashes on invalid numeric input.

---

### 5. Suggested Architecture

```text
mp05_student_score_manager_v1/
  main.py        # CLI loop and I/O
  repository.py  # data structure and CRUD operations
  stats.py       # statistics functions
  README.md
```

Responsibilities:

- `repository.py`
  - Holds a dict `{name: score}` or a list of named records.
  - `add_or_update_student(name: str, score: int) -> None`
  - `get_all_students() -> dict[str, int]` (or list of tuples).
- `stats.py`
  - `compute_min(scores: list[int]) -> int | None`
  - `compute_max(scores: list[int]) -> int | None`
  - `compute_average(scores: list[int]) -> float | None`
- `main.py`
  - Menu, prompts, and formatting.

---

### 6. CLI Usage Examples

```bash
python main.py
```

Example interaction:

```text
1) Add or update student
2) List students
3) Show statistics
0) Exit

Choose: 1
Student name: Alice
Score (0-100): 92
Saved.

Choose: 3
Students: 1
Min score: 92
Max score: 92
Average : 92.0
```

---

### 7. Test Cases (At Least 8)

1. **Add student** – name and score recorded correctly.
2. **Update student** – existing student’s score is overwritten, not duplicated.
3. **Statistics with multiple students** – min, max, and average correct.
4. **Empty state** – statistics handle no students gracefully (e.g., show “N/A”).
5. **Invalid score input** – reject and re-prompt.
6. **Name trimming** – `" Alice "` is treated as `"Alice"`.
7. **Boundary scores** – `0` and `100` accepted and included correctly.
8. **List ordering** – verify the listing is deterministic (e.g., insertion order or sorted).

---

### 8. Level-Up Extensions

- Add a concept of **grades** (A/B/C/D/F) derived from scores.
- Allow **saving/loading** student data to/from a JSON or CSV file (bridge to later modules).
- Provide a **search** function to find a student by partial name.
- Add basic **aggregate reporting** (e.g., number of students per grade).

