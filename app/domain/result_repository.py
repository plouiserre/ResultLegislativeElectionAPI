from abc import ABC, abstractmethod

class ResultRepository(ABC) :
    
    @abstractmethod
    def get_results(self):
        pass