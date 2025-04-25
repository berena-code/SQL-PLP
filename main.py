from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import database

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Task Manager API!"}

class User(BaseModel):
    username: str
    email: str

class TaskCategory(BaseModel):
    category_name: str

class Task(BaseModel):
    task_name: str
    user_id: int
    category_id: int
    is_completed: bool = False
    due_date: str  # YYYY-MM-DD

@app.post("/users")
def create_user(user: User):
    conn = database.get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO Users (username, email) VALUES (%s, %s)", (user.username, user.email))
        conn.commit()
        return {"message": "User created successfully!"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        conn.close()

