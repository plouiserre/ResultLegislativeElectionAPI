from app.domain.factory.factorydeputy import FactoryDeputy
from app.ports.MySql.my_db import MyDb

class MySqlDeputyRepository():
    def __init__(self) -> None:
        self.my_db = MyDb()
        
    
    def get_deputies(self) :
        connexion = self.my_db.get_my_db()
        
        my_cursor = connexion.cursor()
        
        my_cursor.execute("SELECT * FROM ELECTIONSCONGRESSMANS.DEPUTY")
        
        deputies_bdd = my_cursor.fetchall()
        deputies = []
        
        factory = FactoryDeputy()
        
        for deputy_bdd in deputies_bdd :
            deputy = factory.construct_deputy_from_bdd(deputy_bdd)
            deputies.append(deputy)
            
        return deputies