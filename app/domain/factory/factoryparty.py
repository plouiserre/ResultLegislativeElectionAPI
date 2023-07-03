from app.domain.DTO.partyDTO import PartyDTO

class FactoryParty : 
    
    def construct_party(self, id, name, short_name):
        party = PartyDTO()
        party.id = id
        party.name = name
        party.short_name = short_name
        return party