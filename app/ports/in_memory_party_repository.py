from app.domain.DTO.partyDTO import PartyDTO
from app.domain.party_repository import PartyRepository
from app.domain.factory.factoryparty import FactoryParty
from typing import List


class InMemoryPartyRepository(PartyRepository):
    def __init__(self) -> None:
        factory = FactoryParty()
        first_party = factory.construct_party(1, "Divers extrême gauche", "DXG")
        second_party = factory.construct_party(2, "Parti radical de gauche", "RDG")
        third_party = factory.construct_party(3, "Nouvelle union populaire écologique et sociale", "NUP")
        fourth_party = factory.construct_party(4, "Divers gauche", "DVG")
        fifth_party = factory.construct_party(5, "Ecologistes", "ECO")
        sixth_party = factory.construct_party(6, "Regionaliste", "REG")
        seventh_party = factory.construct_party(7, "Ensemble ! (Majorité présidentielle)", "ENS")
        eighth_party = factory.construct_party(8, "Divers Centre", "DVC")
        nineth_party = factory.construct_party(9, "Divers", "DIV")
        tenth_party = factory.construct_party(10, "Union des Démocrates et des Indépendants", "UDI")
        eleventh_party = factory.construct_party(11, "Les Républicains", "LR")
        twelfth_party = factory.construct_party(12, "Divers droite", "DVD")
        thirteenth_party = factory.construct_party(13, "Droite souverainiste", "DSV")
        fourteenth_party = factory.construct_party(14, "Reconquête !", "REC")
        fifteenth_party = factory.construct_party(15, "Rassemblement National", "RN")
        sixteenth_party = factory.construct_party(16, "Divers extrême droite", "DXD") 
        self.parties = [first_party, second_party, third_party, fourth_party, fifth_party, sixth_party, seventh_party, eighth_party,
                   nineth_party, tenth_party, eleventh_party, twelfth_party, thirteenth_party, fourteenth_party, fifteenth_party, sixteenth_party]
        
        
    def get_parties(self) -> List[PartyDTO]:
        return self.parties
    
    
        