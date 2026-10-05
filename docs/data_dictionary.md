# Data dictionary

The workbook reads one CSV, `Sheet1 (Pfizer (1))_Sheet1.csv`, which is **not included in this repository**. The columns, types
and values below come from the workbook's own metadata; check any replacement file with
`python scripts/check_data.py path/to/file.csv`.

The "Pfizer" in the file name is the only place that name appears; nothing in the workbook says whether the records are real,
so treat the data as a sample.

| Column | Type | Used in views | Notes |
|---|---|---|---|
| `ID`, `S N` | integer | no | Row identifiers |
| `Date` | date | all | Engagement date; views aggregate by day, month or quarter |
| `Doctor Name` | string | all | The healthcare professional (HCP) |
| `Brand Name` | string | no | |
| `Category` | string | all | Values seen in the workbook: Platinum, Gold, Silver, Bronze, Others |
| `Positive/Negative1` | string | Efforts, Channel Effectiveness | Values: Positive, Negative (response) |
| `Sale` | integer | Sales | |
| `Average Sales` | real | no | |
| `Count of Doctors`, `Count Variance` | integer | `Count of Doctors` | |
| `CLM Duration`, `Avergae CLM Duration` | integer, real | Efforts, Channel Effectiveness | CLM = closed-loop marketing presentation time. The second column name is misspelled in the source |
| `Meeting Duration(secs)`, `Virtual Call Duration(secs)`, `Webinar Duration(secs)`, `Website Duration(secs)` | integer | Channel Mix | Seconds per channel |
| `Email Open Rate`, `Email Click Rate`, `Educational Material Open Rate`, `Price Variation open rate`, `Webinar Attend rate` | integer / real | `Email Open Rate`, `Webinar Attend rate` | See "Questions to settle" below |
| `RTE Educational Material`, `RTE Price variation`, `RTE Webinar` | integer | Efforts, Channel Effectiveness | Counts; the workbook does not define "RTE" |
| `Total Emails`, `SMS` | integer | `Total Emails` | |
| `Email Clicked`, `Email Response`, `SMS OPEN/Unattended`, `Website Click` | string | no | Categorical engagement flags |

## Questions to settle before trusting the numbers

1. **Rates are summed.** `Channel Mix` (Sheet 14) shows `SUM(Email Open Rate)` and `SUM(Webinar Attend rate)`. These are stored as
   integers; if they are per-row percentages the sum is meaningless, and if they are 0/1 flags it is a count, not a rate.
2. **An average is summed.** `Channel Effectiveness` (Sheet 8) plots `SUM(Avergae CLM Duration)`. Summing a precomputed average
   across doctors and months overstates it; `AVG()` or a ratio of totals is the right aggregation.
3. `avg(0)` appears in the data source metadata as a stray field and is not used.
