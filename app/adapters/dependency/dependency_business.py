from app.domain.business.candidate_business import CandidateBusiness
from app.domain.business.department_business import DepartmentBusiness
from app.domain.business.district_business import DistrictBusiness
from app.domain.business.deputy_business import DeputyBusiness
from app.domain.business.party_business import PartyBusiness
from app.domain.business.result_business import ResultBusiness
from app.ports.MySql.cache import Cache
from app.ports.MySql.my_sql_candidate_repository import MySqlCandidateRepository
from app.ports.MySql.my_sql_department_repository import MySqlDepartmentRepository
from app.ports.MySql.my_sql_deputy_repository import MySqlDeputyRepository
from app.ports.MySql.my_sql_district_repository import MySqlDistrictRepository
from app.ports.MySql.my_sql_party_repository import MySqlPartyRepository
from app.ports.MySql.my_sql_result_repository import MySqlResultRepository

class DependencyBusiness : 
    def __init__(self) -> None:
        cache = Cache()
        candidate_repo = MySqlCandidateRepository(cache)
        party_repo = MySqlPartyRepository(cache)
        department_repo = MySqlDepartmentRepository(cache)
        deputy_repo = MySqlDeputyRepository(cache)
        result_repo = MySqlResultRepository(cache)
        district_repo = MySqlDistrictRepository(cache)
        self.party_business = PartyBusiness(party_repo)
        self.result_business = ResultBusiness(result_repo)
        self.department_business = DepartmentBusiness(department_repo)
        self.district_business = DistrictBusiness(district_repo, self.department_business, self.result_business)
        self.candidate_business = CandidateBusiness(candidate_repo, self.party_business, self.department_business, self.district_business)
        self.deputy_business = DeputyBusiness(deputy_repo, self.candidate_business)