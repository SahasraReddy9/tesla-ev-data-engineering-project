-- FACT TABLE
CREATE TABLE fact_stock_prices (
    company TEXT,
    date DATE,
    open FLOAT,
    close FLOAT,
    high FLOAT,
    low FLOAT,
    volume BIGINT,
    market_cap FLOAT,
    daily_range FLOAT,
    price_change FLOAT,
    price_volume FLOAT
);

-- DIMENSION TABLE
CREATE TABLE dim_company (
    company TEXT PRIMARY KEY
);
