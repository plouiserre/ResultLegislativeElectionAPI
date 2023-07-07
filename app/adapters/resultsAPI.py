from app.domain.result_business import ResultBusiness
from fastapi import HTTPException, APIRouter, Depends

router = APIRouter()

def init_result_business() :
    result_business = ResultBusiness()
    return result_business

@router.get("/results/", tags= ["results"])
async def get_results(result_business = Depends(init_result_business)):
    try :
        results = result_business.get_results()
        return results
    except :
        raise HTTPException(status_code = 500, detail= "Treatment failed")