-- Author: Mikias Hailu
-- This query script to run msql commands
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL ALL PRIVILEGES ON *.* TO'user_0d_1'@'localhost'IDENTIFIED BY 'user_0d_1_pw
FLUSH PRIVILEGES;
