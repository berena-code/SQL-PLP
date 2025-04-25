from fastapi import FastAPI
import mysql.connector
from pydantic import BaseModel

app = FastAPI()

# MySQL connection setup
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1Whitetiger$",
    database="task_manager_db"
)
cursor = conn.cursor()

# Pydantic models for data validation
class Task(BaseModel):
    task_name: str
    description: str
    due_date: str
    status: str
    user_id: int
    category_id: int

# CRUD Operations
@app.post("/tasks/")
async def create_task(task: Task):
    query = """INSERT INTO Tasks (task_name, description, due_date, status, user_id, category_id)
               VALUES (%s, %s, %s, %s, %s, %s)"""
    values = (task.task_name, task.description, task.due_date, task.status, task.user_id, task.category_id)
    cursor.execute(query, values)
    conn.commit()
    return {"message": "Task created successfully!"}

@app.get("/tasks/{task_id}")
async def read_task(task_id: int):
    cursor.execute("SELECT * FROM Tasks WHERE task_id = %s", (task_id,))
    task = cursor.fetchone()
    if task:
        return {"task_id": task[0], "task_name": task[1], "description": task[2], "due_date": task[3], "status": task[4]}
    return {"message": "Task not found"}

# More endpoints (Update, Delete) should be added similarly

