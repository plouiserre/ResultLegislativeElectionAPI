import unittest

from app.domain.factory.factoryparty import FactoryParty
from tests.assert_test import AssertTest

class FactoryPartyTest(unittest.TestCase) : 
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.assert_test = AssertTest(self)
        
    
    def test_construct_party(self) : 
        factory = FactoryParty()
        first_party = factory.construct_party(1, "Divers extrême gauche", "DXG")
        
        first_party_check = [1, "Divers extrême gauche", "DXG"]
        self.assert_test.assert_party_dto(first_party_check, first_party)
        
        
    def test_construct_party_from_bdd(self) : 
        factory = FactoryParty()
        
        party_data = [1, "Divers extrême gauche", "DXG"]
        party = factory.construct_party_from_bdd(party_data)
        
        self.assert_test.assert_party_dto(party_data, party)