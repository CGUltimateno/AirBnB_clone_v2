-- Set up the database and a user for the system

-- Create database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost'
IDENTIFIED BY 'hbnb_test_pwd';

-- Grant user hbnb_dev permissions to hbnb_dev_db
GRANT ALL
ON hbnb_test_db.*
TO 'hbnb_test'@'localhost';

-- Grant user read-only permission to performance_schema
GRANT SELECT
ON performance_schema.*
TO 'hbnb_test'@'localhost';


-- Enforce new privileges
FLUSH PRIVILEGES