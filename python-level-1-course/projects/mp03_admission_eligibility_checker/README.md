## MP03 – Admission Eligibility Checker

### 1. Problem Statement

You are implementing a simplified admission rules engine for a training program or university.  
Given a candidate’s details (e.g., age, test score, work experience), determine whether they are:

- **Accepted**
- **Waitlisted**
- **Rejected**

The logic must be transparent, maintainable, and easy to extend with new rules.

---

### 2. User Stories

- **As an admissions officer**, I want a clear decision (“Accepted/Waitlisted/Rejected”) based on consistent rules.
- **As a developer**, I want the decision logic to be easy to read and modify as policies change.
- **As a reviewer**, I want the rules extracted into well-named functions rather than scattered conditionals.

---

### 3. Inputs and Outputs

**Inputs** (via CLI prompts)

- Age (integer).
- Entrance test score (0–100).
- Years of relevant work experience (integer, may be 0).

**Outputs**

- Primary decision: `ACCEPTED`, `WAITLISTED`, or `REJECTED`.
- Optional: short explanation, e.g., `"Accepted: score >= 85 and experience >= 1 year"`.

Example:

```text
Age: 22
Test score (0-100): 88
Years of experience: 2

Decision: ACCEPTED
Reason  : High score and sufficient experience.
```

---

### 4. Constraints and Validation Rules

- Age must be **>= 16** and reasonable (e.g., < 100); otherwise reject with a message.
- Score must be between **0 and 100** inclusive.
- Experience must be **>= 0**.
- Invalid numeric input must be handled via a retry loop; no crashes.

Sample policy (tune as desired but keep non-trivial):

- **ACCEPTED** if:
  - `score >= 85` and `experience >= 1`, or
  - `score >= 90` regardless of experience.
- **WAITLISTED** if:
  - `70 <= score < 85`, or
  - `score >= 85` but `experience == 0`.
- Otherwise: **REJECTED**.

---

### 5. Suggested Architecture

```text
mp03_admission_eligibility_checker/
  main.py          # CLI entrypoint and orchestration
  rules.py         # pure eligibility rules / decision logic
  validators.py    # input validation helpers
  README.md
```

Responsibilities:

- `validators.py`:
  - `read_int_in_range(prompt, min_value, max_value)`
  - `read_non_negative_int(prompt)`
- `rules.py`:
  - `classify_applicant(age, score, experience) -> tuple[str, str]`
    - Returns `(decision, reason)`.
- `main.py`:
  - Gathers input via validators.
  - Calls `classify_applicant`.
  - Prints decision and reason.

---

### 6. CLI Usage Examples

```bash
python main.py
```

Example interaction:

```text
Age: 22
Test score (0-100): 88
Years of experience: 0

Decision: WAITLISTED
Reason  : High score but no relevant experience yet.
```

---

### 7. Test Cases (At Least 8)

1. **High score, experience >= 1** → `ACCEPTED`.
2. **Very high score (>= 90), zero experience** → `ACCEPTED`.
3. **Score between 70 and 84 inclusive, any experience** → `WAITLISTED`.
4. **Score >= 85 but experience == 0** → `WAITLISTED`.
5. **Score below 70** → `REJECTED`.
6. **Age less than minimum (e.g., 15)** → reject input with message or classify as rejected with reason.
7. **Invalid numeric input (`abc` for score)** → re-prompt, no crash.
8. **Boundary values**: score exactly 70, 85, 90 to verify policy edges.

---

### 8. Level-Up Extensions

- Support additional criteria (e.g., interview score, recommendation strength).
- Write a **batch mode** that reads applicants from a CSV file and outputs results.
- Add basic **logging** of decisions to a file (for audit).
- Provide a `--dry-run` mode that prints decisions without any side effects.

