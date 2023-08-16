-- Author: Mikias Hailu
-- This query shwos records are ordered by ascending genre name
SELECT m.`name`
  FROM `tv_genres` AS m
       INNER JOIN `tv_show_genres` AS n
       ON m.`id` = n.`genre_id`

       INNER JOIN `tv_shows` AS u
       ON u.`id` = n.`show_id`
       WHERE u.`title` = "Dexter"
 ORDER BY m.`name`;
