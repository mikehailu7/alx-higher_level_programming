-- Author: Mikias Hailu
-- This query will show records are sorted by ascending tv_shows.title 
SELECT m.`title`, n.`genre_id`
  FROM `tv_shows` AS m
        INNER JOIN `tv_show_genres` AS n
	ON m.`id` = n.`show_id`
 ORDER BY m.`title`, n.`genre_id`;
