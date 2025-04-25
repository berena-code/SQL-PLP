CREATE DATABASE TaskManagerDB;
USE TaskManagerDB;

CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL
);

CREATE TABLE TaskCategories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(50) NOT NULL
);

CREATE TABLE Tasks (
    task_id INT AUTO_INCREMENT PRIMARY KEY,
    task_name VARCHAR(100) NOT NULL,
    user_id INT,
    category_id INT,
    is_completed BOOLEAN DEFAULT FALSE,
    due_date DATE,
    CONSTRAINT fk_task_user FOREIGN KEY (user_id) REFERENCES Users(user_id),
    CONSTRAINT fk_task_category FOREIGN KEY (category_id) REFERENCES TaskCategories(category_id)
);