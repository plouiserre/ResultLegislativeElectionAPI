from app.domain.business.result_business import ResultBusiness
from app.ports.InMemory.in_memory_result_repository import InMemoryResultRepository
from fastapi import HTTPException, APIRouter, Depends

router = APIRouter()

def init_result_business() :
    repo = InMemoryResultRepository()
    result_business = ResultBusiness(repo)
    return result_business

@router.get("/results/", tags= ["results"])
async def get_results(result_business = Depends(init_result_business)):
    try :
        results = result_business.get_results()
        return results
    except :
        raise HTTPException(status_code = 500, detail= "Treatment failed")