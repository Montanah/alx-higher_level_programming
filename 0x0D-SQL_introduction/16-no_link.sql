-- Lists all records of second-table with a name value
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
