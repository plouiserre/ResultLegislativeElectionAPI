class CandidateBusiness() : 
    def __init__(self, CandidateRepository, PartyRepository) -> None:
        self.candidate_repo = CandidateRepository
        self.party_repo = PartyRepository
        
    
    def get_candidates(self) : 
        
        candidates = self.candidate_repo.get_candidates()
        
        parties = self.party_repo.get_parties()
        
        for candidate in candidates : 
            for party in parties :
                if candidate.party_id == party.id :
                    candidate.party_name = party.name
                    break
                else : 
                    continue
        return candidates