from fastapi import FastAPI
from .adapters import candidatesAPI

app = FastAPI()

app.include_router(candidatesAPI.router)

@app.get("/")
def Index():
    return {"Message": "Hello World"}