from fastapi import FastAPI

app = FastAPI()


@app.get("/register")
def register(name: str):

    return {
        "message": f"Welcome {name}"
    }