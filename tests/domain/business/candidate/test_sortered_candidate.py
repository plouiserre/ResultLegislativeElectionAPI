import unittest
import datetime

from app.domain.business.candidate.sortered_candidate import SorteredCandidate
from tests.assert_test import AssertTest
from tests.faker.faker_party import getParties_by_id
from tests.faker.faker_candidate import getCandidates_by_id


class SorteredCandidateTest(unittest.TestCase) : 
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.assert_test = AssertTest(self)
        
        
    def test_get_top_candidates_results_small_samples(self):
        candidates = getCandidates_by_id([2, 8, 14, 26, 28])
        parties = getParties_by_id([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
        
        business = SorteredCandidate(candidates, parties)
        
        candidates_results = business.sort_all_candidates(3)
        candidates_results_first_round = candidates_results["first_round"]
        candidates_results_second_round = candidates_results["second_round"]
        
        self.assertEqual(2, len(candidates_results))
        
        self.assertEqual(3, len(candidates_results_first_round))
        
        one_candidate = candidates_results_first_round[0]
        one_candidate_check = [14, "AUTAIN", "Clémentine", "F", datetime.datetime(1973,5,26), 3, "Nouvelle union populaire écologique et sociale", "Profession de l'information, des arts et des spectacles", True, "XXXX", 9400, 14.83, 46.15, 11296, 17.753,	100]
        self.assert_test.assert_candidate_dto(one_candidate_check, one_candidate)
        
        two_candidate = candidates_results_first_round[1]
        two_candidate_check = [28, "DIAZ", "Edwige", "F", datetime.datetime(1987, 10, 15), 15, "Rassemblement National", "Cadre administratif et commercial d'entreprise", False, "XXXX", 18662, 18.9, 39.42, 25092, 26.954, 59.467]
        self.assert_test.assert_candidate_dto(two_candidate_check, two_candidate)
        
        three_candidate = candidates_results_first_round[2]
        three_candidate_check = [26, "BOUDIÉ", "Florent", "M", datetime.datetime(1973, 9, 22), 7, "Ensemble ! (Majorité présidentielle)", "Cadre de la fonction publique", True, "XXXX", 13565, 16.29, 32.7, 19581, 24.502, 51.424]
        self.assert_test.assert_candidate_dto(three_candidate_check, three_candidate)
                
        self.assertEqual(3, len(candidates_results_second_round))
        
        one_candidate = candidates_results_second_round[0]
        one_candidate_check = [14, "AUTAIN", "Clémentine", "F", datetime.datetime(1973,5,26), 3, "Nouvelle union populaire écologique et sociale", "Profession de l'information, des arts et des spectacles", True, "XXXX", 9400, 14.83, 46.15, 11296, 17.753,	100]
        self.assert_test.assert_candidate_dto(one_candidate_check, one_candidate)
        
        two_candidate = candidates_results_second_round[1]
        two_candidate_check = [28, "DIAZ", "Edwige", "F", datetime.datetime(1987, 10, 15), 15, "Rassemblement National", "Cadre administratif et commercial d'entreprise", False, "XXXX", 18662, 18.9, 39.42, 25092, 26.954, 59.467]
        self.assert_test.assert_candidate_dto(two_candidate_check, two_candidate)
        
        three_candidate = candidates_results_second_round[2]
        three_candidate_check = [26, "BOUDIÉ", "Florent", "M", datetime.datetime(1973, 9, 22), 7, "Ensemble ! (Majorité présidentielle)", "Cadre de la fonction publique", True, "XXXX", 13565, 16.29, 32.7, 19581, 24.502, 51.424]
        self.assert_test.assert_candidate_dto(three_candidate_check, three_candidate)        
          
        
    def test_get_top_candidates_results(self):
        candidates = getCandidates_by_id([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 
                                                                22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35])
        parties= getParties_by_id([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
        
        business = SorteredCandidate(candidates, parties)
        
        candidates_results = business.sort_all_candidates(6)
        candidates_results_first_round = candidates_results["first_round"]
        candidates_results_second_round = candidates_results["second_round"]
        
        self.assertEqual(2, len(candidates_results))
        
        self.assertEqual(6, len(candidates_results_first_round))
        
        one_candidate = candidates_results_first_round[0]
        one_candidate_check = [14, "AUTAIN", "Clémentine", "F", datetime.datetime(1973,5,26), 3, "Nouvelle union populaire écologique et sociale", "Profession de l'information, des arts et des spectacles", True, "XXXX", 9400, 14.83, 46.15, 11296, 17.753,	100]
        self.assert_test.assert_candidate_dto(one_candidate_check, one_candidate)
        
        two_candidate = candidates_results_first_round[1]
        two_candidate_check = [31, "OZIOL", "Nathalie", "F", datetime.datetime(1990, 2, 18), 3, "Nouvelle union populaire écologique et sociale", "Professeur, profession scientifique", False, "XXXX", 11513, 17.6,	40.37, 17008, 25.99, 63.33]
        self.assert_test.assert_candidate_dto(two_candidate_check, two_candidate)
        
        three_candidate = candidates_results_first_round[2]
        three_candidate_check = [28, "DIAZ", "Edwige", "F", datetime.datetime(1987, 10, 15), 15, "Rassemblement National", "Cadre administratif et commercial d'entreprise", False, "XXXX", 18662, 18.9, 39.42, 25092, 26.954, 59.467]
        self.assert_test.assert_candidate_dto(three_candidate_check, three_candidate)
            
        four_candidate = candidates_results_first_round[3]
        four_candidate_check = [23, "BARTHÈS", "Christophe", "M", datetime.datetime(1966, 10, 12), 15, "Rassemblement National", "Agriculteur sur moyenne exploitation", False, "XXXX", 15871, 16.12, 32.8, 23914, 25.07, 50.815]
        self.assert_test.assert_candidate_dto(four_candidate_check, four_candidate)
        
        five_candidate = candidates_results_first_round[4]
        five_candidate_check = [26, "BOUDIÉ", "Florent", "M", datetime.datetime(1973, 9, 22), 7, "Ensemble ! (Majorité présidentielle)", "Cadre de la fonction publique", True, "XXXX", 13565, 16.29, 32.7, 19581, 24.502, 51.424]
        self.assert_test.assert_candidate_dto(five_candidate_check, five_candidate)
        
        six_candidate = candidates_results_first_round[5]
        six_candidate_check = [2, "RAVACLEY", "Stéphane", "M", datetime.datetime(1970,6,6), 3, "Nouvelle union populaire écologique et sociale", "Artisan", False, "XXXX", 13112, 16.56, 32.51, 17594, 22.22, 47.75]
        self.assert_test.assert_candidate_dto(six_candidate_check, six_candidate)
        
        self.assertEqual(6, len(candidates_results_second_round))
        
        one_candidate = candidates_results_second_round[0]
        one_candidate_check = [14, "AUTAIN", "Clémentine", "F", datetime.datetime(1973,5,26), 3, "Nouvelle union populaire écologique et sociale", "Profession de l'information, des arts et des spectacles", True, "XXXX", 9400, 14.83, 46.15, 11296, 17.753,	100]
        self.assert_test.assert_candidate_dto(one_candidate_check, one_candidate)
        
        two_candidate = candidates_results_second_round[1]
        two_candidate_check = [31, "OZIOL", "Nathalie", "F", datetime.datetime(1990, 2, 18), 3, "Nouvelle union populaire écologique et sociale", "Professeur, profession scientifique", False, "XXXX", 11513, 17.6,	40.37, 17008, 25.99, 63.33]
        self.assert_test.assert_candidate_dto(two_candidate_check, two_candidate)
        
        three_candidate = candidates_results_second_round[2]
        three_candidate_check = [18, "RAY", "Nicolas", "M", datetime.datetime(1981, 5, 14), 11, "Les Républicains", "Cadre de la fonction publique", False, "XXXX", 9594, 11.96, 24.22, 19296, 26.194, 63.272]
        self.assert_test.assert_candidate_dto(three_candidate_check, three_candidate)
        
        four_candidate = candidates_results_second_round[3]
        four_candidate_check = [28, "DIAZ", "Edwige", "F", datetime.datetime(1987, 10, 15), 15, "Rassemblement National", "Cadre administratif et commercial d'entreprise", False, "XXXX", 18662, 18.9, 39.42, 25092, 26.954, 59.467]
        self.assert_test.assert_candidate_dto(four_candidate_check, four_candidate)
        
        five_candidate = candidates_results_second_round[4]
        five_candidate_check = [33, "CRISTOL", "Laurence", "F", datetime.datetime(1967, 11, 8), 7, "Ensemble ! (Majorité présidentielle)",  "Professeur, profession scientifique", False, "XXXX",	12457, 13.5, 26.68, 22907, 25.764, 54.725]
        self.assert_test.assert_candidate_dto(five_candidate_check, five_candidate)
        
        six_candidate = candidates_results_second_round[5]
        six_candidate_check = [4, "ALAUZET", "Eric", "M", datetime.datetime(1958,6,7), 7, "Ensemble ! (Majorité présidentielle)", "Profession libérale", True, "XXXX", 12647, 15.98, 31.36, 19255, 24.32, 52.25]
        self.assert_test.assert_candidate_dto(six_candidate_check, six_candidate)