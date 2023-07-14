from abc import ABC, abstractmethod

class CandidateRepository(ABC) :
    
    @abstractmethod
    def get_candidates(self):
        pass