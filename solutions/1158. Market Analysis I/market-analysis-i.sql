SELECT Users.user_id AS buyer_id, join_date, IFNULL(COUNT(IF(YEAR(order_date) = 2019, order_date, NULL)), 0) AS orders_in_2019
FROM Users
LEFT JOIN Orders ON Users.user_id = Orders.buyer_id
GROUP BY Users.user_id
ORDER BY Users.user_id ASC;
