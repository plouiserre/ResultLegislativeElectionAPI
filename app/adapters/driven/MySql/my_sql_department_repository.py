from app.domain.factory.factorydepartment import FactoryDepartment
from app.domain.repository.department_repository import DepartmentRepository
from app.adapters.driven.MySql.my_db import MyDb

class MySqlDepartmentRepository(DepartmentRepository) :
    def __init__(self, cache) -> None:
        self.my_db = MyDb()
        self.__cache = cache
        
        
    def get_departments(self) : 
        departments = []
        
        if self.__cache.is_datas_cached("departments"):
            departments = self.__cache.get_datas("departments")
        else : 
            connexion = self.my_db.get_my_db()
            
            my_cursor = connexion.cursor()
            
            my_cursor.execute("SELECT * FROM ELECTIONSCONGRESSMANS.DEPARTMENT")
            
            departments_bdd = my_cursor.fetchall()
            
            factory = FactoryDepartment()
            for department_bdd in departments_bdd : 
                department = factory.construct_department_from_bdd(department_bdd)
                departments.append(department)
                
            self.__cache.add_datas(departments, "departments")
                
        return departments