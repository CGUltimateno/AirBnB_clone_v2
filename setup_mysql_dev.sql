-- Set up the database and a user for the system

CREATE DATABASE IF NOT EXIST hbnb_dev_db;

CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost'
IDENTIFIED BY 'hbnb_dev_pwd';

GRANT ALL
ON hbnb_dev_db.*
TO 'hbnb_dev'@'localhost';

GRANT SELECT
ON performance_schema.*
TO 'hbnb_dev'@'localhost';


FLUSH PRIVILEGES