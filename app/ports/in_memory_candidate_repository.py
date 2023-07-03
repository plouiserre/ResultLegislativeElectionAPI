import datetime

from app.domain.candidate_repository import CandidateRepository
from app.domain.DTO.candidateDTO import CandidateDTO
from app.domain.factory.factorycandidate import FactoryCandidate
from typing import List

class InMemoryCandidateRepository(CandidateRepository) : 
    def __init__(self) -> None:
        factory = FactoryCandidate()
        first_candidate = factory.construct_candidate(1, "VUITTON", "Brigitte", "F", datetime.datetime(1957,11,29), 1, "Professeur, profession scientifique", False, 779, 0.98, 1.93, 0, 0, 0)
        second_candidate = factory.construct_candidate(2, "RAVACLEY", "Stéphane", "M", datetime.datetime(1970,6,6), 3, "Artisan", False, 13112, 16.56, 32.51, 17594, 22.22, 47.75)
        third_candidate = factory.construct_candidate(3, "THOMASSIN", "Geoffrey", "M", datetime.datetime(1986,10,19),9, "Profession intermédiaire administrative et commerciale des entreprises", False, 216, 0.27, 0.54, 0, 0, 0 )
        fourth_candidate = factory.construct_candidate(4, "ALAUZET", "Eric", "M", datetime.datetime(1958,6,7), 7, "Profession libérale", True, 12647, 15.98, 31.36, 19255, 24.32, 52.25)
        self.__candidates = [first_candidate, second_candidate, third_candidate, fourth_candidate]
        
    def get_candidates(self) -> List[CandidateDTO] : 
        return self.__candidates