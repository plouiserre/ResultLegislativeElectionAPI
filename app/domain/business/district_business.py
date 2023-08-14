from app.domain.DTO.departmentDTO import DepartmentDTO
from app.domain.factory.factorydistrictresult import FactoryDistrictResult

class DistrictBusiness :
    #TODO replace department_repo by department_business
    def __init__(self, district_repo, department_business, result_business) -> None:
        self.district_repo = district_repo
        self.department_business = department_business
        self.result_business = result_business
        
    
    def get_districts(self) : 
        districts = self.district_repo.get_districts()
        return districts
    
    
    def get_districts_by_department_id(self, department_id):
        districts = []
        
        districts_from_repo = self.get_districts()
        
        for district_from_repo in districts_from_repo :
            if district_from_repo.department_id == department_id : 
                districts.append(district_from_repo)
                
        return districts
    
    
    def get_districts_by_department_name(self, department_name) : 
        districts = []
        department = DepartmentDTO()
        
        departments_from_repo = self.department_business.get_departments()
        
        for department_from_repo in departments_from_repo : 
            if department_from_repo.name == department_name : 
                department = department_from_repo
                break
            
        if department.name != "" :        
            districts = self.get_districts_by_department_id(department.id)        
            return districts
        else :
            return None
        
        
    def get_districts_by_voting_rate(self) : 
        districts = self.district_repo.get_districts()
        
        all_results = self.result_business.get_rounds_participation_sorted()        
                    
        
        all_first_round_districts_results_sortered = self.__get_districts_results_by_round(all_results["first_round"], districts)
        
        all_second_round_districts_results_sortered = self.__get_districts_results_by_round(all_results["second_round"], districts)
        
        results = {}
        results["first_round"] = all_first_round_districts_results_sortered
        results["second_round"] = all_second_round_districts_results_sortered
        
        return results
    
    
    def __get_districts_results_by_round(self, results, districts):
        factory = FactoryDistrictResult()        
        districts_results_sortered = []
        for result in results : 
            for district in districts : 
                if result.district_id == district.id :
                    department_name = self.department_business.get_department_name_from_department_id(district.department_id)
                    district_result = factory.construct_district_result(district, result.rate_voting, department_name)
                    districts_results_sortered.append(district_result)
                    break
        return districts_results_sortered