import pandas as pd

def assert_string_column(series):
    assert pd.api.types.is_object_dtype(series) or pd.api.types.is_string_dtype(series), \
        f"Column {series.name} is not string-like (got {series.dtype})"
    
def test_reviews_schema_and_types():
    df = pd.read_csv("out/clean_reviews.csv")

    expected_columns = {
        "review_id": "object",
        "order_id": "object",
        "score": "int",
        "timestamp": "datetime64[ns]"
    }

    for col in expected_columns:
        assert col in df.columns, f"Missing column: {col}"

    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

    assert pd.api.types.is_string_dtype(df["review_id"])
    assert pd.api.types.is_string_dtype(df["order_id"])
    assert pd.api.types.is_integer_dtype(df["score"]) or pd.api.types.is_float_dtype(df["score"])
    assert pd.api.types.is_datetime64_any_dtype(df["timestamp"])

    for col in ["review_id", "order_id"]:
        assert df[col].notna().all()
