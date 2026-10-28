import json
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

nb_path = r"c:\HOC_HANH\Mon dang hoc\ITA201\smartedu-ai\notebooks\smartedu_assignment.ipynb"
with open(nb_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

print(f"Total cells: {len(nb['cells'])}")
for i, c in enumerate(nb['cells']):
    src = c['source'][0].strip() if c['source'] else 'empty'
    print(f"{i:02d} [{c['cell_type']}]: {src[:70]}")
