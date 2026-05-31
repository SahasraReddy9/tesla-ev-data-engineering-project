from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import os


# -----------------------------
# EXTRACT
# -----------------------------
def extract():
    data = {
        "company": ["Tesla", "Ford", "GM"],
        "stock_price": [250, 120, 95],
        "volume": [1000000, 800000, 600000]
    }

    df = pd.DataFrame(data)
    df.to_csv("/tmp/ev_raw.csv", index=False)
    print("Extract completed")


# -----------------------------
# TRANSFORM
# -----------------------------
def transform():
    df = pd.read_csv("/tmp/ev_raw.csv")

    df["price_volume"] = df["stock_price"] * df["volume"]

    df.to_csv("/tmp/ev_transformed.csv", index=False)
    print("Transform completed")


# -----------------------------
# LOAD
# -----------------------------
def load():
    df = pd.read_csv("/tmp/ev_transformed.csv")

    output_path = "/tmp/ev_final_output.csv"
    df.to_csv(output_path, index=False)

    print(f"Load completed -> {output_path}")


# -----------------------------
# DAG
# -----------------------------
with DAG(
    dag_id="tesla_etl_dag",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
) as dag:

    t1 = PythonOperator(
        task_id="extract_data",
        python_callable=extract
    )

    t2 = PythonOperator(
        task_id="transform_data",
        python_callable=transform
    )

    t3 = PythonOperator(
        task_id="load_data",
        python_callable=load
    )

    t1 >> t2 >> t3
