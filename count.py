from pathlib import Path

FOLDER = "dataset-28"

count = sum(1 for f in Path(FOLDER).rglob("*") if f.is_file())
print(count)
