from app.domain.business.department_business import DepartmentBusiness
from app.domain.business.district_business import DistrictBusiness
from app.domain.business.result_business import ResultBusiness
from app.ports.MySql.cache import Cache
from app.ports.MySql.my_sql_department_repository import MySqlDepartmentRepository
from app.ports.MySql.my_sql_district_repository import MySqlDistrictRepository
from app.ports.MySql.my_sql_result_repository import MySqlResultRepository
from app.utils.helper import ManageHttpException

from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter()

def init_district_business():
    cache = Cache()
    district_repo = MySqlDistrictRepository(cache)
    department_repo = MySqlDepartmentRepository(cache)
    department_business = DepartmentBusiness(department_repo)
    result_repo = MySqlResultRepository(cache)
    result_business = ResultBusiness(result_repo)
    district_business = DistrictBusiness(district_repo, department_business, result_business)
    return district_business


@router.get("/districts/", tags=["districts"])
async def get_districts_from_department(department: str = "", sort : str = "", district_business = Depends(init_district_business)) : 
    try : 
        if sort == "result" : 
            districts_result = district_business.get_districts_by_voting_rate()
        else :
            districts_result = district_business.get_districts_by_department_name(department)
            if districts_result == None : 
                raise HTTPException (status_code= status.HTTP_404_NOT_FOUND, detail = "No result")            
        return districts_result
    except Exception as e :
        ManageHttpException(e)