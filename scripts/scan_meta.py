import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
for p in sorted(ROOT.glob("python-level-*-course/modules/*/*_Concepts.ipynb")):
    nb = json.loads(p.read_text(encoding="utf-8"))
    meta = nb.get("metadata", {})
    issues = []
    if "kernelspec" not in meta:
        issues.append("no kernelspec")
    if "language_info" not in meta:
        issues.append("no language_info")
    if nb.get("nbformat") != 4:
        issues.append("nbformat=" + str(nb.get("nbformat")))
    for i, c in enumerate(nb["cells"]):
        if c["cell_type"] == "code" and "execution_count" not in c:
            issues.append(f"cell{i} no execution_count")
        src = c.get("source", [])
        if isinstance(src, list) and len(src) == 0:
            issues.append(f"cell{i} empty source")
        if c["cell_type"] == "code" and "outputs" not in c:
            issues.append(f"cell{i} no outputs")
    if issues:
        print(p.relative_to(ROOT), issues)
print("scan complete")
