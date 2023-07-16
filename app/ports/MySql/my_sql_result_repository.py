from app.domain.factory.factoryresult import FactoryResult
from app.ports.MySql.my_db import MyDb

class MySqlResultRepository():
    def __init__(self) -> None:
        self.my_db = MyDb()
    
    def get_results(self) : 
        connexion = self.my_db.get_my_db()
        
        my_cursor = connexion.cursor()
        
        my_cursor.execute("SELECT * FROM ELECTIONSCONGRESSMANS.RESULT")
        
        results_bdd = my_cursor.fetchall()
        results = []
        
        factory = FactoryResult()
        
        for result_bdd in results_bdd : 
            result = factory.construct_result_from_bdd(result_bdd)
            results.append(result)
            
        return results