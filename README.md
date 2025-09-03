# ETL VSCode Starter

A simple **YAML-driven ETL pipeline** built in Python, designed for learning and quick prototyping.  
It demonstrates how to extract, transform, and load CSV data into cleaned datasets using a **configurable pipeline**.


## 📂 Project Structure

etl_vscode_starter/
├── .vscode/ # VSCode settings (launch, tasks, settings)
├── data/ # Raw CSV input files
├── out/ # Cleaned CSV outputs (auto-generated)
├── etl_config.yaml # ETL rules (columns, renames, types)
├── etl_pipeline.py # Python ETL runner
├── requirements.txt # Python dependencies
└── README.md # Project documentation


## ⚙️ Features

- Configurable ETL via **YAML** (`etl_config.yaml`)
- Cleans raw CSVs → outputs standardized CSVs in `out/`
- Handles:
  - Column selection & renaming
  - String trimming
  - Datetime & numeric conversion
  - Null checks
- Ready-to-run in **VSCode** with:
  - Launch config (`F5`)
  - Custom task runner (`Run ETL`)


## 🚀 Setup Instructions

### 1. Clone this repo
```bash
git clone https://github.com/vinski-dev/etl_vscode_starter.git
cd etl_vscode_starter

2. Create a virtual environment
Windows (PowerShell):
python -m venv .venv
.\.venv\Scripts\Activate.ps1

macOS/Linux (bash/zsh):
python3 -m venv .venv
source .venv/bin/activate

3. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

🗂️ Data
Put raw CSV files into the data/ folder:

orders.csv
order_items.csv
customers.csv
products.csv
sellers.csv
reviews.csv

A sample orders.csv is included so you can test right away.

▶️ Run the ETL
Option A — Command Line
python etl_pipeline.py

Option B — VSCode Task
Ctrl/Cmd + Shift + P → “Run Task” → Run ETL

Option C — Debugger
Press F5 → choose Run ETL (etl_pipeline.py)

Outputs will be written to out/ (e.g., out/clean_orders.csv).

⚡ Customize ETL

Modify etl_config.yaml to:
Select columns
Rename fields
Convert datatypes
Drop invalid rows
Change output paths

Example:

orders:
  input_csv: "data/orders.csv"
  output_csv: "out/clean_orders.csv"
  columns: ["order_id", "customer_id", "order_status", "order_purchase_timestamp"]
  rename_map:
    order_status: "status"
    order_purchase_timestamp: "order_date"
  datetime_cols: ["order_date"]
  strip_cols: ["order_id", "customer_id", "status"]
  dropna_cols: ["order_id", "customer_id", "order_date"]


🧰 Requirements

Python 3.10+
VSCode with extensions:
Python (Microsoft)
YAML (Red Hat)

📌 Next Steps

Extend etl_config.yaml to handle more datasets
Add schema validation with pytest
Load cleaned data into a database (e.g., Postgres, BigQuery, Snowflake)


📄 License

MIT License.
Feel free to fork, modify, and use for your own projects.




