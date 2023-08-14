class DepartmentBusiness : 
    
    def __init__(self, department_repo) -> None:
        self.department_repo = department_repo
        
    
    def get_departments(self) : 
        departments = self.department_repo.get_departments()
        return departments
    
    
    def get_department_by_name(self, department_name):
        department_result = None
        departments = self.get_departments()
        
        for department in departments:
            if department.name == department_name : 
                department_result = department
                break
        return department_result
    
    
    def get_department_name_from_department_id(self, department_id) : 
        department_name = ""
        departments = self.department_repo.get_departments()
       
        for department in departments : 
           if department.id == department_id : 
               department_name = department.name
               break
        
        return department_name