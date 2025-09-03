import pandas as pd


def assert_string_column(series):
    assert pd.api.types.is_object_dtype(series) or pd.api.types.is_string_dtype(
        series
    ), f"Column {series.name} is not string-like (got {series.dtype})"


def test_order_items_schema_and_types():
    df = pd.read_csv("out/clean_order_items.csv")

    expected_columns = {
        "order_id": "object",
        "product_id": "object",
        "price": "float",
        "shipping_cost": "float",
    }

    for col in expected_columns:
        assert col in df.columns, f"Missing column: {col}"

    assert pd.api.types.is_string_dtype(df["order_id"])
    assert pd.api.types.is_string_dtype(df["product_id"])
    assert pd.api.types.is_float_dtype(df["price"])
    assert pd.api.types.is_float_dtype(df["shipping_cost"])

    for col in ["order_id", "product_id", "price"]:
        assert df[col].notna().all(), f"Null values found in {col}"
