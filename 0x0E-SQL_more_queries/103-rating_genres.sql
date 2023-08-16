-- Author: Mikias Hailu
-- This query will show records are ordered by descending rating
SELECT `name`, SUM(`rate`) AS `rating`
  FROM `tv_genres` AS m
       INNER JOIN `tv_show_genres` AS n
       ON n.`genre_id` = m.`id`

       INNER JOIN `tv_show_ratings` AS l
       ON l.`show_id` = n.`show_id`
 GROUP BY `name`
 ORDER BY `rating` DESC;
