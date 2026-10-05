# HCP Performance Dashboard (Tableau)

[![CI](https://github.com/sriharsha-d7/hcp-performance-dashboard-tableau/actions/workflows/ci.yml/badge.svg)](https://github.com/sriharsha-d7/hcp-performance-dashboard-tableau/actions/workflows/ci.yml)

A Tableau workbook that analyses engagement with healthcare professionals (HCPs) across channels. Five dashboards, 13 worksheets
and **14 measures** answer: who are the doctors by category, what do they buy, how much effort goes into each, and which
channel works.

[`HCP PERFORMANCE DASHBOARD.twb`](HCP%20PERFORMANCE%20DASHBOARD.twb)

## Dashboards

| Dashboard | Question it answers | Measures |
|---|---|---|
| **Category** | How are doctors distributed across categories (Platinum, Gold, Silver, Bronze, Others), over time? | Count of doctors |
| **Sales** | Which categories and doctors drive sales? | Sale |
| **Efforts** | How much closed-loop-marketing (CLM) effort and educational-material engagement goes to positive vs negative responders? | CLM duration, RTE educational material |
| **Channel Effectiveness** | Which engagement types (educational material, price variation, webinar, email) and how long are CLM sessions? | Average CLM duration, RTE educational / price variation / webinar, total emails |
| **Channel Mix** | How is time split across virtual calls, webinars, website visits and meetings? | Virtual call, webinar, website, meeting duration; email open rate; webinar attend rate |

Every worksheet, mark type and field per dashboard is listed in [`docs/workbook_inventory.md`](docs/workbook_inventory.md), and the
columns the workbook expects in [`docs/data_dictionary.md`](docs/data_dictionary.md). Both are generated from or checked against
the workbook, so they cannot drift.

## Before you open it: the data file is not in this repository

The workbook reads a CSV from the author's `Downloads` folder through a Tableau extract kept in a temp folder, and neither file
was committed. On another machine Tableau will ask you to locate the data source. See [`data/README.md`](data/README.md) for how to
reconnect, and validate a file against the workbook's expected schema with `python scripts/check_data.py <file.csv>`.

## Checks

```bash
pip install -r requirements.txt
pytest                          # 6 tests: workbook structure, field/schema consistency, schema checker
python scripts/build_docs.py    # regenerate docs/workbook_inventory.md
```

CI runs both on every push.

## Findings from reviewing the workbook

- **Five duplicate dashboards.** `Dashboard 1` to `Dashboard 5` use the same worksheets as `Category`, `Sales`, `Efforts`,
  `Channel Effectiveness` and `Channel Mix` and can be deleted.
- **Aggregation to check:** Sheet 8 sums a precomputed average (`SUM(Avergae CLM Duration)`), and Sheet 14 sums two "rate"
  fields. Details and what to verify are in the data dictionary.
- **Naming:** worksheets are `Sheet 1` to `Sheet 14` (no `Sheet 3`), and the data has the misspelled field `Avergae CLM Duration`.

## Limitations

- No screenshots are included: the workbook can't be rendered without Tableau and its data. Adding a PNG of each dashboard under
  `docs/` is the highest-value next step for this repository.
- The data's source and provenance are not documented in the workbook; "Pfizer" appears only in the CSV's file name, so this
  README treats the data as a sample and makes no claims about real-world results.
- The workbook file itself is unchanged, since edits to Tableau XML cannot be verified without Tableau.
