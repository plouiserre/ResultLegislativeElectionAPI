import unittest

from app.domain.business.party.party_result_by_department_business import PartyResultByDepartmentBusiness
from app.domain.repository.candidate_repository import CandidateRepository
from app.domain.repository.department_repository import DepartmentRepository
from app.domain.repository.district_repository import DistrictRepository
from app.domain.repository.party_repository import PartyRepository
from tests.assert_test import AssertTest
from tests.faker.faker_candidate import getCandidates_by_partys_departments
from tests.faker.faker_department import getDepartments_by_ids
from tests.faker.faker_district import getDistricts_by_department_id
from tests.faker.faker_party import getParties_by_id
from unittest.mock import patch

class PartyResultByDepartmentBusinessTest(unittest.TestCase) :     
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.assert_test = AssertTest(self)
    
    @patch.object(PartyRepository, "get_parties")
    @patch.object(CandidateRepository, "get_candidates")
    @patch.object(DistrictRepository, "get_districts")
    @patch.object(DepartmentRepository, "get_departments")
    def test_get_top_departments_for_each_four_specifics_parties_all_rounds(self, mock_candidate_repository, mock_party_business, mock_district_repository, mock_department_repository) :
        mock_candidate_repository.get_candidates.return_value = getCandidates_by_partys_departments(["NUP", "LR", "ENS", "RN"], [11, 33, 34, 69])
        
        mock_party_business.get_parties.return_value = getParties_by_id([3, 7, 11, 15])        
        
        mock_department_repository.get_departments.return_value = getDepartments_by_ids([11, 33, 34, 69])
        
        mock_district_repository.get_districts.return_value = getDistricts_by_department_id([11, 33, 34, 69])
        
        business = PartyResultByDepartmentBusiness(mock_party_business, mock_candidate_repository, mock_district_repository, mock_department_repository)
        
        top_departments = business.get_top_departments_for_each_party_all_rounds()
        
        self.assertEqual(len(top_departments), 4)        
        
        nup_departments = top_departments["NUP"]
        self.__assert_third_party_top_department(nup_departments)
        
        ens_departments = top_departments["ENS"]
        self.__assert_seven_party_top_department(ens_departments)
        
        lr_departments = top_departments["LR"]
        self.__assert_eleven_party_top_department(lr_departments)
        
        rn_departments = top_departments["RN"]
        self.__assert_fifteen_party_top_department(rn_departments)
        
        
    def __assert_third_party_top_department(self, third_top_department) : 
        nup_departments_first_round = third_top_department["first_round"]
        self.assert_test.assert_department_party_result_dto([33, "Gironde", 33, 21.18], nup_departments_first_round[0]) 
        self.assert_test.assert_department_party_result_dto([11, "Aude", 11, 23.38], nup_departments_first_round[1]) 
        self.assert_test.assert_department_party_result_dto([34, "Herault", 34, 31.67], nup_departments_first_round[2]) 
        self.assert_test.assert_department_party_result_dto([69, "Rhône", 69, 35.55], nup_departments_first_round[3]) 
        
        nup_departments_second_round = third_top_department["second_round"]
        self.assert_test.assert_department_party_result_dto([11, "Aude", 11, 17.36], nup_departments_second_round[0])
        self.assert_test.assert_department_party_result_dto([33, "Gironde", 33, 17.98], nup_departments_second_round[1])
        self.assert_test.assert_department_party_result_dto([69, "Rhône", 69, 51.87], nup_departments_second_round[2])
        self.assert_test.assert_department_party_result_dto([34, "Herault", 34, 54.10], nup_departments_second_round[3])
        
        
    def __assert_seven_party_top_department(self, seven_top_department) : 
        ens_departments_first_round = seven_top_department["first_round"]
        self.assert_test.assert_department_party_result_dto([69, "Rhône", 69, 20.06], ens_departments_first_round[0]) 
        self.assert_test.assert_department_party_result_dto([11, "Aude", 11, 23.22], ens_departments_first_round[1]) 
        self.assert_test.assert_department_party_result_dto([34, "Herault", 34, 24.55], ens_departments_first_round[2]) 
        self.assert_test.assert_department_party_result_dto([33, "Gironde", 33, 27.31], ens_departments_first_round[3]) 
        
        ens_departments_second_round = seven_top_department["second_round"]
        self.assert_test.assert_department_party_result_dto([69, "Rhône", 69, 18.24], ens_departments_second_round[0])
        self.assert_test.assert_department_party_result_dto([11, "Aude", 11, 24.62], ens_departments_second_round[1])
        self.assert_test.assert_department_party_result_dto([34, "Herault", 34, 28.62], ens_departments_second_round[2])
        self.assert_test.assert_department_party_result_dto([33, "Gironde", 33, 44.49], ens_departments_second_round[3])
        
        
    def __assert_eleven_party_top_department(self, eleven_top_department) : 
        lr_departments_first_round = eleven_top_department["first_round"]
        self.assert_test.assert_department_party_result_dto([11, "Aude", 11, 6.8], lr_departments_first_round[0]) 
        self.assert_test.assert_department_party_result_dto([34, "Herault", 34, 6.90], lr_departments_first_round[1]) 
        self.assert_test.assert_department_party_result_dto([33, "Gironde", 33, 14.07], lr_departments_first_round[2]) 
        self.assert_test.assert_department_party_result_dto([69, "Rhône", 69, 17.03], lr_departments_first_round[3]) 
        
        lr_departments_second_round = eleven_top_department["second_round"]
        self.assert_test.assert_department_party_result_dto([34, "Herault", 34, 0], lr_departments_second_round[0])
        self.assert_test.assert_department_party_result_dto([11, "Aude", 11, 0], lr_departments_second_round[1])
        self.assert_test.assert_department_party_result_dto([69, "Rhône", 69, 16.27], lr_departments_second_round[2])
        self.assert_test.assert_department_party_result_dto([33, "Gironde", 33, 21.09], lr_departments_second_round[3])
        
        
    def __assert_fifteen_party_top_department(self, fifteen_top_department) : 
        rn_departments_first_round = fifteen_top_department["first_round"]
        self.assert_test.assert_department_party_result_dto([69, "Rhône", 69, 20.87], rn_departments_first_round[0]) 
        self.assert_test.assert_department_party_result_dto([11, "Aude", 11, 28.29], rn_departments_first_round[1]) 
        self.assert_test.assert_department_party_result_dto([34, "Herault", 34, 29.01], rn_departments_first_round[2]) 
        self.assert_test.assert_department_party_result_dto([33, "Gironde", 33, 32.0], rn_departments_first_round[3]) 
        
        rn_departments_second_round = fifteen_top_department["second_round"]
        self.assert_test.assert_department_party_result_dto([69, "Rhône", 69, 0.0], rn_departments_second_round[0])
        self.assert_test.assert_department_party_result_dto([34, "Herault", 34, 37.15], rn_departments_second_round[1])
        self.assert_test.assert_department_party_result_dto([11, "Aude", 11, 50.44], rn_departments_second_round[2])
        self.assert_test.assert_department_party_result_dto([33, "Gironde", 33, 56.03], rn_departments_second_round[3])