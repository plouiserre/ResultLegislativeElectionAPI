from app.domain.business.result_business import ResultBusiness
from app.ports.MySql.cache import Cache
from app.ports.MySql.my_sql_result_repository import MySqlResultRepository
from fastapi import HTTPException, APIRouter, Depends

router = APIRouter()

def init_result_business() :
    cache = Cache()
    repo = MySqlResultRepository(cache)
    result_business = ResultBusiness(repo)
    return result_business

@router.get("/results/", tags= ["results"])
async def get_results(result_business = Depends(init_result_business)):
    try :
        results = result_business.get_results()
        return results
    except :
        raise HTTPException(status_code = 500, detail= "Treatment failed")