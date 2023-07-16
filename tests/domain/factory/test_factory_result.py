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
        
        
    #TODO add district id in result_check later
    def test_construct_result_from_bdd(self) : 
        factory = FactoryResult()
        
        #last one district_id useless for the moment
        result_data = [1150, 1,	"Completed", 86187, 43652, 50.65,	42535, 49.35, 490, 0.57, 1.15, 234,	0.27, 0.55,	41811, 48.51, 98.3,	576]
        result_dto = factory.construct_result_from_bdd(result_data)
        
        result_check = [1150, "Completed", 1, 86187, 43652, 50.65, 42535, 49.35, 490, 0.57, 1.15, 234, 0.27, 0.55, 41811, 48.51, 98.3]
        self.assert_test.assert_result_dto(result_check, result_dto)