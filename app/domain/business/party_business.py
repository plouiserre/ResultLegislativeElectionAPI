class PartyBusiness :
    def __init__(self, party_repo) -> None:
        self.party_repo = party_repo
    
    def get_parties(self) : 
        parties = self.party_repo.get_parties()
        return parties