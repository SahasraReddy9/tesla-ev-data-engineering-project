# 🚗 EV Market Intelligence & Investment Analytics Platform

## 📌 Executive Summary

The EV Market Intelligence Platform is an end-to-end data engineering system designed to simulate real-world equity research and investment decision-making across leading electric vehicle companies.

It converts raw time-series stock data into structured financial intelligence, enabling comparison of companies based on price performance, volatility, growth trends, and trading activity.

The system is designed to mimic how a quantitative analyst or portfolio manager would evaluate EV sector stocks.

---

## 🎯 Business Problem

Investors and analysts face three key challenges:

- Lack of unified comparison metrics across EV companies
- Difficulty identifying risk (volatility) vs opportunity (growth)
- No structured system to rank EV companies objectively

This platform solves these problems by building a structured analytics pipeline that transforms raw stock data into ranked investment intelligence.

---

## 🏗️ System Architecture

Data Generator  
→ ETL Pipeline (Python + Pandas)  
→ PostgreSQL Data Warehouse  
→ Apache Airflow Orchestration  
→ SQL Analytics Layer  
→ Streamlit Dashboard  

---

## 🧠 Data Model

### Fact Table
- `fact_stock_prices` → time-series stock price + volume data

### Dimension Table
- `dim_company` → EV company metadata

---

## ⚙️ Pipeline Flow

1. Generate synthetic EV stock dataset  
2. Clean and transform time-series data using Python ETL  
3. Load structured data into PostgreSQL warehouse  
4. Orchestrate pipeline using Apache Airflow DAG  
5. Run analytical SQL models for ranking & scoring  
6. Visualize insights using Streamlit dashboard  

---

## 📊 Analytical Layer (SQL Thinking)

### 1. Performance Ranking
```sql
SELECT company, AVG(close) AS avg_close_price
FROM fact_stock_prices
GROUP BY company
ORDER BY avg_close_price DESC;

SELECT company, STDDEV(close) AS volatility
FROM fact_stock_prices
GROUP BY company
ORDER BY volatility DESC;

SELECT company,
       AVG(price_change) AS avg_growth
FROM fact_stock_prices
GROUP BY company
ORDER BY avg_growth DESC;

🔍 Key Findings (Business Insights)
Tesla ranks highest due to strong stability and market dominance
BYD shows significantly higher growth momentum (~35% stronger than legacy manufacturers)
Rivian and Lucid show higher volatility (~18–22% above baseline), indicating higher risk/reward profiles
Ford and GM show stable but lower growth, typical of mature market behavior

📊 Dashboard Layer (Decision Interface)

Built using Streamlit:

Company-wise performance comparison
Volatility vs growth visualization
Ranking-based investment view
Time-series trend analysis

📌 Project Outcome

This system transforms raw financial data into structured investment intelligence using a full-stack data engineering pipeline.

It simulates real-world equity research workflows used in financial institutions.


---

## NOW DO THIS ONLY

```bash
cd ~/tesla-ev-data-engineering-project
nano README.md
