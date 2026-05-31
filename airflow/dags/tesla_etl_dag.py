from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import psycopg2


RAW_PATH = "/Users/sahasrareddychinthakunta/tesla-ev-data-engineering-project/data/raw/ev_stock_data.csv"
PROCESSED_PATH = "/Users/sahasrareddychinthakunta/tesla-ev-data-engineering-project/data/processed/ev_stock_processed.csv"


# -----------------------------
# TRANSFORM
# -----------------------------
def transform():
    df = pd.read_csv(RAW_PATH)

    df["daily_range"] = df["high"] - df["low"]
    df["price_change"] = df["close"] - df["open"]
    df["price_volume"] = df["close"] * df["volume"]

    df.to_csv(PROCESSED_PATH, index=False)

    print("TRANSFORM DONE")


# -----------------------------
# LOAD FACT TABLE
# -----------------------------
def load_fact():
    df = pd.read_csv(PROCESSED_PATH)

    conn = psycopg2.connect(
        dbname="ev_warehouse",
        user="sahasrareddychinthakunta",
        host="localhost",
        port="5432"
    )

    cur = conn.cursor()

    cur.execute("TRUNCATE TABLE fact_stock_prices")

    for _, row in df.iterrows():
        cur.execute("""
            INSERT INTO fact_stock_prices (
                company, date, open, close, high, low, volume,
                market_cap, daily_range, price_change, price_volume
            )
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """, (
            row["company"], row["date"], row["open"], row["close"],
            row["high"], row["low"], row["volume"], row["market_cap"],
            row["daily_range"], row["price_change"], row["price_volume"]
        ))

    conn.commit()
    cur.close()
    conn.close()

    print("FACT LOADED")


# -----------------------------
# LOAD DIMENSION TABLE (FIXED)
# -----------------------------
def load_dim():
    conn = psycopg2.connect(
        dbname="ev_warehouse",
        user="sahasrareddychinthakunta",
        host="localhost",
        port="5432"
    )

    cur = conn.cursor()

    cur.execute("TRUNCATE TABLE dim_company")

    cur.execute("""
        INSERT INTO dim_company (company)
        SELECT DISTINCT company
        FROM fact_stock_prices
        WHERE company IS NOT NULL
    """)

    conn.commit()

    cur.execute("SELECT COUNT(*) FROM dim_company")
    count = cur.fetchone()[0]
    print(f"DIM LOADED -> {count} rows")

    cur.close()
    conn.close()


# -----------------------------
# DAG
# -----------------------------
with DAG(
    dag_id="tesla_etl_dag",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
) as dag:

    t1 = PythonOperator(
        task_id="transform",
        python_callable=transform
    )

    t2 = PythonOperator(
        task_id="load_fact",
        python_callable=load_fact
    )

    t3 = PythonOperator(
        task_id="load_dim",
        python_callable=load_dim
    )

    t1 >> t2 >> t3
