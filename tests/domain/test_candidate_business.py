import datetime
import unittest

from app.domain.candidatebusiness import CandidateBusiness
from tests.assert_test import AssertTest

#TODO create assert equal for candidate
class CandidateBusinessTest(unittest.TestCase) :
    
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.assert_test = AssertTest(self)
    
    def test_get_candidates(self) : 
        business = CandidateBusiness()
        
        candidates = business.get_candidates()
        
        self.assertEqual(4, len(candidates))
        
        first_candidate = candidates[0]
        candidate_check =[1, "VUITTON", "Brigitte", "F", datetime.datetime(1957,11,29), 1, "Divers extrême gauche", "Professeur, profession scientifique", False, 779, 0.98, 1.93, 0, 0, 0]
        self.assert_test.assert_candidate_dto(candidate_check, first_candidate)
        
        second_candidate = candidates[1]
        candidate_check =[2, "RAVACLEY", "Stéphane", "M", datetime.datetime(1970,6,6), 3, "Nouvelle union populaire écologique et sociale", "Artisan", False, 13112, 16.56, 32.51, 17594, 22.22, 47.75]
        self.assert_test.assert_candidate_dto(candidate_check, second_candidate)
        
        third_candidate = candidates[2]
        candidate_check =[3, "THOMASSIN", "Geoffrey", "M", datetime.datetime(1986,10,19), 9, "Divers", "Profession intermédiaire administrative et commerciale des entreprises", False, 216, 0.27, 0.54, 0, 0, 0]
        self.assert_test.assert_candidate_dto(candidate_check, third_candidate)
            
        fourth_candidate = candidates[3]
        candidate_check =[4, "ALAUZET", "Eric", "M", datetime.datetime(1958,6,7), 7, "Ensemble ! (Majorité présidentielle)", "Profession libérale", True, 12647, 15.98, 31.36, 19255, 24.32, 52.25]
        self.assert_test.assert_candidate_dto(candidate_check, fourth_candidate)
        