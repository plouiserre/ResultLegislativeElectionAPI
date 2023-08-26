from app.adapters.dependency.dependency_business import DependencyBusiness
from app.utils.helper import ManageHttpException

from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter()

def init_department_business():
    dependency = DependencyBusiness()
    department_business = dependency.department_business
    return department_business
    

@router.get("/departments/", tags=["departments"])
async def get_departments(sort : str = "", type : str ="", department_business = Depends(init_department_business)): 
    try : 
        if sort == "result" : 
            if type == "ascending" or type == "descending":
                department_results = department_business.get_departments_by_voting_rate(type)
            else :
                raise HTTPException (status_code= status.HTTP_400_BAD_REQUEST, detail= "Bad Request")
        else : 
            department_results = department_business.get_departments()
        return department_results
    except Exception as e :
        ManageHttpException(e)