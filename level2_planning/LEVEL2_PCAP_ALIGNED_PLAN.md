## Level 2 – PCAP-31-03 Aligned Course Plan

This plan uses the official PCAP-31-03 exam syllabus (`Level_2.pdf`) as the primary source of truth.  
All modules, lessons, and projects explicitly map to **Sections 1–5** and their objective codes.

---

### 1. Direct Mapping to PCAP Sections & Objectives

PCAP defines five sections:

- **Section 1 – Modules and Packages (12%)**
- **Section 2 – Exceptions (14%)**
- **Section 3 – Strings (18%)**
- **Section 4 – Object-Oriented Programming (34%)**
- **Section 5 – Miscellaneous (22%)**

Below is the mapping of course modules to objectives:

#### 1.1 Section 1 – Modules and Packages (PCAP 1.1–1.5)

- **PCAP 1.1–1.4 – Import and use modules**

  - **M01**: Import variants (`import`, `from import`, `import as`, `import *`); `dir()`, `sys.path`; math (ceil, floor, trunc, factorial, hypot, sqrt); random (random, seed, choice, sample); platform (platform, machine, processor, system, version, python_implementation, python_version_tuple).

- **PCAP 1.5 – User-defined modules and packages**

  - **M02**: Creating modules and packages; `__pycache__`; `__name__`; public vs private; `__init__.py`; nested packages; `__all__`.

#### 1.2 Section 2 – Exceptions (PCAP 2.1–2.2)

- **PCAP 2.1–2.2 – Exception handling**

  - **M03**: except variants; exception hierarchy; `raise`, re-raise; `assert`; `except E as e`; `e.args`; custom exception classes.

#### 1.3 Section 3 – Strings (PCAP 3.1–3.3)

- **PCAP 3.1–3.3 – String encoding and methods**

  - **M04**: ASCII, Unicode, UTF-8; `ord()`, `chr()`; indexing, slicing, immutability; iteration, concatenation, comparison; `in`/`not in`; `.isxxx()`, `.join()`, `.split()`, `.sort()`, `sorted()`, `.index()`, `.find()`, `.rfind()`.

#### 1.4 Section 4 – Object-Oriented Programming (PCAP 4.1–4.6)

- **PCAP 4.1–4.4, 4.6 – OOP foundations**

  - **M05**: Class, object, property, method, encapsulation; instance vs class variables; `__dict__`; private components and name mangling; methods and `self`; `hasattr()`, `__name__`, `__module__`, `__bases__`; constructors.

- **PCAP 4.5 – Inheritance and polymorphism**

  - **M06**: Single and multiple inheritance; `isinstance()`; overriding; `is`/`not is`; polymorphism; `__str__()`; diamond inheritance.

#### 1.5 Section 5 – Miscellaneous (PCAP 5.1–5.5)

- **PCAP 5.1–5.3 – Comprehensions, lambdas, closures**

  - **M07**: List comprehensions (if, nested); lambdas; `map()`, `filter()`; closures.

- **PCAP 5.4–5.5 – File I/O**

  - **M08**: I/O terminology; modes; streams; text vs binary; `open()`; `errno`; `close()`, `read()`, `write()`, `readline()`, `readlines()`; bytearray.

---

### 2. Week-by-Week Progression

| Week | Module | Focus | Mini Project |
|------|--------|-------|---------------|
| 1 | M01 | Import variants, dir, sys.path, math, random, platform | Multi-module CLI |
| 2 | M02 | Modules, packages, __init__.py, __name__ | Small package |
| 3 | M03 | Exceptions, hierarchy, custom exceptions | Validator library |
| 4 | M04 | Strings, encoding, ord/chr, methods | String normalizer |
| 5 | M05 | OOP foundations, class, instance vars | Class hierarchy |
| 6 | M06 | Inheritance, polymorphism | Extended hierarchy |
| 7 | M07 | Comprehensions, lambdas, closures | Data pipeline |
| 8 | M08 | File I/O, streams, modes | File persistence |
| 9 | Integration | M01–M08 reinforcement | Optional integration |
| 10 | Capstones | Two capstones end-to-end | Capstone 1 & 2 |

---

### 3. Skills Progression

- **Stage 1 (Weeks 1–2)**: Multi-module programs; standard library and custom packages.
- **Stage 2 (Weeks 3–4)**: Robust error handling with custom exceptions; advanced string processing.
- **Stage 3 (Weeks 5–6)**: Object-oriented design; class hierarchies and polymorphism.
- **Stage 4 (Weeks 7–8)**: Functional-style tools (comprehensions, lambdas, closures); file I/O.
- **Stage 5 (Weeks 9–10)**: Full capstones; professional structure and review.

---

### 4. Bridge Beyond PCAP

- **Job readiness**: Multi-package layout, OOP design, defensive use of exceptions, file-based persistence.
- **Next level**: Testing frameworks, more standard library modules, APIs, tooling.

For detailed module content, see `LEVEL2_MODULE_CONTENT.md` and `../python-level-2-course/modules/`.
