from abc import ABC, abstractmethod

class PartyRepository(ABC) : 
    
    @abstractmethod
    def get_parties(self):
        pass