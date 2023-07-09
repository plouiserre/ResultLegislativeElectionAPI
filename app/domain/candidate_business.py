import datetime 

from app.domain.factory.factorycandidate import FactoryCandidate

class CandidateBusiness() : 
    def __init__(self, CandidateRepository, PartyRepository) -> None:
        self.candidate_repo = CandidateRepository
        self.party_repo = PartyRepository
        
    
    def get_candidates(self, first_name, last_name) : 
        candidates = []
        
        if first_name == "" and last_name == "" :
            candidates = self.candidate_repo.get_candidates()
        else :
            factory = FactoryCandidate()
            candidate = factory.construct_candidate(2, "RAVACLEY", "Stéphane", "M", datetime.datetime(1970,6,6), 3, "Artisan", False, 13112, 16.56, 32.51, 17594, 22.22, 47.75)
            candidates.append(candidate)
        
        parties = self.party_repo.get_parties()
        
        for candidate in candidates : 
            for party in parties :
                if candidate.party_id == party.id :
                    candidate.party_name = party.name
                    break
                else : 
                    continue
        return candidates