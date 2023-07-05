from abc import ABC, abstractclassmethod

class DeputyRepository(ABC):
    
    @abstractclassmethod
    def get_deputies(self):
        pass