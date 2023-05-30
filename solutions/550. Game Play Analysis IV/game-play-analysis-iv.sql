WITH FirstLoggedIn AS (
  SELECT
    player_id,
    MIN(event_date) AS event_date
  FROM
    Activity
  GROUP BY
    player_id
),
HowManyPlayers AS (
  SELECT
    COUNT(DISTINCT player_id) AS how_many_players
  FROM
    Activity
)
SELECT
  ROUND(
    COUNT(DISTINCT Activity.player_id) / (
      SELECT
        how_many_players
      FROM
        HowManyPlayers
    ),
    2
  ) AS fraction
FROM
  Activity
  JOIN FirstLoggedIn ON Activity.player_id = FirstLoggedIn.player_id
  AND Activity.event_date = DATE_ADD(
    FirstLoggedIn.event_date, INTERVAL 1 DAY
  );
