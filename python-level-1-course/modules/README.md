# Module Materials – Notebooks and Code

Each module folder contains:

- **Concept building (Jupyter)**
  - `M0x_Concepts.ipynb` – Markdown cells for headings, explanations, and syntax; code cells for runnable examples. Use for learning and teaching.
  - `M0x_Concepts.preview.html` – Static HTML preview (use this on GitHub if the `.ipynb` preview shows "An error occurred").

- **Example programs (.py)**
  - `examples/*.py` – Small, runnable scripts that illustrate the module’s ideas. Run from the module folder or adjust paths as needed.

- **Practice (.py)**
  - `practice/practice_0x_*.py` – Skeleton or guided tasks for hands-on practice. Fill in the TODOs and run to check your work.

## Layout

```
modules/
  M01_Foundations_and_Tooling/
    M01_Concepts.ipynb
    examples/
      hello_script.py
      lexis_syntax_demo.py
    practice/
      practice_01_env_and_syntax.py
  M02_Data_Types_and_Operators/
    M02_Concepts.ipynb
    examples/
    practice/
  ... (M03 through M08 same pattern)
```

## How to use

1. **Concepts**: Open the module’s `M0x_Concepts.ipynb` in Jupyter or VS Code and run the cells. On GitHub, click `M0x_Concepts.preview.html` instead if the notebook preview fails.
2. **Examples**: Run `python examples/<file>.py` from the module directory.
3. **Practice**: Edit `practice/practice_0x_*.py`, implement the requested logic, then run the file.

All content is aligned with the PCEP-30-02 syllabus and the course’s job-focused, production-oriented goals.
