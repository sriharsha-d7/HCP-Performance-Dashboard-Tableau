"""Parse the Tableau workbook (.twb is XML): worksheets, dashboards, fields, expected data schema."""
from __future__ import annotations

import xml.etree.ElementTree as ET
from pathlib import Path

TWB = Path(__file__).resolve().parents[1] / "HCP PERFORMANCE DASHBOARD.twb"
DERIVATIONS = {"Sum": "SUM", "Avg": "AVG", "Month": "MONTH", "Day": "DAY", "Day-Trunc": "DAY", "Quarter": "QUARTER", "None": ""}
DUPLICATE_OF = {"Dashboard 1": "Category", "Dashboard 2": "Sales", "Dashboard 3": "Efforts",
                "Dashboard 4": "Channel Effectiveness", "Dashboard 5": "Channel Mix"}


def root(path: Path = TWB) -> ET.Element:
    return ET.parse(path).getroot()


def schema(r: ET.Element) -> dict[str, str]:
    """Expected CSV columns -> Tableau type, from the data source's metadata records."""
    out = {}
    for m in r.iter("metadata-record"):
        if m.get("class") == "column":
            name = m.findtext("remote-name")
            if name and name not in out and not name.startswith("avg("):
                out[name] = m.findtext("local-type")
    return out


def worksheets(r: ET.Element) -> dict[str, dict]:
    out = {}
    for w in r.find("worksheets"):
        fields, seen = [], set()
        for ci in w.iter("column-instance"):
            col = ci.get("column").strip("[]")
            d = DERIVATIONS.get(ci.get("derivation"), ci.get("derivation"))
            label = f"{d}({col})" if d in ("SUM", "AVG") else col
            if col not in ("Doctor Name", "Category") and label not in seen:
                seen.add(label)
                fields.append(label)
        marks = sorted({m.get("class") for m in w.iter("mark")})
        out[w.get("name")] = {"marks": marks, "fields": fields}
    return out


def dashboards(r: ET.Element) -> dict[str, list[str]]:
    out = {}
    for d in r.find("dashboards"):
        sheets = []
        for z in d.iter("zone"):
            n = z.get("name")
            if n and not z.get("type-v2") and n not in sheets:
                sheets.append(n)
        out[d.get("name")] = sheets
    return out
