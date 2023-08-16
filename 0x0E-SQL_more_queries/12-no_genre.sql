-- Author: Mikias Hailu
-- This query will lists all shows in the database hbtn_0d_tvshows
SELECT m.`title`, n.`genre_id`
  FROM `tv_shows` AS m
       LEFT JOIN `tv_show_genres` AS n
       ON m.`id` = n.`show_id`
       WHERE n.`genre_id` IS NULL
 ORDER BY m.`title`, n.`genre_id`;
