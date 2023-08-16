-- Author: Mikias Hailu
-- This query script that lists all cities contained in the database
SELECT m.`id`, m.`name`, n.`name`
  FROM `cities` AS m
       INNER JOIN `states` AS n
       ON m.`state_id` = n.`id`
 ORDER BY m.`id`;
