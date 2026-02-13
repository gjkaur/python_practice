## Level 3 – PCPP-32-101 Aligned Course Plan

This plan uses the official PCPP-32-101 exam syllabus (`Level_3.pdf`) as the primary source of truth.  
All modules, lessons, and projects explicitly map to **Sections 1–5** and their objective codes (1.1–5.2).

---

### 1. Direct Mapping to PCPP Sections & Objectives

PCPP defines five sections:

- **Section 1 – Advanced Object-Oriented Programming (35%, 15 items)**
- **Section 2 – Coding Conventions, Best Practices, and Standardization (12%, 7 items)**
- **Section 3 – GUI Programming (20%, 8 items)**
- **Section 4 – Network Programming (18%, 8 items)**
- **Section 5 – File Processing and Communicating with a Program's Environment (15%, 7 items)**

Below is a detailed mapping of course topics to the official objective codes and bullets from `Level_3.pdf`.

#### 1.1 Section 1 – Advanced Object-Oriented Programming (PCPP-32-101 1.1–1.12)

- **PCPP-32-101 1.1 – Understand and explain basic OOP terms and concepts**
  - Essential terminology: class, instance, object, attribute, method, type, instance and class variables, superclasses and subclasses  
  - Reflection: `isinstance()`, `issubclass()`  
  - The `__init__()` method  
  - Creating classes, methods, and class and instance variables; calling methods; accessing class and instance variables  
  - **Course mapping**:
    - Module 1: Lessons 1.1–1.2 (OOP terminology, reflection, `__init__`).  
    - Projects: MP01 OOP class hierarchy.

- **PCPP-32-101 1.2 – Perform Python core syntax operations**
  - Magic methods: comparison methods (e.g., `__eq__(self, other)`), numeric methods (e.g., `__abs__(self)`), type conversion methods (e.g., `__int__(self)`), object introspection (e.g., `__str__(self)`, `__instancecheck__(self, object)`), object attribute access (e.g., `__getattr__(self, attribute)`), accessing containers (e.g., `__getitem__(self, key)`)  
  - Operating with special methods  
  - Extending class implementations to support additional core syntax operations  
  - **Course mapping**:
    - Module 2: Lessons 2.1–2.4 (all magic method categories).  
    - Projects: MP01 (magic methods in class hierarchy), MP02 (decorators using `__call__`).

- **PCPP-32-101 1.3 – Understand and use inheritance, polymorphism, and composition**
  - Class hierarchies  
  - Single vs. multiple inheritance  
  - Method Resolution Order (MRO)  
  - Duck typing  
  - Inheritance vs. composition  
  - Modelling real-life problems using "is a" and "has a" relations  
  - **Course mapping**:
    - Module 1: Lessons 1.3–1.4 (inheritance, polymorphism, composition, MRO).  
    - Projects: MP01 (hierarchies), MP03 (abstract base classes with inheritance).

- **PCPP-32-101 1.4 – Extended function argument syntax and decorators**
  - Special identifiers: `*args`, `**kwargs`  
  - Forwarding arguments to other functions  
  - Function parameter handling  
  - Closures  
  - Function and class decorators  
  - Decorating functions with classes  
  - Creating decorators: implementing decorator patterns, decorator arguments, wrappers  
  - Decorator stacking  
  - Syntactic sugar  
  - Special methods: `__call__`, `__init__`  
  - **Course mapping**:
    - Module 3: Lessons 3.1–3.4 (args/kwargs, closures, decorators, class decorators).  
    - Projects: MP02 Decorator library.

- **PCPP-32-101 1.5 – Design, build, and use Python static and class methods**
  - Implementing class and static methods  
  - Class vs. static methods  
  - The `cls` parameter  
  - The `@classmethod` and `@staticmethod` decorators  
  - Class methods: accessing and modifying the state/methods of a class, creating objects  
  - **Course mapping**:
    - Module 4: Lesson 4.1 (class and static methods).  
    - Projects: MP03 (factory methods using `@classmethod`).

- **PCPP-32-101 1.6 – Understand and use Python abstract classes and methods**
  - Abstract classes and abstract methods: defining, creating, and implementing  
  - Overriding abstract methods  
  - Implementing multiple inheritance from abstract classes  
  - Delivering multiple child classes  
  - **Course mapping**:
    - Module 4: Lessons 4.2–4.3 (abc module, abstract methods, multiple inheritance).  
    - Projects: MP03 Abstract base class framework.

- **PCPP-32-101 1.7 – Understand and use attribute encapsulation**
  - Definition, meaning, usage  
  - Operating with getter, setter, and deleter methods  
  - **Course mapping**:
    - Module 5: Lesson 5.1 (property decorator, getters/setters/deleters).  
    - Projects: MP04 (encapsulated attributes in GUI models).

- **PCPP-32-101 1.8 – Understand and apply subclassing built-in classes**
  - Inheriting properties from built-in classes  
  - Using subclassing to extend class features and modify class methods and attributes  
  - **Course mapping**:
    - Module 5: Lesson 5.2 (subclassing list, dict, str, etc.).  
    - Projects: MP05 (custom list/dict subclasses).

- **PCPP-32-101 1.9 – Advanced techniques for creating and serving exceptions**
  - Exceptions as objects, named attributes of exception objects  
  - Chained exceptions, `__context__` and `__cause__` attributes, implicitly and explicitly chained exceptions  
  - Analyzing exception traceback objects, the `__traceback__` attribute  
  - Operating with different kinds of exceptions  
  - **Course mapping**:
    - Module 6: Lessons 6.1–6.2 (chained exceptions, traceback analysis).  
    - Projects: MP06 (exception hierarchies with chaining).

- **PCPP-32-101 1.10 – Shallow and deep copy operations**
  - Shallow and deep copies of objects  
  - Object: label vs. identity vs. value  
  - The `id()` function and the `is` operand  
  - Operating with `copy()` and `deepcopy()` methods  
  - **Course mapping**:
    - Module 6: Lesson 6.3 (copy module, shallow vs deep).  
    - Projects: MP06 (copying complex objects).

- **PCPP-32-101 1.11 – (De)serialization of Python objects**
  - Object persistence, serialization and deserialization: meaning, purpose, usage  
  - Serializing objects as a single byte stream: the `pickle` module, pickling various data types  
  - The `dumps()` and `loads()` functions  
  - Serializing objects by implementing a serialization dictionary: the `shelve` module, file modes, creating shelve objects  
  - **Course mapping**:
    - Module 7: Lessons 7.1–7.2 (pickle, shelve).  
    - Projects: MP07 (object persistence), Capstone 1 (saving application state).

- **PCPP-32-101 1.12 – Understand and explain metaprogramming**
  - Metaclasses: meaning, purpose, usage  
  - The `type` metaclass and the `type()` function  
  - Special attributes: `__name__`, `__class__`, `__bases__`, `__dict__`  
  - Operating with metaclasses, class variables, and class methods  
  - **Course mapping**:
    - Module 7: Lessons 7.3–7.4 (metaclasses, type, special attributes).  
    - Projects: MP07 (custom metaclass example).

#### 1.2 Section 2 – Coding Conventions & Best Practices (PCPP-32-101 2.1–2.3)

- **PCPP-32-101 2.1 – Understand PEP concept and Python philosophy**
  - The PEP concept and selected PEPs: PEP 1, PEP 8, PEP 20, PEP 257  
  - PEP 1: different types of PEPs, formats, purpose, guidelines  
  - PEP 20: Python philosophy, guiding principles, design; `import this` instruction and PEP 20 aphorisms  
  - **Course mapping**:
    - Module 8: Lesson 8.1 (PEP overview, PEP 20 philosophy).  
    - Projects: All projects reinforce PEP 20 principles.

- **PCPP-32-101 2.2 – Employ PEP 8 guidelines, coding conventions, and best practices**
  - PEP 8 compliant checkers  
  - Recommendations for code layout: indentation, continuation lines, maximum line length, line breaks, blank lines  
  - Default encodings  
  - Module imports  
  - Recommendations for string quotes, whitespace, and trailing commas  
  - Recommendations for using comments: block comments, inline comments  
  - Documentation strings  
  - Naming conventions: naming styles, recommendations  
  - Programming recommendations  
  - **Course mapping**:
    - Module 8: Lessons 8.2–8.3 (PEP 8 deep dive, tooling).  
    - Projects: All projects reviewed for PEP 8 compliance.

- **PCPP-32-101 2.3 – Employ PEP 257 guidelines, conventions, and best practices**
  - Docstrings: rationale, usage  
  - Comments vs. docstrings  
  - PEP 484 and type hints  
  - Creating, using, and accessing docstrings  
  - One-line vs. multi-line docstrings  
  - Documentation standards, linters, fixers  
  - **Course mapping**:
    - Module 8: Lesson 8.4 (PEP 257, type hints).  
    - Projects: All projects require proper docstrings.

#### 1.3 Section 3 – GUI Programming (PCPP-32-101 3.1–3.3)

- **PCPP-32-101 3.1 – Understand basic GUI concepts and terminology**
  - GUI: meaning, rationale, basic terms and definitions  
  - Visual programming: examples, basic features  
  - Widgets/controls – basic terms: windows, title and title bars, buttons, icons, labels, etc.  
  - Classical vs. event-driven programming  
  - Events – basic terms  
  - Widget toolkits/GUI toolkits  
  - **Course mapping**:
    - Module 9: Lesson 9.1 (GUI concepts, event-driven model).  
    - Projects: MP08 GUI introduction.

- **PCPP-32-101 3.2 – Use GUI toolkits to design and build simple GUI applications**
  - Importing tkinter components  
  - Creating an application's main window: `Tk()`, `mainloop()`, `title()` methods  
  - Adding widgets to the window: buttons, labels, frames, `place()` method, widget constructors, location, screen coordinates, size  
  - Launching the event controller: event handlers, defining and using callbacks, `destroy()` method, dialog boxes  
  - Shaping the main window and interacting with the user  
  - Checking the validity of user input and handling errors  
  - Working with Canvas and its methods  
  - Using Entry, Radiobutton, and Button widgets  
  - Managing widgets with grid and place managers  
  - Binding events using `bind()` method  
  - **Course mapping**:
    - Module 9: Lessons 9.2–9.4 (tkinter basics, widgets, layout managers).  
    - Projects: MP08 GUI calculator or todo app.

- **PCPP-32-101 3.3 – Demonstrate proficiency in using widgets and handling events**
  - Settling widgets in the window's interior, geometry managers  
  - Coloring widgets, color modes: RGB, HEX  
  - Event handling: writing event handlers and assigning them to widgets  
  - Event-driven programming: implementing interfaces using events and callbacks  
  - Widget properties and methods  
  - Variables: observable variables and adding observers to variables  
  - Using selected clickable and non-clickable widgets  
  - Identifying and servicing GUI events  
  - **Course mapping**:
    - Module 9: Lessons 9.5–9.6 (advanced widgets, event handling, observable variables).  
    - Projects: MP08 (full GUI app), Capstone 1 (GUI with database).

#### 1.4 Section 4 – Network Programming (PCPP-32-101 4.1–4.4)

- **PCPP-32-101 4.1 – Understand basic concepts of network programming**
  - REST  
  - Network sockets  
  - Domains, addresses, ports, protocols, and services  
  - Network communication: connection-oriented vs. connectionless communication, clients and servers  
  - **Course mapping**:
    - Module 10: Lesson 10.1 (network fundamentals, REST concepts).  
    - Projects: MP09 Network basics.

- **PCPP-32-101 4.2 – Demonstrate proficiency in working with sockets in Python**
  - The `socket` module: importing and creating sockets  
  - Connecting sockets to HTTP servers, closing connections with servers  
  - Sending requests to servers, the `send()` method  
  - Receiving responses from servers, the `recv()` method  
  - Exception handling mechanisms and exception types  
  - **Course mapping**:
    - Module 10: Lessons 10.2–10.3 (socket module, HTTP communication).  
    - Projects: MP09 (basic socket client).

- **PCPP-32-101 4.3 – Employ data transfer mechanisms for network communication**
  - JSON: syntax, structure, data types (numbers, strings, Boolean values, null), compound data (arrays and objects), sample JSON documents  
  - The `json` module: serialization and deserialization, `dumps()` and `loads()` methods, serializing Python objects  
  - XML: syntax, structure, sample XML documents, DTD, XML as a tree  
  - Processing XML files  
  - **Course mapping**:
    - Module 10: Lessons 10.4–10.5 (JSON, XML processing).  
    - Projects: MP09 (JSON/XML parsing), MP10 (REST client with JSON).

- **PCPP-32-101 4.4 – Design, develop, and improve a simple REST client**
  - The `requests` module  
  - Designing, building, and using testing environments  
  - HTTP methods: GET, POST, PUT, DELETE  
  - CRUD  
  - Adding and updating data  
  - Fetching and removing data from servers  
  - Analyzing the server's response  
  - Response status codes  
  - **Course mapping**:
    - Module 10: Lessons 10.6–10.7 (requests module, REST client patterns).  
    - Projects: MP10 REST API client, Capstone 2 (REST client with GUI).

#### 1.5 Section 5 – File Processing & Environment (PCPP-32-101 5.1–5.2)

- **PCPP-32-101 5.1 – Demonstrate proficiency in database programming in Python**
  - The `sqlite3` module  
  - Creating and closing database connection using `connect()` and `close()` methods  
  - Creating tables  
  - Inserting, reading, updating, and deleting data  
  - Transaction demarcation  
  - Cursor methods: `execute()`, `executemany()`, `fetchone()`, `fetchall()`  
  - Creating basic SQL statements (SELECT, INSERT INTO, UPDATE, DELETE, etc.)  
  - **Course mapping**:
    - Module 11: Lessons 11.1–11.3 (sqlite3, CRUD operations, transactions).  
    - Projects: MP11 Database-backed application, Capstone 1 (GUI app with database).

- **PCPP-32-101 5.2 – Demonstrate proficiency in processing different file formats**
  - Parsing XML documents  
  - Searching data in XML documents using `find()` and `findall()` methods  
  - Building XML documents using `Element` class and `SubElement()` function  
  - Reading and writing CSV data using functions and classes: `reader()`, `writer()`, `DictReader()`, `DictWriter()`  
  - Logging events in applications  
  - Working with different levels of logging  
  - Using LogRecord attributes to create log formats  
  - Creating custom handlers and formatters  
  - Parsing and creating configuration files using `ConfigParser` object  
  - Interpolating values in .ini files  
  - **Course mapping**:
    - Module 11: Lessons 11.4–11.7 (XML, CSV, logging, ConfigParser).  
    - Projects: MP11 (file processing), all capstones (logging and config).

---

### 2. Module Structure and Week-by-Week Progression

The course is organized into 12 modules over 12 weeks:

| Week | Module | Focus | PCPP Objectives | Mini Project |
|------|--------|-------|-----------------|--------------|
| 1 | M01 | Advanced OOP Foundations | 1.1, 1.3 | MP01: OOP class hierarchy |
| 2 | M02 | Magic Methods & Special Methods | 1.2 | MP01 (continued) |
| 3 | M03 | Decorators & Extended Arguments | 1.4 | MP02: Decorator library |
| 4 | M04 | Static/Class Methods & Abstract Classes | 1.5, 1.6 | MP03: Abstract base class framework |
| 5 | M05 | Encapsulation & Built-in Subclassing | 1.7, 1.8 | MP04: Encapsulated class design |
| 6 | M06 | Advanced Exceptions & Object Copying | 1.9, 1.10 | MP05: Exception handling system |
| 7 | M07 | Serialization & Metaprogramming | 1.11, 1.12 | MP06: Object persistence system |
| 8 | M08 | PEP Standards & Best Practices | 2.1, 2.2, 2.3 | MP07: Code quality refactor |
| 9 | M09 | GUI Programming with tkinter | 3.1, 3.2, 3.3 | MP08: GUI calculator/todo app |
| 10 | M10 | Network Programming & REST | 4.1, 4.2, 4.3, 4.4 | MP09: REST API client |
| 11 | M11 | Database & File Processing | 5.1, 5.2 | MP10: Database-backed application |
| 12 | M12 | Integration & Capstones | All sections | Capstone 1 & 2 |

---

### 3. Skills Progression Chart

- **Stage 1 – Advanced OOP Mastery (Weeks 1–5)**
  - **Concepts**: Magic methods, inheritance hierarchies, decorators, abstract classes, encapsulation, built-in subclassing.  
  - **Practices**: Designing class hierarchies, implementing special methods, using decorators for cross-cutting concerns.  
  - **Outcome**: Students can design and implement sophisticated OOP solutions using Python's advanced features.

- **Stage 2 – Robustness & Metaprogramming (Weeks 6–7)**
  - **Concepts**: Chained exceptions, object copying, serialization, metaclasses.  
  - **Practices**: Error handling with context, object persistence, metaprogramming patterns.  
  - **Outcome**: Students can build robust systems with advanced error handling and object persistence.

- **Stage 3 – Professional Standards (Week 8)**
  - **Concepts**: PEP 8, PEP 257, type hints, code quality tools.  
  - **Practices**: Writing production-quality code, using linters and formatters, documenting code properly.  
  - **Outcome**: Students produce code that meets professional Python standards.

- **Stage 4 – GUI & Network Programming (Weeks 9–10)**
  - **Concepts**: Event-driven programming, tkinter widgets, sockets, REST APIs, JSON/XML.  
  - **Practices**: Building GUI applications, creating REST clients, handling network communication.  
  - **Outcome**: Students can build interactive applications and integrate with web services.

- **Stage 5 – Data Persistence & Integration (Weeks 11–12)**
  - **Concepts**: SQLite databases, file formats (CSV, XML), logging, configuration management.  
  - **Practices**: Database operations, file processing, application logging, configuration handling.  
  - **Outcome**: Students can build complete applications with data persistence and professional logging.

---

### 4. Bridge to Professional Development

- **Alignment with PCPP-32-101**
  - All 45 exam items (1.1–5.2) are thoroughly covered with practical examples and projects.

- **Professional Readiness**
  - Learners finish with:
    - 10+ mini projects demonstrating advanced Python features.
    - 2 capstones integrating GUI, networking, and database technologies.
    - Experience with professional code standards (PEP 8, PEP 257, type hints).
    - Ability to design and implement complex OOP systems.
    - Skills in GUI development, network programming, and data persistence.

- **Next Steps**
  - Ready for PCPP-32-101 certification exam.
    - Prepared for advanced Python roles requiring OOP, GUI, networking, and database skills.
    - Foundation for Level 4 (PCPP2) topics: advanced frameworks, testing, deployment, and architecture.

---

### 5. Assessment Structure

- **Weekly Assignments**: Mini projects (MP01–MP10) aligned with module objectives.
- **Mid-Course Practical (Week 6)**: OOP-focused exam covering Sections 1.1–1.10.
- **Code Reviews**: Focus on PEP 8/257 compliance, OOP design, error handling.
- **Final Capstones (Week 12)**: Two comprehensive projects integrating multiple sections.
- **Quizzes**: Conceptual questions mapped to PCPP objectives.

For detailed rubrics, see `LEVEL3_RUBRICS.md`.
