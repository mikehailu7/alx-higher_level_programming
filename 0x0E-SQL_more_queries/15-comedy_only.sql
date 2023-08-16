-- Author: Mikias Hailu
-- This query will show records are ordered by descending show title
SELECT m.`title`
  FROM `tv_shows` AS m
       INNER JOIN `tv_show_genres` AS l
       ON m.`id` = l.`show_id`

       INNER JOIN `tv_genres` AS n
       ON n.`id` = l.`genre_id`
       WHERE n.`name` = "Comedy"
 ORDER BY m.`title`;
