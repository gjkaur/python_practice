# Level 1 Python Course – Completion Checklist

Use this to see what is **done** and what is **left** for the course.

---

## 1. Course structure and roadmap

| Item | Status | Notes |
|------|--------|--------|
| Folder: `curriculum/` | Done | |
| `curriculum/ROADMAP.md` | Done | 10-week breakdown, PCEP alignment, skills progression |
| Folder: `modules/` | Done | |
| Folder: `projects/` | Done | |
| Folder: `capstones/` | Done | |
| Folder: `assessments/` | Done | |
| Folder: `resources/` | Done | |
| Folder: `assignments/` | Done | README + W01–W10 weekly assignment sheets |
| Root `README.md` | Done | Course overview and structure |

---

## 2. Curriculum and module content

| Item | Status | Notes |
|------|--------|--------|
| Full course roadmap (modules, weeks, PCEP mapping) | Done | In `curriculum/ROADMAP.md` |
| Weekly breakdown (Weeks 1–10) | Done | In ROADMAP |
| Skills progression | Done | In ROADMAP |
| Module markdown (M01–M08) | Done | `modules/M0x_*.md` – outcomes, concepts, exercises, mini-project, checklist, interview Qs |
| Learning objectives and job-skill phrasing | Done | In each module .md |
| Edge cases and common mistakes | Done | In each module .md |
| Production notes (PEP 8, naming, modularity) | Done | In each module .md |
| Code review checklists (per module) | Done | In each module .md |
| Interview-style questions (8–12 per module) | Done | In each module .md |
| Practice sets (10–15 exercises per module) | Done | In each module .md |

---

## 3. Jupyter notebooks and module code

| Item | Status | Notes |
|------|--------|--------|
| M01–M08 concept notebooks | Done | `modules/M0x_*/M0x_Concepts.ipynb` |
| Markdown: headings, concepts, syntax | Done | In all notebooks |
| Built-in functions and usage | Done | In all notebooks (elaborated) |
| Extra examples and practice in notebooks | Done | “More Examples” and “More Practice” in each |
| Module `examples/*.py` (2+ per module) | Done | In each `M0x_*/examples/` |
| Module `practice/*.py` (1 per module) | Done | In each `M0x_*/practice/` |
| `modules/README.md` | Done | Explains notebooks vs examples vs practice |

---

## 4. Mini projects (10)

| Project | README | Python files | Status |
|---------|--------|--------------|--------|
| mp01_developer_setup_checker | Done | env_report.py, utils_system.py | Done |
| mp02_unit_converter_cli | Done | main.py, converters.py, validators.py | Done |
| mp03_admission_eligibility_checker | Done | main.py, rules.py, validators.py | Done |
| mp04_cli_menu_system | Done | main.py, actions.py, validators.py | Done |
| mp05_student_score_manager_v1 | Done | main.py, repository.py, stats.py | Done |
| mp06_address_book_cli | Done | main.py, contacts.py, formatting.py | Done |
| mp07_functional_refactor | Done | starter_script.py + REFACTOR_INSTRUCTIONS.md + README | Done |
| mp08_safe_calculator | Done | main.py, operations.py, io_utils.py | Done |
| mp09_configurable_reminder_cli | Done | main.py, config.py, reminders.py | Done |
| mp10_password_strength_checker | Done | main.py, rules.py, formatting.py | Done |

Each README includes: problem statement, user stories, I/O, constraints, suggested architecture, CLI examples, test cases, extension tasks.

\* mp07 is intentionally Starter: monolithic unit-converter script to refactor into main + services + validators. “copy from mp02”
---

## 5. Capstones (2)

| Item | Status | Notes |
|------|--------|--------|
| capstone_1_cli_expense_tracker | Done | README + main.py, models.py, services.py, storage.py, validators.py |
| capstone_2_inventory_management_cli | Done | README + cli.py, inventory.py, storage.py, validators.py |
| Full spec, milestones (MVP → v2 → v3) | Done | In each capstone README |
| Rubric (quality, correctness, design, testing) | Done | In each capstone README |
| Suggested folder structure | Done | In READMEs |
| Data persistence (JSON/CSV) | Done | Described and used in code |
| Logging approach | Done | Described in READMEs; can be wired in code |

---

## 6. Assignments and assessments

| Item | Status | Notes |
|------|--------|--------|
| **assignments/** folder | Done | Created with README and W01–W10 weekly sheets |
| Structured practice sheets (e.g. weekly) | Done | `assignments/W01_foundations.md` … `W10_capstones.md` |
| assessments/midterm_practical.md | Done | Scenario, requirements, grading rubric |
| assessments/final_practical.md | Done | Dual-capstone rubric, test scenarios |
| Code review rubrics (standalone) | Done | `assessments/code_review_rubric.md` (master handout) |

---

## 7. Teaching and resources

| Item | Status | Notes |
|------|--------|--------|
| resources/teaching_notes.md | Done | Lecture flow, demos, misconceptions, pacing, Git, feedback |
| Code review guidance | Done | In teaching_notes + per-module checklists |
| Git workflow suggestions | Done | In teaching_notes and project/capstone READMEs |

---

## 8. Professional and PCEP alignment

| Item | Status | Notes |
|------|--------|--------|
| PEP 8 and naming from day one | Done | In M01, ROADMAP, teaching_notes |
| Modular design and separation of concerns | Done | In project/capstone structure and READMEs |
| Error handling and validation | Done | In modules M07, M08 and in project code |
| Logging (introduced; not overdone) | Done | In capstone READMEs and teaching_notes |
| Config file usage | Done | mp09 + capstones |
| PCEP-30-02 alignment (all 4 sections) | Done | ROADMAP + module .md and notebooks |
| Bridge to PCAP / job readiness | Done | In ROADMAP and teaching_notes |

---

## 9. Optional / nice-to-have

| Item | Status | Notes |
|------|--------|--------|
| Sample config.json for mp09 | Done | projects/mp09_configurable_reminder_cli/config.json |
| data/ .gitkeep in capstones | Done | data/.gitkeep in both capstones |
| Single “master” code review rubric (PDF or MD) | Done | assessments/code_review_rubric.md |
| Quiz bank (PCEP-style MCQs) | Optional | Not in scope originally |
| mp07 starter template | Done | starter_script.py + REFACTOR_INSTRUCTIONS.md |

---

## Summary

- **Done:** Curriculum roadmap, 8 module .md files, 8 concept notebooks (with extra examples and practice), 8× examples + practice .py, 10 mini projects (READMEs + code; mp07 includes starter script and refactor instructions), 2 capstones (READMEs + code), midterm and final assessments, teaching_notes, root and module READMEs, PCEP alignment and professional practices.
- **Assignments:** `assignments/` folder with README and weekly sheets W01–W10.
- **Optional done:** Sample `config.json` for mp09, `data/.gitkeep` in both capstones, master `code_review_rubric.md`, mp07 starter script and REFACTOR_INSTRUCTIONS.
- **Optional not done:** Quiz bank (PCEP-style MCQs) – out of original scope.
