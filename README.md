# 🚗 EV Market Intelligence & Investment Analytics Platform

## Executive Summary

The EV Market Intelligence & Investment Analytics Platform is an end-to-end data engineering solution designed to transform raw electric vehicle stock market data into structured investment intelligence.

The platform simulates how analysts, portfolio managers, and business stakeholders evaluate companies within the EV sector by consolidating data ingestion, transformation, warehousing, orchestration, analytics, and visualization into a single workflow.

By combining Python-based ETL processing, PostgreSQL warehousing, Apache Airflow orchestration, advanced SQL analytics, and Streamlit dashboards, the platform creates a repeatable framework for evaluating company performance, measuring risk, identifying growth patterns, and supporting investment decision-making.

The project demonstrates how data engineering serves as the foundation for analytical decision support by converting raw operational data into actionable business intelligence.

---

# Business Context

The electric vehicle industry has become one of the most closely monitored sectors in global markets. Investors and analysts continuously compare manufacturers based on market performance, growth potential, trading activity, and operational stability.

However, raw stock market data alone does not provide meaningful business intelligence. Decision-makers require structured systems capable of transforming fragmented data into measurable performance indicators that support objective evaluation and ranking.

This project addresses that need by building an analytics platform that standardizes EV stock data and produces investment-focused insights through a scalable data pipeline.

---

# Business Problem

Organizations and analysts evaluating EV companies face several challenges:

* Raw stock data is difficult to compare across companies.
* Growth, risk, and market activity must be evaluated simultaneously.
* Large volumes of time-series data require automated processing.
* Decision-makers need ranked and standardized performance indicators.
* Analytical workflows must be reproducible and operationalized.

Without a structured platform, identifying investment opportunities and understanding company performance becomes a manual and time-consuming process.

---

# Solution Overview

The platform establishes a complete analytical workflow that:

* Generates and processes EV stock market data.
* Cleans and standardizes data through an ETL pipeline.
* Stores analytical datasets within a PostgreSQL warehouse.
* Automates execution through Apache Airflow.
* Produces business-focused analytical metrics using SQL.
* Delivers decision-support dashboards through Streamlit.

The result is a centralized system that converts stock market activity into measurable business intelligence.

---

# Architecture Overview

```text
Data Generator
        │
        ▼
Python ETL Pipeline
        │
        ▼
PostgreSQL Data Warehouse
        │
        ▼
Apache Airflow Orchestration
        │
        ▼
SQL Analytics Layer
        │
        ▼
Streamlit Dashboard
```

Each layer is responsible for a specific business function, creating a clear separation between data ingestion, transformation, storage, orchestration, analytics, and presentation.

---

# End-to-End Data Flow

### Stage 1: Data Generation

Synthetic EV stock market data is generated and stored for processing.

### Stage 2: Data Transformation

Python and Pandas process the raw dataset, standardize records, and prepare analytical outputs.

### Stage 3: Data Loading

Transformed data is loaded into PostgreSQL tables designed for analytical workloads.

### Stage 4: Workflow Orchestration

Apache Airflow coordinates pipeline execution through a structured DAG consisting of:

* extract_data
* transform_data
* load_data

### Stage 5: Analytical Processing

SQL models calculate investment-focused metrics and rankings.

### Stage 6: Visualization

Streamlit presents analytical outputs through interactive dashboards.

---

# Data Engineering Approach

The platform was designed around core data engineering principles:

* Automated data processing
* Separation of raw and transformed data
* Warehouse-first analytics design
* Workflow orchestration
* Reusable analytical models
* Business-oriented reporting

Python was selected as the orchestration and ETL language because of its flexibility for data processing workflows.

Pandas was used to efficiently manipulate and transform structured datasets before warehouse loading.

The architecture emphasizes reproducibility, maintainability, and analytical scalability.

---

# Data Model

## Fact Table

### fact_stock_prices

Stores stock-level transactional information including:

* Date
* Company
* Open Price
* Close Price
* Volume
* Derived Metrics

This table serves as the primary analytical fact table.

---

## Dimension Table

### dim_company

Stores company-level reference information used for business analysis and reporting.

The dimensional structure separates descriptive company information from transactional stock activity.

---

# ETL Design

The ETL pipeline follows a structured workflow:

### Extract

Raw EV stock data is collected from source files.

### Transform

Data cleansing and analytical preparation are performed using Pandas.

Transformations prepare the dataset for downstream reporting and analysis.

### Load

Processed records are inserted into PostgreSQL warehouse tables.

The final implementation supports repeatable warehouse loading while maintaining analytical consistency.

---

# Workflow Orchestration

Apache Airflow was selected to operationalize the pipeline.

The DAG contains three primary tasks:

1. extract_data
2. transform_data
3. load_data

This orchestration layer introduces scheduling, monitoring, execution visibility, and workflow dependency management.

Airflow transforms the project from a standalone script into a managed data pipeline.

---

# Data Warehouse Design

PostgreSQL serves as the analytical warehouse.

The warehouse was selected because it provides:

* Strong SQL support
* Aggregation capabilities
* Analytical query performance
* Reliable relational storage
* Structured schema management

The design separates facts and dimensions to support scalable analytical queries.

This structure enables aggregation, ranking, and statistical analysis across large historical datasets.

---

# Analytics & Decision Intelligence Layer

The analytics layer transforms warehouse data into decision-support metrics.

The platform evaluates companies using five key analytical dimensions:

### Average Price

Measures overall market valuation behavior.

Why it matters:

Higher average prices often indicate stronger market valuation and investor confidence.

### Volatility

Measures variability in stock prices.

Why it matters:

Volatility acts as a proxy for investment risk.

### Growth Rate

Measures average directional price movement.

Why it matters:

Growth trends help identify expansion opportunities and momentum.

### Trading Volume

Measures market activity.

Why it matters:

Higher volume often reflects greater investor participation and liquidity.

### Composite Investment Score

Combines multiple performance indicators into a single ranking framework.

Why it matters:

Decision-makers rarely evaluate investments using a single metric.

The composite score creates a more balanced view of performance.

---

# Business Questions Answered

The platform was designed to answer key investment-oriented questions:

* Which EV company demonstrates the strongest overall performance?
* Which company experiences the highest volatility?
* Which company shows the strongest growth trend?
* Which stocks attract the highest trading activity?
* How can multiple metrics be combined into a single investment ranking?

---

# Advanced SQL Analytics

The analytical layer incorporates several SQL techniques:

### Aggregations

Used to calculate averages, volumes, and company-level KPIs.

### Statistical Analysis

Used to calculate volatility through standard deviation.

### Ranking Logic

Used to identify leaders and laggards across analytical categories.

### Composite Scoring

Used to combine multiple business indicators into a unified evaluation framework.

### Analytical Reporting

Used to transform warehouse data into business-focused intelligence.

---

# Key Findings & Insights

Analysis of the warehouse produced several notable observations.

Tesla achieved the highest average closing price and ranked first in the overall investment scoring framework. This indicates that the company consistently maintained the strongest valuation profile within the analyzed dataset.

BYD achieved the highest growth ranking. From an investment perspective, this suggests stronger momentum characteristics relative to the other companies evaluated.

XPeng generated the highest cumulative trading volume. Elevated trading activity often reflects increased market participation and stronger liquidity characteristics.

Rivian, Lucid, NIO, and BYD displayed similar volatility profiles, while Tesla, Ford, GM, and XPeng demonstrated slightly higher volatility measurements. These findings highlight the importance of balancing growth expectations against risk considerations.

The composite ranking model demonstrates how multiple performance dimensions can be consolidated into a structured decision-support framework rather than relying on a single metric.

---

# Dashboard & Visualization Layer

The Streamlit dashboard acts as the presentation layer for business stakeholders.

Dashboard capabilities include:

* Company-level performance comparison
* Average price analysis
* Volume analysis
* Interactive visualizations
* Data exploration views
* Analytical reporting outputs

The dashboard transforms warehouse metrics into consumable business intelligence.

---

# Technology Stack

| Layer           | Technology     |
| --------------- | -------------- |
| Programming     | Python         |
| Data Processing | Pandas         |
| Data Warehouse  | PostgreSQL     |
| Orchestration   | Apache Airflow |
| Analytics       | SQL            |
| Dashboarding    | Streamlit      |
| Visualization   | Plotly         |

---

# Engineering Challenges Solved

This project addresses several practical engineering challenges:

* Building repeatable ETL workflows
* Separating operational and analytical concerns
* Designing warehouse-ready data structures
* Automating execution through orchestration
* Creating reusable SQL analytical models
* Converting warehouse outputs into business dashboards

The resulting platform demonstrates the integration of multiple components into a cohesive analytical system.

---

# Key Metrics Produced

The platform generates:

* Average Closing Price
* Volatility
* Trading Volume
* Growth Metrics
* Composite Investment Score
* Company Rankings

These metrics provide a foundation for investment evaluation and comparative performance analysis.

---

# Business Impact

The platform demonstrates how data engineering enables business decision-making.

Rather than working directly with raw stock records, stakeholders receive structured analytical outputs that simplify comparison, ranking, and performance evaluation.

The architecture supports repeatable analysis while reducing manual effort required to prepare investment intelligence.

By integrating warehousing, orchestration, analytics, and visualization into a unified workflow, the platform creates a reliable foundation for analytical decision support.

---

# Project Outcome

This project demonstrates the design and implementation of a complete data engineering and analytics workflow.

The platform ingests raw stock market data, transforms it through an automated ETL process, stores it within a structured warehouse, orchestrates execution using Apache Airflow, performs advanced analytical processing using SQL, and delivers business intelligence through interactive dashboards.

The final solution showcases the ability to design data platforms, build ETL pipelines, implement warehouse architectures, automate workflows, develop analytical models, and translate raw data into executive decision-support intelligence.

