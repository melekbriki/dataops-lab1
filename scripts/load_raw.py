from pathlib import Path
import duckdb

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data" / "raw"
DB_PATH = ROOT / "warehouse.duckdb"


def main():
    con = duckdb.connect(str(DB_PATH))

    csv_path = DATA_DIR / "orders_day1.csv"

    con.execute("""
        CREATE SCHEMA IF NOT EXISTS raw;
    """)

    con.execute("""
        CREATE OR REPLACE TABLE raw.orders AS
        SELECT *
        FROM read_csv_auto(?)
    """, [str(csv_path)])

    count = con.execute(
        "SELECT COUNT(*) FROM raw.orders"
    ).fetchone()[0]

    print(f"Loaded {count} rows into raw.orders")

    con.close()


if __name__ == "__main__":
    main()