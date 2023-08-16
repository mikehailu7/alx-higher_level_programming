-- Author: Mikias Hailu
-- This query will list all shows contained in the database.
SELECT m.`title`, n.`genre_id`
  FROM `tv_shows` AS m
       LEFT JOIN `tv_show_genres` AS n
       ON m.`id` = n.`show_id`
 ORDER BY m.`title`, n.`genre_id`;
