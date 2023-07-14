import datetime
import unittest

from app.domain.business.candidate_business import CandidateBusiness
from app.domain.factory.factorycandidate import FactoryCandidate
from app.domain.factory.factoryparty import FactoryParty
from app.ports.InMemory.in_memory_candidate_repository import InMemoryCandidateRepository
from app.ports.InMemory.in_memory_party_repository import InMemoryPartyRepository
from unittest.mock import patch
from tests.assert_test import AssertTest

#TODO refaire la classe de test en passant par les méthodes abstraites et non les inmemory repo
class CandidateBusinessTest(unittest.TestCase) :
    
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.assert_test = AssertTest(self)
        
        
    def __get_candidates(self) : 
        candidates = []
        factory = FactoryCandidate()
        first_candidate = factory.construct_candidate(1, "VUITTON", "Brigitte", "F", datetime.datetime(1957,11,29), 1, "Professeur, profession scientifique", False, 779, 0.98, 1.93, 0, 0, 0)
        second_candidate = factory.construct_candidate(2, "RAVACLEY", "Stéphane", "M", datetime.datetime(1970,6,6), 3, "Artisan", False, 13112, 16.56, 32.51, 17594, 22.22, 47.75)
        third_candidate = factory.construct_candidate(3, "THOMASSIN", "Geoffrey", "M", datetime.datetime(1986,10,19),9, "Profession intermédiaire administrative et commerciale des entreprises", False, 216, 0.27, 0.54, 0, 0, 0 )
        fourth_candidate = factory.construct_candidate(4, "ALAUZET", "Eric", "M", datetime.datetime(1958,6,7), 7, "Profession libérale", True, 12647, 15.98, 31.36, 19255, 24.32, 52.25)
        candidates = [first_candidate, second_candidate, third_candidate, fourth_candidate]
        return candidates
    
    
    def __get_parties(self) :
        parties = []
        factory = FactoryParty()
        first_party = factory.construct_party(1, "Divers extrême gauche", "DXG")
        second_party = factory.construct_party(3, "Nouvelle union populaire écologique et sociale", "NUP")
        third_party = factory.construct_party(7, "Ensemble ! (Majorité présidentielle)", "ENS")
        fourth_party = factory.construct_party(9, "Divers", "DIV")
        parties = [first_party, second_party, third_party, fourth_party]
        return parties
    
    
    @patch.object(InMemoryCandidateRepository, "get_candidates")
    @patch.object(InMemoryPartyRepository, "get_parties")
    def test_get_all_candidates(self, mock_candidate_repository, mock_party_repository) : 
        mock_candidate_repository.get_candidates.return_value = self.__get_candidates()
        mock_party_repository.get_parties.return_value = self.__get_parties()
        
        business = CandidateBusiness(mock_candidate_repository, mock_party_repository)
        
        candidates = business.get_candidates("", "")
        
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
        
        
    @patch.object(InMemoryCandidateRepository, "get_candidates")
    @patch.object(InMemoryPartyRepository, "get_parties")
    def test_get_specific_candidate(self, mock_party_repository, mock_candidate_repository) : 
        mock_party_repository.get_parties.return_value = self.__get_parties() 
        mock_candidate_repository.get_candidates.return_value = self.__get_candidates()
        
        business = CandidateBusiness(mock_candidate_repository, mock_party_repository)
        
        candidates = business.get_candidates("Stéphane", "RAVACLEY")
        
        self.assertEqual(1, len(candidates))
        
        first_candidate = candidates[0]
        candidate_check =[2, "RAVACLEY", "Stéphane", "M", datetime.datetime(1970,6,6), 3, "Nouvelle union populaire écologique et sociale", "Artisan", False, 13112, 16.56, 32.51, 17594, 22.22, 47.75]
        self.assert_test.assert_candidate_dto(candidate_check, first_candidate)
        
        
    @patch.object(InMemoryCandidateRepository, "get_candidates")
    @patch.object(InMemoryPartyRepository, "get_parties")
    def test_get_specific_candidate_managing_caps(self, mock_party_repository, mock_candidate_repository) : 
        mock_party_repository.get_parties.return_value = self.__get_parties() 
        mock_candidate_repository.get_candidates.return_value = self.__get_candidates()
        
        business = CandidateBusiness(mock_candidate_repository, mock_party_repository)
        
        candidates = business.get_candidates("stéphane", "ravacley")
        
        self.assertEqual(1, len(candidates))
        
        first_candidate = candidates[0]
        candidate_check =[2, "RAVACLEY", "Stéphane", "M", datetime.datetime(1970,6,6), 3, "Nouvelle union populaire écologique et sociale", "Artisan", False, 13112, 16.56, 32.51, 17594, 22.22, 47.75]
        self.assert_test.assert_candidate_dto(candidate_check, first_candidate)
        
        
    @patch.object(InMemoryCandidateRepository, "get_candidates")
    @patch.object(InMemoryPartyRepository, "get_parties")
    def test_get_specific_candidate_managing_accent(self, mock_party_repository, mock_candidate_repository) : 
        mock_party_repository.get_parties.return_value = self.__get_parties() 
        mock_candidate_repository.get_candidates.return_value = self.__get_candidates()
        
        business = CandidateBusiness(mock_candidate_repository, mock_party_repository)
        
        candidates = business.get_candidates("Stephane", "RAVACLEY")
        
        self.assertEqual(1, len(candidates))
        
        first_candidate = candidates[0]
        candidate_check =[2, "RAVACLEY", "Stéphane", "M", datetime.datetime(1970,6,6), 3, "Nouvelle union populaire écologique et sociale", "Artisan", False, 13112, 16.56, 32.51, 17594, 22.22, 47.75]
        self.assert_test.assert_candidate_dto(candidate_check, first_candidate)
        
        
    def test_get_candidate_id_from_last_name_first_name(self) :
        candidates = self.__get_candidates()
        business = CandidateBusiness(None, None)
        
        candidate_id = business.get_candidate_id(candidates, "Stéphane", "RAVACLEY")
        
        self.assertEqual(2, candidate_id)
        
        
    def test_get_candidate_id_from_last_name_first_name_managing_caps(self) :
        candidates = self.__get_candidates()
        business = CandidateBusiness(None, None)
        
        candidate_id = business.get_candidate_id(candidates, "Stéphane", "ravacley")
        
        self.assertEqual(2, candidate_id)
        
        
    def test_get_candidate_id_from_last_name_first_name_managing_accents(self) :
        candidates = self.__get_candidates()
        business = CandidateBusiness(None, None)
        
        candidate_id = business.get_candidate_id(candidates, "Stephane", "RAVACLEY")
        
        self.assertEqual(2, candidate_id)