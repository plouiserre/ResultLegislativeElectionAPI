class CandidateBusiness() : 
    def __init__(self, CandidateRepository, PartyRepository) -> None:
        self.candidate_repo = CandidateRepository
        self.party_repo = PartyRepository
        
    #TODO manage accent and majuscule
    def get_candidates(self, first_name, last_name) : 
        candidates = []
        candidates_specific = []
        
        candidates = self.candidate_repo.get_candidates()
        
        parties = self.party_repo.get_parties()
        
        for candidate in candidates : 
            if first_name == "" and last_name == "" :
                self.__set_party_name_for_candidate(candidate, parties)
            elif first_name == candidate.first_name and last_name == candidate.last_name : 
                self.__set_party_name_for_candidate(candidate, parties)
                candidates_specific.append(candidate)
            
        if first_name == "" and last_name == "":
            return candidates
        else :
            return candidates_specific
    
    
    def __set_party_name_for_candidate(self, candidate, parties) : 
        for party in parties :
                if candidate.party_id == party.id :
                    candidate.party_name = party.name
                    break
                else : 
                    continue