from app.domain.factory.factoryparty import FactoryParty
from app.ports.MySql.my_db import MyDb

class MySqlPartyRepository():
    def __init__(self) -> None:
        self.my_db = MyDb()
        
    
    def get_parties(self):
        connexion = self.my_db.get_my_db()
        
        my_cursor = connexion.cursor()
        
        my_cursor.execute("SELECT * FROM ELECTIONSCONGRESSMANS.PARTY")
        
        parties_bdd = my_cursor.fetchall()
        parties = []
        
        factory = FactoryParty()
        
        for party_bdd in parties_bdd :
            party = factory.construct_party_from_bdd(party_bdd)
            parties.append(party)
            
        return parties 