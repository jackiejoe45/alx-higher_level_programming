-- lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.
-- Results should display the score and the name (in this order)
-- Records is listed by descending score
-- The database name is passed as an argument to the mysql command

SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
