## Teaching Notes – Python Level 2 (PCAP) Course

These notes support delivery of the Level 2 course in a **job-focused** way while covering every objective in **Level_2.pdf** (PCAP-31-03).

---

### 1. Teaching Philosophy

- Learners have completed Level 1 (or equivalent); build on functions, collections, and basic I/O.
- Emphasize **multi-module** design and **OOP** as the default for larger scripts.
- Tie every topic to **PCAP objective codes** (e.g. PCAP-31-03 4.2) so exam readiness is explicit.
- Use **custom exceptions** and **file I/O** from the start of relevant modules so they become habitual.

---

### 2. Lecture Flow per Module

For each module (M01–M08):

1. **Concept framing (10–15 min)** – Map lesson to Level_2.pdf section and objective numbers.
2. **Live demos (20–25 min)** – Run concept notebook and examples; show import layout, class definition, or exception hierarchy.
3. **Hands-on practice (25–35 min)** – Module practice file and exercises from the .md.
4. **Mini-project tie-in (25–35 min)** – Start or extend the week’s mini project; stress module boundaries and naming.
5. **Retrospective (5–10 min)** – Interview-style questions; common mistakes (see below).

---

### 3. Typical Misconceptions (Level 2)

- **M01–M02 (Modules and packages)**  
  - Putting all code in one file; forgetting __init__.py in packages; confusion between __name__ when run vs imported.

- **M03 (Exceptions)**  
  - Catching too broadly (bare except); not defining custom exceptions for domain errors; forgetting to re-raise or log.

- **M04 (Strings)**  
  - Ignoring encoding when reading/writing files; using .index() without handling ValueError.

- **M05–M06 (OOP)**  
  - Confusing class and instance variables; forgetting self in methods; overriding without calling super() when needed; misuse of is vs ==.

- **M07 (Comprehensions, lambdas, closures)**  
  - Overly complex comprehensions; using lambdas for multi-line logic; closure loops (late binding) in loops.

- **M08 (File I/O)**  
  - Not closing files or using with; ignoring OSError/errno for missing files; mixing text and binary mode.

---

### 4. Pacing (10-Week Format)

- Weeks 1–2: Modules and packages; ensure learners can create and import their own package.
- Weeks 3–4: Exceptions and strings; custom hierarchy and encoding awareness.
- Weeks 5–6: OOP foundations and inheritance; emphasize __init__, self, and polymorphism.
- Weeks 7–8: Comprehensions/lambdas/closures and file I/O; integrate into mini projects.
- Weeks 9–10: Integration and capstones; code review rubric and Git.

---

### 5. Demos and Tools

- Use the **concept notebooks** (M01_Concepts.ipynb through M08_Concepts.ipynb) for live run-through.
- Run **example** scripts from each module to show expected output.
- Point to **Level_2.pdf** for the authoritative topic list; use the plan’s **Module-to-objective mapping** for coverage checks.

---

### 6. Code Review and Feedback

- Use **assessments/code_review_rubric.md** for mini projects and capstones.
- Emphasize: module boundaries, custom exceptions, OOP usage, and safe file I/O.
- Encourage learners to cite **PCAP objective codes** in their README or submission notes.
