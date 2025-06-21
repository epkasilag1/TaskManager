CREATE DATABASE IF NOT EXISTS taskdb;
USE taskdb;

CREATE TABLE IF NOT EXISTS tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    due_date DATE,
    priority ENUM('Low', 'Medium', 'High') DEFAULT 'Medium',
    status ENUM('Pending', 'In Progress', 'Completed') DEFAULT 'Pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO tasks (title, description, due_date, priority, status)
VALUES 
('Buy groceries', 'Buy milk, eggs, and bread from the store.', '2025-06-25', 'Medium', 'Pending'),
('Finish thesis draft', 'Write the results and discussion section.', '2025-06-30', 'High', 'In Progress'),
('Call dentist', 'Schedule an appointment for teeth cleaning.', '2025-06-22', 'Low', 'Pending'),
('Workout session', 'Attend 1-hour HIIT class at the gym.', '2025-06-23', 'Medium', 'Completed'),
('Team meeting', 'Discuss sprint progress with the dev team.', '2025-06-24', 'High', 'Pending');