import unittest

from app.domain.business.department_business import DepartmentBusiness
from app.domain.factory.factorydepartment import FactoryDepartment
from app.ports.MySql.my_sql_department_repository import MySqlDepartmentRepository
from tests.assert_test import AssertTest
from unittest.mock import patch

class DepartmentBusinessTest(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.assert_test = AssertTest(self)
        
        
    def __get_departments(self) :
        factory = FactoryDepartment()
        departments = []
        first_department = factory.construct_department_from_bdd([1, "Ain", 1])
        second_department = factory.construct_department_from_bdd([2, "Aisne", 2])
        third_department = factory.construct_department_from_bdd([3, "Allier", 3])
        thirty_third_department = factory.construct_department_from_bdd([33, "Gironde", 33])
        departments = [first_department, second_department, third_department, thirty_third_department]
        return departments
    
    
    @patch.object(MySqlDepartmentRepository, "get_departments")
    def test_get_departments(self, mock_repo):
        mock_repo.get_departments.return_value = self.__get_departments()
        
        business = DepartmentBusiness(mock_repo)
        
        departments = business.get_departments()
        
        self.assertEqual(4, len(departments))
        
        department_check = [1, "Ain", 1]
        self.assert_test.assert_department_dto(department_check, departments[0])
        
        department_check = [2, "Aisne", 2]
        self.assert_test.assert_department_dto(department_check, departments[1])
        
        department_check = [3, "Allier", 3]
        self.assert_test.assert_department_dto(department_check, departments[2])
        
        department_check = [33, "Gironde", 33]
        self.assert_test.assert_department_dto(department_check, departments[3])
        
        
    @patch.object(MySqlDepartmentRepository, "get_departments")
    def test_get_departments_by_name(self, mock_repo):
        mock_repo.get_departments.return_value = self.__get_departments()
        
        business = DepartmentBusiness(mock_repo)
        
        department = business.get_department_by_name("Gironde")
        
        department_check = [33, "Gironde", 33]
        self.assert_test.assert_department_dto(department_check, department)
