class DistrictBusiness :
    
    def __init__(self, district_repo) -> None:
        self.district_repo = district_repo
    
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