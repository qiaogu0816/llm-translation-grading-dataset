import json
from collections import Counter
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "data" / "正式数据集.jsonl"
rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]

print("样本数:", len(rows))
print("方向:", Counter(r["language_direction"]["source_language"] + "-" + r["language_direction"]["target_language"] for r in rows))
print("等级:", Counter(r["error_severity"] for r in rows))
print("一级类型:", Counter(r["error_type"]["level_1"] for r in rows))
print("二级类型:", Counter(r["error_type"]["level_2"] for r in rows))
