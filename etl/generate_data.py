import pandas as pd
import os

def generate_data():
    file_path = os.path.join("data", "processed", "ev_stock_processed.csv")

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Missing file: {file_path}")

    df = pd.read_csv(file_path)

    print(f"Loaded dataset: {len(df)} rows")
    return df
