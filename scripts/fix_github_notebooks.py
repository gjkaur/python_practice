"""Normalize concept notebooks for reliable GitHub rendering."""
from __future__ import annotations

from pathlib import Path

import nbformat
from nbformat.validator import normalize

ROOT = Path(__file__).resolve().parents[1]

DEFAULT_KERNELSPEC = {
    "display_name": "Python 3",
    "language": "python",
    "name": "python3",
}

DEFAULT_LANGUAGE_INFO = {
    "name": "python",
    "version": "3.11.0",
    "pygments_lexer": "ipython3",
    "codemirror_mode": {"name": "ipython", "version": 3},
    "file_extension": ".py",
    "mimetype": "text/x-python",
    "nbconvert_exporter": "python",
}


def fix_notebook(path: Path) -> None:
    with path.open(encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)

    nb.metadata.pop("widgets", None)
    nb.metadata.setdefault("kernelspec", DEFAULT_KERNELSPEC.copy())
    if not nb.metadata.get("language_info"):
        nb.metadata["language_info"] = DEFAULT_LANGUAGE_INFO.copy()

    for cell in nb.cells:
        if cell.cell_type == "code":
            cell.execution_count = None
            cell.outputs = []

    normalize(nb)

    with path.open("w", encoding="utf-8", newline="\n") as f:
        nbformat.write(nb, f)


def main() -> None:
    paths = sorted(ROOT.glob("python-level-*-course/modules/*/*_Concepts.ipynb"))
    for path in paths:
        fix_notebook(path)
        print(f"fixed: {path.relative_to(ROOT)}")
    print(f"Done. Normalized {len(paths)} notebooks.")


if __name__ == "__main__":
    main()
