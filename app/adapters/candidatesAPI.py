from app.domain.business.candidate_business import CandidateBusiness
from app.domain.business.department_business import DepartmentBusiness
from app.domain.business.district_business import DistrictBusiness
from app.domain.business.party_business import PartyBusiness
from app.ports.MySql.cache import Cache
from app.ports.MySql.my_sql_candidate_repository import MySqlCandidateRepository
from app.ports.MySql.my_sql_department_repository import MySqlDepartmentRepository
from app.ports.MySql.my_sql_district_repository import MySqlDistrictRepository
from app.ports.MySql.my_sql_party_repository import MySqlPartyRepository
from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter()

def init_candidate_business() : 
    cache = Cache()
    candidate_repo = MySqlCandidateRepository(cache)
    party_repo = MySqlPartyRepository(cache)
    party_business = PartyBusiness(party_repo)
    department_repo = MySqlDepartmentRepository(cache)
    department_business = DepartmentBusiness(department_repo)
    district_repo = MySqlDistrictRepository(cache)
    district_business = DistrictBusiness(district_repo)
    candidate_business = CandidateBusiness(candidate_repo, party_business, department_business, district_business)
    return candidate_business


#TODO add 404 error in this method
@router.get("/candidates/", tags=["candidates"])
async def get_candidates(first_name : str ="", last_name: str = "", candidate_business = Depends(init_candidate_business)):
    try :
        candidates_result = candidate_business.get_candidates(first_name, last_name)
        return candidates_result
    except : 
        raise HTTPException(status_code = 500, detail= "Treatment failed")
    

#TODO add 404 error in this method    
@router.get("/candidates/parties/", tags=["candidates"])
async def get_candidates_by_party(party : str = "", candidate_business = Depends(init_candidate_business)) :
    try :
        candidates_result = candidate_business.get_candidates_by_party(party)
        return candidates_result
    except :
        raise HTTPException(status_code = 500, detail= "Treatment failed")
    
    
#TODO factoriser la partie exception
@router.get("/candidates/departments/", tags=["candidates"])
async def get_candidates_by_department(department: str ="", candidate_business = Depends(init_candidate_business)):
    try :
        candidates_result = candidate_business.get_candidates_by_departement(department)
        if candidates_result == None : 
            raise HTTPException (status_code= status.HTTP_404_NOT_FOUND, detail= "No result")
        return candidates_result
    except Exception as e:
        status_code = 500
        detail_message = "Treatment failed"
        if type(e) == HTTPException :
            status_code = e.status_code
            detail_message = "No result"
        raise HTTPException(status_code = status_code, detail= detail_message)
    
    
@router.get("/candidates/districts/{district_id}")
async def get_candidates_by_district(district_id , candidate_business = Depends(init_candidate_business)):
    try :
        candidates_result = candidate_business.get_candidates_by_district(district_id)
        if candidates_result == None : 
            raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail = "No result")
        return candidates_result
    except Exception as e:
        status_code = 500
        detail_message = "Treatment failed"
        if type(e) == HTTPException :
            status_code = e.status_code
            detail_message = "No result"
        raise HTTPException(status_code = status_code, detail = detail_message)