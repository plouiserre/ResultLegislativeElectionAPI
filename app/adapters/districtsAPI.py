from app.domain.business.district_business import DistrictBusiness
from app.ports.MySql.cache import Cache
from app.ports.MySql.my_sql_department_repository import MySqlDepartmentRepository
from app.ports.MySql.my_sql_district_repository import MySqlDistrictRepository
from app.utils.helper import ManageHttpException

from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter()

#TODO see how to test that to fail when something is wrong
def init_district_business():
    cache = Cache()
    district_repo = MySqlDistrictRepository(cache)
    department_repo = MySqlDepartmentRepository(cache)
    district_business = DistrictBusiness(district_repo, department_repo)
    return district_business


@router.get("/districts/", tags=["districts"])
async def get_districts_from_department(department: str = "", district_business = Depends(init_district_business)) : 
    try : 
        districts_result = district_business.get_districts_by_department_name(department)
        if districts_result == None : 
            raise HTTPException (status_code= status.HTTP_404_NOT_FOUND, detail = "No result")            
        return districts_result
    except Exception as e :
        ManageHttpException(e)