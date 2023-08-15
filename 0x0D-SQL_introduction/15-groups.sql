-- Author: Mikias Hailu
-- This query will show records ordered by decending order are ordered by descending count.
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
