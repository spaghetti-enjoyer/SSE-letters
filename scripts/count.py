from pathlib import Path

SMALL = "dataset-28"
BIG = "dataset-64"

def get_count(folder):
    return sum(1 for f in Path(folder).rglob("*") if f.is_file())

print(f"images in the 28x28 dataset: {get_count(SMALL)}\nimages in the 64x64 dataset: {get_count(BIG)}")
