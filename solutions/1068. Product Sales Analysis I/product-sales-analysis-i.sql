SELECT
  product_name,
  Sales.year AS "year",
  price
FROM
  Sales
  JOIN Product ON Sales.product_id = Product.product_id;
