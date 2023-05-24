WITH FirstOrderDate AS (
  SELECT
    customer_id,
    MIN(order_date) AS first_order_date
  FROM
    Delivery
  GROUP BY
    customer_id
)
SELECT
  ROUND(
    SUM(
      CASE WHEN D2.first_order_date = customer_pref_delivery_date THEN 1 ELSE 0 END
    ) / COUNT(*) * 100,
    2
  ) AS immediate_percentage
FROM
  Delivery AS D1
  JOIN FirstOrderDate AS D2 ON D1.customer_id = D2.customer_id
  AND D1.order_date = D2.first_order_date;
