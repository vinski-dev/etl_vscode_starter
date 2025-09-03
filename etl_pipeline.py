import pandas as pd
import yaml

class ETLPipeline:
    def __init__(self, config: dict):
        self.config = config

    def run_table(self, table_name: str):
        cfg = self.config[table_name]
        df = pd.read_csv(cfg["input_csv"])

        # Select + rename
        df = df[cfg["columns"]].copy()
        df = df.rename(columns=cfg.get("rename_map", {}))

        # String cleanup
        for col in cfg.get("strip_cols", []):
            df[col] = df[col].astype(str).str.strip()

        # Datetime conversion
        for col in cfg.get("datetime_cols", []):
            df[col] = pd.to_datetime(df[col], errors="coerce")

        # Numeric conversion
        for col in cfg.get("numeric_cols", []):
            df[col] = pd.to_numeric(df[col], errors="coerce")

        # Drop invalids
        if "dropna_cols" in cfg:
            df = df.dropna(subset=cfg["dropna_cols"])

        # Save
        df.to_csv(cfg["output_csv"], index=False)
        print(f"✅ {table_name} cleaned → {cfg['output_csv']}")
        return df

    def run_all(self):
        for table in self.config.keys():
            self.run_table(table)


if __name__ == "__main__":
    # Load config
    with open("etl_config.yaml", "r") as f:
        config = yaml.safe_load(f)

    pipeline = ETLPipeline(config)
    pipeline.run_all()
