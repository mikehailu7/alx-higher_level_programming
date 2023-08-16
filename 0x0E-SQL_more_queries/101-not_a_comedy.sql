-- Author: Mikias Hailu
-- This query shows records are ordered by ascending show title
SELECT DISTINCT `title`
  FROM `tv_shows` AS m
       LEFT JOIN `tv_show_genres` AS n
       ON n.`show_id` = m.`id`

       LEFT JOIN `tv_genres` AS l
       ON l.`id` = n.`genre_id`
       WHERE m.`title` NOT IN
             (SELECT `title`
                FROM `tv_shows` AS m
	             INNER JOIN `tv_show_genres` AS n
		     ON n.`show_id` = m.`id`

		     INNER JOIN `tv_genres` AS l
		     ON l.`id` = n.`genre_id`
		     WHERE l.`name` = "Comedy")
 ORDER BY `title`;
