import unittest

from app.domain.factory.factorydepartment import FactoryDepartment
from tests.assert_test import AssertTest

class FactoryDepartementTest(unittest.TestCase): 
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.assert_test = AssertTest(self)
        
    def test_construct_department_from_bdd(self):
        factory = FactoryDepartment()
        
        department_data = [139, "Gironde", 33]
        department = factory.construct_department_from_bdd(department_data)
        
        self.assert_test.assert_department_dto(department_data, department)
        
        