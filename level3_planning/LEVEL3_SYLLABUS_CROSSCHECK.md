# Level 3 Course vs PCPP-32-101 Syllabus (Level_3.pdf) – Cross-Check

This document cross-checks every objective and bullet from **Level_3.pdf** (PCPP-32-101 exam syllabus) against the Level 3 course content.  
**Reference**: `Level_3.pdf` (March 11, 2022).

---

## Section 1: Advanced Object-Oriented Programming (35%)

| PCPP Obj | Syllabus bullet / topic | Course location | Status |
|----------|-------------------------|------------------|--------|
| **1.1** | Essential terminology: class, instance, object, attribute, method, type, instance/class variables, superclasses/subclasses | M01 guide, M01 examples, M01 notebook | ✅ |
| **1.1** | Reflection: `isinstance()`, `issubclass()` | M01 all, oop_foundations_demo.py | ✅ |
| **1.1** | The `__init__()` method | M01 | ✅ |
| **1.1** | Creating classes, methods, class/instance variables; calling methods; accessing variables | M01 | ✅ |
| **1.2** | Magic methods: comparison (e.g. `__eq__(self, other)`) | M02, magic_methods_demo.py | ✅ |
| **1.2** | Numeric methods (e.g. `__abs__(self)`) | M02, magic_methods_demo.py | ✅ |
| **1.2** | Type conversion (e.g. `__int__(self)` – PDF typo says __init__) | M02, Fraction example | ✅ |
| **1.2** | Object introspection: `__str__`, `__instancecheck__(self, object)` | M02 demo (CustomType) | ✅ |
| **1.2** | Object attribute access: `__getattr__(self, attribute)` | M02 Config class | ✅ |
| **1.2** | Accessing containers: `__getitem__(self, key)` | M02 Deck, Config | ✅ |
| **1.2** | Operating with special methods; extending class implementations | M02 | ✅ |
| **1.3** | Class hierarchies, single vs multiple inheritance, MRO | M01 | ✅ |
| **1.3** | Duck typing, inheritance vs composition, "is a" and "has a" | M01 | ✅ |
| **1.4** | `*args`, `**kwargs`, forwarding arguments, parameter handling | M03 | ✅ |
| **1.4** | Closures, function and class decorators, decorating functions with classes | M03 | ✅ |
| **1.4** | Decorator patterns, decorator arguments, wrappers, stacking, syntactic sugar | M03 | ✅ |
| **1.4** | Special methods: `__call__`, `__init__` (in decorator context) | M03 Logger class | ✅ |
| **1.5** | Class and static methods, class vs static, `cls`, `@classmethod`, `@staticmethod` | M04 | ✅ |
| **1.5** | Class methods: accessing/modifying class state, creating objects | M04 Date.from_string | ✅ |
| **1.6** | Abstract classes and methods: defining, creating, implementing | M04 | ✅ |
| **1.6** | Overriding abstract methods, multiple inheritance from ABCs, multiple child classes | M04 | ✅ |
| **1.7** | Attribute encapsulation: getter, setter, deleter | M05 Temperature, BankAccount | ✅ |
| **1.8** | Subclassing built-ins, extending/modifying class methods and attributes | M05 UniqueList, CaseInsensitiveDict | ✅ |
| **1.9** | Exceptions as objects, named attributes; chained exceptions, `__context__`, `__cause__` | M06 | ✅ |
| **1.9** | Analyzing traceback objects, `__traceback__` | M06 exceptions_demo.py | ✅ |
| **1.9** | Operating with different kinds of exceptions | M06 | ✅ |
| **1.10** | Shallow and deep copy; label vs identity vs value; `id()`, `is`; `copy()`, `deepcopy()` | M06 | ✅ |
| **1.11** | Object persistence, serialization/deserialization; pickle, dumps/loads; shelve, file modes | M07 | ✅ |
| **1.12** | Metaprogramming, metaclasses, type(), `__name__`, `__class__`, `__bases__`, `__dict__` | M07 | ✅ |

---

## Section 2: Coding Conventions & Best Practices (12%)

| PCPP Obj | Syllabus bullet / topic | Course location | Status |
|----------|-------------------------|------------------|--------|
| **2.1** | PEP concept; selected PEPs: PEP 1, PEP 8, PEP 20, PEP 257 | M08 | ✅ |
| **2.1** | PEP 1: types of PEPs, formats, purpose, guidelines | M08 guide (purpose, types, formats, guidelines) | ✅ |
| **2.1** | PEP 20: philosophy, guiding principles; `import this`, aphorisms | M08, notebook | ✅ |
| **2.2** | PEP 8 compliant checkers | M08 (flake8, black, pylint) | ✅ |
| **2.2** | Code layout: indentation, continuation lines, max line length, line breaks, blank lines | M08 | ✅ |
| **2.2** | Default encodings | M08 guide (UTF-8, encoding declaration) | ✅ |
| **2.2** | Module imports; string quotes, whitespace, trailing commas | M08 | ✅ |
| **2.2** | Comments: block, inline; documentation strings; naming conventions; programming recommendations | M08 | ✅ |
| **2.3** | Docstrings: rationale, usage; comments vs docstrings; PEP 484 type hints | M08 | ✅ |
| **2.3** | One-line vs multi-line docstrings; documentation standards, linters, fixers | M08 | ✅ |

---

## Section 3: GUI Programming (20%)

| PCPP Obj | Syllabus bullet / topic | Course location | Status |
|----------|-------------------------|------------------|--------|
| **3.1** | GUI meaning, rationale; widgets (windows, title bar, buttons, icons, labels); classical vs event-driven; events; toolkits | M09 Lesson 9.1 | ✅ |
| **3.2** | Importing tkinter; Tk(), mainloop(), title(); adding widgets (buttons, labels, frames, place()) | M09 guide + gui_demo (Frame, destroy()) | ✅ |
| **3.2** | Event controller, callbacks, **destroy()** method, dialog boxes | M09; gui_demo create_dialog_demo(), destroy() | ✅ |
| **3.2** | Checking validity of user input, handling errors; Canvas and methods; Entry, Radiobutton, Button; grid and place; bind() | M09, gui_demo.py | ✅ |
| **3.3** | Geometry managers; **coloring widgets, color modes: RGB, HEX** | M09 guide + gui_demo (HEX fill colors) | ✅ |
| **3.3** | Event handlers, event-driven, widget properties; observable variables and observers | M09 | ✅ |
| **3.3** | Clickable/non-clickable widgets; identifying and servicing GUI events | M09 | ✅ |

---

## Section 4: Network Programming (18%)

| PCPP Obj | Syllabus bullet / topic | Course location | Status |
|----------|-------------------------|------------------|--------|
| **4.1** | REST; network sockets; domains, addresses, ports, protocols; connection-oriented vs connectionless; clients/servers | M10 | ✅ |
| **4.2** | socket module; creating sockets; connecting/closing; send(), recv(); exception handling | M10 network_demo.py | ✅ |
| **4.3** | JSON: syntax, structure, data types, compound data; json module dumps/loads | M10 | ✅ |
| **4.3** | XML: syntax, structure, sample docs; **DTD**; XML as tree; processing XML | M10 guide (DTD, XML as tree) + examples | ✅ |
| **4.4** | **requests** module; HTTP GET, POST, PUT, DELETE; CRUD; analyzing response; status codes | M10 RESTClient | ✅ |

---

## Section 5: File Processing & Environment (15%)

| PCPP Obj | Syllabus bullet / topic | Course location | Status |
|----------|-------------------------|------------------|--------|
| **5.1** | sqlite3 module; connect(), close(); creating tables; INSERT, READ, UPDATE, DELETE | M11 database_demo.py | ✅ |
| **5.1** | Transaction demarcation; cursor: execute, executemany, **fetchone**, fetchall; basic SQL | M11 database_demo (fetchone + fetchall) | ✅ |
| **5.2** | Parsing XML; find(), findall(); building XML with Element, SubElement | M10 + M11 guide (XML file processing) | ✅ |
| **5.2** | CSV: reader, writer, DictReader, DictWriter | M11 | ✅ |
| **5.2** | Logging events; logging levels; **LogRecord attributes** for formats; custom handlers and formatters | M11 guide + database_demo (format comment) | ✅ |
| **5.2** | ConfigParser; **interpolating values in .ini files** | M11 guide + database_demo (paths.report) | ✅ |

---

## Summary of Gaps – Addressed

1. **M08 (Section 2)**: Add **default encodings**; optionally expand **PEP 1** (formats, guidelines).
2. **M09 (Section 3)**: Add **destroy()**, **dialog boxes** (messagebox is dialog – make explicit), **Frame** widget, **RGB/HEX** color modes.
3. **M10 (Section 4)**: Optional: mention **DTD** and “XML as a tree” in module or examples.
4. **M11 (Section 5)**: Add **fetchone()** in database example; add **LogRecord** in logging section; add **ConfigParser interpolation** example; optionally add **XML file** parsing/building (Element/SubElement) for 5.2 file processing.

---

## Verification

- **All PCPP objectives 1.1–5.2** are covered by at least one module.
- **Examples**: All modules have `examples/` and `practice/`; notebooks M01–M12 present.
- **Projects**: MP01–MP10 and both capstones map to syllabus sections as in LEVEL3_PCPP_ALIGNED_PLAN.md.
- **Assessments**: Midterm (1.1–1.10), final (all sections), code review rubric align with syllabus.

**Conclusion**: Course is fully aligned with Level_3.pdf with explicit coverage of all syllabus bullets.
