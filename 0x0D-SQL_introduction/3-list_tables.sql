-- 3-list_tables.sql

-- Assuming the first argument is the database name
SET @dbname = QUOTE(ARGV[1]);

-- List all tables in the specified database
USE @dbname;
SHOW TABLES;

