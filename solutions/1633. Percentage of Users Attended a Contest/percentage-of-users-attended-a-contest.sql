SELECT
  contest_id,
  ROUND(
    (
      COUNT(Register.user_id) / (
        SELECT
          COUNT(*)
        FROM
          Users
      )
    ) * 100,
    2
  ) AS percentage
FROM
  Register
  JOIN Users ON Register.user_id = Users.user_id
GROUP BY
  contest_id
ORDER BY
  percentage DESC,
  contest_id ASC;
