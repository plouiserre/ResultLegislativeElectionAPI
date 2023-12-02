import unittest

from app.domain.business.department_business import DepartmentBusiness
from app.domain.business.district_business import DistrictBusiness
from app.domain.business.result_business import ResultBusiness
from app.domain.repository.district_repository import DistrictRepository
from tests.assert_test import AssertTest
from tests.faker.faker_result import getResults
from tests.faker.faker_district import getDistricts_by_id
from tests.faker.faker_department import getDepartments_by_ids
from unittest.mock import patch

class DistrictBusinessTest(unittest.TestCase):
    
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.assert_test = AssertTest(self)
        
    
    @patch.object(DistrictRepository, "get_districts")
    def test_get_districts(self, mock_repo):
        mock_repo.get_districts.return_value = getDistricts_by_id([10, 11, 12, 20])
        
        business = DistrictBusiness(mock_repo, None, None)
        districts = business.get_districts()
        
        self.assertEqual(4, len(districts))
        
        district_check = [10, 1,	"1ère circo",	1]
        self.assert_test.assert_district_dto(district_check, districts[0])
        
        district_check = [11, 2, "2ème circo", 1]
        self.assert_test.assert_district_dto(district_check, districts[1])
        
        district_check = [12, 3,	"3ème circo",	1]
        self.assert_test.assert_district_dto(district_check, districts[2])
        
        district_check = [20, 1,	"1ère circo", 2]
        self.assert_test.assert_district_dto(district_check, districts[3])
        
    
    @patch.object(DistrictRepository, "get_districts")
    def test_get_districts_by_department_id(self, mock_repo):
        mock_repo.get_districts.return_value = getDistricts_by_id([10, 11, 12, 20, 21, 22])
        
        business = DistrictBusiness(mock_repo, None, None)
        districts = business.get_districts_by_department_id(2)
        
        self.assertEqual(3, len(districts))
        
        district_check = [20, 1, "1ère circo", 2]
        self.assert_test.assert_district_dto(district_check, districts[0])
        
        district_check = [21, 2, "2ème circo", 2]
        self.assert_test.assert_district_dto(district_check, districts[1])
        
        district_check = [22, 3, "3ème circo", 2]
        self.assert_test.assert_district_dto(district_check, districts[2])
        
        
    @patch.object(DistrictRepository, "get_districts")
    @patch.object(DepartmentBusiness, "get_departments")
    def test_get_departments_by_department_name(self, mock_district_repo, mock_department_repo) :
        mock_district_repo.get_districts.return_value = getDistricts_by_id([10, 11, 12, 20, 21, 22])
        mock_department_repo.get_departments.return_value = getDepartments_by_ids([1, 2])
        
        business = DistrictBusiness(mock_district_repo, mock_department_repo, None)
        districts = business.get_districts_by_department_name("Aisne")
        
        self.assertEqual(3, len(districts))
        
        district_check = [20, 1, "1ère circo", 2]
        self.assert_test.assert_district_dto(district_check, districts[0])
        
        district_check = [21, 2, "2ème circo", 2]
        self.assert_test.assert_district_dto(district_check, districts[1])
        
        district_check = [22, 3, "3ème circo", 2]
        self.assert_test.assert_district_dto(district_check, districts[2])
        
        
    @patch.object(DistrictRepository, "get_districts")
    @patch.object(DepartmentBusiness, "get_departments")
    def test_get_departments_by_department_name_from_unknow_department(self, mock_district_repo, mock_department_repo) :
        mock_district_repo.get_districts.return_value = getDistricts_by_id([1, 2, 3, 4, 5, 6])
        mock_department_repo.get_departments.return_value = getDepartments_by_ids([1, 2])
        
        business = DistrictBusiness(mock_district_repo, mock_department_repo, None)
        districts = business.get_districts_by_department_name("XXX")
        
        self.assertEqual(districts, None)
        
        
    def __get_results_sorted(self) : 
        first_round_results = getResults([200, 210, 220, 230, 240, 250, 260, 270])
        second_round_results = getResults([205, 215, 225, 235, 245, 255, 265, 275])
        round_results = {"first_round" : first_round_results, "second_round" : second_round_results}
        return round_results
    
        
    @patch.object(DistrictRepository, "get_districts")
    @patch.object(ResultBusiness, "get_rounds_participation_sorted")
    @patch.object(DepartmentBusiness, "get_department_name_from_department_id")
    def test_get_districts_sorted_by_voting_rate(self, mock_district_repo, mock_result_business, mock_department_business) : 
        mock_district_repo.get_districts.return_value = getDistricts_by_id([20, 21, 22, 23, 24, 25, 26, 27])
        
        mock_result_business.get_rounds_participation_sorted.return_value = self.__get_results_sorted()
        
        mock_department_business.get_department_name_from_department_id.return_value = "Aisne"
         
        business = DistrictBusiness(mock_district_repo, mock_department_business, mock_result_business)
        
        districts_sorted = business.get_districts_by_voting_rate("ascending")        
        first_list_districts_result = districts_sorted["first_round"]     
        second_list_districts_result = districts_sorted["second_round"]        
        
        self.assertEqual(2, len(districts_sorted))
        
        self.__assert_districts_sorted(first_list_districts_result)
        
        self.__assert_districts_sorted(second_list_districts_result)
        
        
    def __assert_districts_sorted(self, districts) : 
        self.assertEqual(8, len(districts))
        
        district_check = [20, 1, "1ère circo", 2, 78.8, "Aisne"]
        self.assert_test.assert_district_result_dto(district_check, districts[0])
        
        district_check = [21, 2, "2ème circo", 2, 68.8, "Aisne"]
        self.assert_test.assert_district_result_dto(district_check, districts[1])
        
        district_check = [22, 3, "3ème circo", 2, 15.8, "Aisne"]
        self.assert_test.assert_district_result_dto(district_check, districts[2])
        
        district_check = [23, 4, "4ème circo", 2, 28.8, "Aisne"]
        self.assert_test.assert_district_result_dto(district_check, districts[3])
        
        district_check = [24, 5, "5ème circo", 2, 99.56, "Aisne"]
        self.assert_test.assert_district_result_dto(district_check, districts[4])
        
        district_check = [25, 6, "6ème circo", 2, 65.2, "Aisne"]
        self.assert_test.assert_district_result_dto(district_check, districts[5])
        
        district_check = [26, 7, "7ème circo", 2, 0.45, "Aisne"]
        self.assert_test.assert_district_result_dto(district_check, districts[6])
        
        district_check = [27, 8, "8ème circo", 2, 42.6, "Aisne"]
        self.assert_test.assert_district_result_dto(district_check, districts[7])