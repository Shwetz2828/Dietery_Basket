CREATE DATABASE grocery;

USE grocery;

CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(128) NOT NULL,
    category VARCHAR(64) NOT NULL,
    dietary_preference VARCHAR(64) NOT NULL
);
