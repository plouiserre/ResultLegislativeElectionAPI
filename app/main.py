from fastapi import FastAPI
from .adapters import candidatesAPI, deputiesAPI, resultsAPI

app = FastAPI()

app.include_router(candidatesAPI.router)
app.include_router(deputiesAPI.router)
app.include_router(resultsAPI.router)

@app.get("/")
def Index():
    return {"Message": "Hello World"}