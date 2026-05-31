from fastapi import FastAPI

app = FastAPI()

tasks = []


@app.get("/tasks")
def get_tasks():
    return tasks


@app.post("/tasks")
def create_task():
    tasks.append("Learn FastAPI")

    return {
        "message": "Task Added"
    }