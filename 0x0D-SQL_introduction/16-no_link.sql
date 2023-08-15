-- Author: Mikias Hailu
-- This query will lists all records of the table in descending order
SELECT `score`, `name`FROM `second_table`WHERE `name` != ""
ORDER BY `score` DESC
