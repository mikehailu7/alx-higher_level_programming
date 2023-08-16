-- Author: Mikias Hailu
-- This query will show records are ordered by descending rating
SELECT `title`, SUM(`rate`) AS `rating`
  FROM `tv_shows` AS m
       INNER JOIN `tv_show_ratings` AS n
       ON m.`id` = n.`show_id`
 GROUP BY `title`
 ORDER BY `rating` DESC;
