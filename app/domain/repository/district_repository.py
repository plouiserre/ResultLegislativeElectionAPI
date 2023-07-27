from abc import ABC, abstractclassmethod

class DistrictRepository(ABC):
    
    @abstractclassmethod
    def get_districts(self):
        pass