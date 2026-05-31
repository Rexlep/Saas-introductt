from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello boys"}

@app.get("/about")
def about():
    return {"message": "this is about page"}