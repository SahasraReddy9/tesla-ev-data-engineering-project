import psycopg2
import pandas as pd

DB_CONFIG = {
    "dbname": "ev_warehouse",
    "user": "sahasrareddychinthakunta",
    "password": "",
    "host": "localhost",
    "port": 5432
}

def load_data(df):
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()

    # CLEAN TABLE BEFORE LOAD (FIX DUPLICATION ISSUE)
    cursor.execute("TRUNCATE TABLE fact_stock_prices;")
    cursor.execute("TRUNCATE TABLE dim_company;")

    # LOAD FACT TABLE
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO fact_stock_prices (
                company, date, open, close, high, low,
                volume, market_cap, daily_range,
                price_change, price_volume
            )
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """, tuple(row))

    # LOAD DIMENSION TABLE
    cursor.execute("""
        INSERT INTO dim_company (company)
        SELECT DISTINCT company FROM fact_stock_prices;
    """)

    conn.commit()
    cursor.close()
    conn.close()

    print("LOAD SUCCESS → CLEAN INSERT DONE")
