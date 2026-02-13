## Level 3 – Lesson-Level Module Content

This document details lesson-level content for each module (M01–M12) in the Level 3 Professional Python course, aligned with the PCPP-32-101 syllabus and the high-level plan.

---

### Module 1 – Advanced OOP Foundations (PCPP 1.1, 1.3)

**Lesson 1.1 – OOP Terminology and Reflection**
- **Goal**: Master OOP terminology and use reflection functions (`isinstance`, `issubclass`).
- **Content**:
  - Essential terminology: class, instance, object, attribute, method, type, instance variables vs class variables, superclasses and subclasses.
  - Reflection functions: `isinstance(obj, Class)`, `issubclass(SubClass, BaseClass)`.
  - The `__init__()` method: purpose, parameters, initialization patterns.
  - Creating classes, methods, and class/instance variables; calling methods; accessing variables.
- **Examples**:
  - Define a `Vehicle` class with instance variables (`make`, `model`, `year`) and class variable (`total_vehicles`).
  - Use `isinstance()` to check if an object is an instance of a class or its subclass.
  - Use `issubclass()` to verify inheritance relationships.
- **Edge cases / misconceptions**:
  - Confusing instance variables with class variables (shared vs per-instance).
  - Using `isinstance()` with multiple classes: `isinstance(obj, (Class1, Class2))`.
  - `__init__()` vs `__new__()` (mention `__new__` conceptually, deep dive later).
- **Refactoring / demo**:
  - Start with a procedural approach; refactor into a class hierarchy with proper initialization.

**Lesson 1.2 – Class Variables vs Instance Variables**
- **Goal**: Understand when to use class variables vs instance variables and avoid common pitfalls.
- **Content**:
  - Class variables: shared across all instances, defined at class level.
  - Instance variables: unique to each instance, typically set in `__init__`.
  - Mutable class variables: dangers of shared mutable state (e.g., class-level lists).
  - Accessing class variables: `ClassName.var` vs `instance.var` (instance can shadow class variable).
- **Examples**:
  - Counter class with class variable `count` tracking total instances.
  - Demonstrate mutable class variable bug: shared list across instances.
- **Edge cases / misconceptions**:
  - Accidentally creating instance variables when intending to modify class variables.
  - Mutable defaults in class variables causing unexpected sharing.
- **Refactoring / demo**:
  - Refactor code that incorrectly uses class variables for instance-specific data.

**Lesson 1.3 – Inheritance and Class Hierarchies**
- **Goal**: Design and implement inheritance hierarchies with single and multiple inheritance.
- **Content**:
  - Single inheritance: one parent class.
  - Multiple inheritance: multiple parent classes.
  - Method Resolution Order (MRO): how Python resolves method calls in inheritance chains.
  - Viewing MRO: `ClassName.__mro__` or `ClassName.mro()`.
  - Calling parent methods: `super()` function.
- **Examples**:
  - `Animal` → `Mammal` → `Dog` (single inheritance).
  - `FlyingVehicle` inheriting from both `Vehicle` and `Flyable` (multiple inheritance).
  - Demonstrate MRO with diamond inheritance pattern.
- **Edge cases / misconceptions**:
  - Diamond inheritance problems and how MRO solves them.
  - Incorrect use of `super()` in multiple inheritance scenarios.
  - Method shadowing vs method overriding.
- **Refactoring / demo**:
  - Refactor a flat class design into a proper inheritance hierarchy.

**Lesson 1.4 – Polymorphism and Composition**
- **Goal**: Understand polymorphism (duck typing) and when to use composition vs inheritance.
- **Content**:
  - Polymorphism: same interface, different implementations.
  - Duck typing: "If it walks like a duck and quacks like a duck, it's a duck."
  - Inheritance vs composition: "is a" vs "has a" relationships.
  - Composition: embedding objects as attributes instead of inheriting.
- **Examples**:
  - Polymorphic function that works with any object having `draw()` method.
  - `Car` "has a" `Engine` (composition) vs `Car` "is a" `Vehicle` (inheritance).
  - Refactor inheritance to composition where appropriate.
- **Edge cases / misconceptions**:
  - Overusing inheritance when composition is more appropriate.
  - Confusing polymorphism with inheritance (polymorphism doesn't require inheritance in Python).
- **Refactoring / demo**:
  - Refactor a deep inheritance hierarchy to use composition for better flexibility.

---

### Module 2 – Magic Methods & Special Methods (PCPP 1.2)

**Lesson 2.1 – Comparison Magic Methods**
- **Goal**: Implement comparison operators using magic methods (`__eq__`, `__lt__`, `__le__`, `__gt__`, `__ge__`, `__ne__`).
- **Content**:
  - Comparison methods: `__eq__`, `__ne__`, `__lt__`, `__le__`, `__gt__`, `__ge__`.
  - `@functools.total_ordering` decorator for reducing boilerplate.
  - Rich comparison: implementing `__eq__` and one other enables all comparisons.
- **Examples**:
  - `Point` class with `__eq__` and `__lt__` comparing distance from origin.
  - `Student` class comparing by grade using `@total_ordering`.
- **Edge cases / misconceptions**:
  - Returning `NotImplemented` vs raising `TypeError` for unsupported comparisons.
  - Hashable objects: if `__eq__` is defined, `__hash__` must be defined (or set to `None`).
- **Refactoring / demo**:
  - Replace manual comparison functions with magic methods.

**Lesson 2.2 – Numeric Magic Methods**
- **Goal**: Implement arithmetic operations using numeric magic methods.
- **Content**:
  - Numeric methods: `__add__`, `__sub__`, `__mul__`, `__truediv__`, `__floordiv__`, `__mod__`, `__pow__`, `__abs__`, `__neg__`, `__pos__`.
  - Right-hand operations: `__radd__`, `__rsub__`, etc. (for `other + self`).
  - In-place operations: `__iadd__`, `__isub__`, etc. (for `+=`, `-=`).
- **Examples**:
  - `Vector` class with `__add__`, `__mul__` (scalar multiplication), `__abs__` (magnitude).
  - `Money` class with currency-aware arithmetic.
- **Edge cases / misconceptions**:
  - Handling type mismatches: return `NotImplemented` to allow right-hand methods.
  - In-place methods should modify `self` and return `self`.
- **Refactoring / demo**:
  - Refactor a class with external arithmetic functions to use magic methods.

**Lesson 2.3 – Type Conversion and Introspection Methods**
- **Goal**: Implement type conversion and object representation methods.
- **Content**:
  - Type conversion: `__int__`, `__float__`, `__str__`, `__repr__`, `__bool__`, `__bytes__`.
  - Object representation: `__str__` (user-friendly) vs `__repr__` (developer-friendly, should be unambiguous).
  - Introspection: `__instancecheck__`, `__subclasscheck__` (for custom `isinstance`/`issubclass` behavior).
- **Examples**:
  - `Fraction` class with `__int__`, `__float__`, `__str__`, `__repr__`.
  - Custom `__bool__` for truthiness (e.g., `Container` is truthy if non-empty).
- **Edge cases / misconceptions**:
  - `__repr__` should ideally be evaluable: `eval(repr(obj)) == obj`.
  - `__bool__` vs `__len__`: if `__bool__` is not defined, Python uses `__len__`.
- **Refactoring / demo**:
  - Improve `__repr__` to be more informative and evaluable.

**Lesson 2.4 – Attribute Access and Container Methods**
- **Goal**: Control attribute access and make objects behave like containers.
- **Content**:
  - Attribute access: `__getattr__`, `__setattr__`, `__delattr__`, `__getattribute__`.
  - Container methods: `__getitem__`, `__setitem__`, `__delitem__`, `__len__`, `__contains__`, `__iter__`, `__next__`.
  - Making objects subscriptable and iterable.
- **Examples**:
  - `Config` class with `__getattr__` for dynamic attribute access.
  - `Deck` class implementing `__getitem__`, `__len__`, `__contains__` to behave like a list.
  - `Range` class with `__iter__` and `__next__` for iteration.
- **Edge cases / misconceptions**:
  - `__getattribute__` intercepts all attribute access; must call `super().__getattribute__` or raise `AttributeError`.
  - `__getattr__` only called when attribute not found via normal lookup.
  - Infinite loops in `__setattr__` if not careful (use `object.__setattr__` or `super()`).
- **Refactoring / demo**:
  - Convert a class with explicit getter/setter methods to use `__getattr__`/`__setattr__`.

---

### Module 3 – Decorators & Extended Arguments (PCPP 1.4)

**Lesson 3.1 – Extended Function Arguments (`*args`, `**kwargs`)**
- **Goal**: Use `*args` and `**kwargs` for flexible function signatures.
- **Content**:
  - `*args`: variable positional arguments (tuple).
  - `**kwargs`: variable keyword arguments (dict).
  - Combining positional, keyword, `*args`, and `**kwargs` in function signatures.
  - Forwarding arguments: `func(*args, **kwargs)`.
- **Examples**:
  - `sum_all(*args)` function accepting any number of numbers.
  - `create_user(name, email, **kwargs)` with optional fields.
  - Wrapper function forwarding all arguments: `wrapper(*args, **kwargs): return original(*args, **kwargs)`.
- **Edge cases / misconceptions**:
  - Order matters: `def func(pos, *args, keyword=None, **kwargs)`.
  - `*args` and `**kwargs` are just names; `*` and `**` are the operators.
  - Unpacking: `func(*[1, 2, 3])` expands to `func(1, 2, 3)`.
- **Refactoring / demo**:
  - Refactor multiple overloaded functions into one using `*args`/`**kwargs`.

**Lesson 3.2 – Closures**
- **Goal**: Understand closures and use them to create function factories.
- **Content**:
  - Closure: inner function that captures variables from enclosing scope.
  - Lexical scoping: inner functions can access outer function's variables.
  - Common use cases: function factories, decorators, callbacks.
- **Examples**:
  - `make_multiplier(n)` returning a function that multiplies by `n`.
  - `make_counter()` returning a counter function with private state.
  - Event handler factory using closures.
- **Edge cases / misconceptions**:
  - Late binding: closures capture variable references, not values (use default arguments to capture values).
  - Modifying outer variables: use `nonlocal` keyword.
- **Refactoring / demo**:
  - Refactor a class with a single method into a closure-based function.

**Lesson 3.3 – Function Decorators**
- **Goal**: Create and use function decorators to modify function behavior.
- **Content**:
  - Decorator syntax: `@decorator` above function definition.
  - Decorator as function: `@decorator` is syntactic sugar for `func = decorator(func)`.
  - Simple decorator: function that takes a function and returns a function.
  - Preserving metadata: `@functools.wraps(func)`.
- **Examples**:
  - `@timer` decorator measuring function execution time.
  - `@retry` decorator retrying failed function calls.
  - `@validate_input` decorator checking function arguments.
- **Edge cases / misconceptions**:
  - Decorators execute at function definition time, not call time.
  - Decorated function loses original name/docstring without `@wraps`.
  - Decorator stacking: `@decorator1 @decorator2 def func()` applies bottom-to-top.
- **Refactoring / demo**:
  - Extract cross-cutting concerns (logging, timing) into decorators.

**Lesson 3.4 – Decorators with Arguments and Class Decorators**
- **Goal**: Create decorators that accept arguments and decorators implemented as classes.
- **Content**:
  - Decorator with arguments: three-level function (outer takes args, middle takes func, inner is wrapper).
  - Class decorators: class with `__call__` method.
  - Decorating functions with classes: class instance used as decorator.
- **Examples**:
  - `@repeat(n)` decorator repeating function call `n` times.
  - `@rate_limit(calls_per_second)` decorator limiting function call rate.
  - `Logger` class decorator: `@Logger('module_name')`.
- **Edge cases / misconceptions**:
  - Decorator with arguments: must return a decorator function, not the wrapper directly.
  - Class decorators: `__call__` receives the function as argument.
- **Refactoring / demo**:
  - Convert a function decorator to a class decorator for stateful behavior.

---

### Module 4 – Static/Class Methods & Abstract Classes (PCPP 1.5, 1.6)

**Lesson 4.1 – Static and Class Methods**
- **Goal**: Design and use `@staticmethod` and `@classmethod` appropriately.
- **Content**:
  - Static methods: `@staticmethod`, no `self` or `cls`, utility functions related to class.
  - Class methods: `@classmethod`, receives `cls` (class), can access/modify class state, create instances.
  - When to use: static for utilities, class for alternative constructors and factory methods.
- **Examples**:
  - `MathUtils` class with `@staticmethod add(a, b)`.
  - `Date` class with `@classmethod from_string(cls, date_string)` alternative constructor.
  - `Product` class with `@classmethod create_discount_product(cls, name, price, discount)` factory.
- **Edge cases / misconceptions**:
  - Static methods can be called on instance or class; class methods typically called on class.
  - Class methods can create instances of subclasses when called on subclass.
- **Refactoring / demo**:
  - Refactor module-level utility functions into static methods of a related class.

**Lesson 4.2 – Abstract Base Classes (ABC)**
- **Goal**: Define abstract classes and methods using the `abc` module.
- **Content**:
  - Abstract base class: cannot be instantiated directly, defines interface for subclasses.
  - `abc.ABC` base class or `metaclass=abc.ABCMeta`.
  - Abstract methods: `@abc.abstractmethod`, must be implemented by subclasses.
  - `abc.abstractproperty` (deprecated, use `@property` with `@abstractmethod`).
- **Examples**:
  - `Shape` abstract class with `area()` and `perimeter()` abstract methods.
  - `Animal` abstract class with `make_sound()` abstract method.
  - Attempting to instantiate abstract class raises `TypeError`.
- **Edge cases / misconceptions**:
  - Abstract methods can have implementations (called via `super()`).
  - Mixing abstract and concrete methods in same class.
  - Abstract class can have `__init__` with common initialization.
- **Refactoring / demo**:
  - Refactor a class hierarchy to use ABC for enforcing interface contracts.

**Lesson 4.3 – Multiple Inheritance with Abstract Classes**
- **Goal**: Implement multiple inheritance from abstract classes and deliver multiple child classes.
- **Content**:
  - Multiple inheritance from ABCs: class can inherit from multiple abstract classes.
  - Implementing all abstract methods from all parents.
  - MRO with abstract classes: abstract methods resolved via MRO.
  - Concrete implementations in child classes.
- **Examples**:
  - `FlyingAnimal` inheriting from `Animal` (abstract) and `Flyable` (abstract).
  - `Bird` class implementing both `make_sound()` and `fly()`.
  - Multiple child classes (`Eagle`, `Sparrow`) implementing the same abstract interface.
- **Edge cases / misconceptions**:
  - Diamond inheritance with abstract classes: MRO ensures correct method resolution.
  - Abstract methods from multiple parents must all be implemented.
- **Refactoring / demo**:
  - Design a system using multiple abstract base classes for different concerns (e.g., `Drawable`, `Movable`, `Collidable`).

---

### Module 5 – Encapsulation & Built-in Subclassing (PCPP 1.7, 1.8)

**Lesson 5.1 – Attribute Encapsulation (Properties)**
- **Goal**: Implement getters, setters, and deleters using the `@property` decorator.
- **Content**:
  - Property decorator: `@property` for getter, `@property_name.setter` for setter, `@property_name.deleter` for deleter.
  - Encapsulation: controlling access to attributes, validation, computed properties.
  - Private attributes: single underscore `_attr` (convention) or double underscore `__attr` (name mangling).
- **Examples**:
  - `Temperature` class with `celsius` property, setter validates range.
  - `BankAccount` class with `balance` property (read-only, modified via methods).
  - `Person` class with `age` property computed from `birth_date`.
- **Edge cases / misconceptions**:
  - Properties are accessed like attributes, not called like methods.
  - Deleter is called with `del obj.property`, not `obj.property.delete()`.
  - Name mangling (`__attr`) makes attribute harder to access but not truly private.
- **Refactoring / demo**:
  - Refactor a class with explicit getter/setter methods to use `@property`.

**Lesson 5.2 – Subclassing Built-in Classes**
- **Goal**: Extend built-in classes (`list`, `dict`, `str`, etc.) to add custom behavior.
- **Content**:
  - Inheriting from built-ins: `class MyList(list)`, `class MyDict(dict)`.
  - Overriding methods: `append`, `__getitem__`, `__setitem__`, etc.
  - Extending functionality: adding new methods, modifying existing behavior.
  - Calling parent methods: `super().method()` or `list.method(self, ...)`.
- **Examples**:
  - `UniqueList(list)` that prevents duplicate items.
  - `DefaultDict(dict)` with default value factory (simplified version).
  - `CaseInsensitiveDict(dict)` with case-insensitive keys.
- **Edge cases / misconceptions**:
  - Some built-ins have C implementations; overriding may not work as expected in all cases.
  - `__init__` of built-ins may not call `super().__init__` in the same way.
  - Composition vs inheritance: sometimes wrapping is better than inheriting.
- **Refactoring / demo**:
  - Refactor a wrapper class around a built-in to use inheritance instead.

---

### Module 6 – Advanced Exceptions & Object Copying (PCPP 1.9, 1.10)

**Lesson 6.1 – Chained Exceptions**
- **Goal**: Use exception chaining to preserve error context.
- **Content**:
  - Exception chaining: linking exceptions to show error propagation.
  - Implicit chaining: `__context__` attribute (exception raised in `except` block).
  - Explicit chaining: `raise NewException from OriginalException` (`__cause__` attribute).
  - `raise ... from None`: suppress exception context.
- **Examples**:
  - Database error wrapped in application error: `raise AppError("Failed to save") from db_error`.
  - Exception chain in traceback showing full error path.
  - `raise ValueError("Invalid input") from None` to hide implementation details.
- **Edge cases / misconceptions**:
  - `from None` suppresses both `__context__` and `__cause__`.
  - Chaining preserves original traceback information.
- **Refactoring / demo**:
  - Refactor exception handling to add context via chaining.

**Lesson 6.2 – Traceback Objects**
- **Goal**: Analyze and manipulate exception traceback objects.
- **Content**:
  - `__traceback__` attribute: traceback object attached to exception.
  - `traceback` module: `traceback.format_exc()`, `traceback.print_exc()`, `traceback.format_tb()`.
  - Accessing traceback: `exc.__traceback__`, `sys.exc_info()`.
  - Custom traceback formatting for logging.
- **Examples**:
  - Logging exception with full traceback: `logger.exception("Error occurred")`.
  - Extracting traceback as string: `traceback.format_exc()`.
  - Custom error reporting with formatted traceback.
- **Edge cases / misconceptions**:
  - Traceback objects are only valid during exception handling.
  - `sys.exc_info()` returns `(type, value, traceback)` tuple.
- **Refactoring / demo**:
  - Improve error logging to include formatted tracebacks.

**Lesson 6.3 – Shallow and Deep Copy**
- **Goal**: Understand object copying and when to use shallow vs deep copy.
- **Content**:
  - Object identity: `id(obj)`, `is` operator (identity comparison).
  - Shallow copy: `copy.copy()`, new object, but nested objects are references.
  - Deep copy: `copy.deepcopy()`, recursively copies all nested objects.
  - When to use: shallow for simple objects, deep for nested structures.
- **Examples**:
  - `copy.copy()` on list: new list, but inner lists are shared.
  - `copy.deepcopy()` on nested structure: completely independent copy.
  - Custom `__copy__` and `__deepcopy__` methods for custom copying behavior.
- **Edge cases / misconceptions**:
  - Circular references: `deepcopy()` handles them correctly.
  - Mutable defaults: copying can reveal shared mutable state issues.
  - `copy()` vs `[:]` (shallow copy) vs `list()` constructor (shallow copy).
- **Refactoring / demo**:
  - Fix bugs caused by shared mutable state using proper copying.

---

### Module 7 – Serialization & Metaprogramming (PCPP 1.11, 1.12)

**Lesson 7.1 – Pickle Module**
- **Goal**: Serialize and deserialize Python objects using `pickle`.
- **Content**:
  - Pickle: serializing objects to byte stream.
  - `pickle.dumps(obj)`: object to bytes.
  - `pickle.loads(bytes)`: bytes to object.
  - `pickle.dump(obj, file)`: object to file.
  - `pickle.load(file)`: file to object.
  - Pickling various types: basic types, custom classes, functions (with limitations).
- **Examples**:
  - Serialize a `Person` object to file and load it back.
  - Pickle a list of custom objects.
  - Handle `PickleError` exceptions.
- **Edge cases / misconceptions**:
  - Security: never unpickle untrusted data (can execute arbitrary code).
  - Not all objects are picklable: file handles, network connections, etc.
  - Version compatibility: pickle format may change between Python versions.
- **Refactoring / demo**:
  - Replace manual serialization (JSON with custom encoders) with pickle for complex objects.

**Lesson 7.2 – Shelve Module**
- **Goal**: Use `shelve` for dictionary-like persistent storage.
- **Content**:
  - Shelve: dictionary-like interface to persistent storage (uses pickle under the hood).
  - Creating shelve: `shelve.open(filename, flag='c')`.
  - File modes: 'r' (read), 'w' (write), 'c' (create), 'n' (new).
  - Storing and retrieving objects: `shelf['key'] = obj`, `obj = shelf['key']`.
  - Closing: `shelf.close()` or use context manager.
- **Examples**:
  - Simple database: `shelf['users'] = user_list`, `shelf['settings'] = config_dict`.
  - Persistent cache: storing computed results.
- **Edge cases / misconceptions**:
  - Keys must be strings.
  - Changes not written until `close()` or `sync()`.
  - Not thread-safe for writing.
- **Refactoring / demo**:
  - Replace file-based JSON storage with shelve for better performance.

**Lesson 7.3 – Metaclasses Introduction**
- **Goal**: Understand metaclasses and their purpose.
- **Content**:
  - Metaclass: class of a class (class is an instance of its metaclass).
  - Default metaclass: `type`.
  - `type(name, bases, dict)`: dynamic class creation.
  - Custom metaclass: class inheriting from `type` or using `metaclass=` parameter.
- **Examples**:
  - Creating class dynamically: `MyClass = type('MyClass', (Base,), {'attr': value})`.
  - Simple metaclass: `class Meta(type): ... class MyClass(metaclass=Meta): ...`.
  - Metaclass `__new__` and `__init__` methods.
- **Edge cases / misconceptions**:
  - Metaclasses are advanced; use sparingly (prefer decorators or other patterns when possible).
  - Metaclass `__new__` creates the class object.
  - All classes in inheritance chain must have compatible metaclasses.
- **Refactoring / demo**:
  - Convert a class decorator pattern to a metaclass (if appropriate).

**Lesson 7.4 – Special Attributes and Metaclass Operations**
- **Goal**: Use special class attributes and operate with metaclasses.
- **Content**:
  - Special attributes: `__name__`, `__class__`, `__bases__`, `__dict__`, `__module__`, `__qualname__`.
  - Inspecting classes: accessing these attributes programmatically.
  - Metaclass operations: modifying class creation, adding methods/attributes dynamically.
  - Class variables and class methods in metaclass context.
- **Examples**:
  - Inspect class hierarchy: `cls.__bases__`, `cls.__mro__`.
  - Metaclass adding methods to all classes: registry pattern.
  - `__dict__` inspection: seeing all attributes and methods.
- **Edge cases / misconceptions**:
  - `__dict__` doesn't include inherited attributes (use `dir()` or `vars()`).
  - Metaclass can modify class before it's fully created.
- **Refactoring / demo**:
  - Use metaclass to automatically register classes in a registry.

---

### Module 8 – PEP Standards & Best Practices (PCPP 2.1, 2.2, 2.3)

**Lesson 8.1 – PEP Concepts and Python Philosophy**
- **Goal**: Understand PEPs and Python's design philosophy (PEP 20).
- **Content**:
  - PEP: Python Enhancement Proposal.
  - PEP 1: PEP purpose, types (Standards Track, Informational, Process), format.
  - PEP 20: "The Zen of Python" (`import this`).
  - Key principles: readability, simplicity, explicit over implicit, etc.
- **Examples**:
  - Run `import this` and discuss each aphorism.
  - Code examples violating vs following Zen principles.
  - Reading a real PEP (e.g., PEP 8 summary).
- **Edge cases / misconceptions**:
  - PEPs are guidelines, not strict rules (but important for consistency).
  - "There should be one obvious way to do it" vs Python's flexibility.
- **Refactoring / demo**:
  - Refactor code to better align with Zen of Python principles.

**Lesson 8.2 – PEP 8 Guidelines Deep Dive**
- **Goal**: Apply PEP 8 guidelines comprehensively.
- **Content**:
  - Code layout: indentation (4 spaces), continuation lines, max line length (79/99), blank lines.
  - Imports: standard library, third-party, local; alphabetical order; `from import` style.
  - String quotes: prefer double quotes, be consistent.
  - Whitespace: around operators, in function calls, trailing commas.
  - Comments: block comments, inline comments (use sparingly).
  - Naming: `snake_case` for functions/variables, `PascalCase` for classes, `UPPER_CASE` for constants.
  - Programming recommendations: comparisons to `None`, `True`, `False`; exception handling.
- **Examples**:
  - PEP 8 compliant vs non-compliant code examples.
  - Using `black`, `flake8`, `pylint` to check compliance.
- **Edge cases / misconceptions**:
  - Line length: 79 for docstrings/comments, 99 for code (or team standard).
  - Consistency within project may override strict PEP 8 in some cases.
- **Refactoring / demo**:
  - Run linter on existing code and fix all PEP 8 violations.

**Lesson 8.3 – PEP 8 Tooling**
- **Goal**: Use tools to enforce PEP 8 compliance.
- **Content**:
  - `flake8`: style checker.
  - `black`: opinionated formatter (not strictly PEP 8 but widely adopted).
  - `pylint`: comprehensive linter.
  - `autopep8`: automatically fixes PEP 8 issues.
  - IDE integration: VS Code/Cursor settings for auto-formatting.
- **Examples**:
  - Running `flake8` on a file and fixing reported issues.
  - Configuring `black` in `pyproject.toml`.
  - Pre-commit hooks for automatic checking.
- **Edge cases / misconceptions**:
  - Tools may have slightly different interpretations of PEP 8.
  - `black` makes some decisions that differ from PEP 8 (line length, string quotes).
- **Refactoring / demo**:
  - Set up automated PEP 8 checking in a project.

**Lesson 8.4 – PEP 257 Docstrings and Type Hints**
- **Goal**: Write proper docstrings (PEP 257) and use type hints (PEP 484).
- **Content**:
  - PEP 257: docstring conventions.
  - One-line docstrings: `"""Brief description."""`
  - Multi-line docstrings: summary line, blank line, detailed description.
  - Docstring for modules, classes, functions.
  - PEP 484: type hints using `typing` module.
  - Basic types: `int`, `str`, `List[int]`, `Dict[str, int]`, `Optional[str]`, `Union[int, str]`.
  - Function annotations: `def func(x: int) -> str: ...`
- **Examples**:
  - Properly documented class with module, class, and method docstrings.
  - Function with type hints: `def process_data(items: List[Dict[str, Any]]) -> int: ...`
  - Using `mypy` for type checking.
- **Edge cases / misconceptions**:
  - Type hints are optional and don't affect runtime (but tools like `mypy` can check them).
  - Docstrings are accessible via `__doc__` attribute.
  - `typing` module provides generic types for containers.
- **Refactoring / demo**:
  - Add comprehensive docstrings and type hints to an existing module.

---

### Module 9 – GUI Programming with tkinter (PCPP 3.1, 3.2, 3.3)

**Lesson 9.1 – GUI Concepts and Event-Driven Programming**
- **Goal**: Understand GUI concepts and the event-driven programming model.
- **Content**:
  - GUI: Graphical User Interface.
  - Widgets/controls: windows, buttons, labels, entry fields, etc.
  - Event-driven programming: program responds to user events (clicks, key presses).
  - Classical vs event-driven: sequential vs reactive.
  - Event loop: continuously checking for and handling events.
- **Examples**:
  - Compare: CLI program (sequential) vs GUI program (event-driven).
  - Simple event: button click triggers function call.
- **Edge cases / misconceptions**:
  - GUI programs don't "finish" like CLI programs; they run until closed.
  - Blocking operations freeze GUI; need async or threading for long tasks.
- **Refactoring / demo**:
  - Convert a simple CLI program to GUI (conceptual, before tkinter details).

**Lesson 9.2 – tkinter Basics: Windows and Widgets**
- **Goal**: Create a basic tkinter window and add simple widgets.
- **Content**:
  - Importing: `from tkinter import *` or `import tkinter as tk`.
  - Main window: `root = tk.Tk()`, `root.title("Title")`, `root.mainloop()`.
  - Basic widgets: `tk.Label()`, `tk.Button()`, `tk.Entry()`.
  - Adding widgets: `widget.pack()`, `widget.grid()`, `widget.place()`.
  - Widget configuration: `widget.config(text="New text")` or `widget['text'] = "New text"`.
- **Examples**:
  - "Hello World" GUI: window with label and button.
  - Simple form: labels and entry fields.
- **Edge cases / misconceptions**:
  - `mainloop()` blocks; code after it doesn't run until window closes.
  - Widgets must be added to a parent (window or frame).
- **Refactoring / demo**:
  - Build a simple form step-by-step, adding widgets incrementally.

**Lesson 9.3 – Layout Managers: pack, grid, place**
- **Goal**: Use layout managers effectively to arrange widgets.
- **Content**:
  - `pack()`: simple, automatic layout (top-to-bottom or left-to-right).
  - `grid()`: table-like layout with rows and columns.
  - `place()`: absolute positioning with x/y coordinates.
  - When to use: `pack` for simple, `grid` for forms, `place` for precise control (rarely).
- **Examples**:
  - Login form using `grid()`: username label/entry, password label/entry, submit button.
  - Toolbar using `pack(side=tk.LEFT)`.
  - Mixed layout: frame with `pack()`, widgets inside with `grid()`.
- **Edge cases / misconceptions**:
  - Don't mix `pack()` and `grid()` in same parent (use frames).
  - `grid()` rows/columns start at 0; `sticky` parameter for alignment.
- **Refactoring / demo**:
  - Refactor a window using `place()` to use `grid()` for better responsiveness.

**Lesson 9.4 – Event Handlers and Callbacks**
- **Goal**: Connect widgets to functions using event handlers.
- **Content**:
  - Command parameter: `Button(command=callback_function)`.
  - Event binding: `widget.bind('<Event>', handler)`.
  - Common events: `<Button-1>` (left click), `<Key>`, `<Return>`, `<FocusIn>`.
  - Event object: handler receives event object with information.
  - `destroy()`: closing windows programmatically.
- **Examples**:
  - Button that calls function when clicked.
  - Entry field that responds to Enter key press.
  - Window close button handler.
- **Edge cases / misconceptions**:
  - Callback functions should not take arguments (unless using lambda or `functools.partial`).
  - Event binding returns an ID; can unbind with `unbind()`.
- **Refactoring / demo**:
  - Add event handlers to make a static GUI interactive.

**Lesson 9.5 – Advanced Widgets: Canvas, Entry, Radiobutton**
- **Goal**: Use advanced widgets for richer interfaces.
- **Content**:
  - `Canvas`: drawing area for graphics, shapes, images.
  - Canvas methods: `create_rectangle()`, `create_oval()`, `create_line()`, `create_text()`.
  - `Entry`: single-line text input.
  - `Radiobutton`: radio button group (mutually exclusive options).
  - `Checkbutton`: checkbox (multiple selections).
  - `Text`: multi-line text widget.
  - `Listbox`: list of selectable items.
- **Examples**:
  - Drawing app: canvas with shapes drawn on click.
  - Form with radio buttons for options.
  - Text editor using `Text` widget.
- **Edge cases / misconceptions**:
  - Radio buttons need shared `tk.StringVar()` or `tk.IntVar()` for grouping.
  - Canvas coordinates: (0,0) is top-left.
- **Refactoring / demo**:
  - Enhance a simple form with radio buttons and validation.

**Lesson 9.6 – Observable Variables and Advanced Event Handling**
- **Goal**: Use `StringVar`, `IntVar`, etc., and handle complex events.
- **Content**:
  - Observable variables: `tk.StringVar()`, `tk.IntVar()`, `tk.BooleanVar()`.
  - Tracers: `var.trace('w', callback)` to watch for changes.
  - Widget `textvariable` parameter: binding variable to widget.
  - Advanced event handling: mouse movements, keyboard shortcuts, focus events.
- **Examples**:
  - Two entry fields synchronized via `StringVar`.
  - Real-time calculation: entry field updates label via variable tracer.
  - Keyboard shortcuts: `bind('<Control-s>', save_function)`.
- **Edge cases / misconceptions**:
  - Tracer callback receives special arguments: `callback(*args)`.
  - Variables must be kept in scope (store as instance variable, not local).
- **Refactoring / demo**:
  - Refactor a GUI to use observable variables for cleaner data flow.

---

### Module 10 – Network Programming & REST (PCPP 4.1, 4.2, 4.3, 4.4)

**Lesson 10.1 – Network Programming Fundamentals**
- **Goal**: Understand network concepts: sockets, protocols, REST.
- **Content**:
  - Network sockets: endpoints for network communication.
  - Domains, addresses, ports: IP addresses, domain names, port numbers.
  - Protocols: TCP (connection-oriented), UDP (connectionless).
  - REST: Representational State Transfer, HTTP-based API architecture.
  - Clients and servers: request-response model.
- **Examples**:
  - Diagram: client → socket → network → socket → server.
  - REST API example: `GET /users`, `POST /users`, etc.
- **Edge cases / misconceptions**:
  - Ports 0-1023 are well-known (require privileges); use 1024+ for development.
  - REST is an architectural style, not a protocol (HTTP is the protocol).
- **Refactoring / demo**:
  - Compare: direct socket communication vs REST API (conceptual).

**Lesson 10.2 – Socket Programming Basics**
- **Goal**: Create sockets and communicate over networks.
- **Content**:
  - `socket` module: `socket.socket(family, type)`.
  - Socket types: `socket.AF_INET` (IPv4), `socket.SOCK_STREAM` (TCP).
  - Client: `socket.connect((host, port))`, `socket.send(data)`, `socket.recv(size)`.
  - Server: `socket.bind((host, port))`, `socket.listen()`, `socket.accept()`.
  - Closing: `socket.close()`.
- **Examples**:
  - Simple HTTP client: connect to web server, send GET request, receive response.
  - Echo server: receives message, sends it back.
- **Edge cases / misconceptions**:
  - `send()` may not send all data; use loop or `sendall()`.
  - `recv()` blocks until data received; use timeout or non-blocking mode.
  - Always close sockets to free resources.
- **Refactoring / demo**:
  - Build a simple HTTP request manually using sockets.

**Lesson 10.3 – Exception Handling in Network Programming**
- **Goal**: Handle network errors gracefully.
- **Content**:
  - Network exceptions: `socket.error`, `socket.timeout`, `ConnectionRefusedError`, `ConnectionResetError`.
  - Timeouts: `socket.settimeout(seconds)`.
  - Retry logic: handling transient network failures.
  - Context managers: `with socket.socket() as s:` for automatic cleanup.
- **Examples**:
  - Network client with try/except for connection errors.
  - Retry decorator for network operations.
- **Edge cases / misconceptions**:
  - Network operations can fail for many reasons (timeout, connection refused, etc.).
  - Always handle exceptions; don't assume network calls succeed.
- **Refactoring / demo**:
  - Add robust error handling to a socket-based client.

**Lesson 10.4 – JSON Serialization**
- **Goal**: Serialize and deserialize data using JSON.
- **Content**:
  - JSON: JavaScript Object Notation, text-based data format.
  - JSON syntax: objects `{}`, arrays `[]`, strings, numbers, booleans, `null`.
  - `json` module: `json.dumps(obj)` (to string), `json.loads(string)` (from string).
  - `json.dump(obj, file)`, `json.load(file)` for file I/O.
  - Serializing custom objects: default function for non-serializable types.
- **Examples**:
  - Convert Python dict to JSON string and back.
  - Save/load configuration as JSON file.
  - Custom encoder for `datetime` objects.
- **Edge cases / misconceptions**:
  - JSON doesn't support all Python types (use `default` parameter for custom types).
  - JSON strings must use double quotes (not single quotes).
  - `json.loads()` raises `JSONDecodeError` for invalid JSON.
- **Refactoring / demo**:
  - Replace manual string formatting with JSON for data exchange.

**Lesson 10.5 – XML Processing**
- **Goal**: Parse and create XML documents.
- **Content**:
  - XML: eXtensible Markup Language, tree structure.
  - XML syntax: tags, attributes, elements, root element.
  - `xml.etree.ElementTree`: `ET.parse(file)`, `ET.fromstring(string)`.
  - Element methods: `find(tag)`, `findall(tag)`, `get(attr)`, `text`, `iter()`.
  - Creating XML: `ET.Element()`, `ET.SubElement()`, `ET.dump()`.
- **Examples**:
  - Parse XML config file: `root.findall('setting')`.
  - Extract data from XML: `element.text`, `element.get('attribute')`.
  - Build XML document programmatically.
- **Edge cases / misconceptions**:
  - XML is case-sensitive.
  - `find()` returns first match; `findall()` returns list.
  - XML namespaces require special handling.
- **Refactoring / demo**:
  - Convert XML-based config to JSON (or vice versa) for comparison.

**Lesson 10.6 – requests Module Basics**
- **Goal**: Use `requests` library for HTTP communication.
- **Content**:
  - `requests` module: high-level HTTP library.
  - Basic methods: `requests.get(url)`, `requests.post(url, data=...)`, `requests.put()`, `requests.delete()`.
  - Response object: `response.status_code`, `response.text`, `response.json()`, `response.headers`.
  - Parameters: `params={}` for query string, `json={}` for JSON body, `headers={}` for headers.
- **Examples**:
  - Fetch data from REST API: `response = requests.get('https://api.example.com/users')`.
  - POST request with JSON: `requests.post(url, json={'name': 'John'})`.
  - Handle status codes: `if response.status_code == 200: ...`
- **Edge cases / misconceptions**:
  - `requests` raises exceptions for network errors; use try/except.
  - `response.json()` raises error if response isn't valid JSON.
  - Always check `status_code`; 2xx is success, 4xx is client error, 5xx is server error.
- **Refactoring / demo**:
  - Replace manual socket HTTP code with `requests` library.

**Lesson 10.7 – Building a REST Client**
- **Goal**: Design and implement a complete REST client.
- **Content**:
  - REST client design: CRUD operations (Create, Read, Update, Delete).
  - HTTP methods mapping: GET (read), POST (create), PUT (update), DELETE (delete).
  - Error handling: checking status codes, handling errors appropriately.
  - Response parsing: JSON, XML, or text.
  - Testing: using mock servers or test APIs.
- **Examples**:
  - `RESTClient` class with methods: `get_user(id)`, `create_user(data)`, `update_user(id, data)`, `delete_user(id)`.
  - Handling pagination: `GET /users?page=1&limit=10`.
  - Authentication: adding API keys or tokens to headers.
- **Edge cases / misconceptions**:
  - REST is stateless; each request contains all necessary information.
  - Idempotency: PUT and DELETE should be idempotent (safe to retry).
  - Rate limiting: APIs may limit requests per time period.
- **Refactoring / demo**:
  - Build a complete REST client class with error handling and retry logic.

---

### Module 11 – Database & File Processing (PCPP 5.1, 5.2)

**Lesson 11.1 – SQLite Database Basics**
- **Goal**: Connect to SQLite database and perform basic operations.
- **Content**:
  - `sqlite3` module: built-in SQL database.
  - Connection: `sqlite3.connect('database.db')`, `connection.close()`.
  - Cursor: `connection.cursor()`, `cursor.execute(sql)`, `cursor.fetchone()`, `cursor.fetchall()`.
  - Creating tables: `CREATE TABLE` SQL statement.
  - Basic SQL: `SELECT`, `INSERT INTO`, `UPDATE`, `DELETE`.
- **Examples**:
  - Create database and table: `CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)`.
  - Insert data: `INSERT INTO users (name) VALUES (?)`.
  - Query data: `SELECT * FROM users WHERE id = ?`.
- **Edge cases / misconceptions**:
  - Use parameterized queries (`?` placeholders) to prevent SQL injection.
  - `fetchone()` returns one row (tuple or None); `fetchall()` returns list of rows.
  - Always close connections (or use context manager).
- **Refactoring / demo**:
  - Replace file-based storage (CSV/JSON) with SQLite database.

**Lesson 11.2 – CRUD Operations and Transactions**
- **Goal**: Perform complete CRUD operations and manage transactions.
- **Content**:
  - CRUD: Create (INSERT), Read (SELECT), Update (UPDATE), Delete (DELETE).
  - Transactions: `connection.commit()`, `connection.rollback()`.
  - `executemany()`: executing same statement with multiple parameter sets.
  - Context manager: `with sqlite3.connect(...) as conn:` for automatic commit/rollback.
- **Examples**:
  - Complete user management: create, read, update, delete users.
  - Batch insert: `executemany('INSERT INTO users (name) VALUES (?)', names_list)`.
  - Transaction: multiple operations that succeed or fail together.
- **Edge cases / misconceptions**:
  - Changes not saved until `commit()` (or connection closes with autocommit).
  - `executemany()` is more efficient than loop of `execute()`.
  - Transactions ensure data consistency.
- **Refactoring / demo**:
  - Add transaction support to existing database operations.

**Lesson 11.3 – Advanced SQLite: Joins and Aggregations**
- **Goal**: Use SQL features: joins, aggregations, constraints.
- **Content**:
  - Foreign keys: `FOREIGN KEY (user_id) REFERENCES users(id)`.
  - Joins: `INNER JOIN`, `LEFT JOIN`.
  - Aggregations: `COUNT()`, `SUM()`, `AVG()`, `MAX()`, `MIN()`, `GROUP BY`.
  - Constraints: `PRIMARY KEY`, `UNIQUE`, `NOT NULL`, `CHECK`.
- **Examples**:
  - Related tables: `users` and `orders` with foreign key relationship.
  - Query with join: `SELECT users.name, COUNT(orders.id) FROM users LEFT JOIN orders ON users.id = orders.user_id GROUP BY users.id`.
- **Edge cases / misconceptions**:
  - Foreign keys must reference existing rows (or use `ON DELETE CASCADE`).
  - `GROUP BY` groups rows; aggregations compute per group.
- **Refactoring / demo**:
  - Normalize a flat table structure into related tables with joins.

**Lesson 11.4 – CSV Processing**
- **Goal**: Read and write CSV files using `csv` module.
- **Content**:
  - `csv` module: `csv.reader(file)`, `csv.writer(file)`.
  - `csv.DictReader(file)`: reads rows as dictionaries.
  - `csv.DictWriter(file, fieldnames)`: writes rows from dictionaries.
  - Dialects: `csv.excel`, `csv.unix_dialect`, custom dialects.
- **Examples**:
  - Read CSV: `for row in csv.DictReader(file): print(row['name'])`.
  - Write CSV: `writer.writerow(['name', 'age'])`, `writer.writerows(rows)`.
  - Convert CSV to list of dictionaries.
- **Edge cases / misconceptions**:
  - CSV files must be opened with `newline=''` parameter.
  - `DictReader` uses first row as fieldnames (or specify `fieldnames` parameter).
  - Handle missing fields, extra fields, or malformed rows.
- **Refactoring / demo**:
  - Replace manual CSV parsing (split by comma) with `csv` module.

**Lesson 11.5 – Logging Module**
- **Goal**: Use `logging` module for application logging.
- **Content**:
  - Logging levels: `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`.
  - Basic logging: `logging.basicConfig(level=logging.INFO)`.
  - Logging: `logging.debug()`, `logging.info()`, `logging.warning()`, `logging.error()`.
  - LogRecord attributes: `%(asctime)s`, `%(levelname)s`, `%(message)s`, `%(filename)s`, `%(lineno)d`.
  - Format strings: `logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s')`.
- **Examples**:
  - Configure logging to file and console.
  - Different log levels for different modules.
  - Structured logging with context information.
- **Edge cases / misconceptions**:
  - Logging is hierarchical: logger name with dots (e.g., `'app.module'`) creates hierarchy.
  - `basicConfig()` only works if logging not configured yet.
  - Use appropriate level: DEBUG for development, INFO for normal, ERROR for problems.
- **Refactoring / demo**:
  - Replace `print()` statements with proper logging.

**Lesson 11.6 – Custom Handlers and Formatters**
- **Goal**: Create custom logging handlers and formatters.
- **Content**:
  - Handlers: `logging.FileHandler()`, `logging.StreamHandler()`, `logging.RotatingFileHandler()`.
  - Formatters: `logging.Formatter(format_string)`.
  - Custom handler: subclass `logging.Handler`, implement `emit()`.
  - Multiple handlers: logger can have multiple handlers (file + console).
- **Examples**:
  - Rotating file handler: logs rotate when file reaches size limit.
  - Custom formatter: JSON format for log aggregation.
  - Email handler: send critical errors via email (conceptual).
- **Edge cases / misconceptions**:
  - Formatter attached to handler, not logger.
  - Handler level can be different from logger level.
- **Refactoring / demo**:
  - Set up production-ready logging with file rotation and custom formatting.

**Lesson 11.7 – ConfigParser Module**
- **Goal**: Parse and create configuration files using `configparser`.
- **Content**:
  - `configparser` module: `ConfigParser()` object.
  - INI file format: sections `[section]`, options `key = value`.
  - Reading: `config.read('config.ini')`, `config.get(section, key)`, `config.getint()`, `config.getboolean()`.
  - Writing: `config.add_section()`, `config.set()`, `config.write(file)`.
  - Interpolation: `%(variable)s` syntax in values.
- **Examples**:
  - Configuration file: `[database] host = localhost port = 5432`.
  - Reading config: `db_host = config.get('database', 'host')`.
  - Interpolation: `path = %(home)s/data` where `home` is defined in `[DEFAULT]`.
- **Edge cases / misconceptions**:
  - Section names are case-sensitive by default (can use `optionxform`).
  - Interpolation can reference other options in same or DEFAULT section.
  - Use `getboolean()` for true/false values (handles various formats).
- **Refactoring / demo**:
  - Replace hardcoded configuration values with ConfigParser-based config file.

---

### Module 12 – Integration & Capstones (All Sections)

**Lesson 12.1 – Project Planning and Architecture**
- **Goal**: Plan a comprehensive project integrating multiple PCPP topics.
- **Content**:
  - Requirements analysis: identifying features and constraints.
  - Architecture design: separating GUI, business logic, data access layers.
  - Technology choices: tkinter for GUI, sqlite3 for database, requests for APIs.
  - Project structure: organizing modules, packages, tests.
- **Examples**:
  - Capstone project: Personal Finance Manager (GUI + database + optional REST API).
  - Architecture diagram: GUI → Services → Database layers.
- **Edge cases / misconceptions**:
  - Don't put all code in one file; use proper module structure.
  - Plan for testing and error handling from the start.
- **Refactoring / demo**:
  - Design architecture for a capstone project.

**Lesson 12.2 – Integration Patterns**
- **Goal**: Integrate GUI, database, and network components effectively.
- **Content**:
  - MVC pattern: Model (data/database), View (GUI), Controller (logic).
  - Separation of concerns: GUI doesn't directly access database.
  - Error handling across layers: GUI catches and displays user-friendly errors.
  - Threading: long operations (network, database) shouldn't freeze GUI.
- **Examples**:
  - GUI calls service layer, service layer accesses database.
  - Progress indicators for long operations.
- **Edge cases / misconceptions**:
  - tkinter is single-threaded; use `after()` for periodic tasks, threading for blocking operations.
  - Database connections should be managed (connection pooling in larger apps).
- **Refactoring / demo**:
  - Refactor a monolithic GUI app into MVC structure.

**Lesson 12.3 – Testing and Quality Assurance**
- **Goal**: Test integrated applications and ensure quality.
- **Content**:
  - Unit testing: testing individual components (services, database access).
  - Integration testing: testing components together.
  - GUI testing: using `unittest` with tkinter (challenging but possible).
  - Code quality: PEP 8, type hints, docstrings.
- **Examples**:
  - Test database operations independently of GUI.
  - Mock network requests for testing without real API.
- **Edge cases / misconceptions**:
  - GUI testing is harder; focus on testing business logic separately.
  - Use dependency injection to make code testable.
- **Refactoring / demo**:
  - Add unit tests to existing capstone project.

**Lesson 12.4 – Documentation and Deployment**
- **Goal**: Document projects and prepare for deployment.
- **Content**:
  - README: project description, installation, usage, architecture.
  - Code documentation: docstrings, type hints, comments.
  - User documentation: how to use the application.
  - Deployment considerations: packaging, dependencies, distribution.
- **Examples**:
  - Complete README for capstone project.
  - Docstrings for all public classes and functions.
- **Edge cases / misconceptions**:
  - Documentation should be written for users (README) and developers (code docs).
  - Consider cross-platform compatibility (Windows, macOS, Linux).
- **Refactoring / demo**:
  - Create comprehensive documentation for a capstone project.

---

This completes the detailed lesson-level content for all 12 modules, covering every PCPP-32-101 objective (1.1–5.2) with practical examples, edge cases, and refactoring demonstrations.
