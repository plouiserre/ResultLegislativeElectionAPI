from app.utils.helper import getLabelFormatted

class CandidateBusiness() : 
    def __init__(self, CandidateRepository, PartyRepository) -> None:
        self.candidate_repo = CandidateRepository
        self.party_repo = PartyRepository
        self.first_name = ""
        self.last_name = ""
        self.candidates = []
        self.candidates_specific = []
        
    def get_candidates(self, first_name, last_name) : 
        self.first_name = first_name
        self.last_name = last_name
        self.candidates = self.candidate_repo.get_candidates()
        
        parties = self.party_repo.get_parties()
        
        for candidate in self.candidates : 
            if first_name == "" and last_name == "" :
                self.__set_party_name_for_candidate(candidate, parties)
            else :
                self.__search_candidates_from_first_name_last_name(candidate, parties)
            
        if first_name == "" and last_name == "":
            return self.candidates
        else :
            return self.candidates_specific
                
                
    def __search_candidates_from_first_name_last_name(self, candidate, parties):
        first_name_lower_no_accent = getLabelFormatted(self.first_name)
        first_name_candidate_lower_no_accent = getLabelFormatted(candidate.first_name)
        last_name_lower_no_accent = getLabelFormatted(self.last_name)
        last_name_candidate_lower_no_accent = getLabelFormatted(candidate.last_name)
        if first_name_lower_no_accent == first_name_candidate_lower_no_accent and last_name_lower_no_accent == last_name_candidate_lower_no_accent : 
                self.__set_party_name_for_candidate(candidate, parties)
                self.candidates_specific.append(candidate)
    
    
    def __set_party_name_for_candidate(self, candidate, parties) : 
        for party in parties :
                if candidate.party_id == party.id :
                    candidate.party_name = party.name
                    break
                else : 
                    continue
        