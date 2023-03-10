SELECT DISTINCT
  SalesPerson.name AS Name 
FROM 
  SalesPerson 
  LEFT JOIN Orders ON Orders.sales_id = SalesPerson.sales_id 
  LEFT JOIN Company ON Orders.com_id = Company.com_id 
WHERE 
  SalesPerson.name NOT IN (
    SELECT 
      SalesPerson.name AS Name 
    FROM 
      SalesPerson 
      LEFT JOIN Orders ON Orders.sales_id = SalesPerson.sales_id 
      LEFT JOIN Company ON Orders.com_id = Company.com_id 
    WHERE 
      Company.name = "RED"
  );
