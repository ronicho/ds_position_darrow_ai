import json
from pathlib import Path

def strip_jet(obj):
    if isinstance(obj, dict):
        obj.pop("jetTransient", None)
        for v in obj.values():
            strip_jet(v)
    elif isinstance(obj, list):
        for v in obj:
            strip_jet(v)

for path in Path(".").rglob("*.ipynb"):
    print(f"Cleaning {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    strip_jet(data)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
