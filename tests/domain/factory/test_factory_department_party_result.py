import unittest

from app.domain.factory.factorydepartmentpartyresult import FactoryDeartmentPartyResult
from tests.assert_test import AssertTest

class FactoryDepartmentPartyResult(unittest.TestCase) :
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.assert_test = AssertTest(self)
        
    
    def test_factory_department_party_result(self) : 
        factory_department_party_result = FactoryDeartmentPartyResult()
        dep_party_result = factory_department_party_result.construct_department_party_result(650, "Gironde", 33, 66.67)
        
        department_result_check = [650, "Gironde", 33, 66.67]
        self.assert_test.assert_department_party_result_dto(department_result_check, dep_party_result)