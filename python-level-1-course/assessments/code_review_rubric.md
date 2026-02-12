# Master Code Review Rubric – Level 1 Python

Use this rubric for **self-review**, **peer review**, or **instructor feedback** on mini projects and capstones. Tick each item as Met / Partial / Not met, and add brief notes where helpful.

---

## 1. Structure and Design

| Criterion | Met | Partial | Not met | Notes |
|-----------|-----|---------|---------|--------|
| Clear entrypoint (e.g. `main()` or `if __name__ == "__main__"`) | | | | |
| Logic in functions rather than long top-level script | | | | |
| Separation of concerns (I/O vs business logic vs validation) | | | | |
| Modules have a single, clear responsibility | | | | |
| No unnecessary globals; constants are named and minimal | | | | |

---

## 2. Style and Readability (PEP 8)

| Criterion | Met | Partial | Not met | Notes |
|-----------|-----|---------|---------|--------|
| 4 spaces indentation; no tabs | | | | |
| `snake_case` for variables and functions | | | | |
| Descriptive names (no single-letter except loop counters where clear) | | | | |
| Line length reasonable (e.g. under 88–100 chars where possible) | | | | |
| Comments explain *why* where needed; no obvious restatements | | | | |
| Docstrings on public functions (at least one-line summary) | | | | |

---

## 3. Input and Error Handling

| Criterion | Met | Partial | Not met | Notes |
|-----------|-----|---------|---------|--------|
| Invalid input handled (no uncaught crashes for normal misuse) | | | | |
| User-facing messages are clear and actionable | | | | |
| Exceptions used appropriately (try/except where needed) | | | | |
| No silent failures; errors reported or logged | | | | |

---

## 4. Correctness and Behavior

| Criterion | Met | Partial | Not met | Notes |
|-----------|-----|---------|---------|--------|
| Program meets the stated requirements (README / spec) | | | | |
| Edge cases considered (e.g. empty list, zero, missing file) | | | | |
| Output format matches spec or is clearly documented | | | | |
| No regressions (refactors preserve behavior) | | | | |

---

## 5. Version Control and Workflow

| Criterion | Met | Partial | Not met | Notes |
|-----------|-----|---------|---------|--------|
| Git used (repo present with commits) | | | | |
| Commits are small and purposeful | | | | |
| Commit messages describe intent, not just “fix” or “update” | | | | |
| No unnecessary large or binary files committed | | | | |

---

## 6. Professional Practices (Where Applicable)

| Criterion | Met | Partial | Not met | Notes |
|-----------|-----|---------|---------|--------|
| Configuration or paths not hardcoded where avoidable | | | | |
| File I/O handles missing files or errors | | | | |
| Logging or clear warnings used instead of only print | | | | |
| No secrets or credentials in code or config | | | | |

---

## Summary

- **Met**: Criterion fully satisfied.
- **Partial**: Some aspects done; room for improvement.
- **Not met**: Criterion not satisfied or not attempted.

**Overall**: _____ / 6 sections. Focus improvements on the sections marked Partial or Not met.

---

## Related

- Per-module checklists: see each module `.md` (e.g. `modules/M01_Foundations_and_Tooling.md`, Section 7).
- Midterm/Final rubrics: `midterm_practical.md`, `final_practical.md`.
- Teaching notes: `resources/teaching_notes.md`.
