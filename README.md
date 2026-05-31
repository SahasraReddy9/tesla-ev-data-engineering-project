# 🚗 EV Market Intelligence System (Tesla EV Analytics Platform)

## 📌 Executive Summary

The EV Market Intelligence System is an end-to-end data engineering and analytics platform designed to simulate real-world investment decision-making across leading electric vehicle companies.

It transforms raw time-series EV stock data into structured insights using automated pipelines, enabling ranking, volatility tracking, and growth-based investment intelligence.

---

## 🎯 Business Problem

Financial analysts and retail investors often struggle to:

- Compare EV companies using consistent metrics
- Identify stable vs volatile stocks
- Detect growth trends across competitors
- Make data-driven portfolio allocation decisions

This project solves that by building a unified analytics system that converts raw stock data into actionable business intelligence.

---

## 🏗️ System Architecture

Data Generation Layer  
→ ETL Pipeline (Python + Pandas)  
→ Data Warehouse (PostgreSQL)  
→ Orchestration Layer (Apache Airflow)  
→ Analytics Layer (SQL Engine)  
→ Visualization Layer (Streamlit Dashboard)

---

## 🧠 Core Capabilities

### 1. Automated Data Pipeline
- Generates synthetic EV stock market data
- Cleans and transforms time-series datasets
- Loads structured data into PostgreSQL warehouse

### 2. Orchestrated Workflow (Airflow)
- Fully automated DAG with:
  - extract_data
  - transform_data
  - load_data
- Ensures reproducible daily pipeline execution

### 3. Analytical Data Warehouse
- Fact Table: `fact_stock_prices`
- Dimension Table: `dim_company`

Enables:
- Time-series analysis
- Cross-company comparisons
- Financial metric aggregation

---

## 📊 Advanced Business Analytics (SQL Layer)

The system computes:

- 📈 Average stock performance ranking
- ⚡ Volatility scoring (risk analysis)
- 📊 Growth trend detection
- 💰 Trading volume analysis
- 🧮 Composite investment score model

This enables classification of companies into:

- High-growth emerging players
- Stable large-cap leaders
- High-volatility risk assets

---

## 📉 Key Business Insights Generated

- Tesla identified as a high-value stable market leader
- BYD shows strong growth momentum in EV sector
- Legacy manufacturers show lower growth consistency
- New entrants exhibit higher volatility but potential upside

---

## 📊 Dashboard (Decision Layer)

Built using Streamlit to enable:

- Company-wise performance comparison
- Trend visualization over time
- Interactive KPI exploration
- Investment ranking insights

This layer simulates a real-world financial analytics dashboard used by portfolio managers.

---

## 🧰 Tech Stack

- Python (ETL & processing)
- Pandas (data transformation)
- PostgreSQL (data warehouse)
- Apache Airflow (pipeline orchestration)
- SQL (analytics layer)
- Streamlit (dashboard)
- Plotly (visualization)

---

## 📦 Data Model

### Fact Table
- `fact_stock_prices` → Time-series EV stock data

### Dimension Table
- `dim_company` → EV company metadata

---

## ⚙️ Pipeline Flow

1. Generate EV stock dataset
2. Clean & transform data using ETL pipeline
3. Load into PostgreSQL warehouse
4. Orchestrate using Airflow DAG
5. Run analytical SQL models
6. Visualize insights in dashboard

---

## 📌 Project Outcome

This system demonstrates a production-style data engineering workflow that transforms raw financial data into actionable business intelligence for EV market analysis and investment decision support.

---

## 🚀 Skills Demonstrated

- End-to-end Data Engineering pipeline design
- Data modeling (Star schema design)
- Workflow orchestration (Airflow DAGs)
- SQL analytics engineering
- Business intelligence system design
- Data visualization and dashboarding
