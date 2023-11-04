import unittest

from app.domain.factory.factorydepartmentpartyresult import FactoryDepartmentPartyResult
from tests.assert_test import AssertTest
from tests.faker.faker_candidate import getCandidates_by_partys_departments
from tests.faker.faker_department import getDepartments_by_ids

class FactoryDepartmentPartyResultTest(unittest.TestCase) :
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.assert_test = AssertTest(self)
        
    
    def test_factory_department_party_result(self) : 
        factory_department_party_result = FactoryDepartmentPartyResult()
        
        dep_party_result = factory_department_party_result.construct_department_party_result(650, "Gironde", 33, 66.67)
        
        department_result_check = [650, "Gironde", 33, 66.67]
        self.assert_test.assert_department_party_result_dto(department_result_check, dep_party_result)
        
        
    def test_factory_department_party_result_from_candidates_list(self) : 
        factory_department_party_result = FactoryDepartmentPartyResult()
        candidates = getCandidates_by_partys_departments(["ENS"], [33])
        first_round_voting = []
        for candidate in candidates : 
            first_round_voting.append(candidate.rate_vote_expressed_first_round)
        dept = getDepartments_by_ids([33])[0]
        
        dep_party_result = factory_department_party_result.construct_department_party_result_from_list_voting_stats(dept, first_round_voting)
        
        department_result_check = [33, "Gironde", 33, 27.31]
        self.assert_test.assert_department_party_result_dto(department_result_check, dep_party_result)