import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Tesla EV Data Engineering Dashboard",
    layout="wide"
)

st.title("Tesla EV Data Engineering Pipeline Dashboard")

df = pd.read_csv("data/processed/ev_stock_processed.csv")

st.metric("Total Records", len(df))
st.metric("Companies", df["company"].nunique())

col1, col2 = st.columns(2)

with col1:
    company_counts = (
        df.groupby("company")
        .size()
        .reset_index(name="records")
    )

    fig1 = px.bar(
        company_counts,
        x="company",
        y="records",
        title="Records by Company"
    )

    st.plotly_chart(fig1, use_container_width=True)

with col2:
    avg_close = (
        df.groupby("company")["close"]
        .mean()
        .reset_index()
    )

    fig2 = px.bar(
        avg_close,
        x="company",
        y="close",
        title="Average Closing Price"
    )

    st.plotly_chart(fig2, use_container_width=True)

daily_volume = (
    df.groupby("company")["volume"]
    .sum()
    .reset_index()
)

fig3 = px.pie(
    daily_volume,
    names="company",
    values="volume",
    title="Volume Distribution"
)

st.plotly_chart(fig3, use_container_width=True)

st.dataframe(df.head(100))
