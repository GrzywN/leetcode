SELECT
  product_name,
  SUM(unit) AS unit
FROM
  Orders
  JOIN Products ON Orders.product_id = Products.product_id
WHERE
  YEAR(order_date) = 2020
  AND MONTH(order_date) = 2
GROUP BY
  Orders.product_id
HAVING
  unit >= 100;
