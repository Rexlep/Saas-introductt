from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

tasks = []


class Task(BaseModel):
    title: str


@app.get("/tasks")
def get_tasks():
    return tasks


@app.post("/tasks")
def create_task(task: Task):
    tasks.append(task.title)

    return {
        "message": "Task Added"
    }


@app.delete("/tasks/{task_index}")
def delete_task(task_index: int):

    tasks.pop(task_index)

    return {
        "message": "TaskDeleted"
    }


@app.put("/tasks/{task_index}")
def update_task(task_index: int, task: Task):

    tasks[task_index] = task.title

    return {"message": "Task Updated"}