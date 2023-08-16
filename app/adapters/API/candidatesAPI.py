from app.utils.helper import ManageHttpException
from app.adapters.dependency.dependency_business import DependencyBusiness
from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter()
def init_candidate_business() : 
    dependency = DependencyBusiness()
    candidate_business = dependency.candidate_business
    return candidate_business

@router.get("/candidates/", tags=["candidates"])
async def get_candidates(first_name : str ="", last_name: str = "", party : str = "", department: str ="", district : int = 0, candidate_business = Depends(init_candidate_business)):
    try :
        if party != "" : 
            candidates_result = candidate_business.get_candidates_by_party(party)
        elif department != "" : 
            candidates_result = candidate_business.get_candidates_by_departement(department)
        elif district != 0 :
            candidates_result = candidate_business.get_candidates_by_district(district)
        else :
            candidates_result = candidate_business.get_candidates(first_name, last_name)
        if candidates_result == None : 
            raise HTTPException (status_code= status.HTTP_404_NOT_FOUND, detail= "No result")
        return candidates_result
    except Exception as e: 
        ManageHttpException(e)  