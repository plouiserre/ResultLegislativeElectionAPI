from app.domain.business.candidate_business import CandidateBusiness
from app.ports.MySql.cache import Cache
from app.ports.MySql.my_sql_candidate_repository import MySqlCandidateRepository
from app.ports.MySql.my_sql_party_repository import MySqlPartyRepository
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()

def init_candidate_business() : 
    cache = Cache()
    candidate_repo = MySqlCandidateRepository(cache)
    party_repo = MySqlPartyRepository(cache)
    candidate_business = CandidateBusiness(candidate_repo, party_repo)
    return candidate_business


@router.get("/candidates/", tags=["candidates"])
async def get_candidates(first_name : str ="", last_name: str = "", candidate_business = Depends(init_candidate_business)):
    try :
        candidates_result = candidate_business.get_candidates(first_name, last_name)
        return candidates_result
    except : 
        raise HTTPException(status_code = 500, detail= "Treatment failed")
    
    
@router.get("/candidates/parties/", tags=["candidates"])
async def get_candidates_by_party(party : str = "", candidate_business = Depends(init_candidate_business)) :
    try :
        candidates_result = candidate_business.get_candidates_by_party(party)
        return candidates_result
    except :
        raise HTTPException(status_code = 500, detail= "Treatment failed")