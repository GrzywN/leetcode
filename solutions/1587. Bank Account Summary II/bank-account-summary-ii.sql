SELECT 
  name AS NAME, 
  SUM(Transactions.amount) AS BALANCE 
FROM 
  Transactions 
  JOIN Users ON Transactions.account = Users.account 
GROUP BY 
  Transactions.account 
HAVING 
  SUM(Transactions.amount) > 10000;
