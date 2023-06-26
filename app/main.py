from fastapi import FastAPI
from .routeurs import candidates

app = FastAPI()

app.include_router(candidates.router)

@app.get("/")
def Index():
    return {"Message": "Hello World"}