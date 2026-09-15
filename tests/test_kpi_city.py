from src.kpi_city import city_kpi


def test_city_kpi_returns_mumbai_metrics():
    result = city_kpi("Mumbai")

    assert result["customer_count"] == 3
    assert result["total_monthly_spend"] == 13300.5
    assert result["churn_rate"] == 1 / 3


def test_city_kpi_does_not_allow_sql_injection():
    result = city_kpi("Mumbai' OR 1=1 --")

    assert result["customer_count"] == 0
    assert result["total_monthly_spend"] == 0