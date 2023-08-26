from app.domain.factory.factorycandidate import FactoryCandidate
from app.domain.repository.candidate_repository import CandidateRepository
from app.ports.MySql.my_db import MyDb

class MySqlCandidateRepository(CandidateRepository) :
    def __init__(self, cache) -> None:
        self.my_db = MyDb()
        self.__cache = cache
        
        
    def get_candidates(self) : 
        candidates = []
            
        if self.__cache.is_datas_cached("candidates"):
            candidates = self.__cache.get_datas("candidates")
        else :
            connexion = self.my_db.get_my_db()
            
            my_cursor = connexion.cursor()
            
            my_cursor.execute("SELECT * FROM ELECTIONSCONGRESSMANS.CANDIDATE")
            
            candidates_bdd = my_cursor.fetchall()
            
            factory = FactoryCandidate()
            for candidate_bdd in candidates_bdd : 
                candidate = factory.construct_candidate_from_bdd(candidate_bdd)
                candidates.append(candidate)
                
            self.__cache.add_datas(candidates, "candidates")
            
        return candidates