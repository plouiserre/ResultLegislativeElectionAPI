import datetime
import unittest

from app.factory.factorycandidate import FactoryCandidate
from tests.assert_test import AssertTest

class FactoryCandidateTest(unittest.TestCase) :
    
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.assert_test = AssertTest(self)
    
    def test_construct_candidate(self) : 
        factory = FactoryCandidate()
        
        candidate = factory.construct_candidate(1, "VUITTON", "Brigitte", "F", datetime.datetime(1957,11,29), 1, "Professeur, profession scientifique", False, 779, 0.98, 1.93, 0, 0, 0)
        
        candidate_check =[1, "VUITTON", "Brigitte", "F", datetime.datetime(1957,11,29), 1, "" , "Professeur, profession scientifique", False, 779, 0.98, 1.93, 0, 0, 0]
        self.assert_test.assert_candidate_dto(candidate_check, candidate)