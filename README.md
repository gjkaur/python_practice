# Python Professional Course – Complete Curriculum

A structured, certification-aligned Python curriculum in three levels: **PCEP** (Level 1), **PCAP** (Level 2), and **PCPP** (Level 3). Each level includes planning documents, modules, mini projects, capstones, assignments, and assessments.

---

## Course Overview

| Level | Certification | Syllabus | Duration | Course Folder | Planning Folder |
|-------|---------------|----------|----------|---------------|-----------------|
| **Level 1** | PCEP (Entry) | PCEP-30-02 | ~10 weeks | [python-level-1-course/](python-level-1-course/) | [level1_planning/](level1_planning/) |
| **Level 2** | PCAP (Associate) | PCAP-31-03 | ~10 weeks | [python-level-2-course/](python-level-2-course/) | [level2_planning/](level2_planning/) |
| **Level 3** | PCPP (Professional) | PCPP-32-101 | ~12 weeks | [python-level-3-course/](python-level-3-course/) | [level3_planning/](level3_planning/) |

---

## Level 1 – PCEP (Certified Entry-Level Python Programmer)

**Goal:** Take a beginner to job-ready, production-oriented Python while fully covering the PCEP-30-02 syllabus and preparing for PCAP.

- **Topics:** Environment setup, fundamentals, control flow, data collections, functions, exceptions, clean code, testing, logging, project structure.
- **Outcomes:** Clean PEP 8 code, small CLI apps with validation and logging, Git workflow, defensive programming, modular design, PCEP exam readiness.
- **Highlights:** 10 mini projects, 2 capstones (e.g. CLI Expense Tracker, Inventory Management), weekly assignments, midterm and final practicals.

→ **Start here:** [python-level-1-course/](python-level-1-course/) · [level1_planning/](level1_planning/)

---

## Level 2 – PCAP (Certified Associate in Python Programming)

**Goal:** Build multi-module, object-oriented Python applications while fully covering the PCAP-31-03 syllabus.

- **Topics:** Modules and standard library, exceptions, strings, OOP (classes, inheritance, polymorphism), comprehensions and functional tools, file I/O.
- **Outcomes:** Modules and packages, custom exceptions, OOP design, file I/O, multi-module CLI applications with persistence.
- **Highlights:** 8 modules (M01–M08), 8 mini projects, 2 capstones (Expense Tracker OOP, Inventory OOP), Jupyter notebooks, assignments W01–W10.

→ **Start here:** [python-level-2-course/](python-level-2-course/) · [level2_planning/](level2_planning/)

---

## Level 3 – PCPP (Certified Professional in Python Programming 1)

**Goal:** Build production-ready applications with advanced OOP, GUI, networking, and databases while fully covering the PCPP-32-101 syllabus.

- **Topics:** Advanced OOP (magic methods, decorators, static/class methods, ABCs, encapsulation, built-in subclassing), exceptions and copying, serialization and metaprogramming, PEP standards, GUI (tkinter), network programming (REST, JSON/XML), SQLite, CSV, logging, ConfigParser.
- **Outcomes:** Sophisticated OOP design, GUI apps, REST clients, database-backed apps, PEP 8/257/484, integration of GUI + DB + networking.
- **Highlights:** 12 modules (M01–M12), 10 mini projects, 2 capstones (Full-Stack GUI with DB, REST Client with GUI), Jupyter notebooks, assignments W01–W12.

→ **Start here:** [python-level-3-course/](python-level-3-course/) · [level3_planning/](level3_planning/)

---

## Repository Structure (Top Level)

```
.
├── README.md                    # This file – complete course overview
├── python-level-1-course/       # Level 1: PCEP-aligned course content
├── python-level-2-course/       # Level 2: PCAP-aligned course content
├── python-level-3-course/       # Level 3: PCPP-aligned course content
├── level1_planning/             # Level 1: planning docs, specs, rubrics
├── level2_planning/             # Level 2: planning docs, specs, rubrics
├── level3_planning/             # Level 3: planning docs, specs, rubrics
└── .cursor/
    └── rules/                   # Cursor rules for syllabus alignment (e.g. PCPP Level 3)
```

Each **python-level-X-course/** folder contains:

- **curriculum/** – Roadmap and alignment
- **modules/** – Module guides, Jupyter notebooks, examples, practice
- **projects/** – Mini project READMEs and code
- **capstones/** – Capstone specs and code
- **assignments/** – Weekly assignment sheets
- **assessments/** – Rubrics for midterm, final, code review
- **resources/** – Teaching notes and references

Each **levelX_planning/** folder contains:

- Aligned plan (PCEP/PCAP/PCPP), module content, project specs, rubrics, teaching assets.

---

## Progression and Prerequisites

- **Level 1** – No prior Python required. Completing it prepares for PCEP and Level 2.
- **Level 2** – Assumes Level 1 (or PCEP-level knowledge). Completing it prepares for PCAP and Level 3.
- **Level 3** – Assumes Level 2 (or PCAP-level knowledge, including OOP, modules, exceptions, file I/O). Completing it prepares for PCPP-32-101 and advanced professional Python work.

---

## How to Use This Repository

- **Instructor-led:** Use each level’s `curriculum/` and `modules/` for planning; `assignments/` and `assessments/` for grading; `projects/` and `capstones/` for hands-on work.
- **Self-paced:** Start with `curriculum/ROADMAP.md` in the level you’re on; work through modules in order, then mini projects and capstones; use assessment rubrics as self-check.
- **Certification:** Level 1 → PCEP; Level 2 → PCAP; Level 3 → PCPP-32-101. Syllabi (e.g. Level_1.pdf, Level_2.pdf, Level_3.pdf) are the source of truth; planning docs map objectives to modules and projects.

---

## Branches

- **main** – Default branch; may contain all levels or the primary production content.
- **level2-course** – Level 2 (PCAP) course content.
- **level3-course** – Level 3 (PCPP) course content.

Check out the branch that matches the level you’re working on.

---

## Principles Across All Levels

- **Syllabus alignment** – Content is mapped to official exam objectives (PCEP-30-02, PCAP-31-03, PCPP-32-101).
- **Professional practices** – PEP 8, docstrings, type hints where applicable, Git, logging, modular design, testing basics.
- **Project-based learning** – Mini projects and capstones in every level.
- **Clear progression** – Each level builds on the previous; capstones integrate the skills of that level.

For level-specific details, open the README inside each **python-level-X-course/** folder.
