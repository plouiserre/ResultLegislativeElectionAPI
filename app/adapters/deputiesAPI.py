from app.domain.deputy_business import DeputyBusiness
from fastapi import APIRouter, Depends, HTTPException
from app.ports.in_memory_deputy_repository import InMemoryDeputyRepository

router = APIRouter()

def init_deputy_business() :
    repo = InMemoryDeputyRepository()
    deputy_business = DeputyBusiness(repo)
    return deputy_business


@router.get("/deputies/", tags=["deputies"])
async def get_deputies(deputy_business = Depends(init_deputy_business)) : 
    try :
        deputies_result = deputy_business.get_deputies()
        return deputies_result
    except :
        raise HTTPException(status_code = 500, detail= "Treatment failed")