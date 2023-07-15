from app.domain.business.candidate_business import CandidateBusiness
from app.ports.InMemory.in_memory_candidate_repository import InMemoryCandidateRepository
from app.ports.MySql.my_sql_candidate_repository import MySqlCandidateRepository
from app.ports.MySql.my_sql_party_repository import MySqlPartyRepository
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()

def init_candidate_business() : 
    candidate_repo = MySqlCandidateRepository()
    party_repo = MySqlPartyRepository()
    candidate_business = CandidateBusiness(candidate_repo, party_repo)
    return candidate_business


@router.get("/candidates/", tags=["candidates"])
async def get_candidates(first_name : str ="", last_name: str = "", candidate_business = Depends(init_candidate_business)):
    try :
        candidates_result = candidate_business.get_candidates(first_name, last_name)
        return candidates_result
    except : 
        raise HTTPException(status_code = 500, detail= "Treatment failed")