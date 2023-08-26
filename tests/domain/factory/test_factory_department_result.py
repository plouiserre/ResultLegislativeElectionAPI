import unittest

from app.domain.DTO.departmentresultDTO import DepartmentResultDTO
from app.domain.factory.factorydepartment import FactoryDepartment
from app.domain.factory.factorydepartmentresult import FactoryDepartmentResult
from tests.assert_test import AssertTest

class FactoryDepartmentResultTest(unittest.TestCase) : 
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.assert_test = AssertTest(self)
        
    
    def test_factory_department_result(self):
        factory_department = FactoryDepartment()
        dep = factory_department.construct_department_from_bdd([650, "Gironde", 33])
        rate_voting = 66.67
        
        factory = FactoryDepartmentResult()
        dep_result = factory.construct_department_result_from_department(dep, rate_voting)
        
        department_result_check = [650, "Gironde", 33, 66.67]
        self.assert_test.assert_department_result_dto(department_result_check, dep_result)