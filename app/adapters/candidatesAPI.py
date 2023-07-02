from fastapi import APIRouter, Depends, HTTPException
from app.domain.candidatebusiness import CandidateBusiness


router = APIRouter()

def init_candidate_business() : 
    candidate_business = CandidateBusiness()
    return candidate_business


@router.get("/candidates/", tags=["candidates"])
async def get_candidates(candidate_business = Depends(init_candidate_business)):
    try :
        candidates_result = candidate_business.get_candidates()
        return candidates_result
    except : 
        raise HTTPException(status_code = 500, detail= "Treatment failed")