from fastapi import FastAPI

app = FastAPI()


@app.get("/register")
def register(name: str):

    return {
        "message": f"Welcome {name}"
    }


@app.get("/product")
def get_products():
    return ['Laptop',  'Mouse', 'Keyboard']


@app.get("/products")
def create_product():
    return {"message": "Product Created"}
