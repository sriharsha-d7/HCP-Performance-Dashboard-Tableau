# Data

Put the source CSV here as `Sheet1 (Pfizer (1))_Sheet1.csv` (the file name the workbook expects), then in Tableau choose
*Data > Edit Data Source > Edit Connection* and point to it. Validate it first:

```bash
python scripts/check_data.py "data/Sheet1 (Pfizer (1))_Sheet1.csv"
```

CSV files in this folder are git-ignored on purpose; do not commit real healthcare-professional data.
