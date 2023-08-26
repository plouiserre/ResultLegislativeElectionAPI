import unittest

from app.domain.business.party_business import PartyBusiness
from app.domain.factory.factoryparty import FactoryParty
from app.ports.InMemory.in_memory_party_repository import InMemoryPartyRepository
from tests.assert_test import AssertTest
from tests.faker import getParties
from unittest.mock import patch

class PartyBusinessTest(unittest.TestCase) : 
    
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.assert_test = AssertTest(self)
        
        
    @patch.object(InMemoryPartyRepository, "get_parties")
    def test_get_parties(self, mock_party_repository) : 
        mock_party_repository.get_parties.return_value = getParties([1, 3, 7, 9])
        
        business = PartyBusiness(mock_party_repository)
        parties = business.get_parties()
        
        self.assertEqual(4, len(parties))
        
        party_check = [1, "Divers extrême gauche", "DXG"]
        self.assert_test.assert_party_dto(party_check, parties[0])
        
        party_check = [3, "Nouvelle union populaire écologique et sociale", "NUP"]
        self.assert_test.assert_party_dto(party_check, parties[1])
        
        party_check = [7, "Ensemble ! (Majorité présidentielle)", "ENS"]
        self.assert_test.assert_party_dto(party_check, parties[2])
        
        party_check = [9, "Divers", "DIV"]
        self.assert_test.assert_party_dto(party_check, parties[3])
        
        
    @patch.object(InMemoryPartyRepository, "get_parties")
    def test_get_parties_by_short_name(self, mock_party_repository) : 
        mock_party_repository.get_parties.return_value = getParties([1, 3, 7, 9])
        
        business = PartyBusiness(mock_party_repository)
        party = business.get_party_by_short_name("ENS")
        
        party_check = [7, "Ensemble ! (Majorité présidentielle)", "ENS"]
        self.assert_test.assert_party_dto(party_check, party)
        