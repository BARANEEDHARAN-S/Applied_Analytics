from pathlib import Path
import sqlite3

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = PROJECT_ROOT / "data" / "raw" / "customers_raw.csv"
DB_PATH = PROJECT_ROOT / "data" / "db" / "analytics.db"


def load_csv_to_sqlite() -> None:
    """Load the raw customer CSV into the SQLite database."""
    customers = pd.read_csv(CSV_PATH)
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(DB_PATH) as connection:
        customers.to_sql("customers_raw", connection, if_exists="replace", index=False)

    print(f"Loaded {len(customers)} rows into {DB_PATH}")


if __name__ == "__main__":
    load_csv_to_sqlite()