import datetime
import unittest

from app.domain.deputy_business import DeputyBusiness
from tests.assert_test import AssertTest

class DeputyBusinessTest(unittest.TestCase):
    
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.assert_test = AssertTest(self)
        
    
    def test_get_deputies(self):
        dep = DeputyBusiness()
        
        deputies = dep.get_deputies()
        
        self.assertEqual(4, len(deputies))
        
        first_deputy = deputies[0]
        first_deputy_check = [1, "DUFREGNE", "Jean-Paul", "M",  datetime.datetime(1958, 3, 28), True]
        self.assert_test.assert_deputy_dto(first_deputy_check, first_deputy)
        
        second_deputy = deputies[1]
        second_deputy_check = [2, "PERCHE", "Philippe", "M",  datetime.datetime(1987,11,19), False]
        self.assert_test.assert_deputy_dto(second_deputy_check, second_deputy)
        
        third_deputy = deputies[2]
        deputy_check = [3, "BENOIT-GOLA", "Anne-Cécile", "F",  datetime.datetime(1973,7,24), False]
        self.assert_test.assert_deputy_dto(deputy_check, third_deputy)
        
        fourth_deputy = deputies[3]
        deputy_check = [4, "LEROUX", "Sylvain", "M",  datetime.datetime(1978,6,25), False]
        self.assert_test.assert_deputy_dto(deputy_check, fourth_deputy)