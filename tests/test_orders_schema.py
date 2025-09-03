import pandas as pd

def assert_string_column(series):
    assert pd.api.types.is_object_dtype(series) or pd.api.types.is_string_dtype(series), \
        f"Column {series.name} is not string-like (got {series.dtype})"
    
def test_orders_schema_and_types():
    # Load cleaned orders
    df = pd.read_csv("out/clean_orders.csv")

    # Define expected columns and dtypes
    expected_columns = {
        "order_id": "object",
        "customer_id": "object",
        "status": "object",
        "order_date": "datetime64[ns]"
    }

    # Check all expected columns exist
    for col in expected_columns:
        assert col in df.columns, f"Missing column: {col}"

    # Convert order_date to datetime if not already
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

    # Check dtypes
    assert pd.api.types.is_string_dtype(df["order_id"])
    assert pd.api.types.is_string_dtype(df["customer_id"])
    assert pd.api.types.is_string_dtype(df["status"])
    assert pd.api.types.is_datetime64_any_dtype(df["order_date"])

    # Ensure no NA values in required fields
    required_cols = ["order_id", "customer_id", "order_date"]
    for col in required_cols:
        assert df[col].notna().all(), f"Null values found in {col}"
