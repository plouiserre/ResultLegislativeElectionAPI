from app.domain.business.candidate_business import CandidateBusiness
from app.domain.business.department_business import DepartmentBusiness
from app.domain.business.deputy_business import DeputyBusiness
from app.domain.business.district_business import DistrictBusiness
from app.domain.business.party_business import PartyBusiness
from app.domain.business.result_business import ResultBusiness
from fastapi import APIRouter, Depends, HTTPException, status
from app.ports.MySql.cache import Cache
from app.ports.MySql.my_sql_candidate_repository import MySqlCandidateRepository
from app.ports.MySql.my_sql_department_repository import MySqlDepartmentRepository
from app.ports.MySql.my_sql_deputy_repository import MySqlDeputyRepository
from app.ports.MySql.my_sql_district_repository import MySqlDistrictRepository
from app.ports.MySql.my_sql_party_repository import MySqlPartyRepository
from app.ports.MySql.my_sql_result_repository import MySqlResultRepository
from app.utils.helper import ManageHttpException

router = APIRouter()

def init_deputy_business() :
    cache = Cache()
    candidate_repo = MySqlCandidateRepository(cache)
    department_repo = MySqlDepartmentRepository(cache)
    deputy_repo = MySqlDeputyRepository(cache)
    district_repo = MySqlDistrictRepository(cache)
    party_repo = MySqlPartyRepository(cache)
    result_repo = MySqlResultRepository(cache)
    department_business = DepartmentBusiness(department_repo)
    result_business = ResultBusiness(result_repo)
    district_business = DistrictBusiness(district_repo, department_business, result_business)
    party_business = PartyBusiness(party_repo)
    candidate_business = CandidateBusiness(candidate_repo, party_business, department_business, district_business)
    deputy_business = DeputyBusiness(deputy_repo, candidate_business)
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