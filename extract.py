import pandas as pd
from pathlib import Path

DATA_DIR = Path("data/mot_test_results_2025")

FILES = sorted(DATA_DIR.glob("mot_2025_*.csv"))

def extract(*file_paths):

    for file_path in file_paths:

        print(f"Reading {file_path}")

        chunks = pd.read_csv(
            file_path, 
            chunksize=100_000,
            on_bad_lines="warn"
            )

        for chunk in chunks:
            yield chunk

if __name__ == "__main__":
    chunk_count = 0
    row_count = 0

    for chunk in extract(*FILES):
        chunk_count += 1
        row_count += len(chunk)

    print(f"Processed {chunk_count} chunks")
    print(f"Processed {row_count} rows")

