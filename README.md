# 🚗 Tesla EV Data Engineering Pipeline

## Overview
End-to-end data engineering project simulating Tesla EV stock analytics using a complete modern data stack.

---

## Architecture Flow

Python Data Generator  
→ ETL Pipeline (Pandas)  
→ PostgreSQL Data Warehouse  
→ Apache Airflow Orchestration  
→ Streamlit Dashboard  

---

## Tech Stack
- Python
- Pandas
- PostgreSQL
- Apache Airflow
- Streamlit
- Plotly

---

## Data Model

### Fact Table
- fact_stock_prices (stock-level time series data)

### Dimension Table
- dim_company (company metadata)

---

## Airflow DAG
- tesla_etl_dag
- Tasks:
  - extract_data
  - transform_data
  - load_data

---

## Dashboard Features
- Company-wise stock distribution
- Average stock prices
- Volume analysis
- Interactive charts (Plotly)
- Data preview table

---

## How to Run

### ETL
```bash
python etl/run_etl.py
