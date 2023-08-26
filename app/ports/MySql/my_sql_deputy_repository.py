from app.domain.factory.factorydeputy import FactoryDeputy
from app.domain.repository.deputy_repository import DeputyRepository
from app.ports.MySql.my_db import MyDb

class MySqlDeputyRepository(DeputyRepository):
    def __init__(self, cache) -> None:
        self.my_db = MyDb()
        self.__cache = cache
        
    
    def get_deputies(self) :
        deputies = []
        if self.__cache.is_datas_cached("deputies") :
            deputies = self.__cache.get_datas("deputies")
        else : 
            connexion = self.my_db.get_my_db()
            
            my_cursor = connexion.cursor()
            
            my_cursor.execute("SELECT * FROM ELECTIONSCONGRESSMANS.DEPUTY")
            
            deputies_bdd = my_cursor.fetchall()
            
            factory = FactoryDeputy()
            
            for deputy_bdd in deputies_bdd :
                deputy = factory.construct_deputy_from_bdd(deputy_bdd)
                deputies.append(deputy)
                
            self.__cache.add_datas(deputies, "deputies")
            
        return deputies