from app.adapters.dependency.dependency_business import DependencyBusiness
from app.utils.helper import ManageHttpException

from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter()

def init_district_business():
    dependency = DependencyBusiness()
    district_business = dependency.district_business
    return district_business


@router.get("/districts/", tags=["districts"])
async def get_districts(department: str = "", sort : str = "",  type : str  = "", district_business = Depends(init_district_business)) : 
    try : 
        if sort == "result" : 
            if type =="ascending" or type == "descending" : 
                districts_result = district_business.get_districts_by_voting_rate(type)
            else :
                raise HTTPException (status_code= status.HTTP_400_BAD_REQUEST, detail= "Bad Request")
        else :
            districts_result = district_business.get_districts_by_department_name(department)
            if districts_result == None : 
                raise HTTPException (status_code= status.HTTP_404_NOT_FOUND, detail = "No result")            
        return districts_result
    except Exception as e :
        ManageHttpException(e)