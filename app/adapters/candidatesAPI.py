from app.domain.business.candidate_business import CandidateBusiness
from app.ports.InMemory.in_memory_candidate_repository import InMemoryCandidateRepository
from app.ports.InMemory.in_memory_party_repository import InMemoryPartyRepository
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()

def init_candidate_business() : 
    candidate_repo = InMemoryCandidateRepository()
    party_repo = InMemoryPartyRepository()
    candidate_business = CandidateBusiness(candidate_repo, party_repo)
    return candidate_business


@router.get("/candidates/", tags=["candidates"])
async def get_candidates(first_name : str ="", last_name: str = "", candidate_business = Depends(init_candidate_business)):
    try :
        candidates_result = candidate_business.get_candidates(first_name, last_name)
        return candidates_result
    except : 
        raise HTTPException(status_code = 500, detail= "Treatment failed")