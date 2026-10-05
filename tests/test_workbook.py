import sys
from pathlib import Path

import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import check_data  # noqa: E402
import workbook as wb  # noqa: E402


@pytest.fixture(scope="module")
def r():
    return wb.root()


def test_workbook_is_well_formed_and_has_expected_size(r):
    ws, db = wb.worksheets(r), wb.dashboards(r)
    assert len(ws) == 13 and len(db) == 10


def test_every_dashboard_only_uses_existing_worksheets(r):
    ws = wb.worksheets(r)
    for name, sheets in wb.dashboards(r).items():
        assert sheets, name
        assert set(sheets) <= set(ws), name


def test_numbered_dashboards_duplicate_the_named_ones(r):
    db = wb.dashboards(r)
    for dup, original in wb.DUPLICATE_OF.items():
        assert set(db[dup]) == set(db[original]), (dup, original)


def test_every_field_used_in_a_view_exists_in_the_data_schema(r):
    schema = wb.schema(r)
    import re

    used = {re.sub(r"^(SUM|AVG)\((.*)\)$", r"\2", f) for v in wb.worksheets(r).values() for f in v["fields"]}
    calc = {"Calculation_1273392822305742850"}  # the 'Zero' calculated field
    assert used - calc <= set(schema), used - calc - set(schema)


def test_schema_has_expected_columns(r):
    s = wb.schema(r)
    assert len(s) == 31 and s["Date"] == "date" and s["Sale"] == "integer"


def test_schema_checker_accepts_valid_and_rejects_broken_data(r):
    expected = wb.schema(r)
    good = pd.DataFrame({c: ("2024-01-01" if t == "date" else (1.5 if t == "real" else (1 if t == "integer" else "x")))
                         for c, t in expected.items()}, index=[0])
    assert check_data.check(good, expected) == []
    bad = good.drop(columns=["Sale"]).assign(**{"Email Open Rate": "n/a", "Date": "not a date"})
    problems = check_data.check(bad, expected)
    assert any("Sale" in p for p in problems) and any("Email Open Rate" in p for p in problems) and any("Date" in p for p in problems)
