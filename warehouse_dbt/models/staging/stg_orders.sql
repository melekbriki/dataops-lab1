WITH cleaned AS (
    SELECT
        order_id,
        order_date,
        customer_id,
        CASE
            WHEN LOWER(TRIM(country)) = 'tunisia' THEN 'Tunisia'
            WHEN LOWER(TRIM(country)) = 'morocco' THEN 'Morocco'
            WHEN LOWER(TRIM(country)) = 'france' THEN 'France'
            WHEN LOWER(TRIM(country)) = 'germany' THEN 'Germany'
            WHEN LOWER(TRIM(country)) = 'italy' THEN 'Italy'
            ELSE TRIM(country)
        END AS country,
        TRIM(product) AS product,
        quantity,
        unit_price
    FROM raw.orders
)
SELECT DISTINCT *
FROM cleaned