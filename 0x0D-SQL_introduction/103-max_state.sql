-- Author: Mikias Hailu
-- This query will display the max temperature of each state
SELECT `state`, MAX(`value`) AS `max_temp`
FROM `temperatures`GROUP BY `state`
ORDER BY `state`;
