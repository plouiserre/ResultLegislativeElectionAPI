import datetime

from app.domain.factory.factorydeputy import FactoryDeputy

class DeputyBusiness : 
    def __init__(self, DeputyRepository) -> None:
        self.deputy_repo = DeputyRepository
    
    def get_deputies(self):
        deputies = self.deputy_repo.get_deputies()
        return deputies