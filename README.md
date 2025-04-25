
# 📊 Week 8 Assignment – MySQL Database + FastAPI CRUD API

## 📝 Description

This project is divided into two parts:

### Question 1: Inventory Tracking System (SQL Only)

A fully functional **Inventory Tracking Database** built using MySQL. It includes:

- Proper table relationships (1-Many, Many-Many)
- Constraints like `PRIMARY KEY`, `FOREIGN KEY`, `NOT NULL`, and `UNIQUE`
- Sample data for 6+ records per table

### Question 2: Task Manager App (Python + MySQL)

A CRUD API created using FastAPI (Python) connected to a MySQL database. This mini task management system supports:

- Creating, reading, updating, and deleting tasks
- Connecting tasks with users and categories
- FastAPI endpoints with MySQL backend
- Lightweight design without ORM (pure SQL queries)

---

## 🛠️ How to Set Up and Run the Project

### ✅ Prerequisites

- Python 3.8+
- MySQL Server
- `pip` installed

### 📦 Install Required Packages

```bash
pip install fastapi uvicorn mysql-connector-python
```

---

## 💾 SQL Setup (For Both Parts)

### 🔹 Step 1: Import SQL Scripts

1. Open MySQL Workbench or your MySQL terminal
2. Run the provided `.sql` files:
   - `inventory_tracking.sql` (for Question 1)
   - `task_manager.sql` (for Question 2)

These scripts will create the databases and insert sample data.

---

## 🚀 Running the FastAPI Server (Question 2)

In your terminal:

```bash
uvicorn main:app --reload
```

Then open your browser and go to:

```
http://127.0.0.1:8000/docs
```

This will open Swagger UI to test all CRUD endpoints.

---

## 📂 Folder Structure

```
project-root/
├── inventory_tracking.sql         # Question 1 SQL script
├── task_manager.sql               # Question 2 SQL script
├── main.py                        # FastAPI app
├── database.py                    # MySQL connection file
├── README.md                      # This file
```

---

## 🧭 ERD

Create your ERD using a tool like [dbdiagram.io](https://dbdiagram.io/) or MySQL Workbench.

🖼️ ERD Screenshot: *(insert screenshot here)*  
📎 ERD Link: *(insert link here)*

---

## 💡 Author Notes

- SQL scripts are clean and well-commented
- FastAPI code uses MySQL connector (no ORM) for transparency
- Designed for beginner-to-intermediate database learners

---

## 🙌 Credits

Built for educational purposes as part of a **Database and API Integration** assignment (Week 8).

