# Python Level 2 – Associate Professional Course

**Goal**: Build job-ready, multi-module and object-oriented Python applications while fully covering the **PCAP-31-03** syllabus (Level_2.pdf) and reinforcing professional practices.

This repository contains the curriculum assets for the **Python Level 2** course:

- **curriculum/** – ROADMAP with week-by-week flow and PCAP section mapping.
- **modules/** – Eight modules (M01–M08): .md guides, concept notebooks, examples, practice.
- **projects/** – Eight mini projects (mp01–mp08) with READMEs and code.
- **capstones/** – Two capstones (Expense Tracker OOP, Inventory OOP) with specs and code.
- **assignments/** – Weekly assignment sheets (W01–W10).
- **assessments/** – Midterm and final practical rubrics, code review rubric.
- **resources/** – Teaching notes for delivery and pacing.

## Course Outcomes

By the end of Level 2, learners will be able to:

- **Import and create** modules and packages; use standard library (math, random, platform) and __init__.py, __name__, __pycache__.
- **Handle errors** with built-in and custom exception hierarchies; use raise, assert, and except variants correctly.
- **Process strings** with encoding awareness and built-in methods (ord/chr, join/split, find, etc.).
- **Design with OOP**: classes, instance/class variables, methods, inheritance, polymorphism, __str__, constructors.
- **Use** list comprehensions, lambdas, closures, map/filter.
- **Perform file I/O** with open, read/write/readlines, text vs binary, and errno handling.
- **Build** small multi-module CLI applications with persistence and clear structure.

## Repository Structure

- `curriculum/ROADMAP.md` – High-level flow and PCAP alignment.
- `modules/` – One folder per module (M01–M08) with .md, .ipynb, examples/, practice/.
- `projects/` – Mini project READMEs and Python code.
- `capstones/` – Capstone READMEs and full implementations.
- `assignments/` – Weekly sheets linking to modules and projects.
- `assessments/` – Rubrics for midterm, final, and code review.
- `resources/teaching_notes.md` – Delivery and misconceptions.

## Usage

- **Instructor-led**: Use ROADMAP and module .md for session planning; assignments and assessments for grading.
- **Self-paced**: Follow ROADMAP; work through modules in order, then mini projects and capstones.
- **Alignment**: All content is aligned with Level_2.pdf (PCAP-31-03). The Cursor rule `.cursor/rules/pcap-level2-syllabus-alignment.mdc` keeps edits aligned with the syllabus.

## Principles

- **PCAP coverage**: Every objective and sub-bullet from Level_2.pdf is covered; see the plan’s Complete topic list and Module-to-objective mapping.
- **Job-focused**: Multi-module layout, OOP design, custom exceptions, file I/O, PEP 8.
- **Bridge beyond**: Prepares for advanced testing, APIs, and tooling.

For the detailed roadmap, see `curriculum/ROADMAP.md`.
