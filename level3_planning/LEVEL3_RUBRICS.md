## Level 3 – Evaluation Rubrics

This document defines rubrics for:
- Weekly assignments and mini projects.
- Code reviews (peer or instructor).
- Quizzes (conceptual understanding).
- Mid-course practical exam.
- Final practical capstones.

Rubrics are aligned with PCPP-32-101 objectives and professional coding standards.

---

### 1. Weekly Assignment & Mini Project Rubric

Use a 0–3 scale per criterion (0 = Not met, 1 = Partially, 2 = Mostly, 3 = Fully). Total score /30.

**1.1 Correctness (0–9)**
- **0**: Code does not run or fails basic scenarios; key requirements unmet.
- **3**: Code runs but fails many core scenarios or crashes on common input.
- **6**: Mostly correct; minor logic errors or unhandled edge cases remain.
- **9**: Correct behavior across specified requirements and common edge cases.

**1.2 PCPP Concept Alignment (0–6)**
- Checks use of concepts targeted that week (e.g., magic methods, decorators, abstract classes, GUI, networking).
- **0**: Target concepts misused or largely ignored.
- **3**: Concepts used but with notable misunderstandings or anti-patterns.
- **6**: Concepts correctly and appropriately applied to solve the problem.

**1.3 Code Structure & Professional Quality (0–6)**
- Naming (PEP 8), function/class decomposition, docstrings (PEP 257), type hints (PEP 484).
- **0**: Unstructured, confusing code; poor naming; no docstrings; no type hints.
- **3**: Some structure and reasonable naming, but missing docstrings or type hints in many places.
- **6**: Clear, modular structure with comprehensive docstrings and type hints; follows PEP 8/257/484.

**1.4 Error Handling & Robustness (0–3)**
- **0**: No validation; program easily crashes; no exception handling.
- **1**: Minimal checks; basic exception handling but misses important cases.
- **2**: Handles common errors with appropriate exceptions and user-friendly messages.
- **3**: Comprehensive error handling with chained exceptions, logging, and graceful degradation.

**1.5 Advanced OOP & Design Patterns (0–3)**
- **0**: No use of advanced OOP features (magic methods, properties, inheritance hierarchies).
- **1**: Some advanced features used but incorrectly or unnecessarily.
- **2**: Appropriate use of advanced OOP features; good design patterns.
- **3**: Sophisticated OOP design with proper use of inheritance, composition, encapsulation, and design patterns.

**1.6 Testing & Quality Assurance (0–3)**
- **0**: No tests or documented checks.
- **1**: Some manual test cases described in comments or README.
- **2**: At least basic automated tests for core logic; uses `unittest` or `pytest`.
- **3**: Good test coverage with unit tests, integration tests, and edge case coverage.

---

### 2. Code Review Rubric (Peer or Instructor)

Each category can be rated as **Pass** / **Needs Work** / **Excellent**, with 1–2 sentences of feedback.

**2.1 Readability & Style**
- Uses PEP 8 naming, consistent indentation, appropriate comments/docstrings (PEP 257), type hints (PEP 484).
- Code is understandable without running it.
- **Pass**: Code follows PEP 8 and has basic docstrings.
- **Needs Work**: Violations of PEP 8, missing docstrings, or unclear code.
- **Excellent**: Exemplary adherence to PEP 8/257/484, self-documenting code.

**2.2 Correctness & Edge Cases**
- Implements specified behavior; considers typical edge cases.
- No obvious logic flaws in core flows.
- **Pass**: Core functionality works; handles common edge cases.
- **Needs Work**: Logic errors or missing edge case handling.
- **Excellent**: Robust handling of edge cases, defensive programming.

**2.3 OOP Design & Architecture**
- Proper use of classes, inheritance, composition, encapsulation.
- Magic methods used appropriately.
- Design patterns applied where beneficial.
- **Pass**: Basic OOP structure; classes and methods used correctly.
- **Needs Work**: Poor OOP design, misuse of inheritance, missing encapsulation.
- **Excellent**: Sophisticated OOP design with appropriate patterns and abstractions.

**2.4 Error Handling & Logging**
- Uses specific exceptions instead of bare `except`.
- Exception chaining where appropriate.
- Logging for important events and errors.
- **Pass**: Basic exception handling; some logging.
- **Needs Work**: Bare `except`, no logging, or poor error messages.
- **Excellent**: Comprehensive exception handling with chaining, structured logging.

**2.5 Testability & Tests**
- Presence of pure functions and testable classes.
- Tests are meaningful and cover important paths.
- **Pass**: Some tests present; core logic is testable.
- **Needs Work**: No tests or untestable code structure.
- **Excellent**: High test coverage with well-designed test cases.

**2.6 PCPP Objective Coverage**
- Explicit use of PCPP concepts (magic methods, decorators, abstract classes, etc.).
- **Pass**: Uses required PCPP concepts correctly.
- **Needs Work**: Missing required concepts or incorrect usage.
- **Excellent**: Demonstrates mastery of PCPP concepts with advanced applications.

---

### 3. Quiz Rubric (Conceptual)

Quizzes focus on PCPP-32-101 objectives: OOP, magic methods, decorators, GUI, networking, databases.

**3.1 Multiple-Choice Questions**
- Typically 1 point per question.
- Focused on:
  - Magic methods: which method is called for `==`, `+`, `str()`, etc.
  - Decorators: syntax, execution order, decorator with arguments.
  - Inheritance: MRO, multiple inheritance, abstract classes.
  - GUI: event-driven programming, tkinter widgets, event handlers.
  - Networking: sockets, REST, JSON/XML, HTTP methods.
  - Databases: SQLite operations, transactions, SQL syntax.
  - Serialization: pickle, shelve, JSON.
  - Metaclasses: `type`, special attributes, class creation.

**3.2 Short Answer / Explanation Questions**
- Scored 0–2:
  - **0**: Incorrect or missing explanation.
  - **1**: Partially correct but vague or incomplete reasoning.
  - **2**: Accurate explanation using correct terminology and examples.

Examples:
- Conceptual: "Explain the difference between `@staticmethod` and `@classmethod`. When would you use each?"
- Debugging: "Why does this code raise a `TypeError` when trying to pickle this object? How can you fix it?"
- Design: "Design a class hierarchy for a drawing application. Explain your choices regarding inheritance vs composition."

**3.3 Code Analysis Questions**
- Given code snippet, identify:
  - Which magic methods are being called.
  - What the output will be.
  - How to fix or improve the code.
- Scored 0–3 based on accuracy and completeness.

---

### 4. Mid-Course Practical Exam Rubric (Week 6)

Suitable for Week 6 practical focused on advanced OOP (Sections 1.1–1.10). Suggested /100 weighting:

**4.1 Core Correctness (30)**
- Implements required features correctly (OOP hierarchy, magic methods, exceptions, copying).
- Handles basic specified scenarios without errors.

**4.2 Advanced OOP Concepts (25)**
- Appropriately uses:
  - Magic methods (comparison, numeric, container methods).
  - Inheritance hierarchies with proper MRO understanding.
  - Decorators (function and class decorators).
  - Abstract classes and methods.
  - Properties and encapsulation.
  - Exception chaining and traceback handling.
  - Object copying (shallow vs deep).

**4.3 Code Organization & Professional Quality (20)**
- Code is broken into well-designed classes with clear responsibilities.
- Follows PEP 8, PEP 257 (docstrings), and PEP 484 (type hints) reasonably well.
- Avoids duplication and uses design patterns appropriately.

**4.4 Error Handling & Robustness (15)**
- Comprehensive exception handling with chained exceptions.
- Validates inputs and handles edge cases gracefully.
- Uses specific exception types, not bare `except`.

**4.5 Design & Architecture (10)**
- Good use of inheritance, composition, and encapsulation.
- Appropriate application of OOP principles ("is a" vs "has a").
- Code demonstrates understanding of when to use different patterns.

**Score Bands**
- **0–49**: Fail – Major requirements missing or unstable program.
- **50–79**: Pass – Meets core requirements with acceptable structure.
- **80–100**: Strong Pass – Robust, well-structured solution with excellent OOP design.

---

### 5. Final Practical / Capstone Rubric

Used to evaluate capstone projects in Week 12. Suggested /100 weighting:

**5.1 Functionality vs Requirements (25)**
- Implements required features (GUI, database, networking, etc.).
- Key user flows work correctly and are demonstrable.
- Integration between components (GUI ↔ services ↔ database) works seamlessly.

**5.2 Architecture & Separation of Concerns (20)**
- Follows recommended architecture:
  - Clear separation: GUI, services, data access layers.
  - Proper use of models, views, controllers (or similar pattern).
- Modules have clear, single responsibilities.
- Code is organized in logical packages/modules.

**5.3 Advanced OOP & Design Patterns (15)**
- Sophisticated use of OOP features:
  - Magic methods where appropriate.
  - Proper inheritance hierarchies.
  - Encapsulation with properties.
  - Abstract classes if applicable.
  - Design patterns (factory, observer, etc.) where beneficial.

**5.4 Code Quality & Professionalism (15)**
- Consistent naming and formatting (PEP 8 compliant).
- Comprehensive docstrings (PEP 257) for all public APIs.
- Type hints (PEP 484) throughout codebase.
- No dead code or debugging artifacts.
- Project structure is professional and maintainable.

**5.5 Error Handling, Logging, and Configuration (10)**
- Common invalid inputs handled gracefully (no unexpected tracebacks).
- Exceptions used properly (specific types, chaining where appropriate).
- Logging captures important events and failures (using `logging` module).
- Configuration externalized (ConfigParser or similar).
- Error messages are user-friendly (especially in GUI).

**5.6 Testing (10)**
- Automated tests exist for core logic functions:
  - Unit tests for services, models, database operations.
  - Integration tests for component interactions.
- Tests are meaningful (cover typical and edge cases) and pass reliably.
- Test coverage is reasonable (aim for 60%+ of core logic).

**5.7 Documentation & Git History (5)**
- README clearly documents:
  - Project purpose and features.
  - Installation and setup instructions.
  - How to run the application.
  - Architecture overview.
  - Example usage or screenshots.
- Git history shows iterative development instead of last-minute dump.
- Commit messages are descriptive and follow conventions.

**Score Bands**
- **90–100**: Excellent – Near "professional developer ready" level; production-quality code with minor polish needed.
- **75–89**: Strong – Solid understanding and implementation; a few improvements needed for production.
- **60–74**: Adequate – Meets course outcomes but with notable weaknesses in design or implementation.
- **<60**: Incomplete or significantly flawed; major rework needed.

---

### 6. PCPP Objective Coverage Tracking

For each assignment and exam, track which PCPP objectives are demonstrated:

**Tracking Template**
- **MP01**: 1.1 (OOP terminology), 1.2 (magic methods), 1.3 (inheritance)
- **MP02**: 1.4 (decorators, extended arguments)
- **MP03**: 1.5 (class/static methods), 1.6 (abstract classes)
- **MP04**: 1.7 (encapsulation), 1.8 (built-in subclassing)
- **MP05**: 1.9 (advanced exceptions), 1.10 (copying)
- **MP06**: 1.11 (serialization), 1.12 (metaprogramming)
- **MP07**: 2.1, 2.2, 2.3 (PEP standards)
- **MP08**: 3.1, 3.2, 3.3 (GUI programming)
- **MP09**: 4.1, 4.2, 4.3, 4.4 (network programming)
- **MP10**: 5.1, 5.2 (database and file processing)
- **Capstones**: All sections (1.1–5.2)

**Coverage Verification**
- Each PCPP objective (1.1–5.2) must appear in at least:
  - One mini project.
  - One quiz question.
  - One code review discussion.
  - Final capstone (all objectives should be demonstrable).

---

### 7. Portfolio & Capstone Review Guidelines

In addition to numeric rubrics, use a brief qualitative review:

- **Problem Statement Clarity**
  - Can the student clearly describe what their project does and for whom?
  - Is the problem well-scoped and realistic?

- **Architecture Explanation**
  - Can they explain how components interact (GUI, services, database, networking)?
  - Do they understand the separation of concerns?

- **OOP Design Decisions**
  - Can they justify class hierarchies, use of inheritance vs composition?
  - Do they understand when to use magic methods, decorators, abstract classes?

- **Professional Practices**
  - Do they follow PEP 8, PEP 257, use type hints?
  - Is error handling comprehensive and user-friendly?
  - Is logging used appropriately?

- **Reflection & Next Steps**
  - Can they identify areas for improvement?
  - What would they add in a "Level 4" version?
  - How would they deploy or scale this application?

These narrative elements help students practice professional communication about their code alongside the more formal, numeric evaluation.

---

### 8. Special Considerations for Level 3

**Advanced Topics**
- Students are expected to demonstrate deeper understanding than Level 1/2.
- Code should show awareness of design patterns and best practices.
- Mistakes are learning opportunities; focus on understanding why something is wrong, not just that it's wrong.

**Integration Focus**
- Capstones emphasize integrating multiple technologies (GUI + database + networking).
- Students should understand how components work together, not just in isolation.

**Professional Readiness**
- Code quality standards are higher (PEP 8/257/484 compliance expected).
- Error handling and logging are mandatory, not optional.
- Documentation should be production-ready.

**PCPP Exam Preparation**
- Rubrics align with PCPP-32-101 exam format (multiple choice, code analysis).
- Students should be able to explain concepts, not just implement them.
- Focus on understanding "why" not just "how".

---

This completes the evaluation rubrics for Level 3, ensuring comprehensive assessment aligned with PCPP-32-101 objectives and professional standards.
