import datetime
import unittest

from app.domain.deputy_business import DeputyBusiness
from app.domain.factory.factorydeputy import FactoryDeputy
from app.ports.in_memory_deputy_repository import InMemoryDeputyRepository
from tests.assert_test import AssertTest
from unittest.mock import patch

class DeputyBusinessTest(unittest.TestCase):
    
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.assert_test = AssertTest(self)
        
        
    def __get_deputies(self) :
        factory = FactoryDeputy()
        first_deputy = factory.construct_deputy(1, "M", "DUFREGNE", "Jean-Paul", datetime.datetime(1958, 3, 28), True)
        second_deputy = factory.construct_deputy(2, "M", "PERCHE", "Philippe", datetime.datetime(1987, 11, 19), False)
        third_deputy = factory.construct_deputy(3, "F", "BENOIT-GOLA", "Anne-Cécile", datetime.datetime(1973, 7, 24), False)
        fourth_deputy = factory.construct_deputy(4, "M", "LEROUX", "Sylvain", datetime.datetime(1978, 6, 25), False)
        deputies = [first_deputy, second_deputy, third_deputy, fourth_deputy]
        return deputies
        
    
    @patch.object(InMemoryDeputyRepository, 'get_deputies')
    def test_get_deputies(self, mock_deputy_repository):
        mock_deputy_repository.get_deputies.return_value = self.__get_deputies()
        dep = DeputyBusiness(mock_deputy_repository)
        
        deputies = dep.get_deputies("", "")
        
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
        
        
    @patch.object(InMemoryDeputyRepository, 'get_deputies')
    def test_get_specific_deputies(self, mock_deputy_repository):
        mock_deputy_repository.get_deputies.return_value = self.__get_deputies()
        dep = DeputyBusiness(mock_deputy_repository)
        
        deputies = dep.get_deputies("Anne-Cécile", "BENOIT-GOLA")
        
        self.assertEqual(1, len(deputies))
         
        first_deputy = deputies[0]
        deputy_check = [3, "BENOIT-GOLA", "Anne-Cécile", "F",  datetime.datetime(1973,7,24), False]
        self.assert_test.assert_deputy_dto(deputy_check, first_deputy)
        
        
    @patch.object(InMemoryDeputyRepository, 'get_deputies')
    def test_get_specific_deputies_managing_caps(self, mock_deputy_repository):
        mock_deputy_repository.get_deputies.return_value = self.__get_deputies()
        dep = DeputyBusiness(mock_deputy_repository)
        
        deputies = dep.get_deputies("anne-cécile", "benoit-gola")
        
        self.assertEqual(1, len(deputies))
         
        first_deputy = deputies[0]
        deputy_check = [3, "BENOIT-GOLA", "Anne-Cécile", "F",  datetime.datetime(1973,7,24), False]
        self.assert_test.assert_deputy_dto(deputy_check, first_deputy)
        
        
    @patch.object(InMemoryDeputyRepository, 'get_deputies')
    def test_get_specific_deputies_managing_accent(self, mock_deputy_repository):
        mock_deputy_repository.get_deputies.return_value = self.__get_deputies()
        dep = DeputyBusiness(mock_deputy_repository)
        
        deputies = dep.get_deputies("Anne-Cecile", "BENOIT-GOLA")
        
        self.assertEqual(1, len(deputies))
         
        first_deputy = deputies[0]
        deputy_check = [3, "BENOIT-GOLA", "Anne-Cécile", "F",  datetime.datetime(1973,7,24), False]
        self.assert_test.assert_deputy_dto(deputy_check, first_deputy)