from app.domain.factory.factoryparty import FactoryParty
from app.domain.repository.party_repository import PartyRepository
from app.ports.MySql.my_db import MyDb

class MySqlPartyRepository(PartyRepository):
    def __init__(self, cache) -> None:
        self.my_db = MyDb()
        self.__cache = cache
        
    
    def get_parties(self):
        parties = []
        if self.__cache.is_datas_cached("parties") : 
            parties = self.__cache.get_datas("parties")
        else :
            connexion = self.my_db.get_my_db()
            
            my_cursor = connexion.cursor()
            
            my_cursor.execute("SELECT * FROM ELECTIONSCONGRESSMANS.PARTY")
            
            parties_bdd = my_cursor.fetchall()
            
            factory = FactoryParty()
            
            for party_bdd in parties_bdd :
                party = factory.construct_party_from_bdd(party_bdd)
                parties.append(party)
                
            self.__cache.add_datas(parties, "parties")
            
        return parties 