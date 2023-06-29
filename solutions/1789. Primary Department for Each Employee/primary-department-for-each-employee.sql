(
  SELECT
    employee_id,
    department_id
  FROM
    Employee
  WHERE
    primary_flag LIKE 'Y'
)
UNION ALL
  (
    SELECT
      DISTINCT employee_id,
      department_id
    FROM
      Employee
    WHERE
      primary_flag LIKE 'N'
      AND employee_id NOT IN (
        SELECT
          employee_id
        FROM
          Employee
        WHERE
          primary_flag LIKE 'Y'
      )
  );
