-- SQLite
WITH all_tables AS (SELECT name FROM sqlite_master WHERE type = 'table') 
SELECT at.name table_name, pti.*
FROM all_tables at INNER JOIN pragma_table_info(at.name) pti 
WHERE table_name LIKE 'core%' OR table_name = 'auth_user'
ORDER BY table_name;