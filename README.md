# Task Manager CLI (Python + MySQL)

A simple command-line task management tool built with Python and MySQL. You can add, list, update, mark as complete, and delete tasks through an interactive CLI.

---

## Features

- Add new tasks with priority and due date
- List all tasks (with optional filters)
- Update existing tasks
- Mark tasks as completed
- Delete tasks

---

## Requirements

> This project was developed and tested using **Python 3.13.5**.
- [XAMPP](https://www.apachefriends.org/index.html) (for MySQL server)
- Python package/s:
  - `pymysql`

---

## Setup Instructions

### 1. Start MySQL using XAMPP

- Launch XAMPP Control Panel
- Start the **MySQL** module
- Make sure the default port (3306) is active

### 2. Clone the repository

```bash
git clone https://github.com/epkasilag1/TaskManager.git
cd TaskManager

```
### 3. Initialize database and sample rows
```bash
python initDb.py

```

### 4. Run the program
```bash
python main.py

```
