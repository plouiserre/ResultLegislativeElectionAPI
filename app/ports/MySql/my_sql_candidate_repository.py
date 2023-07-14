from app.domain.factory.factorycandidate import FactoryCandidate
from app.ports.MySql.my_db import MyDb

class MySqlCandidateRepository :
    def __init__(self) -> None:
        self.my_db = MyDb()
        
        
    def get_candidates(self) : 
        connexion = self.my_db.get_my_db()
        
        my_cursor = connexion.cursor()
        
        my_cursor.execute("SELECT * FROM ELECTIONSCONGRESSMANS.CANDIDATE")
        
        candidates_bdd = my_cursor.fetchall()
        candidates = []
        
        factory = FactoryCandidate()
        for candidate_bdd in candidates_bdd : 
            candidate = factory.construct_candidate_from_bdd(candidate_bdd)
            candidates.append(candidate)
            
        return candidates