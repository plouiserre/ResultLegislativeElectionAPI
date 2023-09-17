from fastapi import FastAPI
from app.adapters.driving.API import candidatesAPI, departementsAPI, deputiesAPI, districtsAPI, partiesAPI, resultsAPI

app = FastAPI()

app.include_router(candidatesAPI.router)
app.include_router(deputiesAPI.router)
app.include_router(districtsAPI.router)
app.include_router(departementsAPI.router)
app.include_router(partiesAPI.router)
app.include_router(resultsAPI.router)

@app.get("/")
def Index():
    return {"Message": "Hello World"}