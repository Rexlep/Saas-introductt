from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def home():
    return {"message": "this is home page"}


@app.get("/product/{product_id}")
def get_product(product_id: int):
    return {"product_id": product_id}


@app.get("/user/{username}")
def get_user(username: str):
    return {
        "username": username,
        "message": f"Welcome {username}"
    }