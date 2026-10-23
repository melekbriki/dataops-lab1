SELECT
    country,
    COUNT(*) AS nb_orders,
    SUM(quantity) AS total_quantity,
    SUM(quantity * unit_price) AS total_revenue
FROM {{ ref('clean_orders') }}
GROUP BY country