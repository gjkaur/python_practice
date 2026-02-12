## Level 2 – Module Content and Syllabus Alignment

This document details content for each module (M01–M08) in the Level 2 Python course, aligned with PCAP-31-03 (Level_2.pdf).

---

### M01 – Modules and the Standard Library (PCAP 1.1–1.4)

**Goal**: Import and use modules; use math, random, platform; discover module contents with `dir()` and `sys.path`.

**Core concepts**:
- Import variants: `import`, `from import`, `import as`, `import *` (and when to avoid `*`).
- `dir()` and `sys.path` for discovery and import resolution.
- math: ceil, floor, trunc, factorial, hypot, sqrt.
- random: random(), seed(), choice(), sample().
- platform: platform(), machine(), processor(), system(), version(), python_implementation(), python_version_tuple().

**Artifacts**: M01_Concepts.ipynb, examples (import_variants_demo.py, standard_lib_demo.py), practice_01_modules.py.

---

### M02 – User-Defined Modules and Packages (PCAP 1.5)

**Goal**: Create modules and packages; understand `__pycache__`, `__name__`, `__init__.py`, public/private, nested packages.

**Core concepts**:
- Module: single .py file; package: directory with `__init__.py`.
- `__pycache__`: bytecode caching.
- `__name__`: script vs import guard (`if __name__ == "__main__"`).
- `__init__.py` and re-exporting public API.
- `__all__` for controlling `from mod import *`.
- Public vs private (single underscore convention).
- Nested packages: `from pkg.subpkg import mod`.

**Artifacts**: M02_Concepts.ipynb, examples (package_demo.py), practice_02_packages.py, mymath.py, mypkg, mod_for_all.py.

---

### M03 – Exceptions (PCAP 2.1–2.2)

**Goal**: Use except variants; understand hierarchy; raise/assert; define and use custom exceptions.

**Core concepts**:
- try/except, except (E1, E2), try/except/else.
- Exception hierarchy: BaseException, Exception, ValueError, TypeError, etc.
- raise, re-raise; assert.
- Custom exceptions: subclass Exception; e.args.
- Order of except clauses (most specific first).

**Artifacts**: M03_Concepts.ipynb, examples (exceptions_demo.py), practice_03_exceptions.py.

---

### M04 – Strings (PCAP 3.1–3.3)

**Goal**: Encoding (ASCII, Unicode, UTF-8); ord/chr; indexing, slicing; built-in string methods.

**Core concepts**:
- ASCII, Unicode, code points; UTF-8 encoding.
- ord(c), chr(i).
- Indexing, slicing (including negative step), immutability.
- in, not in; iteration.
- .isalpha(), .isdigit(), .isalnum(), .isspace().
- .find(), .rfind(), .index(); .split(), .join(); sorted(s).

**Artifacts**: M04_Concepts.ipynb, examples (strings_demo.py), practice_04_strings.py.

---

### M05 – OOP Foundations (PCAP 4.1–4.4, 4.6)

**Goal**: Class, object; instance vs class variables; methods, self; introspection; constructors.

**Core concepts**:
- Class and object; properties (attributes).
- Instance variables vs class variables; `__dict__`.
- Methods and self; __init__ constructor.
- hasattr, getattr, setattr; __name__, __module__, __bases__.
- Private components; name mangling (single vs double underscore).

**Artifacts**: M05_Concepts.ipynb, examples (oop_demo.py), practice_05_oop.py.

---

### M06 – Inheritance and Polymorphism (PCAP 4.5)

**Goal**: Single and multiple inheritance; isinstance; overriding; polymorphism; __str__; diamond inheritance.

**Core concepts**:
- class C(A): syntax; overriding methods.
- isinstance(obj, Class); polymorphism.
- super(); __str__.
- Multiple inheritance; MRO; diamond problem.

**Artifacts**: M06_Concepts.ipynb, examples (inheritance_demo.py), practice_06_inheritance.py.

---

### M07 – Comprehensions, Lambdas, Closures (PCAP 5.1–5.3)

**Goal**: List comprehensions; lambdas; map/filter; closures.

**Core concepts**:
- [expr for x in iterable]; [expr for x in iterable if condition]; nested comprehensions.
- Dict and set comprehensions.
- lambda args: expr.
- map(f, iterable), filter(pred, iterable).
- Closures: functions capturing names from enclosing scope.

**Artifacts**: M07_Concepts.ipynb, examples (comprehensions_demo.py), practice_07_comprehensions.py.

---

### M08 – File I/O (PCAP 5.4–5.5)

**Goal**: open modes; streams; read/write; text vs binary; errno; bytearray.

**Core concepts**:
- open(path, mode, encoding); with statement.
- Modes: r, w, a, rb, wb.
- read(), readline(), readlines(); write(), writelines().
- for line in f: iteration.
- OSError, FileNotFoundError; errno.ENOENT.
- bytearray.

**Artifacts**: M08_Concepts.ipynb, examples (file_io_demo.py), practice_08_file_io.py.

---

For implementation details, see `../python-level-2-course/modules/`.
