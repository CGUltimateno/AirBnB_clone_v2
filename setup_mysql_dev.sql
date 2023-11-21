-- Set up the database and a user for the system

-- Create database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost'
IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant user hbnb_dev permissions to hbnb_dev_db
GRANT ALL
ON hbnb_dev_db.*
TO 'hbnb_dev'@'localhost';

-- Grant user read-only permission to performance_schema
GRANT SELECT
ON performance_schema.*
TO 'hbnb_dev'@'localhost';


-- Enforce new privileges
FLUSH PRIVILEGES