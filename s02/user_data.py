import os
import psycopg2
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

class Task(BaseModel):
    title: str

load_dotenv()

conn = psycopg2.connect(
    password="1384amiR",
    user="postgres",
    database="task_manager",
    host="localhost",
    port=5432
)

cursor = conn.cursor()

app = FastAPI()


@app.post("/task")
def create_task(task: Task):
    cursor.execute(
        "INSERT INTO tasks (title) VALUES (%s)", (task.title,)
    )

    conn.commit()

    return {
        "message": "Task saved",
        "data": task.title
    }


@app.get("/tasks")
def get_tasks():
    cursor.execute(
        "SELECT * FROM tasks"
    )

    rows = cursor.fetchall()
    tasks = []

    for row in rows:
        tasks.append(
            {
                "id": row[0],
                "title": row[1]
            }
        )

    return tasks