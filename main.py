from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Welcome to the world of FastAPI!"}

@app.get("/items/{item}")
def read_item(item: str, q: str = None):
    return {"item": item, "q": q}