SELECT
  Sales.product_id,
  Sales.year AS first_year,
  quantity,
  price
FROM
  Sales
  JOIN (
    SELECT
      Sales.product_id AS product_id,
      MIN(Sales.year) AS first_year
    FROM
      Sales
    GROUP BY
      Sales.product_id
  ) T1 ON Sales.product_id = T1.product_id
  AND Sales.year = T1.first_year;
