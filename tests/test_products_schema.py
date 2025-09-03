import pandas as pd


def assert_string_column(series):
    assert pd.api.types.is_object_dtype(series) or pd.api.types.is_string_dtype(
        series
    ), f"Column {series.name} is not string-like (got {series.dtype})"


def test_products_schema_and_types():
    df = pd.read_csv("out/clean_products.csv")

    expected_columns = {
        "product_id": "string",
        "category": "string",
        "weight_g": "float",
        "length_cm": "float",
        "height_cm": "float",
        "width_cm": "float",
    }

    for col in expected_columns:
        assert col in df.columns, f"Missing column: {col}"

    # Flexible string checks
    assert_string_column(df["product_id"])
    assert_string_column(df["category"])

    # Numeric checks
    for col in ["weight_g", "length_cm", "height_cm", "width_cm"]:
        assert pd.api.types.is_float_dtype(df[col]) or pd.api.types.is_integer_dtype(
            df[col]
        ), f"{col} must be numeric, got {df[col].dtype}"

    # Null check
    assert df["product_id"].notna().all()
