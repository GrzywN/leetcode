SELECT 
  activity_date as day, 
  COUNT(DISTINCT user_id) AS active_users 
FROM 
  Activity 
WHERE 
  activity_date BETWEEN DATE_ADD("2019-07-27", INTERVAL -29 DAY) 
  AND "2019-07-27" 
GROUP BY 
  activity_date;
