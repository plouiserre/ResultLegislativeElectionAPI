from abc import ABC, abstractclassmethod

class DepartmentRepository(ABC):
    
    @abstractclassmethod
    def get_departments(self):
        pass