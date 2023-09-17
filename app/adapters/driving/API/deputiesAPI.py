from app.adapters.dependency.dependency_business import DependencyBusiness
from fastapi import APIRouter, Depends, HTTPException, status
from app.utils.helper import ManageHttpException

router = APIRouter()

def init_deputy_business() :
    dependency = DependencyBusiness()
    deputy_business = dependency.deputy_business
    return deputy_business


@router.get("/deputies/", tags=["deputies"])
async def get_deputies(dp_first_name : str ="", dp_last_name : str = "", cn_first_name : str = "", cn_last_name : str = "", deputy_business = Depends(init_deputy_business)) : 
    try :
        if cn_first_name != "" and cn_last_name != "":
            deputies_result =  deputy_business.get_deputy_from_candidate_identity(cn_first_name, cn_last_name)
            if deputies_result == None :
                raise HTTPException (status_code= status.HTTP_404_NOT_FOUND, detail= "No result")
        else :
            deputies_result = deputy_business.get_deputies(dp_first_name, dp_last_name)
        return deputies_result
    except Exception as e:
        ManageHttpException(e)  