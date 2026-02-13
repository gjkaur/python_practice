## Level 2 – Teaching Assets and Supporting Materials

Supporting materials for the Level 2 (PCAP-aligned) course.

---

### 1. Module Artifacts (per module)

Each module folder contains:
- **M0x_Concepts.ipynb** – Concept notebook with explanations and runnable code.
- **examples/*.py** – Small runnable scripts.
- **practice/practice_0x_*.py** – Guided practice; solutions provided.

Location: `../python-level-2-course/modules/`.

---

### 2. Starter Templates

**2.1 Multi-Module Script Template**
- `main.py` – entry point; imports from modules.
- `report.py` or `utils.py` – business logic; no raw input.
- `if __name__ == "__main__":` guard.

**2.2 Package Template**
- `pkg/__init__.py` – re-exports; __all__.
- `pkg/submod/__init__.py`, `helpers.py`.
- `run.py` at root.

**2.3 OOP Domain Template**
- `models.py` – classes.
- `services.py` – business logic.
- `main.py` – CLI.

**2.4 Exception Template**
- `exceptions.py` – custom exception classes.
- `validators.py` – functions that raise.
- `main.py` – try/except flow.

---

### 3. Syllabus Alignment Rule

Cursor rule: `.cursor/rules/pcap-level2-syllabus-alignment.mdc`

- Ensures content aligns with Level_2.pdf (PCAP-31-03).
- Applies to python-level-2-course/**/*.{md,py}.
- Covers all PCAP sections 1–5.

---

### 4. Assessments

- **assignments/** – Weekly assignments (W01–W10).
- **assessments/** – code_review_rubric.md, midterm_practical.md, final_practical.md.
- **projects/** – MP01–MP08 mini projects.
- **capstones/** – Capstone 1 and 2.

---

### 5. Additional Resources

- **Level_2.pdf** – PCAP-31-03 official syllabus.
- **curriculum/ROADMAP.md** – Week-by-week progression.
- **resources/teaching_notes.md** – Instructor notes.

---

For implementation, see `../python-level-2-course/`.
