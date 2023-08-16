-- Author: Mikias Hailu
-- This query will show records are sorted by ascending genre name.
SELECT DISTINCT `name`
  FROM `tv_genres` AS m
       INNER JOIN `tv_show_genres` AS n
       ON m.`id` = n.`genre_id`

       INNER JOIN `tv_shows` AS l
       ON n.`show_id` = l.`id`
       WHERE m.`name` NOT IN
             (SELECT `name`
                FROM `tv_genres` AS m
	             INNER JOIN `tv_show_genres` AS n
		     ON m.`id` = n.`genre_id`

		     INNER JOIN `tv_shows` AS l
		     ON n.`show_id` = l.`id`
		     WHERE l.`title` = "Dexter")
 ORDER BY m.`name`;
