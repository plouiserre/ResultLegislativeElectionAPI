from app.domain.business.deputy_business import DeputyBusiness
from fastapi import APIRouter, Depends, HTTPException, status
from app.ports.in_memory_candidate_repository import InMemoryCandidateRepository
from app.ports.in_memory_deputy_repository import InMemoryDeputyRepository

router = APIRouter()

def init_deputy_business() :
    deputy_repo = InMemoryDeputyRepository()
    candidate_repo = InMemoryCandidateRepository()
    deputy_business = DeputyBusiness(deputy_repo, candidate_repo)
    return deputy_business


@router.get("/deputies/", tags=["deputies"])
async def get_deputies(first_name : str ="", last_name : str = "", deputy_business = Depends(init_deputy_business)) : 
    try :
        deputies_result = deputy_business.get_deputies(first_name, last_name)
        return deputies_result
    except :
        raise HTTPException(status_code = 500, detail= "Treatment failed")
    

@router.get("/deputies/candidates", tags=["deputies"])
async def get_deputies_from_candidates(first_name : str = "", last_name : str = "", deputy_business = Depends(init_deputy_business)) :
    try :
        deputy_result =  deputy_business.get_deputy_from_candidate_identity(first_name, last_name)
        if deputy_result == None :
            raise HTTPException (status_code= status.HTTP_404_NOT_FOUND, detail= "No result")
        return deputy_result
    except Exception as e:
        status_code = 500
        detail_message = "Treatment failed"
        if type(e) == HTTPException :
            status_code = e.status_code
            detail_message = "No result"
        raise HTTPException(status_code = status_code, detail= detail_message)