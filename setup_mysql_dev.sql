-- Prepares a MySQL server for the project.
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

USE hbnb_dev_db;

-- Create tables for all models
CREATE TABLE IF NOT EXISTS states (
    id VARCHAR(60) PRIMARY KEY,
    name VARCHAR(128) NOT NULL
);

CREATE TABLE IF NOT EXISTS cities (
    id VARCHAR(60) PRIMARY KEY,
    name VARCHAR(128) NOT NULL,
    state_id VARCHAR(60),
    FOREIGN KEY (state_id) REFERENCES states(id)
);