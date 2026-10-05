"""Validate a CSV against the schema the workbook expects.  Usage: python scripts/check_data.py path/to/data.csv"""
from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).parent))
import workbook  # noqa: E402

KIND = {"string": "object", "integer": "int", "real": "float", "date": "date"}


def check(df: pd.DataFrame, expected: dict[str, str]) -> list[str]:
    problems = [f"missing column: {c}" for c in expected if c not in df]
    for col, typ in expected.items():
        if col not in df:
            continue
        s = df[col]
        if typ == "integer" and not pd.api.types.is_numeric_dtype(s):
            problems.append(f"{col}: expected integer, got {s.dtype}")
        elif typ == "real" and not pd.api.types.is_numeric_dtype(s):
            problems.append(f"{col}: expected number, got {s.dtype}")
        elif typ == "date" and pd.to_datetime(s, errors="coerce").isna().any():
            problems.append(f"{col}: contains values that are not dates")
    if "Date" in df and not df["Date"].isna().all():
        pass
    return problems


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(__doc__)
        return 2
    expected = workbook.schema(workbook.root())
    df = pd.read_csv(argv[1])
    problems = check(df, expected)
    extra = [c for c in df if c not in expected]
    print(f"{len(df):,} rows, {len(df.columns)} columns; workbook expects {len(expected)}")
    if extra:
        print("columns not used by the workbook:", ", ".join(extra))
    for p in problems:
        print("PROBLEM:", p)
    print("OK: schema matches" if not problems else f"{len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
