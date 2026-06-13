from fastapi import FastAPI
from s03.project.schemas import tasks as task_router

app = FastAPI()

app.include_router(task_router)