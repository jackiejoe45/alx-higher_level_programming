-- creates the MySQL server user user_0d_1.
-- user_0d_1 hasall privileges on the MySQL server
-- The user_0d_1 password is set to user_0d_1_pwd
-- If the user user_0d_1 already exists, the script does not fail

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
