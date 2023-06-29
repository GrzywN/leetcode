SELECT
  DISTINCT L1.num AS ConsecutiveNums
FROM
  Logs L1,
  Logs L2,
  Logs L3
WHERE
  l1.id = l2.id - 1
  AND l2.id = l3.id - 1
  AND l1.num = l2.num
  AND l2.num = l3.num;
