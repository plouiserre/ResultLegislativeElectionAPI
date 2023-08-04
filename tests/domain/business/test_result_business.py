import unittest

from app.domain.factory.factoryresult import FactoryResult
from app.domain.business.result_business import ResultBusiness
from app.domain.repository.result_repository import ResultRepository
from tests.assert_test import AssertTest
from unittest.mock import patch

##TODO simply data replacing by XXX useless value
##TODO rename to simplify method test

class ResultBusinessTest(unittest.TestCase) :
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.assert_test = AssertTest(self)
        
    def __get_results_from_two_rounds(self) :
        factory = FactoryResult()
        first_result = factory.construct_result(1, "Completed", 2, 876, 5, 0.65, 666, 78.8, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 23)
        second_result = factory.construct_result(2, "Completed", 1, 276, 23, 1.65, 866, 68.8, 3, 5.2, 1.7, 566, 88.8, 3, 5.2, 1.7, 2.7, 24)
        third_result = factory.construct_result(3, "Completed", 2, 576, 23, 8.65, 566, 68.8, 8, 8.2, 8.7, 605, 68.8, 13, 3.2, 4.7, 5.7, 25)
        fourth_result = factory.construct_result(4, "Completed", 1, 676, 50, 10.65, 266, 28.8, 5, 23.2, 4.7, 266, 48.8, 8, 4.2, 2.7, 0.9, 26)
        results = [first_result, second_result, third_result, fourth_result]
        return results
    
    
    def __get_results_first_rounds(self) :
        factory = FactoryResult()
        first_result = factory.construct_result(1, "Completed", 1, 876, 5, 0.65, 666, 78.8, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 23)
        second_result = factory.construct_result(2, "Completed", 1, 276, 23, 1.65, 866, 68.8, 3, 5.2, 1.7, 566, 88.8, 3, 5.2, 1.7, 2.7, 24)
        third_result = factory.construct_result(3, "Completed", 1, 576, 23, 8.65, 566, 15.8, 8, 8.2, 8.7, 605, 68.8, 13, 3.2, 4.7, 5.7, 25)
        fourth_result = factory.construct_result(4, "Completed", 1, 676, 50, 10.65, 266, 28.8, 5, 23.2, 4.7, 266, 48.8, 8, 4.2, 2.7, 0.9, 26)
        results = [first_result, second_result, third_result, fourth_result]
        return results
    
    
    def __get_eight_results_first_round(self): 
        factory = FactoryResult()
        fifth_result = factory.construct_result(5, "Completed", 1, 876, 5, 0.65, 666, 99.56, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 23)
        sixth_result = factory.construct_result(6, "Completed", 1, 876, 5, 0.65, 666, 65.2, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 24)
        seventh_result = factory.construct_result(7, "Completed", 1, 876, 5, 0.65, 666, 0.45, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 25)
        eighth_result = factory.construct_result(8, "Completed", 1, 876, 5, 0.65, 666, 42.6, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 26)
        results = self.__get_results_first_rounds()
        results.append(fifth_result)
        results.append(sixth_result)
        results.append(seventh_result)
        results.append(eighth_result)
        return results
        
        
    @patch.object(ResultRepository, 'get_results')
    def test_get_results(self, mock_result_repository) :
        mock_result_repository.get_results.return_value = self.__get_results_from_two_rounds()
        business = ResultBusiness(mock_result_repository)
        
        results = business.get_results()
        
        self.assertEqual(4, len(results))
        
        first_result = results[0]
        first_result_check = [1, "Completed", 2, 876, 5, 0.65, 666, 78.8, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 23]
        self.assert_test.assert_result_dto(first_result_check, first_result)
        
        second_result = results[1]
        second_result_check = [2, "Completed", 1, 276, 23, 1.65, 866, 68.8, 3, 5.2, 1.7, 566, 88.8, 3, 5.2, 1.7, 2.7, 24]
        self.assert_test.assert_result_dto(second_result_check, second_result)
        
        third_result = results[2]
        third_result_check = [3, "Completed", 2, 576, 23, 8.65, 566, 68.8, 8, 8.2, 8.7, 605, 68.8, 13, 3.2, 4.7, 5.7, 25]
        self.assert_test.assert_result_dto(third_result_check, third_result)
       
        fourth_result = results[3]
        fourth_result_check = [4, "Completed", 1, 676, 50, 10.65, 266, 28.8, 5, 23.2, 4.7, 266, 48.8, 8, 4.2, 2.7, 0.9, 26]
        self.assert_test.assert_result_dto(fourth_result_check, fourth_result)
        
        
    @patch.object(ResultRepository, 'get_results')
    def test_get_four_results_sorted_participation_first_round_from_first_rounds(self, mock_result_repository) : 
        mock_result_repository.get_results.return_value = self.__get_results_first_rounds()
        business = ResultBusiness(mock_result_repository)
        
        results_all_rounds = business.get_rounds_participation_sorted()
        
        results = results_all_rounds["first_round"]
        self.assertEqual(4, len(results)) 
        
        first_result = results[0]
        first_result_check = [3, "Completed", 1, 576, 23, 8.65, 566, 15.8, 8, 8.2, 8.7, 605, 68.8, 13, 3.2, 4.7, 5.7, 25]
        self.assert_test.assert_result_dto(first_result_check, first_result)
        
        second_result = results[1]
        second_result_check = [4, "Completed", 1, 676, 50, 10.65, 266, 28.8, 5, 23.2, 4.7, 266, 48.8, 8, 4.2, 2.7, 0.9, 26]
        self.assert_test.assert_result_dto(second_result_check, second_result)
        
        third_result = results[2]
        third_result_check = [2, "Completed", 1, 276, 23, 1.65, 866, 68.8, 3, 5.2, 1.7, 566, 88.8, 3, 5.2, 1.7, 2.7, 24]
        self.assert_test.assert_result_dto(third_result_check, third_result)
       
        fourth_result = results[3]
        fourth_result_check =  [1, "Completed", 1, 876, 5, 0.65, 666, 78.8, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 23]
        self.assert_test.assert_result_dto(fourth_result_check, fourth_result)
        
        
    @patch.object(ResultRepository, 'get_results')
    def test_get_eight_results_sorted_participation_first_round(self, mock_result_repository) :         
        mock_result_repository.get_results.return_value = self.__get_eight_results_first_round()
        business = ResultBusiness(mock_result_repository)
        
        results_all_rounds = business.get_rounds_participation_sorted()
        
        self.__assert_results(results_all_rounds, "first_round")
        
    
    def __get_eight_results_second_rounds(self): 
        factory = FactoryResult()
        first_result = factory.construct_result(1, "Completed", 2, 876, 5, 0.65, 666, 78.8, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 23)
        second_result = factory.construct_result(2, "Completed", 2, 276, 23, 1.65, 866, 68.8, 3, 5.2, 1.7, 566, 88.8, 3, 5.2, 1.7, 2.7, 24)
        third_result = factory.construct_result(3, "Completed", 2, 576, 23, 8.65, 566, 15.8, 8, 8.2, 8.7, 605, 68.8, 13, 3.2, 4.7, 5.7, 25)
        fourth_result = factory.construct_result(4, "Completed", 2, 676, 50, 10.65, 266, 28.8, 5, 23.2, 4.7, 266, 48.8, 8, 4.2, 2.7, 0.9, 26)
        fifth_result = factory.construct_result(5, "Completed", 2, 876, 5, 0.65, 666, 99.56, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 23)
        sixth_result = factory.construct_result(6, "Completed", 2, 876, 5, 0.65, 666, 65.2, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 24)
        seventh_result = factory.construct_result(7, "Completed", 2, 876, 5, 0.65, 666, 0.45, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 25)
        eighth_result = factory.construct_result(8, "Completed", 2, 876, 5, 0.65, 666, 42.6, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 26)
        results = [first_result, second_result, third_result, fourth_result, fifth_result, sixth_result, seventh_result, eighth_result]
        return results
    
    
    @patch.object(ResultRepository, 'get_results')
    def test_get_eight_results_sorted_participation_second_round(self, mock_result_repository) :         
        mock_result_repository.get_results.return_value = self.__get_eight_results_second_rounds()
        business = ResultBusiness(mock_result_repository)
        
        results_all_rounds = business.get_rounds_participation_sorted()
        
        self.__assert_results(results_all_rounds, "second_round")
        
        
    def __get_sixteenth_results_all_rounds(self) : 
        results_round_mocked = []
        result_first_round_mocked = self.__get_eight_results_first_round()
        for result_mocked in result_first_round_mocked : 
            results_round_mocked.append(result_mocked)
        result_second_round_mocked = self.__get_eight_results_second_rounds()
        for result_mocked in result_second_round_mocked : 
            results_round_mocked.append(result_mocked)
        return results_round_mocked
        
        
    @patch.object(ResultRepository, 'get_results')
    def test_get_eight_results_sorted_participation_all_rounds(self, mock_result_repository) :         
        mock_result_repository.get_results.return_value = self.__get_sixteenth_results_all_rounds()
        business = ResultBusiness(mock_result_repository)
        
        results = business.get_rounds_participation_sorted()
        
        self.assertEqual(2, len(results)) 
        
        self.__assert_results(results, "first_round")
        
        self.__assert_results(results, "second_round")
        
        
    def __assert_results(self, results, key_round) :
        round_number = 0
        if key_round == "first_round" :
            round_number = 1
        else : 
            round_number = 2
        
        second_round_result = results[key_round]
        self.assertEqual(8, len(second_round_result)) 
        
        first_result = second_round_result[0]
        first_result_check = [7, "Completed", round_number, 876, 5, 0.65, 666, 0.45, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 25]
        self.assert_test.assert_result_dto(first_result_check, first_result)
        
        second_result = second_round_result[1]
        second_result_check = [3, "Completed", round_number, 576, 23, 8.65, 566, 15.8, 8, 8.2, 8.7, 605, 68.8, 13, 3.2, 4.7, 5.7, 25]
        self.assert_test.assert_result_dto(second_result_check, second_result)
        
        third_result = second_round_result[2]
        third_result_check = [4, "Completed", round_number, 676, 50, 10.65, 266, 28.8, 5, 23.2, 4.7, 266, 48.8, 8, 4.2, 2.7, 0.9, 26]
        self.assert_test.assert_result_dto(third_result_check, third_result)
       
        fourth_result = second_round_result[3]
        fourth_result_check =  [8, "Completed", round_number, 876, 5, 0.65, 666, 42.6, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 26]
        self.assert_test.assert_result_dto(fourth_result_check, fourth_result)
        
        fifth_result = second_round_result[4]
        fifth_result_check = [6, "Completed", round_number, 876, 5, 0.65, 666, 65.2, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 24]
        self.assert_test.assert_result_dto(fifth_result_check, fifth_result)
        
        sixth_result = second_round_result[5]
        sixth_result_check = [2, "Completed", round_number, 276, 23, 1.65, 866, 68.8, 3, 5.2, 1.7, 566, 88.8, 3, 5.2, 1.7, 2.7, 24]
        self.assert_test.assert_result_dto(sixth_result_check, sixth_result)
        
        seventh_result = second_round_result[6]
        seventh_result_check = [1, "Completed", round_number, 876, 5, 0.65, 666, 78.8, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 23]
        self.assert_test.assert_result_dto(seventh_result_check, seventh_result)
       
        eighth_result = second_round_result[7]
        eighth_result_check =  [5, "Completed", round_number, 876, 5, 0.65, 666, 99.56, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 23]
        self.assert_test.assert_result_dto(eighth_result_check, eighth_result) 
        
        
    
        
    ##TODO for the moment this UT is useless. If it stay it delete it  
    # @patch.object(ResultRepository, 'get_results')
    # def test_get_fifth_results_sorted_participation_first_round_with_equality_from_first_rounds(self, mock_result_repository) : 
    #     factory = FactoryResult()
    #     fifth_results_mocked = factory.construct_result(5, "Completed", 1, 276, 23, 1.65, 866, 68.8, 3, 5.2, 1.7, 566, 88.8, 3, 5.2, 1.7, 2.7)
    #     results_mocked = self.__get_results_first_rounds()
    #     results_mocked.append(fifth_results_mocked)
    #     mock_result_repository.get_results.return_value = results_mocked
    #     business = ResultBusiness(mock_result_repository)
        
    #     results = business.get_first_round_participation_sorted()
        
    #     self.assertEqual(5, len(results)) 
        
    #     first_result = results[0]
    #     first_result_check = [3, "Completed", 1, 576, 23, 8.65, 566, 15.8, 8, 8.2, 8.7, 605, 68.8, 13, 3.2, 4.7, 5.7]
    #     self.assert_test.assert_result_dto(first_result_check, first_result)
        
    #     second_result = results[1]
    #     second_result_check = [4, "Completed", 1, 676, 50, 10.65, 266, 28.8, 5, 23.2, 4.7, 266, 48.8, 8, 4.2, 2.7, 0.9]
    #     self.assert_test.assert_result_dto(second_result_check, second_result)
        
    #     third_result = results[2]
    #     third_result_check = [2, "Completed", 1, 276, 23, 1.65, 866, 68.8, 3, 5.2, 1.7, 566, 88.8, 3, 5.2, 1.7, 2.7]
    #     self.assert_test.assert_result_dto(third_result_check, third_result)
       
    #     fourth_result = results[3]
    #     fourth_result_check =  [5, "Completed", 1, 276, 23, 1.65, 866, 68.8, 3, 5.2, 1.7, 566, 88.8, 3, 5.2, 1.7, 2.7]
    #     self.assert_test.assert_result_dto(fourth_result_check, fourth_result)
        
    #     fifth_result = results[4]
    #     fifth_result_check =  [1, "Completed", 1, 876, 5, 0.65, 666, 78.8, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7]
    #     self.assert_test.assert_result_dto(fifth_result_check, fifth_result)