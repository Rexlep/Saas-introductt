import os
import psycopg2
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException

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
        "SELECT * FROM tasks "
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


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    cursor.execute(
        "SELECT * FROM tasks WHERE id = (%s)", (task_id,))

    task = cursor.fetchone()

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not founded"
        )

    return {
        "id": task[0],
        "title": task[1]
    }


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    cursor.execute(
        """
        UPDATE tasks
        SET title = %s 
        WHERE id = %s
        """, (task.title, task_id)
    )

    if cursor.rowcount == 0:
        raise HTTPException(
            status_code=404,
            detail="Task Not founded"
        )

    conn.commit()

    return {
        "message": "Task Updated successfully"
    }