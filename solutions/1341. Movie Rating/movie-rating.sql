WITH BestUser AS (
  SELECT 
    name, 
    COUNT(*) 
  FROM 
    MovieRating 
    JOIN Users ON MovieRating.user_id = Users.user_id 
  GROUP BY 
    Users.user_id 
  ORDER BY 
    COUNT(*) DESC, 
    name ASC
), 
BestMoviesFeb2020 AS (
  SELECT 
    title, 
    AVG(rating) AS average_rating 
  FROM 
    MovieRating 
    JOIN Movies ON MovieRating.movie_id = Movies.movie_id 
  WHERE 
    MONTH(created_at) = 2 
    AND YEAR(created_at) = 2020 
  GROUP BY 
    Movies.movie_id 
  ORDER BY 
    average_rating DESC, 
    title ASC
) (
  SELECT 
    name AS results 
  FROM 
    BestUser 
  LIMIT 
    1
) 
UNION ALL 
  (
    SELECT 
      title AS results 
    FROM 
      BestMoviesFeb2020 
    LIMIT 
      1
  );
