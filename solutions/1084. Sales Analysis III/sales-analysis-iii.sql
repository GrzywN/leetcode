SELECT 
  Product.product_id, 
  Product.product_name 
FROM 
  Sales 
  JOIN Product ON Sales.product_id = Product.product_id 
GROUP BY 
  Product.product_id 
HAVING 
  MIN(Sales.sale_date) >= "2019-01-01" 
  AND MAX(Sales.sale_date) <= "2019-03-31";
