# Week 10 – Capstones and Professionalization

**Modules**: M06–M08 (integration)  
**Projects**: [Capstone 1 – CLI Expense Tracker](../capstones/capstone_1_cli_expense_tracker/), [Capstone 2 – Inventory Management CLI](../capstones/capstone_2_inventory_management_cli/)

---

## Learning focus

- End-to-end CLI applications with persistence (JSON/CSV).
- Modular architecture: models, services, storage, validators.
- Git workflow: branches, commits, (optional) pull request and code review.
- Short architecture walkthrough and demo.

---

## Reading and specs

- [Capstone 1 README](../capstones/capstone_1_cli_expense_tracker/README.md) – spec, milestones, rubric.
- [Capstone 2 README](../capstones/capstone_2_inventory_management_cli/README.md) – spec, milestones, rubric.
- [Code review rubric](../assessments/code_review_rubric.md) for self- or peer review.
- [Teaching notes – Capstones](../resources/teaching_notes.md) (if your instructor shared them).

---

## Capstone 1 – CLI Expense Tracker

1. Implement MVP: add expense, list expenses, basic persistence (e.g. JSON file in `data/`).
2. Add validators (amount > 0, date format, category if required).
3. Optionally: filtering by date/category, totals, logging.
4. Run through the capstone README test scenarios; self-assess with the rubric.

---

## Capstone 2 – Inventory Management CLI

1. Implement MVP: add item, list items, update quantity, persistence (e.g. JSON in `data/`).
2. Add validators (quantity >= 0, required fields).
3. Optionally: search, low-stock warning, logging.
4. Run through the capstone README test scenarios; self-assess with the rubric.

---

## Professionalization tasks

1. Create a branch for each capstone (or one branch per feature); commit with clear messages.
2. Fill the [code review rubric](../assessments/code_review_rubric.md) for your own code (or swap with a peer).
3. Prepare a 5–10 minute walkthrough: project structure, one user flow, one design decision (e.g. where validation lives).

---

## Checklist

- [ ] Capstone 1 MVP complete and persisted
- [ ] Capstone 2 MVP complete and persisted
- [ ] Code review rubric completed (self or peer)
- [ ] Git history with meaningful commits
- [ ] Ready to demo and explain structure
