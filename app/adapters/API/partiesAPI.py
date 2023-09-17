from app.utils.helper import ManageHttpException
from app.adapters.dependency.dependency_business import DependencyBusiness
from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter()
def init_party_business() : 
    dependency = DependencyBusiness()
    party_business = dependency.party_business
    return party_business


@router.get("/parties/", tags=["parties"])
async def get_parties(sort : str ="", top : int = 0, party_business = Depends(init_party_business)) : 
    try : 
        if top > 0 and sort == "rate_voting":
            results = party_business.get_top_candidates_for_each_party_all_rounds(top)
            return results
        else :            
            raise HTTPException (status_code= status.HTTP_400_BAD_REQUEST, detail= "Bad request dumbass")
    except Exception as e : 
        ManageHttpException(e)