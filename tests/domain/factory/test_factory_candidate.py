import datetime
import unittest

from app.domain.factory.factorycandidate import FactoryCandidate
from tests.assert_test import AssertTest

class FactoryCandidateTest(unittest.TestCase) :    
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.assert_test = AssertTest(self)
    
    def test_construct_candidate(self) : 
        factory = FactoryCandidate()
        
        candidate = factory.construct_candidate(1, "VUITTON", "Brigitte", "F", datetime.datetime(1957,11,29), 1, "Professeur, profession scientifique", False, 66, 779, 0.98, 1.93, 0, 0, 0)
        
        candidate_check =[1, "VUITTON", "Brigitte", "F", datetime.datetime(1957,11,29), 1, "" , "Professeur, profession scientifique", False, 66, 779, 0.98, 1.93, 0, 0, 0]
        self.assert_test.assert_candidate_dto(candidate_check, candidate)
        
        
    def test_construct_candidate_from_bdd(self) : 
        factory = FactoryCandidate()
        
        candidate_data = [6291, "GUILLERMAIN", "Vincent", "M", datetime.datetime(1976, 8, 10), 7, "Agriculteur sur petite exploitation", 0, 576, 8071, 9.36, 19.3, 0, 0, 0]
        candidate = factory.construct_candidate_from_bdd(candidate_data)
        
        candidate_check = [6291, "GUILLERMAIN", "Vincent", "M", datetime.datetime(1976, 8, 10), 7, "", "Agriculteur sur petite exploitation", False, 576, 8071, 9.36, 19.3, 0, 0, 0]
        self.assert_test.assert_candidate_dto(candidate_check, candidate)