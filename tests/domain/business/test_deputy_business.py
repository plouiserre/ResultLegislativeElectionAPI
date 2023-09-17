import datetime
import unittest

from app.domain.business.candidate.candidate_business import CandidateBusiness
from app.domain.business.deputy_business import DeputyBusiness
from app.adapters.driven.InMemory.in_memory_deputy_repository import InMemoryDeputyRepository
from tests.assert_test import AssertTest
from tests.faker import getCandidates, getDeputies
from unittest.mock import patch

class DeputyBusinessTest(unittest.TestCase):
    
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.assert_test = AssertTest(self)
        
        
    @patch.object(InMemoryDeputyRepository, 'get_deputies')
    def test_get_deputies(self, mock_deputy_repository):
        mock_deputy_repository.get_deputies.return_value = getDeputies([1, 2, 3, 4])
        dep = DeputyBusiness(mock_deputy_repository, None)
        
        deputies = dep.get_deputies("", "")
        
        self.assertEqual(4, len(deputies))
         
        first_deputy = deputies[0]
        first_deputy_check = [1, "DUFREGNE", "Jean-Paul", "M",  datetime.datetime(1958, 3, 28), 2, True]
        self.assert_test.assert_deputy_dto(first_deputy_check, first_deputy)
        
        second_deputy = deputies[1]
        second_deputy_check = [2, "PERCHE", "Philippe", "M",  datetime.datetime(1987,11,19), 3, False]
        self.assert_test.assert_deputy_dto(second_deputy_check, second_deputy)
        
        third_deputy = deputies[2]
        deputy_check = [3, "BENOIT-GOLA", "Anne-Cécile", "F",  datetime.datetime(1973,7,24), 4, False]
        self.assert_test.assert_deputy_dto(deputy_check, third_deputy)
        
        fourth_deputy = deputies[3]
        deputy_check = [4, "LEROUX", "Sylvain", "M",  datetime.datetime(1978,6,25), 987, False]
        self.assert_test.assert_deputy_dto(deputy_check, fourth_deputy)
        
        
    @patch.object(InMemoryDeputyRepository, 'get_deputies')
    def test_get_specific_deputies(self, mock_deputy_repository):
        mock_deputy_repository.get_deputies.return_value = getDeputies([1, 2, 3, 4])
        dep = DeputyBusiness(mock_deputy_repository, None)
        
        deputies = dep.get_deputies("Anne-Cécile", "BENOIT-GOLA")
        
        self.assertEqual(1, len(deputies))
         
        first_deputy = deputies[0]
        deputy_check = [3, "BENOIT-GOLA", "Anne-Cécile", "F",  datetime.datetime(1973,7,24), 4, False]
        self.assert_test.assert_deputy_dto(deputy_check, first_deputy)
        
        
    @patch.object(InMemoryDeputyRepository, 'get_deputies')
    def test_get_specific_deputies_managing_caps(self, mock_deputy_repository):
        mock_deputy_repository.get_deputies.return_value = getDeputies([1, 2, 3, 4])
        dep = DeputyBusiness(mock_deputy_repository, None)
        
        deputies = dep.get_deputies("anne-cécile", "benoit-gola")
        
        self.assertEqual(1, len(deputies))
         
        first_deputy = deputies[0]
        deputy_check = [3, "BENOIT-GOLA", "Anne-Cécile", "F",  datetime.datetime(1973,7,24), 4, False]
        self.assert_test.assert_deputy_dto(deputy_check, first_deputy)
        
        
    @patch.object(InMemoryDeputyRepository, 'get_deputies')
    def test_get_specific_deputies_managing_accent(self, mock_deputy_repository):
        mock_deputy_repository.get_deputies.return_value = getDeputies([1, 2, 3, 4])
        dep = DeputyBusiness(mock_deputy_repository, None)
        
        deputies = dep.get_deputies("Anne-Cecile", "BENOIT-GOLA")
        
        self.assertEqual(1, len(deputies))
         
        first_deputy = deputies[0]
        deputy_check = [3, "BENOIT-GOLA", "Anne-Cécile", "F",  datetime.datetime(1973,7,24), 4, False]
        self.assert_test.assert_deputy_dto(deputy_check, first_deputy)
        
        
    @patch.object(CandidateBusiness, "get_candidates")
    @patch.object(InMemoryDeputyRepository, 'get_deputies')
    def test_get_deputy_from_candidate_thomassin(self, mock_deputy_repository, mock_candidate_business):
        mock_deputy_repository.get_deputies.return_value = getDeputies([1, 2, 3, 4])
        mock_candidate_business.get_candidates.return_value = getCandidates([3])
        dep = DeputyBusiness(mock_deputy_repository, mock_candidate_business)
        
        deputy = dep.get_deputy_from_candidate_identity("Geoffrey", "THOMASSIN")
        
        deputy_check = [2, "PERCHE", "Philippe", "M",  datetime.datetime(1987, 11, 19), 3, False]
        self.assert_test.assert_deputy_dto(deputy_check, deputy)
        
        
    @patch.object(CandidateBusiness, "get_candidates")
    @patch.object(InMemoryDeputyRepository, 'get_deputies')
    def test_get_deputy_from_candidate_benoit_gola(self, mock_deputy_repository, mock_candidate_business):
        mock_deputy_repository.get_deputies.return_value = getDeputies([1, 2, 3, 4])
        mock_candidate_business.get_candidates.return_value = getCandidates([4])
        dep = DeputyBusiness(mock_deputy_repository, mock_candidate_business)
        
        deputy = dep.get_deputy_from_candidate_identity("Eric", "ALAUZET")
        
        deputy_check = [3, "BENOIT-GOLA", "Anne-Cécile", "F",  datetime.datetime(1973,7,24), 4, False]
        self.assert_test.assert_deputy_dto(deputy_check, deputy)
        
        
    @patch.object(CandidateBusiness, "get_candidates")
    @patch.object(InMemoryDeputyRepository, 'get_deputies')
    def test_get_deputy_from_candidate_benoit_gola_managing_caps(self, mock_deputy_repository, mock_candidate_business):
        mock_deputy_repository.get_deputies.return_value = getDeputies([1, 2, 3, 4])
        mock_candidate_business.get_candidates.return_value = getCandidates([4])
        dep = DeputyBusiness(mock_deputy_repository, mock_candidate_business)
        
        deputy = dep.get_deputy_from_candidate_identity("eric", "ALAUZET")
        
        deputy_check = [3, "BENOIT-GOLA", "Anne-Cécile", "F",  datetime.datetime(1973,7,24), 4, False]
        self.assert_test.assert_deputy_dto(deputy_check, deputy)
        
        
    @patch.object(CandidateBusiness, "get_candidates")
    @patch.object(InMemoryDeputyRepository, 'get_deputies')
    def test_get_deputy_from_candidate_jp_drugregne_managing_accent(self, mock_deputy_repository, mock_candidate_business):
        mock_deputy_repository.get_deputies.return_value = getDeputies([1, 2, 3, 4])
        mock_candidate_business.get_candidates.return_value = getCandidates([2])
        dep = DeputyBusiness(mock_deputy_repository, mock_candidate_business)
        
        deputy = dep.get_deputy_from_candidate_identity("Stephane", "RAVACLEY")
        
        deputy_check = [1, "DUFREGNE", "Jean-Paul", "M", datetime.datetime(1958, 3, 28), 2, True]
        self.assert_test.assert_deputy_dto(deputy_check, deputy)
        
        
    @patch.object(CandidateBusiness, "get_candidates")
    @patch.object(InMemoryDeputyRepository, 'get_deputies')
    def test_get_deputy_from_candidate_unknown(self, mock_deputy_repository, mock_candidate_business):
        mock_deputy_repository.get_deputies.return_value = getDeputies([1, 2, 3, 4])
        mock_candidate_business.get_candidates.return_value = getCandidates([1, 2, 3, 4])
        dep = DeputyBusiness(mock_deputy_repository, mock_candidate_business)
        
        deputy = dep.get_deputy_from_candidate_identity("John", "DOE")
        
        self.assertEqual(None, deputy)