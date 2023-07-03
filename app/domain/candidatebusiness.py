

import datetime

from app.domain.factory.factorycandidate import FactoryCandidate
from app.domain.DTO.partyDTO import PartyDTO

class CandidateBusiness() : 
    def __init__(self) -> None:
        pass
    
    def get_candidates(self) : 
        factory = FactoryCandidate()
        first_candidate = factory.construct_candidate(1, "VUITTON", "Brigitte", "F", datetime.datetime(1957,11,29), 1, "Professeur, profession scientifique", False, 779, 0.98, 1.93, 0, 0, 0)
        second_candidate = factory.construct_candidate(2, "RAVACLEY", "Stéphane", "M", datetime.datetime(1970,6,6), 3, "Artisan", False, 13112, 16.56, 32.51, 17594, 22.22, 47.75)
        third_candidate = factory.construct_candidate(3, "THOMASSIN", "Geoffrey", "M", datetime.datetime(1986,10,19),9, "Profession intermédiaire administrative et commerciale des entreprises", False, 216, 0.27, 0.54, 0, 0, 0 )
        fourth_candidate = factory.construct_candidate(4, "ALAUZET", "Eric", "M", datetime.datetime(1958,6,7), 7, "Profession libérale", True, 12647, 15.98, 31.36, 19255, 24.32, 52.25)
        candidates = [first_candidate, second_candidate, third_candidate, fourth_candidate]
        
        parties = self.__get_parties()
        
        for candidate in candidates : 
            for party in parties :
                if candidate.party_id == party.id :
                    candidate.party_name = party.name
                    break
                else : 
                    continue
        return candidates
    
    
    def __get_parties(self) :
        first_party = self.__set_party(1, "Divers extrême gauche", "DXG")
        second_party = self.__set_party(2, "Parti radical de gauche", "RDG")
        third_party = self.__set_party(3, "Nouvelle union populaire écologique et sociale", "NUP")
        fourth_party = self.__set_party(4, "Divers gauche", "DVG")
        fifth_party = self.__set_party(5, "Ecologistes", "ECO")
        sixth_party = self.__set_party(6, "Regionaliste", "REG")
        seventh_party = self.__set_party(7, "Ensemble ! (Majorité présidentielle)", "ENS")
        eighth_party = self.__set_party(8, "Divers Centre", "DVC")
        nineth_party = self.__set_party(9, "Divers", "DIV")
        tenth_party = self.__set_party(10, "Union des Démocrates et des Indépendants", "UDI")
        eleventh_party = self.__set_party(11, "Les Républicains", "LR")
        twelfth_party = self.__set_party(12, "Divers droite", "DVD")
        thirteenth_party = self.__set_party(13, "Droite souverainiste", "DSV")
        fourteenth_party = self.__set_party(14, "Reconquête !", "REC")
        fifteenth_party = self.__set_party(15, "Rassemblement National", "RN")
        sixteenth_party = self.__set_party(16, "Divers extrême droite", "DXD") 
        parties = [first_party, second_party, third_party, fourth_party, fifth_party, sixth_party, seventh_party, eighth_party,
                   nineth_party, tenth_party, eleventh_party, twelfth_party, thirteenth_party, fourteenth_party, fifteenth_party, sixteenth_party]
        return parties
    
        
    def __set_party(self, id, name, short_name) : 
        party = PartyDTO()
        party.id = id
        party.name = name
        party.short_name = short_name
        return party
        