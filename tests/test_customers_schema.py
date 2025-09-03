import pandas as pd


def assert_string_column(series):
    assert pd.api.types.is_object_dtype(series) or pd.api.types.is_string_dtype(
        series
    ), f"Column {series.name} is not string-like (got {series.dtype})"


def test_customers_schema_and_types():
    df = pd.read_csv("out/clean_customers.csv")

    expected_columns = {
        "customer_id": "object",
        "location_city": "object",
        "location_state": "object",
    }

    for col in expected_columns:
        assert col in df.columns, f"Missing column: {col}"

    assert pd.api.types.is_string_dtype(df["customer_id"])
    assert pd.api.types.is_string_dtype(df["location_city"])
    assert pd.api.types.is_string_dtype(df["location_state"])

    assert df["customer_id"].notna().all()
