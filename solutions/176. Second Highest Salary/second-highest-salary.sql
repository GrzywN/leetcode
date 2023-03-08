SELECT 
  MAX(t.salary) AS SecondHighestSalary 
FROM 
  (
    SELECT 
      salary 
    FROM 
      Employee 
    WHERE 
      salary NOT IN (
        SELECT 
          MAX(salary) 
        FROM 
          Employee
      )
  ) as t;
