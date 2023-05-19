SELECT
  Prices.product_id,
  ROUND(
    SUM(units * price) / SUM(units),
    2
  ) AS average_price
FROM
  Prices
  JOIN UnitsSold ON Prices.product_id = UnitsSold.product_id
  AND UnitsSold.purchase_date BETWEEN start_date
  AND end_date
GROUP BY
  Prices.product_id;
