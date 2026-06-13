from fastapi import APIRouter, HTTPException
from s03.project.database import cursor, conn
from s03.project.schemas.tasks import TaskCreate

router = APIRouter()


@router.post("/tasks")
def create_task(task: TaskCreate):

    cursor.execute(
        "INSERT INTO tasks (title) VALUES (%s)",
        (task.title,)
    )

    conn.commit()

    return {"message": "created"}


@router.get("/tasks/{task_id}")
def get_task(task_id: int):

    cursor.execute(
        "SELECT * FROM tasks WHERE id = %s",
        (task_id,)
    )

    task = cursor.fetchone()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return {"id": task[0], "title": task[1]}


@router.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskCreate):

    cursor.execute(
        "UPDATE tasks SET title = %s WHERE id = %s",
        (task.title, task_id)
    )

    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Task not found")

    conn.commit()

    return {"message": "updated"}


@router.delete("/tasks/{task_id}")
def delete_task(task_id: int):

    cursor.execute(
        "DELETE FROM tasks WHERE id = %s",
        (task_id,)
    )

    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Task not found")

    conn.commit()

    return {"message": "deleted"}