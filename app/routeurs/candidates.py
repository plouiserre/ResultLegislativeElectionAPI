from fastapi import APIRouter

router = APIRouter()

@router.get("/candidates/", tags=["candidates"])
async def get_candidates():
    json = [{"LastName" : "Cazenave", "FirstName" : "Thomas", "Sexe" : "M"}, {"LastName" : "TRASTOUR-ISNART", "FirstName" : "Laurence", "Sexe" : "F"}]
    return json