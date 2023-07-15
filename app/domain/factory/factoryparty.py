from app.domain.DTO.partyDTO import PartyDTO

class FactoryParty : 
    
    def construct_party(self, id, name, short_name):
        party = PartyDTO()
        party.id = id
        party.name = name
        party.short_name = short_name
        return party
    
    
    def construct_party_from_bdd(self, datas) : 
        party = PartyDTO()
        party.id = datas[0]
        party.name = datas[1]
        party.short_name = datas[2]
        return party