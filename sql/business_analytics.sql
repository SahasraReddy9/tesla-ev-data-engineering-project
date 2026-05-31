-- =====================================================
-- ADVANCED BUSINESS ANALYTICS LAYER (SENIOR LEVEL)
-- =====================================================


-- 1. COMPANY PERFORMANCE RANKING (WINDOW FUNCTION)
-- Rank companies by average closing price

SELECT 
    company,
    AVG(close)::numeric(12,2) AS avg_close_price,
    RANK() OVER (ORDER BY AVG(close) DESC) AS price_rank
FROM fact_stock_prices
GROUP BY company
ORDER BY price_rank;



-- 2. DAILY MOVEMENT STABILITY (VOLATILITY SCORE)
-- Lower volatility = more stable company

SELECT 
    company,
    STDDEV(close)::numeric(12,2) AS volatility,
    DENSE_RANK() OVER (ORDER BY STDDEV(close)) AS stability_rank
FROM fact_stock_prices
GROUP BY company
ORDER BY stability_rank;



-- 3. MARKET ACTIVITY LEADERS (VOLUME POWER RANKING)

SELECT 
    company,
    SUM(volume) AS total_volume,
    RANK() OVER (ORDER BY SUM(volume) DESC) AS volume_rank
FROM fact_stock_prices
GROUP BY company
ORDER BY volume_rank;



-- 4. GROWTH TREND SCORE (PRICE MOMENTUM)

SELECT 
    company,
    AVG(price_change)::numeric(12,4) AS avg_growth,
    RANK() OVER (ORDER BY AVG(price_change) DESC) AS growth_rank
FROM fact_stock_prices
GROUP BY company
ORDER BY growth_rank;



-- 5. FINAL COMPOSITE PERFORMANCE SCORE (BUSINESS KPI MODEL)

SELECT 
    company,

    AVG(close)::numeric(12,2) AS avg_price,
    STDDEV(close)::numeric(12,2) AS volatility,
    SUM(volume) AS total_volume,
    AVG(price_change)::numeric(12,4) AS growth_score,

    -- Composite score (simple weighted business metric)
    (
        AVG(close) * 0.4 +
        AVG(price_change) * 0.3 +
        (SUM(volume) / 1000000000) * 0.3
    )::numeric(12,2) AS composite_score,

    RANK() OVER (
        ORDER BY 
        (
            AVG(close) * 0.4 +
            AVG(price_change) * 0.3 +
            (SUM(volume) / 1000000000) * 0.3
        ) DESC
    ) AS overall_rank

FROM fact_stock_prices
GROUP BY company
ORDER BY overall_rank;
