# Workbook inventory

Generated from the `.twb` by `scripts/build_docs.py`.

## Dashboards

The workbook contains 10 dashboards, but `Dashboard 1` to `Dashboard 5` use exactly the same worksheets as `Category`, `Sales`, `Efforts`, `Channel Effectiveness` and `Channel Mix`. They look like leftovers from before the dashboards were renamed; deleting them in Tableau would lose nothing, since the named copies hold the same sheets.

| Dashboard | Duplicate | Worksheets | What it shows |
|---|---|---|---|
| **Category** | `Dashboard 1` | Sheet 1, Sheet 2 | How many doctors sit in each category, over time (pie + bar by day/month/quarter) |
| **Sales** | `Dashboard 2` | Sheet 4, Sheet 5 | Sales by category, doctor and month |
| **Efforts** | `Dashboard 3` | Sheet 6, Sheet 7 | Engagement effort (CLM duration, educational-material interactions) split by Positive/Negative response |
| **Channel Effectiveness** | `Dashboard 4` | Sheet 8, Sheet 9 | Average CLM duration and the RTE email/webinar/price-variation counts |
| **Channel Mix** | `Dashboard 5` | Sheet 10, Sheet 11, Sheet 12, Sheet 13, Sheet 14 | Time spent per channel (virtual call, webinar, website, meeting) by day, plus averages and email/webinar rates |

## Worksheets

| Worksheet | Mark type | Measures and dimensions (beside Category and Doctor Name) |
|---|---|---|
| Sheet 1 | Pie | `Date`, `SUM(Count of Doctors)` |
| Sheet 2 | Bar | `Date`, `SUM(Count of Doctors)` |
| Sheet 4 | Pie | `Date`, `SUM(Calculation_1273392822305742850)`, `SUM(Sale)` |
| Sheet 5 | Automatic | `Date`, `SUM(Sale)` |
| Sheet 6 | Automatic | `Date`, `Positive/Negative1`, `SUM(CLM Duration)` |
| Sheet 7 | Automatic | `Date`, `Positive/Negative1`, `SUM(RTE Educational Material)` |
| Sheet 8 | Bar | `Date`, `Positive/Negative1`, `SUM(Avergae CLM Duration)`, `SUM(CLM Duration)` |
| Sheet 9 | Automatic | `Date`, `SUM(RTE Educational Material)`, `SUM(RTE Price variation)`, `SUM(RTE Webinar)`, `SUM(Total Emails)` |
| Sheet 10 | Automatic | `Date`, `SUM(Virtual Call Duration(secs))` |
| Sheet 11 | Automatic | `Date`, `SUM(Webinar Duration(secs))` |
| Sheet 12 | Automatic | `Date`, `SUM(Website Duration(secs))` |
| Sheet 13 | Automatic | `Date`, `SUM(Meeting Duration(secs))` |
| Sheet 14 | Automatic | `AVG(Meeting Duration(secs))`, `AVG(Virtual Call Duration(secs))`, `AVG(Webinar Duration(secs))`, `AVG(Website Duration(secs))`, `Date`, `SUM(Email Open Rate)`, `SUM(Webinar Attend rate)` |

## Calculated fields

Only one: `Zero = 0` (used in `Sheet 4`).
