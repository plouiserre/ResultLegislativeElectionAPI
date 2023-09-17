from app.domain.factory.factoryresult import FactoryResult
from app.domain.repository.result_repository import ResultRepository
from app.adapters.driven.MySql.my_db import MyDb

class MySqlResultRepository(ResultRepository):
    def __init__(self, cache) -> None:
        self.my_db = MyDb()
        self.__cache = cache
    
    def get_results(self) : 
        results = []
        if self.__cache.is_datas_cached("results") :
            results = self.__cache.get_datas("results")
        else : 
            connexion = self.my_db.get_my_db()
            
            my_cursor = connexion.cursor()
            
            my_cursor.execute("SELECT * FROM ELECTIONSCONGRESSMANS.RESULT")
            
            results_bdd = my_cursor.fetchall()
            
            factory = FactoryResult()
            
            for result_bdd in results_bdd : 
                result = factory.construct_result_from_bdd(result_bdd)
                results.append(result)
            self.__cache.add_datas(results, "results")
            
        return results