from app.domain.business.result_business import ResultBusiness
from app.adapters.driven.MySql.cache import Cache
from app.adapters.driven.MySql.my_sql_result_repository import MySqlResultRepository
from app.utils.helper import ManageHttpException
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
    except Exception as e :
        ManageHttpException(e)