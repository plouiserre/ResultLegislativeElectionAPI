from app.domain.DTO.departmentDTO import DepartmentDTO

class DistrictBusiness :
    
    def __init__(self, district_repo, department_repo) -> None:
        self.district_repo = district_repo
        self.department_repo = department_repo
    
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