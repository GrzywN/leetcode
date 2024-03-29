SELECT
  requester_id AS id,
  (
    SELECT
      COUNT(*)
    FROM
      RequestAccepted
    WHERE
      id = requester_id
      OR id = accepter_id
  ) AS num
FROM
  RequestAccepted
GROUP BY
  requester_id
ORDER BY
  num DESC
LIMIT
  1;
