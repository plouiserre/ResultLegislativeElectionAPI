import unittest

from app.domain.factory.factoryresult import FactoryResult
from app.domain.business.result_business import ResultBusiness
from ports.InMemory.test_in_memory_result_repository import InMemoryResultRepository
from tests.assert_test import AssertTest
from unittest.mock import patch

class ResultBusinessTest(unittest.TestCase) :
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.assert_test = AssertTest(self)
        
    def __get_results(self) :
        factory = FactoryResult()
        first_result = factory.construct_result(1, "Completed", 2, 876, 5, 0.65, 666, 78.8, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7)
        second_result = factory.construct_result(2, "Completed", 1, 276, 23, 1.65, 866, 68.8, 3, 5.2, 1.7, 566, 88.8, 3, 5.2, 1.7, 2.7)
        third_result = factory.construct_result(3, "Completed", 2, 576, 23, 8.65, 566, 68.8, 8, 8.2, 8.7, 605, 68.8, 13, 3.2, 4.7, 5.7)
        fourth_result = factory.construct_result(4, "Completed", 1, 676, 50, 10.65, 266, 28.8, 5, 23.2, 4.7, 266, 48.8, 8, 4.2, 2.7, 0.9)
        results = [first_result, second_result, third_result, fourth_result]
        return results
        
        
    @patch.object(InMemoryResultRepository, 'get_results')
    def test_get_results(self, mock_result_repository) :
        mock_result_repository.get_results.return_value = self.__get_results()
        business = ResultBusiness(mock_result_repository)
        
        results = business.get_results()
        
        self.assertEqual(4, len(results))
        
        first_result = results[0]
        first_result_check = [1, "Completed", 2, 876, 5, 0.65, 666, 78.8, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7]
        self.assert_test.assert_result_dto(first_result_check, first_result)
        
        second_result = results[1]
        second_result_check = [2, "Completed", 1, 276, 23, 1.65, 866, 68.8, 3, 5.2, 1.7, 566, 88.8, 3, 5.2, 1.7, 2.7]
        self.assert_test.assert_result_dto(second_result_check, second_result)
        
        third_result = results[2]
        third_result_check = [3, "Completed", 2, 576, 23, 8.65, 566, 68.8, 8, 8.2, 8.7, 605, 68.8, 13, 3.2, 4.7, 5.7]
        self.assert_test.assert_result_dto(third_result_check, third_result)
       
        fourth_result = results[3]
        fourth_result_check = [4, "Completed", 1, 676, 50, 10.65, 266, 28.8, 5, 23.2, 4.7, 266, 48.8, 8, 4.2, 2.7, 0.9]
        self.assert_test.assert_result_dto(fourth_result_check, fourth_result)