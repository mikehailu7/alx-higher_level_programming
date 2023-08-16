-- Author: Mikias Hailu
-- This query lists all genres from the database tv shows
SELECT m.`name` AS `genre`,
       COUNT(*) AS `number_of_shows`
  FROM `tv_genres` AS m
       INNER JOIN `tv_show_genres` AS u
       ON m.`id` = u.`genre_id`
 GROUP BY m.`name`
 ORDER BY `number_of_shows` DESC;
