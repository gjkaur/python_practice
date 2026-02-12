## M02 – User-Defined Modules and Packages

**PCAP Alignment**: Section 1 (1.5) – Create and use user-defined modules and packages.  
**Professional Focus**: Package layout, public API, `__init__.py`, naming.

---

### 1. Outcomes

By the end of this module you will:

- Create a **module** (single `.py` file) and import it.
- Create a **package** (directory with `__init__.py`) and import from it.
- Explain the role of `__pycache__` and bytecode.
- Use `__name__` for dual use (script vs import).
- Distinguish **public** vs **private** variables (e.g. `_private` convention).
- Use and write `__init__.py` (empty or with exports).
- Understand **searching for/through** modules and packages.
- Contrast **nested packages** with plain directory trees (packages are importable).

---

### 2. Core Concepts (PCAP 1.5)

#### 2.1 Idea and rationale

- Modules: reuse and organization; packages: grouping related modules.
- Rationale: maintainability, namespace separation, testability.

#### 2.2 __pycache__

- Python compiles `.py` to bytecode (`.pyc`) in `__pycache__/` for faster loading.

#### 2.3 __name__

- When run as script: `__name__ == "__main__"`. When imported: `__name__` is the module name. Use for `if __name__ == "__main__":` test blocks.

#### 2.4 Public and private variables

- Convention: names starting with `_` are “private” (not exported by `from mod import *` if `__all__` is used).
- No true privacy; name mangling for class attributes with `__` (covered in OOP).

#### 2.5 __init__.py

- Marks directory as package. Can be empty or run init code; often used to re-export public API (`from .submod import foo`).

#### 2.6 Searching for/through modules and packages

- Import system searches `sys.path`; packages are found by presence of `__init__.py` (or namespace packages in Python 3).

#### 2.7 Nested packages vs directory trees

- Nested package: `pkg/subpkg/` with `__init__.py` in each; import with `from pkg.subpkg import mod`.
- A directory without `__init__.py` is not a package (just a folder).

---

### 2.8 Edge Cases and Production Notes

- **Circular imports**: Module A imports B, B imports A → can fail at load. Resolve by moving shared code to a third module or deferring import inside a function.
- **__all__**: List of names to export when `from mod import *` is used; without it, all names not starting with _ are exported.
- **Run as script vs import**: Use `if __name__ == "__main__":` for code that should run only when the file is executed, not when imported.

---

### 3. Exercises (10+)

1. Create a file `mymath.py` with a function `double(x)`; import it and call `double(5)`.
2. Create package `mypkg` with `__init__.py` that defines `VERSION = "1.0"`; import and print `mypkg.VERSION`.
3. In a module, print `__name__` when run as script and when imported.
4. Add `__all__ = ["public_func"]` to a module and define `public_func` and `_private_helper`; try `from mod import *` and confirm only `public_func` appears.
5. Create nested package `outer.inner` with one function in `inner`; import from another script.
6. Explain what appears in `__pycache__` after importing your module.
7. In `__init__.py`, re-export a function from a submodule so users can `from pkg import foo`.
8. Add a `if __name__ == "__main__":` block that runs a quick test.
9. Simulate “searching through” a package by listing names with `dir(pkg)`.
10. Create a directory without `__init__.py` and show that it cannot be imported as a package.

---

### 4. Mini-Project – Small Package with Public API

#### 4.1 Problem Statement

Build a small package with at least two submodules and a clear **public API** exposed via **__init__.py**. Use **__name__** for script vs import and optional **__all__** to control exports.

#### 4.2 Requirements

- One top-level package directory with **__init__.py** (and optionally **__all__**).
- At least two .py modules inside the package (e.g. utils.py, core.py).
- **__init__.py** re-exports at least two public names so **from pkg import foo, bar** works.
- At least one module has **if __name__ == "__main__":** with a short test or demo.
- No circular imports; use **_private** for internal helpers where appropriate.

#### 4.3 Suggested Folder Structure

```text
mp02_small_package/
  mypkg/
    __init__.py   # re-export public API
    utils.py
    core.py
  main.py         # from mypkg import ...; demo
  README.md
```

#### 4.4 Acceptance Tests (High-Level)

- **from mypkg import ...** works for the re-exported names.
- Running the package (or a submodule) as script runs only the **__main__** block.
- **dir(mypkg)** shows the intended public API.

---

### 5. Code Review Checklist

- [ ] Package has `__init__.py`; public API is clear.
- [ ] No circular imports; `__name__` used correctly for script vs import.
- [ ] Private names use `_` convention where appropriate.

---

### 6. Interview-Style Questions

1. What is the purpose of `__init__.py`?
2. When is `__name__` equal to `"__main__"`?
3. What is stored in `__pycache__`?
4. How do you define a “private” name in a module (convention)?
5. What is the difference between a package and a directory that just contains `.py` files?
6. How would you re-export symbols from a submodule in `__init__.py`?
7. What is `__all__` and when is it used?
8. Explain nested packages with an example import.
