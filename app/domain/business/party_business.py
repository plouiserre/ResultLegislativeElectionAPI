class PartyBusiness :
    def __init__(self, party_repo) -> None:
        self.party_repo = party_repo
    
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