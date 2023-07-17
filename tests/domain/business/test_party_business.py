import unittest

from app.domain.business.party_business import PartyBusiness
from app.domain.factory.factoryparty import FactoryParty
from app.ports.InMemory.in_memory_party_repository import InMemoryPartyRepository
from tests.assert_test import AssertTest
from unittest.mock import patch

class PartyBusinessTest(unittest.TestCase) : 
    
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.assert_test = AssertTest(self)
    
    def __get_parties(self) :
        parties = []
        factory = FactoryParty()
        first_party = factory.construct_party(1, "Divers extrême gauche", "DXG")
        second_party = factory.construct_party(3, "Nouvelle union populaire écologique et sociale", "NUP")
        third_party = factory.construct_party(7, "Ensemble ! (Majorité présidentielle)", "ENS")
        fourth_party = factory.construct_party(9, "Divers", "DIV")
        parties = [first_party, second_party, third_party, fourth_party]
        return parties
    
    @patch.object(InMemoryPartyRepository, "get_parties")
    def test_get_parties(self, mock_party_repository) : 
        mock_party_repository.get_parties.return_value = self.__get_parties()
        
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
        