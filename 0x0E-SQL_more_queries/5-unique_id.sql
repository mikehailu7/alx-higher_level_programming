-- Author: Mikias Hailu
-- This query will create the table unique id with id and varchar prop
CREATE TABLE IF NOT EXISTS `unique_id` (
    `id`   INT          DEFAULT 1 UNIQUE,
    `name` VARCHAR(256)
);
