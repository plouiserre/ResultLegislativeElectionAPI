from app.domain.DTO.resultDTO import ResultDTO
from app.domain.factory.factoryresult import FactoryResult
from app.domain.repository.result_repository import ResultRepository
from typing import List

class InMemoryResultRepository(ResultRepository) :
    def __init__(self) -> None:
        factory = FactoryResult()
        first_result = factory.construct_result(1, "Completed", 2, 876, 5, 0.65, 666, 78.8, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 23)
        second_result = factory.construct_result(2, "Completed", 1, 276, 23, 1.65, 866, 68.8, 3, 5.2, 1.7, 566, 88.8, 3, 5.2, 1.7, 2.7, 24)
        third_result = factory.construct_result(3, "Completed", 2, 576, 23, 8.65, 566, 68.8, 8, 8.2, 8.7, 605, 68.8, 13, 3.2, 4.7, 5.7, 25)
        fourth_result = factory.construct_result(4, "Completed", 1, 676, 50, 10.65, 266, 28.8, 5, 23.2, 4.7, 266, 48.8, 8, 4.2, 2.7, 0.9, 26)
        self.results = [first_result, second_result, third_result, fourth_result]
        
    def get_results(self) -> List[ResultDTO]:
        return self.results
