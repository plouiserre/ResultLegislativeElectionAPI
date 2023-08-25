from app.adapters.dependency.dependency_business import DependencyBusiness
from app.utils.helper import ManageHttpException

from fastapi import APIRouter, Depends

router = APIRouter()

def init_department_business():
    dependency = DependencyBusiness()
    department_business = dependency.department_business
    return department_business
    

@router.get("/departments/", tags=["departments"])
async def get_departments(sort : str = "", department_business = Depends(init_department_business)): 
    try : 
        if sort == "result" : 
            department_results = department_business.get_departments_by_voting_rate()
        else : 
            department_results = department_business.get_departments()
        return department_results
    except Exception as e :
        ManageHttpException(e)