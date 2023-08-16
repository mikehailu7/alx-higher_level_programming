-- Author: Mikias Hailu
-- This query will show records ordered by ascending genre name and show titielshow.
SELECT m.`title`, n.`name`
  FROM `tv_shows` AS m
       LEFT JOIN `tv_show_genres` AS l
       ON m.`id` = l.`show_id`

       LEFT JOIN `tv_genres` AS n
       ON l.`genre_id` = n.`id`
 ORDER BY m.`title`, n.`name`;
