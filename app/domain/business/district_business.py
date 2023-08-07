from app.domain.DTO.departmentDTO import DepartmentDTO

class DistrictBusiness :
    #TODO replace department_repo by department_business
    def __init__(self, district_repo, department_repo, result_business) -> None:
        self.district_repo = district_repo
        self.department_repo = department_repo
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
        
        departments_from_repo = self.department_repo.get_departments()
        
        for department_from_repo in departments_from_repo : 
            if department_from_repo.name == department_name : 
                department = department_from_repo
                break
            
        if department.name != "" :        
            districts = self.get_districts_by_department_id(department.id)        
            return districts
        else :
            return None
        
        
    #TODO méthode à changer ici
    def get_districts_by_voting_rate(self) : 
        districts = self.district_repo.get_districts()
        
        all_results = self.result_business.get_rounds_participation_sorted()
        
        all_first_round_result_sortered = self.__get_districts_sorted_by_result_specific_round(all_results["first_round"], districts)
        
        all_second_round_result_sortered = self.__get_districts_sorted_by_result_specific_round(all_results["second_round"], districts)
        
        results = {}
        results["first_round"] = all_first_round_result_sortered
        results["second_round"] = all_second_round_result_sortered
        
        return results
    
    
    def __get_districts_sorted_by_result_specific_round(self, results, districts) : 
        all_district_sorted = []
        all_first_round_result_sortered = results
        for result in all_first_round_result_sortered : 
            for district in districts : 
                if result.district_id == district.id : 
                    all_district_sorted.append(district)
                else :
                    continue
        return all_district_sorted