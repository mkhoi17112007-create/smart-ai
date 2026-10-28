import json
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open(r'c:\HOC_HANH\Mon dang hoc\ITA201\smartedu-ai\notebooks\smartedu_assignment.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

for idx in range(7, 16):
    cell = nb['cells'][idx]
    print(f"=== CELL {idx} ({cell.get('cell_type')}) ===")
    print(''.join(cell.get('source', [])))
    print("="*60)
