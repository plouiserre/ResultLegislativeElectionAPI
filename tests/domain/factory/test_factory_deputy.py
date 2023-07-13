import datetime
import unittest

from app.domain.factory.factorydeputy import FactoryDeputy
from tests.assert_test import AssertTest

class FactoryDeputyTest(unittest.TestCase) : 
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.assert_test = AssertTest(self)
        
        
    def test_construct_deputy(self) : 
        factory = FactoryDeputy()
        
        deputy = factory.construct_deputy(66, "M", "DUFREGNE", "Jean-Paul", datetime.datetime(1958, 3, 28), 2, True)
        
        deputy_check = [66, "DUFREGNE", "Jean-Paul", "M",  datetime.datetime(1958, 3, 28), 2, True]
        self.assert_test.assert_deputy_dto(deputy_check, deputy)