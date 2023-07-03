import unittest

from app.ports.in_memory_party_repository import InMemoryPartyRepository
from tests.assert_test import AssertTest

class InMemoryPartyRepositoryTest(unittest.TestCase) : 
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.assert_test = AssertTest(self)
        
    def test_get_parties(self) : 
        repo = InMemoryPartyRepository()
        
        parties = repo.get_parties()
        
        self.assertEqual(16, len(parties))
        
        first_party_check = [1, "Divers extrême gauche", "DXG"]
        first_party = parties[0]
        self.assert_test.assert_party_dto(first_party_check, first_party)
        
        second_party_check = [2, "Parti radical de gauche", "RDG"]
        second_party = parties[1]
        self.assert_test.assert_party_dto(second_party_check, second_party)
         
        third_party_check = [3, "Nouvelle union populaire écologique et sociale", "NUP"]
        third_party = parties[2]
        self.assert_test.assert_party_dto(third_party_check, third_party)
        
        fourth_party_check = [4, "Divers gauche", "DVG"]
        fourth_party = parties[3]
        self.assert_test.assert_party_dto(fourth_party_check, fourth_party)
        
        fifth_party_check = [5, "Ecologistes", "ECO"]
        fifth_party = parties[4]
        self.assert_test.assert_party_dto(fifth_party_check, fifth_party)
        
        sixth_party_check = [6, "Regionaliste", "REG"]
        sixth_party = parties[5]
        self.assert_test.assert_party_dto(sixth_party_check, sixth_party)
        
        seventh_party_check = [7, "Ensemble ! (Majorité présidentielle)", "ENS"]
        seventh_party = parties[6]
        self.assert_test.assert_party_dto(seventh_party_check, seventh_party)
        
        eighth_party_check = [8, "Divers Centre", "DVC"]
        eighth_party = parties[7]
        self.assert_test.assert_party_dto(eighth_party_check, eighth_party)
        
        nineth_party_check = [9, "Divers", "DIV"]
        nineth_party = parties[8]
        self.assert_test.assert_party_dto(nineth_party_check, nineth_party)
        
        tenth_party_check = [10, "Union des Démocrates et des Indépendants", "UDI"]
        tenth_party = parties[9]
        self.assert_test.assert_party_dto(tenth_party_check, tenth_party)
        
        eleventh_party_check = [11, "Les Républicains", "LR"]
        eleventh_party = parties[10]
        self.assert_test.assert_party_dto(eleventh_party_check, eleventh_party)
        
        twelfth_party_check = [12, "Divers droite", "DVD"]
        twelfth_party = parties[11]
        self.assert_test.assert_party_dto(twelfth_party_check, twelfth_party)
        
        thirteenth_party_check = [13, "Droite souverainiste", "DSV"]
        thirteenth_party = parties[12]
        self.assert_test.assert_party_dto(thirteenth_party_check, thirteenth_party)
        
        fourteen_party_check = [14, "Reconquête !", "REC"]
        fourteenth_party = parties[13]
        self.assert_test.assert_party_dto(fourteen_party_check, fourteenth_party)
        
        fifteen_party_check = [15, "Rassemblement National", "RN"]
        fifteenth_party = parties[14]
        self.assert_test.assert_party_dto(fifteen_party_check, fifteenth_party)
        
        sixteenth_party_check = [16, "Divers extrême droite", "DXD"]
        sixteenth_party = parties[15]
        self.assert_test.assert_party_dto(sixteenth_party_check, sixteenth_party)