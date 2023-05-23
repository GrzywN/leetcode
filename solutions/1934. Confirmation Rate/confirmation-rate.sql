SELECT
  Signups.user_id,
  ROUND(
    IFNULL(
      SUM(
        IF(action = "confirmed", 1, 0)
      ) / (
        SUM(
          IF(action = "confirmed", 1, 0)
        ) + SUM(
          IF(action = "timeout", 1, 0)
        )
      ),
      0
    ),
    2
  ) AS confirmation_rate
FROM
  Confirmations
  RIGHT JOIN Signups ON Confirmations.user_id = Signups.user_id
GROUP BY
  user_id;
