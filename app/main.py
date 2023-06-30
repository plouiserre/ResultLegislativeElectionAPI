from fastapi import FastAPI
from .adapters import candidates_API

app = FastAPI()

app.include_router(candidates_API.router)

@app.get("/")
def Index():
    return {"Message": "Hello World"}