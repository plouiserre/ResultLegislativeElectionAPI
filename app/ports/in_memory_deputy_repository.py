import datetime

from app.domain.deputy_repository import DeputyRepository
from app.domain.factory.factorydeputy import FactoryDeputy

class InMemoryDeputyRepository(DeputyRepository) : 
    def __init__(self) -> None:
        super().__init__()
        factory = FactoryDeputy()
        first_deputy = factory.construct_deputy(1, "M", "DUFREGNE", "Jean-Paul", datetime.datetime(1958, 3, 28), True)
        second_deputy = factory.construct_deputy(2, "M", "PERCHE", "Philippe", datetime.datetime(1987, 11, 19), False)
        third_deputy = factory.construct_deputy(3, "F", "BENOIT-GOLA", "Anne-Cécile", datetime.datetime(1973, 7, 24), False)
        fourth_deputy = factory.construct_deputy(4, "M", "LEROUX", "Sylvain", datetime.datetime(1978, 6, 25), False)
        self.deputies = [first_deputy, second_deputy, third_deputy, fourth_deputy]
        
    def get_deputies(self) : 
        return self.deputies