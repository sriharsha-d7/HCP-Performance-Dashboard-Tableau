"""Generate docs/workbook_inventory.md from the .twb so the documentation cannot drift from the workbook."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import workbook as wb  # noqa: E402

DOCS = Path(__file__).resolve().parents[1] / "docs"
PURPOSE = {
    "Category": "How many doctors sit in each category, over time (pie + bar by day/month/quarter)",
    "Sales": "Sales by category, doctor and month",
    "Efforts": "Engagement effort (CLM duration, educational-material interactions) split by Positive/Negative response",
    "Channel Effectiveness": "Average CLM duration and the RTE email/webinar/price-variation counts",
    "Channel Mix": "Time spent per channel (virtual call, webinar, website, meeting) by day, plus averages and email/webinar rates",
}


def main() -> None:
    r = wb.root()
    ws, db = wb.worksheets(r), wb.dashboards(r)
    lines = ["# Workbook inventory", "", "Generated from the `.twb` by `scripts/build_docs.py`.", "",
             "## Dashboards", "", "The workbook contains 10 dashboards, but `Dashboard 1` to `Dashboard 5` use exactly the same worksheets as "
             "`Category`, `Sales`, `Efforts`, `Channel Effectiveness` and `Channel Mix`. They look like leftovers from before the "
             "dashboards were renamed; deleting them in Tableau would lose nothing, since the named copies hold the same sheets.", "",
             "| Dashboard | Duplicate | Worksheets | What it shows |", "|---|---|---|---|"]
    inv = {v: k for k, v in wb.DUPLICATE_OF.items()}
    for name in PURPOSE:
        lines.append(f"| **{name}** | `{inv[name]}` | {', '.join(sorted(db[name], key=lambda x: int(x.split()[1])))} | {PURPOSE[name]} |")
    lines += ["", "## Worksheets", "", "| Worksheet | Mark type | Measures and dimensions (beside Category and Doctor Name) |", "|---|---|---|"]
    for name in sorted(ws, key=lambda x: int(x.split()[1])):
        lines.append(f"| {name} | {', '.join(ws[name]['marks'])} | {', '.join(f'`{f}`' for f in ws[name]['fields'])} |")
    lines += ["", "## Calculated fields", "", "Only one: `Zero = 0` (used in `Sheet 4`).", ""]
    (DOCS / "workbook_inventory.md").write_text("\n".join(lines))
    print("docs regenerated")


if __name__ == "__main__":
    main()
