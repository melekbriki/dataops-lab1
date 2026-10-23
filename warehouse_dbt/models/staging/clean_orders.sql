SELECT *
FROM {{ ref('stg_orders') }}
WHERE quantity > 0
  AND unit_price >= 0
  AND customer_id IS NOT NULL
  AND order_date IS NOT NULL