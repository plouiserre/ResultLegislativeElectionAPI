import unittest

from app.domain.factory.factoryresult import FactoryResult
from tests.assert_test import AssertTest

class FactoryResultTest(unittest.TestCase) : 
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.assert_test = AssertTest(self)
        
    def test_construct_result(self) : 
        factory = FactoryResult()
        
        result_dto = factory.construct_result(1, "Completed", 2, 876, 5, 0.65, 666, 78.8, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7)
        
        result_check = [1, "Completed", 2, 876, 5, 0.65, 666, 78.8, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7]
        self.assert_test.assert_result_dto(result_check, result_dto)