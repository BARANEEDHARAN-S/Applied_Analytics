from pathlib import Path
import sqlite3


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DB_PATH = PROJECT_ROOT / "data" / "db" / "analytics.db"


def city_kpi(city: str) -> dict[str, float | int | str]:
    """Return customer KPIs for exactly one city."""
    query = """
        SELECT
            city,
            COUNT(*) AS customer_count,
            COALESCE(SUM(monthly_spend), 0) AS total_monthly_spend,
            COALESCE(AVG(monthly_spend), 0) AS average_monthly_spend,
            COALESCE(AVG(churned), 0) AS churn_rate
        FROM customers_raw
        WHERE city = ?
        GROUP BY city
    """

    with sqlite3.connect(DB_PATH) as connection:
        row = connection.execute(query, (city,)).fetchone()

    if row is None:
        return {
            "city": city,
            "customer_count": 0,
            "total_monthly_spend": 0,
            "average_monthly_spend": 0,
            "churn_rate": 0,
        }

    return {
        "city": row[0],
        "customer_count": row[1],
        "total_monthly_spend": row[2],
        "average_monthly_spend": row[3],
        "churn_rate": row[4],
    }


if __name__ == "__main__":
    print(city_kpi("Mumbai"))
    print(city_kpi("Mumbai' OR 1=1 --"))