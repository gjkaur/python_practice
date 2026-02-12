# Master Code Review Rubric – Level 2 Python

Use for **self-review**, **peer review**, or **instructor feedback** on mini projects and capstones. Aligned with PCAP-31-03 and Level_2.pdf.

---

## 1. Structure and Design

| Criterion | Met | Partial | Not met | Notes |
|-----------|-----|---------|---------|--------|
| Clear entrypoint (main() or if __name__ == "__main__") | | | | |
| Multi-module layout; single responsibility per module | | | | |
| Separation of concerns (I/O, business logic, validation, models) | | | | |
| Package/module imports correct and minimal | | | | |
| No unnecessary globals | | | | |

---

## 2. OOP (PCAP 4.x)

| Criterion | Met | Partial | Not met | Notes |
|-----------|-----|---------|---------|--------|
| Class(es) with __init__ and instance attributes | | | | |
| Methods use self correctly | | | | |
| Optional: inheritance and polymorphism used appropriately | | | | |
| __str__ or clear string representation where useful | | | | |

---

## 3. Exceptions (PCAP 2.x)

| Criterion | Met | Partial | Not met | Notes |
|-----------|-----|---------|---------|--------|
| Custom exception(s) defined and used | | | | |
| Except branches ordered (specific first) | | | | |
| User-facing error messages clear | | | | |
| No silent failures | | | | |

---

## 4. File I/O and Correctness (PCAP 5.4–5.5)

| Criterion | Met | Partial | Not met | Notes |
|-----------|-----|---------|---------|--------|
| open/read/write used correctly; files closed (or with) | | | | |
| Missing file or OSError handled (e.g. errno) | | | | |
| Program meets spec; edge cases considered | | | | |

---

## 5. Style and Professional Practices

| Criterion | Met | Partial | Not met | Notes |
|-----------|-----|---------|---------|--------|
| PEP 8 (indentation, naming, length) | | | | |
| Docstrings on public functions/classes | | | | |
| Terminology and structure align with Level_2.pdf where applicable | | | | |

---

**Summary**: Tick Met / Partial / Not met per section. Focus improvements on Partial and Not met.
