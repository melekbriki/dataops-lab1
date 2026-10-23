from pathlib import Path
import duckdb

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "warehouse.duckdb"


def main():
    con = duckdb.connect(str(DB_PATH))

    result = con.execute("""
        SELECT country, COUNT(*) AS nb_orders
        FROM raw.orders
        GROUP BY country
        ORDER BY country
    """).df()

    print(result)

    con.close()


if __name__ == "__main__":
    main()