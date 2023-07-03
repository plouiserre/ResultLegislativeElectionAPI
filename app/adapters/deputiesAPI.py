from fastapi import APIRouter

router = APIRouter()

@router.get("/deputies", tags=["deputies"])
async def get_deputies() : 
    json = [{"LastName":"CARPENTIER", "FirstName":"Julien", "Sexe":"M"},{"LastName":"DUFREGNE", "FirstName":"Jean-Paul", "Sexe":"M"},{"LastName":"BENOIT-GOLA", "FirstName":"Anne-Cécile", "Sexe":"F"}]
    return json