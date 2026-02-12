## Level 2 Python – Curriculum Roadmap

**Course Name**: Python Level 2 – Associate Professional  
**Primary Alignment**: PCAP-31-03 (Certified Associate in Python Programming)  
**Secondary Goal**: Job-ready multi-module and OOP Python; bridge to advanced topics.

---

### 1. High-Level Flow

The course is structured into **eight Level 2 modules**, delivered over approximately **10 weeks**. Every objective and sub-bullet from **Level_2.pdf** (PCAP-31-03) is covered; see the Module-to-objective mapping in the plan.

- **M01 – Modules and the Standard Library (PCAP 1.1–1.4)**  
  Import variants, `dir()`, `sys.path`; math, random, and platform modules.
- **M02 – User-Defined Modules and Packages (PCAP 1.5)**  
  `__init__.py`, `__name__`, `__pycache__`, public/private, nested packages.
- **M03 – Exceptions (PCAP 2.1–2.2)**  
  Exception hierarchy, except variants, `raise`/`assert`, custom exception classes.
- **M04 – Strings (PCAP 3.1–3.3)**  
  Encoding (ASCII, Unicode, UTF-8), `ord()`/`chr()`, indexing/slicing, built-in string methods.
- **M05 – Object-Oriented Programming Foundations (PCAP 4.1–4.4, 4.6)**  
  Class, object, instance vs class variables, methods, `self`, introspection, constructors.
- **M06 – Inheritance and Polymorphism (PCAP 4.5)**  
  Single/multiple inheritance, `isinstance()`, overriding, `is`/`not is`, `__str__()`, diamonds.
- **M07 – Comprehensions, Lambdas, and Closures (PCAP 5.1–5.3)**  
  List comprehensions, lambdas, `map()`/`filter()`, closures.
- **M08 – File I/O (PCAP 5.4–5.5)**  
  I/O terminology, `open()`, streams, text/binary modes, `read`/`write`/`readlines`, `bytearray`.

Each module maps to PCAP objective codes, contains lesson-level outcomes and mini projects, and builds toward the two capstones.

See module-level details in `../modules/`.

---

### 2. Week-by-Week Progression

**Week 1 – Modules and Standard Library (PCAP 1.1–1.4)**  
_Module_: M01  
_Focus_: Import variants (`import`, `from import`, `import as`, `import *`); `dir()`, `sys.path`; math (ceil, floor, trunc, factorial, hypot, sqrt); random (random, seed, choice, sample); platform (platform, machine, processor, system, version, python_implementation, python_version_tuple).  
**Mini Project**: Multi-module CLI using math/random/platform.

**Week 2 – User-Defined Modules and Packages (PCAP 1.5)**  
_Module_: M02  
_Focus_: Creating modules and packages; `__pycache__`; `__name__`; public vs private variables; `__init__.py`; searching modules/packages; nested packages vs directory trees.  
**Mini Project**: Small package with subpackages and clear public API.

**Week 3 – Exceptions (PCAP 2.1–2.2)**  
_Module_: M03  
_Focus_: except variants; exception hierarchy; `raise`, `raise ex`; `assert`; `except E as e`; `arg` property; defining and using custom exception classes.  
**Mini Project**: Validator library with custom exception hierarchy.

**Week 4 – Strings (PCAP 3.1–3.3)**  
_Module_: M04  
_Focus_: ASCII, Unicode, UTF-8, code points, escape sequences; `ord()`, `chr()`; indexing, slicing, immutability; iteration, concatenation, comparison; `in`/`not in`; `.isxxx()`, `.join()`, `.split()`, `.sort()`, `sorted()`, `.index()`, `.find()`, `.rfind()`.  
**Mini Project**: String/encoding normalizer or text processor.

**Week 5 – OOP Foundations (PCAP 4.1–4.4, 4.6)**  
_Module_: M05  
_Focus_: Class, object, property, method, encapsulation; instance vs class variables; `__dict__`; private components and name mangling; methods and `self`; `hasattr()`, `__name__`, `__module__`, `__bases__`; constructors.  
**Mini Project**: Class hierarchy for a domain (e.g. products, accounts).

**Week 6 – Inheritance and Polymorphism (PCAP 4.5)**  
_Module_: M06  
_Focus_: Single and multiple inheritance; `isinstance()`; overriding; `is`/`not is`; polymorphism; overriding `__str__()`; diamond inheritance.  
**Mini Project**: Extend Week 5 hierarchy with inheritance and polymorphism.

**Week 7 – Comprehensions, Lambdas, Closures (PCAP 5.1–5.3)**  
_Module_: M07  
_Focus_: List comprehensions (if operator, nested); lambdas; functions taking lambdas; `map()`, `filter()`; closures (meaning, defining, using).  
**Mini Project**: Data pipeline or transformer using comprehensions and lambdas.

**Week 8 – File I/O (PCAP 5.4–5.5)**  
_Module_: M08  
_Focus_: I/O modes; predefined streams; handles vs streams; text vs binary; `open()`; `errno`; `close()`, `.read()`, `.write()`, `.readline()`, `readlines()`; bytearray as I/O buffer.  
**Mini Project**: File-based persistence layer or log processor.

**Week 9 – Integration and Capstone Prep**  
_Modules_: M01–M08 (reinforcement)  
_Focus_: Combining modules, OOP, exceptions, I/O, and functional patterns; code review; testing key logic.  
**Mini Project**: Optional small integration project or capstone milestone.

**Week 10 – Capstones and Professionalization**  
_Focus_: Two capstone projects end-to-end; modular architecture; custom exceptions; OOP design; file I/O; Git, branches, code review.

---

### 3. Alignment to PCAP-31-03 Objectives

**Section 1 – Modules and Packages (12%)**  
- M01: 1.1–1.4 (import, dir, sys.path, math, random, platform).  
- M02: 1.5 (user-defined modules/packages, __pycache__, __name__, __init__.py, nested packages).

**Section 2 – Exceptions (14%)**  
- M03: 2.1–2.2 (except variants, hierarchy, raise/assert, custom exceptions).

**Section 3 – Strings (18%)**  
- M04: 3.1–3.3 (encoding, ord/chr, indexing/slicing, string methods).

**Section 4 – Object-Oriented Programming (34%)**  
- M05: 4.1–4.4, 4.6 (OOP notions, properties, methods, introspection, constructors).  
- M06: 4.5 (inheritance, isinstance, overriding, polymorphism, __str__, diamonds).

**Section 5 – Miscellaneous (22%)**  
- M07: 5.1–5.3 (list comprehensions, lambdas, map/filter, closures).  
- M08: 5.4–5.5 (I/O terminology, open, streams, read/write, bytearray).

---

### 4. Skills Progression

- **Stage 1 (Weeks 1–2)**: Multi-module programs; standard library and custom packages.
- **Stage 2 (Weeks 3–4)**: Robust error handling with custom exceptions; advanced string processing.
- **Stage 3 (Weeks 5–6)**: Object-oriented design; class hierarchies and polymorphism.
- **Stage 4 (Weeks 7–8)**: Functional-style tools (comprehensions, lambdas, closures); file I/O.
- **Stage 5 (Weeks 9–10)**: Full capstones; professional structure and review.

---

### 5. Bridge Beyond PCAP

- **Job readiness**: Multi-package layout, OOP design, defensive use of exceptions, file-based persistence.
- **Next level**: Testing frameworks, more standard library modules, APIs, tooling.

For detailed teaching plans, see the per-module documents under `../modules/`.
