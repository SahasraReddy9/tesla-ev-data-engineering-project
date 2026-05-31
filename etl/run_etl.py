from generate_data import generate_data
from load_to_postgres import load_data

def main():
    print("ETL STARTED")

    df = generate_data()
    load_data(df)

    print("ETL COMPLETED")

if __name__ == "__main__":
    main()
