WITH ManagerDirectReports AS (
  SELECT
    managerId,
    COUNT(managerId) AS directReports
  FROM
    Employee
  GROUP BY
    managerId
  HAVING
    directReports >= 5
)
SELECT
  name
FROM
  Employee
  JOIN ManagerDirectReports ON Employee.id = ManagerDirectReports.managerId;
