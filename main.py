from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mysql.connector
from typing import List, Optional
from datetime import date

# FastAPI app setup
app = FastAPI()

# Connect to the MySQL database
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",  # your MySQL host (usually localhost)
        user="root",       # your MySQL username
        password="1Whitetiger$",  # your MySQL password
        database="TaskManagerDB"  # the database you created
    )

# Pydantic models to validate the data
class User(BaseModel):
    username: str
    email: str

class TaskCategory(BaseModel):
    category_name: str

class Task(BaseModel):
    task_name: str
    user_id: int
    category_id: int
    is_completed: Optional[bool] = False
    due_date: Optional[date] = None

# Create a User (POST /users/)
@app.post("/users/")
async def create_user(user: User):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Users (username, email) VALUES (%s, %s)", (user.username, user.email))
    connection.commit()
    cursor.close()
    connection.close()
    return {"message": "User created successfully"}

# Get all Users (GET /users/)
@app.get("/users/", response_model=List[User])
async def get_users():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Users")
    users = cursor.fetchall()
    cursor.close()
    connection.close()
    return users

# Create a Task Category (POST /categories/)
@app.post("/categories/")
async def create_category(category: TaskCategory):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO TaskCategories (category_name) VALUES (%s)", (category.category_name,))
    connection.commit()
    cursor.close()
    connection.close()
    return {"message": "Category created successfully"}

# Create a Task (POST /tasks/)
@app.post("/tasks/")
async def create_task(task: Task):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO Tasks (task_name, user_id, category_id, is_completed, due_date) VALUES (%s, %s, %s, %s, %s)",
        (task.task_name, task.user_id, task.category_id, task.is_completed, task.due_date)
    )
    connection.commit()
    cursor.close()
    connection.close()
    return {"message": "Task created successfully"}

# Get all Tasks (GET /tasks/)
@app.get("/tasks/", response_model=List[Task])
async def get_tasks():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Tasks")
    tasks = cursor.fetchall()
    cursor.close()
    connection.close()
    return tasks
