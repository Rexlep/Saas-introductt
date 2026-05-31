from fastapi import FastAPI

app = FastAPI()

task = []


@app.get("/task/{task_name}")
def create_task(task_name: str):
    task.append(task_name)

    return {
        "message": "Task created",
        "task": task
    }