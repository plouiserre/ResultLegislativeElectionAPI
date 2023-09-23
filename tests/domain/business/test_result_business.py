import unittest

from app.domain.business.result_business import ResultBusiness
from app.domain.repository.result_repository import ResultRepository
from tests.assert_test import AssertTest
from tests.faker.faker_result import getResults
from unittest.mock import patch

class ResultBusinessTest(unittest.TestCase) :
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.assert_test = AssertTest(self)
        
        
    @patch.object(ResultRepository, 'get_results')
    def test_get_results(self, mock_result_repository) :
        mock_result_repository.get_results.return_value = getResults([100, 105, 110, 115])
    
        business = ResultBusiness(mock_result_repository)
        
        results = business.get_results()
        
        self.assertEqual(4, len(results))
        
        first_result = results[0]
        first_result_check = [100, "Completed", 1, 876, 5, 0.65, 666, 98.8, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 10]
        self.assert_test.assert_result_dto(first_result_check, first_result)
        
        second_result = results[1]
        second_result_check = [105, "Completed", 2, 876, 5, 0.65, 666, 18.8, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 10]
        self.assert_test.assert_result_dto(second_result_check, second_result)
        
        third_result = results[2]
        third_result_check = [110, "Completed", 1, 276, 23, 1.65, 866, 38.8, 3, 5.2, 1.7, 566, 88.8, 3, 5.2, 1.7, 2.7, 11]
        self.assert_test.assert_result_dto(third_result_check, third_result)
       
        fourth_result = results[3]
        fourth_result_check = [115, "Completed", 2, 276, 23, 1.65, 866, 68.8, 3, 5.2, 1.7, 566, 88.8, 3, 5.2, 1.7, 2.7, 11]
        self.assert_test.assert_result_dto(fourth_result_check, fourth_result)
        
        
    @patch.object(ResultRepository, 'get_results')
    def test_get_four_results_sorted_participation_first_round_from_first_rounds(self, mock_result_repository) : 
        mock_result_repository.get_results.return_value = getResults([100, 110, 120, 220])
        business = ResultBusiness(mock_result_repository)
        
        results_all_rounds = business.get_rounds_participation_sorted("ascending")
        
        results = results_all_rounds["first_round"]
        self.assertEqual(4, len(results)) 
        
        first_result = results[0]
        first_result_check = [220, "Completed", 1, 576, 23, 8.65, 566, 15.8, 8, 8.2, 8.7, 605, 68.8, 13, 3.2, 4.7, 5.7, 22]
        self.assert_test.assert_result_dto(first_result_check, first_result)
        
        second_result = results[1]
        second_result_check = [120, "Completed", 1, 576, 23, 8.65, 566, 35.8, 8, 8.2, 8.7, 605, 68.8, 13, 3.2, 4.7, 5.7, 12]
        self.assert_test.assert_result_dto(second_result_check, second_result)
        
        third_result = results[2]
        third_result_check = [110, "Completed", 1, 276, 23, 1.65, 866, 38.8, 3, 5.2, 1.7, 566, 88.8, 3, 5.2, 1.7, 2.7, 11]
        self.assert_test.assert_result_dto(third_result_check, third_result)
       
        fourth_result = results[3]
        fourth_result_check =  [100, "Completed", 1, 876, 5, 0.65, 666, 98.8, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 10]
        self.assert_test.assert_result_dto(fourth_result_check, fourth_result)
        
        
    @patch.object(ResultRepository, 'get_results')
    def test_get_eight_results_sorted_participation_first_round(self, mock_result_repository) :         
        mock_result_repository.get_results.return_value = getResults([200, 210, 220, 230, 240, 250, 260, 270])
        
        business = ResultBusiness(mock_result_repository)
        
        results_all_rounds = business.get_rounds_participation_sorted("ascending")
        
        self.__assert_results_sorted(results_all_rounds, "first_round")
        
    @patch.object(ResultRepository, 'get_results')
    def test_get_eight_results_sorted_participation_second_round(self, mock_result_repository) :         
        mock_result_repository.get_results.return_value = getResults([205, 215, 225, 235, 245, 255, 265, 275])
        business = ResultBusiness(mock_result_repository)
        
        results_all_rounds = business.get_rounds_participation_sorted("ascending")
        
        self.__assert_results_sorted(results_all_rounds, "second_round")
        
        
    @patch.object(ResultRepository, 'get_results')
    def test_get_eight_results_sorted_participation_all_rounds(self, mock_result_repository) :         
        mock_result_repository.get_results.return_value = getResults([200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250, 255, 260, 265, 270, 275])
        business = ResultBusiness(mock_result_repository)
        
        results = business.get_rounds_participation_sorted("ascending")
        
        self.assertEqual(2, len(results)) 
        
        self.__assert_results_sorted(results, "first_round")

        self.__assert_results_sorted(results, "second_round")
        
        
    def __assert_results_sorted(self, results, key_round) :
        round_number = 0
        if key_round == "first_round" :
            round_number = 1
        else : 
            round_number = 2
        
        round_result = results[key_round]
        self.assertEqual(8, len(round_result)) 
        
        first_result = round_result[0]
        id = self.__get_id_result_fake(260, round_number)
        first_result_check = [id, "Completed", round_number, 876, 5, 0.65, 666, 0.45, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 26]
        self.assert_test.assert_result_dto(first_result_check, first_result)
        
        second_result = round_result[1]
        id = self.__get_id_result_fake(220, round_number)
        second_result_check = [id, "Completed", round_number, 576, 23, 8.65, 566, 15.8, 8, 8.2, 8.7, 605, 68.8, 13, 3.2, 4.7, 5.7, 22]
        self.assert_test.assert_result_dto(second_result_check, second_result)
        
        third_result = round_result[2]
        id = self.__get_id_result_fake(230, round_number)
        third_result_check = [id, "Completed", round_number, 676, 50, 10.65, 266, 28.8, 5, 23.2, 4.7, 266, 48.8, 8, 4.2, 2.7, 0.9, 23]
        self.assert_test.assert_result_dto(third_result_check, third_result)
       
        fourth_result = round_result[3]
        id = self.__get_id_result_fake(270, round_number)
        fourth_result_check =  [id, "Completed", round_number, 876, 5, 0.65, 666, 42.6, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 27]
        self.assert_test.assert_result_dto(fourth_result_check, fourth_result)
        
        fifth_result = round_result[4]
        id = self.__get_id_result_fake(250, round_number)
        fifth_result_check = [id, "Completed", round_number, 876, 5, 0.65, 666, 65.2, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 25]
        self.assert_test.assert_result_dto(fifth_result_check, fifth_result)
        
        sixth_result = round_result[5]
        id = self.__get_id_result_fake(210, round_number)
        sixth_result_check = [id, "Completed", round_number, 276, 23, 1.65, 866, 68.8, 3, 5.2, 1.7, 566, 88.8, 3, 5.2, 1.7, 2.7, 21]
        self.assert_test.assert_result_dto(sixth_result_check, sixth_result)
        
        seventh_result = round_result[6]
        id = self.__get_id_result_fake(200, round_number)
        seventh_result_check = [id, "Completed", round_number, 876, 5, 0.65, 666, 78.8, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 20]
        self.assert_test.assert_result_dto(seventh_result_check, seventh_result)
       
        eighth_result = round_result[7]
        id = self.__get_id_result_fake(240, round_number)
        eighth_result_check =  [id, "Completed", round_number, 876, 5, 0.65, 666, 99.56, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 24]
        self.assert_test.assert_result_dto(eighth_result_check, eighth_result) 
        
        
    @patch.object(ResultRepository, 'get_results')
    def test_get_eight_results_sorted_participation_all_rounds_descending(self, mock_result_repository) :         
        mock_result_repository.get_results.return_value = getResults([200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250, 255, 260, 265, 270, 275])
        business = ResultBusiness(mock_result_repository)
        
        results = business.get_rounds_participation_sorted("descending")
        
        self.assertEqual(2, len(results)) 
        
        self.__assert_results_sorted_descending(results, "first_round")

        self.__assert_results_sorted_descending(results, "second_round")
        
        
    def __assert_results_sorted_descending(self, results, key_round) :
        round_number = 0
        if key_round == "first_round" :
            round_number = 1
        else : 
            round_number = 2
        
        round_result = results[key_round]
        self.assertEqual(8, len(round_result)) 
       
        first_result = round_result[0]
        id = self.__get_id_result_fake(240, round_number)
        first_result_check =  [id, "Completed", round_number, 876, 5, 0.65, 666, 99.56, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 24]
        self.assert_test.assert_result_dto(first_result_check, first_result) 
        
        second_result = round_result[1]
        id = self.__get_id_result_fake(200, round_number)
        second_result_check = [id, "Completed", round_number, 876, 5, 0.65, 666, 78.8, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 20]
        self.assert_test.assert_result_dto(second_result_check, second_result)
        
        third_result = round_result[2]
        id = self.__get_id_result_fake(210, round_number)
        third_result_check = [id, "Completed", round_number, 276, 23, 1.65, 866, 68.8, 3, 5.2, 1.7, 566, 88.8, 3, 5.2, 1.7, 2.7, 21]
        self.assert_test.assert_result_dto(third_result_check, third_result)
        
        fourth_result = round_result[3]
        id = self.__get_id_result_fake(250, round_number)
        fourth_result_check = [id, "Completed", round_number, 876, 5, 0.65, 666, 65.2, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 25]
        self.assert_test.assert_result_dto(fourth_result_check, fourth_result)
       
        fifth_result = round_result[4]
        id = self.__get_id_result_fake(270, round_number)
        fifth_result_check =  [id, "Completed", round_number, 876, 5, 0.65, 666, 42.6, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 27]
        self.assert_test.assert_result_dto(fifth_result_check, fifth_result)
        
        sixth_result = round_result[5]
        id = self.__get_id_result_fake(230, round_number)
        sixth_result_check = [id, "Completed", round_number, 676, 50, 10.65, 266, 28.8, 5, 23.2, 4.7, 266, 48.8, 8, 4.2, 2.7, 0.9, 23]
        self.assert_test.assert_result_dto(sixth_result_check, sixth_result)
        
        seventh_result = round_result[6]
        id = self.__get_id_result_fake(220, round_number)
        seventh_result_check = [id, "Completed", round_number, 576, 23, 8.65, 566, 15.8, 8, 8.2, 8.7, 605, 68.8, 13, 3.2, 4.7, 5.7, 22]
        self.assert_test.assert_result_dto(seventh_result_check, seventh_result)
        
        eighth_result = round_result[7]
        id = self.__get_id_result_fake(260, round_number)
        eighth_result_check = [id, "Completed", round_number, 876, 5, 0.65, 666, 0.45, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 26]
        self.assert_test.assert_result_dto(eighth_result_check, eighth_result)
        
        
    def __get_id_result_fake(self, id, round_number) : 
        if round_number == 1 : 
            return id 
        else : 
            return id + 5