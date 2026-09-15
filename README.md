# Applied Analytics Mini Project

## Run commands

```powershell
python -m pip install -r requirements.txt
python src/etl_load_sqlite.py
python src/kpi_city.py
python -m pytest
```

## Files

- `data/raw/customers_raw.csv`: Sample customer data.
- `data/db/analytics.db`: SQLite database created by the ETL script.
- `src/etl_load_sqlite.py`: Loads the CSV into the SQLite table.
- `src/kpi_city.py`: Calculates city KPIs with parameterized SQL.
- `tests/test_kpi_city.py`: Tests normal lookup and injection protection.
- `requirements.txt`: Lists pandas and pytest.