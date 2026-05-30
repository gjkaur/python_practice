"""Export HTML previews for concept notebooks (viewable on GitHub)."""
from __future__ import annotations

from pathlib import Path

import nbformat
from nbconvert import HTMLExporter

ROOT = Path(__file__).resolve().parents[1]
BANNER = """\
<div style="background:#fff3cd;border:1px solid #ffc107;border-radius:6px;padding:12px 16px;margin-bottom:20px;font-family:sans-serif;">
  <strong>GitHub .ipynb preview unavailable?</strong>
  Open the <code>.ipynb</code> in Jupyter/VS Code, or use
  <a href="https://nbviewer.org/github/gjkaur/python_practice/blob/main/{repo_path}">NBViewer</a>.
</div>
"""


def export_notebook(ipynb: Path) -> Path:
    nb = nbformat.read(ipynb.open(encoding="utf-8"), as_version=4)
    exporter = HTMLExporter()
    exporter.template_name = "classic"
    html, _ = exporter.from_notebook_node(nb)

    repo_path = ipynb.relative_to(ROOT).as_posix()
    html = BANNER.format(repo_path=repo_path) + html

    out = ipynb.with_suffix(".preview.html")
    out.write_text(html, encoding="utf-8", newline="\n")
    return out


def main() -> None:
    paths = sorted(ROOT.glob("python-level-*-course/modules/*/*_Concepts.ipynb"))
    for ipynb in paths:
        out = export_notebook(ipynb)
        print(f"exported: {out.relative_to(ROOT)}")
    print(f"Done. Exported {len(paths)} HTML previews.")


if __name__ == "__main__":
    main()
