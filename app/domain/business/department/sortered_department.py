

class SorteredDepartment : 
    def __init__(self, departments, districts) -> None:
        self.departments = departments
        self.districts = districts
    
    
    def departments_sortered_by_districts(self) : 
        results = {}
        for department in self.departments : 
            for district in self.districts : 
                if district.department_id == department.id : 
                    results[district.id] = department
        return results