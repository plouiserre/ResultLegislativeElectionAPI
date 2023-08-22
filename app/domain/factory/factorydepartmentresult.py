from app.domain.DTO.departmentresultDTO import DepartmentResultDTO

class FactoryDepartmentResult:
    def construct_department_result_from_department(self, department, rate_voting) :
        department_result = DepartmentResultDTO()
        department_result.id = department.id
        department_result.name = department.name
        department_result.number = department.number
        department_result.rate_voting = rate_voting
        return department_result
    
    
    def construct_department_result(self, id, name, number, rate_voting) :
        department_result = DepartmentResultDTO()
        department_result.id = id
        department_result.name = name
        department_result.number = number
        department_result.rate_voting = rate_voting
        return department_result