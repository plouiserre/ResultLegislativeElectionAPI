from app.domain.DTO.departmentDTO import DepartmentDTO

class FactoryDepartment:
    def construct_department_from_bdd(self, department_data):
        department = DepartmentDTO()
        department.id = department_data[0]
        department.name = department_data[1]
        department.number = department_data[2]
        return department