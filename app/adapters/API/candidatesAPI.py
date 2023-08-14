from app.domain.business.candidate_business import CandidateBusiness
from app.domain.business.department_business import DepartmentBusiness
from app.domain.business.district_business import DistrictBusiness
from app.domain.business.party_business import PartyBusiness
from app.domain.business.result_business import ResultBusiness
from app.ports.MySql.cache import Cache
from app.ports.MySql.my_sql_candidate_repository import MySqlCandidateRepository
from app.ports.MySql.my_sql_department_repository import MySqlDepartmentRepository
from app.ports.MySql.my_sql_district_repository import MySqlDistrictRepository
from app.ports.MySql.my_sql_party_repository import MySqlPartyRepository
from app.ports.MySql.my_sql_result_repository import MySqlResultRepository
from app.utils.helper import ManageHttpException
from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter()
#TODO find a way to test all init
def init_candidate_business() : 
    cache = Cache()
    candidate_repo = MySqlCandidateRepository(cache)
    party_repo = MySqlPartyRepository(cache)
    party_business = PartyBusiness(party_repo)
    department_repo = MySqlDepartmentRepository(cache)
    department_business = DepartmentBusiness(department_repo)
    result_repo = MySqlResultRepository(cache)
    district_repo = MySqlDistrictRepository(cache)
    result_business = ResultBusiness(result_repo)
    district_business = DistrictBusiness(district_repo, department_repo, result_business)
    candidate_business = CandidateBusiness(candidate_repo, party_business, department_business, district_business)
    return candidate_business

@router.get("/candidates/", tags=["candidates"])
async def get_candidates(first_name : str ="", last_name: str = "", candidate_business = Depends(init_candidate_business)):
    try :
        candidates_result = candidate_business.get_candidates(first_name, last_name)
        return candidates_result
    except : 
        raise HTTPException(status_code = 500, detail= "Treatment failed")
    
#TODO corriger cette méthode pour qu'elle respecte la bonne convention de nommage
@router.get("/candidates/parties/", tags=["candidates"])
async def get_candidates_by_party(party : str = "", candidate_business = Depends(init_candidate_business)) :
    try :
        candidates_result = candidate_business.get_candidates_by_party(party)
        if candidates_result == None :
            raise HTTPException (status_code= status.HTTP_404_NOT_FOUND, detail = "No result")
        return candidates_result
    except Exception as e:
        ManageHttpException(e)
    
#TODO corriger cette méthode pour qu'elle respecte la bonne convention de nommage
@router.get("/candidates/departments/", tags=["candidates"])
async def get_candidates_by_department(department: str ="", candidate_business = Depends(init_candidate_business)):
    try :
        candidates_result = candidate_business.get_candidates_by_departement(department)
        if candidates_result == None : 
            raise HTTPException (status_code= status.HTTP_404_NOT_FOUND, detail= "No result")
        return candidates_result
    except Exception as e:
        ManageHttpException(e)
    
#TODO corriger cette méthode pour qu'elle respecte la bonne convention de nommage
@router.get("/candidates/districts/{district_id}")
async def get_candidates_by_district(district_id , candidate_business = Depends(init_candidate_business)):
    try :
        candidates_result = candidate_business.get_candidates_by_district(district_id)
        if candidates_result == None : 
            raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail = "No result")
        return candidates_result
    except Exception as e:
        ManageHttpException(e)