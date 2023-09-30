from app.domain.business.candidate.sortered_candidate import SorteredCandidate

class PartyBusiness :
    def __init__(self, party_repo, candidate_repo) -> None:
        self.party_repo = party_repo
        self.candidate_repo = candidate_repo
    
    def get_parties(self) : 
        parties = self.party_repo.get_parties()
        return parties
    
    
    def get_party_by_short_name(self, short_name):
        party_by_short_name = None
        parties = self.party_repo.get_parties()
        for party in parties : 
            if party.short_name == short_name : 
                party_by_short_name = party
                break
        return party_by_short_name
    
    
    def get_top_candidates_for_each_party_all_rounds(self, limit) :
        all_candidates = self.candidate_repo.get_candidates()
        all_parties = self.party_repo.get_parties()
        all_candidates_by_party = {}
        
        for candidate in all_candidates :
            for party in all_parties : 
                if candidate.party_id == party.id : 
                    if (party.short_name in all_candidates_by_party) == False:
                        all_candidates_by_party[party.short_name] = []
                    all_candidates_by_party[party.short_name].append(candidate)
                    break                    

        for party in all_parties :
            candidates = all_candidates_by_party[party.short_name]
            sortered  = SorteredCandidate(candidates, all_parties)
            candidates_sortered = sortered.sort_all_candidates(limit)
            all_candidates_by_party[party.short_name] = candidates_sortered        
            
        return all_candidates_by_party
    
    
    def get_top_departments_for_each_each_party_all_rounds(self, limit) : 
        print("I love C#")