## Level 2 – Mini Project and Capstone Specifications

This document defines specifications for all mini projects (MP01–MP08) and capstones, aligned with PCAP-31-03.

Each project includes: Goal, Requirements, Acceptance Criteria, Suggested Structure.

---

### MP01 – Multi-Module CLI Using Standard Library (Week 1)

**PCAP**: 1.1–1.4  
**Goal**: Use math, random, platform; demonstrate import variants; clear module separation.

**Requirements**:
- CLI that uses math, random, platform.
- Output: OS, Python version tuple, random number, math result (e.g. sqrt, ceil).
- Separate module for report logic; main script for CLI.

**Acceptance Criteria**:
- Run `python main.py` → no crash; output includes platform, math, and random results.
- Fixed seed (e.g. --seed) → reproducible output.
- `dir(report)` shows expected names.

**Suggested Structure**: main.py, report.py.

---

### MP02 – Small Package with Subpackages (Week 2)

**PCAP**: 1.5  
**Goal**: Create package with subpackage; clear public API via __init__.py; __name__ for script vs import.

**Requirements**:
- Package with at least one subpackage.
- __init__.py re-exports; __all__.
- `from pkg import something` works.

**Acceptance Criteria**:
- `from pkg import foo` works when foo re-exported.
- `if __name__ == "__main__":` runs demo; import does not.
- `dir(pkg)` shows public names.

**Suggested Structure**: pkg/__init__.py, pkg/utils/__init__.py, pkg/utils/helpers.py, run.py.

---

### MP03 – Validator Library with Custom Exceptions (Week 3)

**PCAP**: 2.1–2.2  
**Goal**: Custom exception hierarchy; validator functions that raise domain-specific errors.

**Requirements**:
- Custom exceptions (e.g. ValidationError, InvalidFormatError).
- Validator functions that raise on invalid input.
- try/except with specific handlers.

**Acceptance Criteria**:
- Invalid input → specific exception raised.
- Caller can catch and handle by type.
- Clear error messages in e.args.

**Suggested Structure**: exceptions.py, validators.py, main.py.

---

### MP04 – String Normalizer (Week 4)

**PCAP**: 3.1–3.3  
**Goal**: String processing; encoding awareness; ord/chr; split/join; find/index.

**Requirements**:
- Normalize text (case, whitespace, encoding).
- Use ord/chr, split/join, find/rfind as appropriate.
- Handle non-ASCII characters.

**Acceptance Criteria**:
- Normalize sample strings correctly.
- Edge cases (empty, Unicode) handled.
- Code demonstrates PCAP string methods.

**Suggested Structure**: normalizer.py, main.py.

---

### MP05 – Class Hierarchy for Domain (Week 5)

**PCAP**: 4.1–4.4, 4.6  
**Goal**: OOP foundations; class, instance vars, methods, constructors.

**Requirements**:
- Domain classes (e.g. Product, Account).
- Instance and class variables.
- Methods with self; __init__.
- hasattr, __dict__ where appropriate.

**Acceptance Criteria**:
- Create instances; call methods.
- Class variables shared; instance vars per object.
- Clear encapsulation.

**Suggested Structure**: models.py, main.py.

---

### MP06 – Inheritance and Polymorphism (Week 6)

**PCAP**: 4.5  
**Goal**: Extend MP05 hierarchy; isinstance; overriding; polymorphism.

**Requirements**:
- Subclasses extend base classes.
- Override methods; use super().
- isinstance; polymorphism in functions.
- __str__ for readable output.

**Acceptance Criteria**:
- Subclass instances work where base expected.
- Overridden methods called correctly.
- isinstance checks pass.

**Suggested Structure**: models.py (extended), main.py.

---

### MP07 – Data Pipeline with Comprehensions (Week 7)

**PCAP**: 5.1–5.3  
**Goal**: Comprehensions; lambdas; map/filter; closures.

**Requirements**:
- Transform data using list comprehensions.
- map/filter with lambdas.
- Closure where useful (e.g. make_filter).

**Acceptance Criteria**:
- Pipeline transforms input to output.
- Comprehensions and lambdas used appropriately.
- Code readable and exam-aligned.

**Suggested Structure**: pipeline.py, main.py.

---

### MP08 – File-Based Persistence Layer (Week 8)

**PCAP**: 5.4–5.5  
**Goal**: open; read/write/readlines; with; errno; text vs binary.

**Requirements**:
- save_text(path, content), load_text(path).
- Handle FileNotFoundError; use e.errno.
- Use with for automatic close.

**Acceptance Criteria**:
- Save and load text correctly.
- Missing file → handled, no crash.
- with used for file handles.

**Suggested Structure**: storage.py, main.py.

---

### Capstone 1 – Expense Tracker (OOP)

**PCAP**: 1.x, 2.x, 4.x, 5.4–5.5  
**Goal**: Full integration: modules, OOP, exceptions, file I/O.

**Requirements**:
- Expense class; ExpenseStore.
- Custom exceptions (ValidationError).
- JSON file persistence.
- CLI: add, list, summary, exit.

**Suggested Structure**: main.py, models.py, services.py, storage.py, validators.py, exceptions.py, data/.

---

### Capstone 2 – Inventory OOP

**PCAP**: Same as Capstone 1 with inventory domain.  
**Goal**: Similar integration; different domain; reinforces patterns.

**Requirements**: Same structure as Capstone 1; inventory domain (items, stock, categories).

---

For implementation details, see `../python-level-2-course/projects/` and `../python-level-2-course/capstones/`.
