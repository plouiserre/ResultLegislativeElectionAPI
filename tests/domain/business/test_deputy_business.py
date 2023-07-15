import datetime
import unittest

from app.domain.business.candidate_business import CandidateBusiness
from app.domain.business.deputy_business import DeputyBusiness
from app.domain.factory.factorycandidate import FactoryCandidate
from app.domain.factory.factorydeputy import FactoryDeputy
from app.ports.InMemory.in_memory_deputy_repository import InMemoryDeputyRepository
from tests.assert_test import AssertTest
from unittest.mock import patch

class DeputyBusinessTest(unittest.TestCase):
    
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.assert_test = AssertTest(self)
        
        
    def __get_deputies(self) :
        factory = FactoryDeputy()
        first_deputy = factory.construct_deputy(1, "M", "DUFREGNE", "Jean-Paul", datetime.datetime(1958, 3, 28), 2, True)
        second_deputy = factory.construct_deputy(2, "M", "PERCHE", "Philippe", datetime.datetime(1987, 11, 19), 24, False)
        third_deputy = factory.construct_deputy(3, "F", "BENOIT-GOLA", "Anne-Cécile", datetime.datetime(1973, 7, 24), 132, False)
        fourth_deputy = factory.construct_deputy(4, "M", "LEROUX", "Sylvain", datetime.datetime(1978, 6, 25), 987, False)
        deputies = [first_deputy, second_deputy, third_deputy, fourth_deputy]
        return deputies
    
    
    def __get_candidates(self) : 
        candidates = []
        factory = FactoryCandidate()
        first_candidate = factory.construct_candidate(1, "VUITTON", "Brigitte", "F", datetime.datetime(1957,11,29), 1, "Professeur, profession scientifique", False, 779, 0.98, 1.93, 0, 0, 0)
        second_candidate = factory.construct_candidate(2, "RAVACLEY", "Stéphane", "M", datetime.datetime(1970,6,6), 3, "Artisan", False, 13112, 16.56, 32.51, 17594, 22.22, 47.75)
        third_candidate = factory.construct_candidate(24, "THOMASSIN", "Geoffrey", "M", datetime.datetime(1986,10,19),9, "Profession intermédiaire administrative et commerciale des entreprises", False, 216, 0.27, 0.54, 0, 0, 0 )
        fourth_candidate = factory.construct_candidate(132, "ALAUZET", "Eric", "M", datetime.datetime(1958,6,7), 7, "Profession libérale", True, 12647, 15.98, 31.36, 19255, 24.32, 52.25)
        candidates = [first_candidate, second_candidate, third_candidate, fourth_candidate]
        return candidates
        
    
    @patch.object(InMemoryDeputyRepository, 'get_deputies')
    def test_get_deputies(self, mock_deputy_repository):
        mock_deputy_repository.get_deputies.return_value = self.__get_deputies()
        dep = DeputyBusiness(mock_deputy_repository, None)
        
        deputies = dep.get_deputies("", "")
        
        self.assertEqual(4, len(deputies))
         
        first_deputy = deputies[0]
        first_deputy_check = [1, "DUFREGNE", "Jean-Paul", "M",  datetime.datetime(1958, 3, 28), 2, True]
        self.assert_test.assert_deputy_dto(first_deputy_check, first_deputy)
        
        second_deputy = deputies[1]
        second_deputy_check = [2, "PERCHE", "Philippe", "M",  datetime.datetime(1987,11,19), 24, False]
        self.assert_test.assert_deputy_dto(second_deputy_check, second_deputy)
        
        third_deputy = deputies[2]
        deputy_check = [3, "BENOIT-GOLA", "Anne-Cécile", "F",  datetime.datetime(1973,7,24), 132, False]
        self.assert_test.assert_deputy_dto(deputy_check, third_deputy)
        
        fourth_deputy = deputies[3]
        deputy_check = [4, "LEROUX", "Sylvain", "M",  datetime.datetime(1978,6,25), 987, False]
        self.assert_test.assert_deputy_dto(deputy_check, fourth_deputy)
        
        
    @patch.object(InMemoryDeputyRepository, 'get_deputies')
    def test_get_specific_deputies(self, mock_deputy_repository):
        mock_deputy_repository.get_deputies.return_value = self.__get_deputies()
        dep = DeputyBusiness(mock_deputy_repository, None)
        
        deputies = dep.get_deputies("Anne-Cécile", "BENOIT-GOLA")
        
        self.assertEqual(1, len(deputies))
         
        first_deputy = deputies[0]
        deputy_check = [3, "BENOIT-GOLA", "Anne-Cécile", "F",  datetime.datetime(1973,7,24), 132, False]
        self.assert_test.assert_deputy_dto(deputy_check, first_deputy)
        
        
    @patch.object(InMemoryDeputyRepository, 'get_deputies')
    def test_get_specific_deputies_managing_caps(self, mock_deputy_repository):
        mock_deputy_repository.get_deputies.return_value = self.__get_deputies()
        dep = DeputyBusiness(mock_deputy_repository, None)
        
        deputies = dep.get_deputies("anne-cécile", "benoit-gola")
        
        self.assertEqual(1, len(deputies))
         
        first_deputy = deputies[0]
        deputy_check = [3, "BENOIT-GOLA", "Anne-Cécile", "F",  datetime.datetime(1973,7,24), 132, False]
        self.assert_test.assert_deputy_dto(deputy_check, first_deputy)
        
        
    @patch.object(InMemoryDeputyRepository, 'get_deputies')
    def test_get_specific_deputies_managing_accent(self, mock_deputy_repository):
        mock_deputy_repository.get_deputies.return_value = self.__get_deputies()
        dep = DeputyBusiness(mock_deputy_repository, None)
        
        deputies = dep.get_deputies("Anne-Cecile", "BENOIT-GOLA")
        
        self.assertEqual(1, len(deputies))
         
        first_deputy = deputies[0]
        deputy_check = [3, "BENOIT-GOLA", "Anne-Cécile", "F",  datetime.datetime(1973,7,24), 132, False]
        self.assert_test.assert_deputy_dto(deputy_check, first_deputy)
        
        
    def __get_candidate_id(self, id_to_return) :
        return id_to_return
        
    @patch.object(CandidateBusiness, "get_candidates")
    @patch.object(InMemoryDeputyRepository, 'get_deputies')
    def test_get_deputy_from_candidate_thomassin(self, mock_deputy_repository, mock_candidate_business):
        mock_deputy_repository.get_deputies.return_value = self.__get_deputies()
        mock_candidate_business.get_candidates.return_value = self.__get_candidates()
        mock_candidate_business.get_candidate_id.return_value =  self.__get_candidate_id(24)
        dep = DeputyBusiness(mock_deputy_repository, mock_candidate_business)
        
        deputy = dep.get_deputy_from_candidate_identity("Geoffrey", "THOMASSIN")
        
        deputy_check = [2, "PERCHE", "Philippe", "M",  datetime.datetime(1987, 11, 19), 24, False]
        self.assert_test.assert_deputy_dto(deputy_check, deputy)
        
        
        
    @patch.object(CandidateBusiness, "get_candidates")
    @patch.object(InMemoryDeputyRepository, 'get_deputies')
    def test_get_deputy_from_candidate_benoit_gola(self, mock_deputy_repository, mock_candidate_business):
        mock_deputy_repository.get_deputies.return_value = self.__get_deputies()
        mock_candidate_business.get_candidates.return_value = self.__get_candidates()
        mock_candidate_business.get_candidate_id.return_value =  self.__get_candidate_id(132)
        dep = DeputyBusiness(mock_deputy_repository, mock_candidate_business)
        
        deputy = dep.get_deputy_from_candidate_identity("Eric", "ALAUZET")
        
        deputy_check = [3, "BENOIT-GOLA", "Anne-Cécile", "F",  datetime.datetime(1973,7,24), 132, False]
        self.assert_test.assert_deputy_dto(deputy_check, deputy)
        
        
    @patch.object(CandidateBusiness, "get_candidates")
    @patch.object(InMemoryDeputyRepository, 'get_deputies')
    def test_get_deputy_from_candidate_benoit_gola_managing_caps(self, mock_deputy_repository, mock_candidate_business):
        mock_deputy_repository.get_deputies.return_value = self.__get_deputies()
        mock_candidate_business.get_candidates.return_value = self.__get_candidates()
        mock_candidate_business.get_candidate_id.return_value =  self.__get_candidate_id(132)
        dep = DeputyBusiness(mock_deputy_repository, mock_candidate_business)
        
        deputy = dep.get_deputy_from_candidate_identity("eric", "ALAUZET")
        
        deputy_check = [3, "BENOIT-GOLA", "Anne-Cécile", "F",  datetime.datetime(1973,7,24), 132, False]
        self.assert_test.assert_deputy_dto(deputy_check, deputy)
        
        
    @patch.object(CandidateBusiness, "get_candidates")
    @patch.object(InMemoryDeputyRepository, 'get_deputies')
    def test_get_deputy_from_candidate_jp_drugregne_managing_accent(self, mock_deputy_repository, mock_candidate_business):
        mock_deputy_repository.get_deputies.return_value = self.__get_deputies()
        mock_candidate_business.get_candidates.return_value = self.__get_candidates()
        mock_candidate_business.get_candidate_id.return_value =  self.__get_candidate_id(2)
        dep = DeputyBusiness(mock_deputy_repository, mock_candidate_business)
        
        deputy = dep.get_deputy_from_candidate_identity("Stephane", "RAVACLEY")
        
        deputy_check = [1, "DUFREGNE", "Jean-Paul", "M", datetime.datetime(1958, 3, 28), 2, True]
        self.assert_test.assert_deputy_dto(deputy_check, deputy)
        
        
    @patch.object(CandidateBusiness, "get_candidates")
    @patch.object(InMemoryDeputyRepository, 'get_deputies')
    def test_get_deputy_from_candidate_unknown(self, mock_deputy_repository, mock_candidate_business):
        mock_deputy_repository.get_deputies.return_value = self.__get_deputies()
        mock_candidate_business.get_candidates.return_value = self.__get_candidates()
        dep = DeputyBusiness(mock_deputy_repository, mock_candidate_business)
        
        deputy = dep.get_deputy_from_candidate_identity("John", "DOE")
        
        self.assertEqual(None, deputy)