import unittest

from app.domain.business.department_business import DepartmentBusiness
from app.domain.business.district_business import DistrictBusiness
from app.domain.business.result_business import ResultBusiness
from app.domain.factory.factorydepartment import FactoryDepartment
from app.domain.factory.factorydistrict import FactoryDistrict
from app.domain.factory.factoryresult import FactoryResult
from app.domain.repository.district_repository import DistrictRepository
from tests.assert_test import AssertTest
from unittest.mock import patch

class DistrictBusinessTest(unittest.TestCase):
    
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.assert_test = AssertTest(self)
        
    
    def __get_districts(self) : 
        factory = FactoryDistrict()
        first_district = factory.construct_district_from_bdd([1, 1,	"1ère circonscription",	1])
        second_district = factory.construct_district_from_bdd([2, 2, "2ème circonscription", 2])
        third_district = factory.construct_district_from_bdd([3, 3,	"3ème circonscription",	1])
        fourth_district = factory.construct_district_from_bdd([4, 4, "4ème circonscription", 2])
        districts = [first_district, second_district, third_district, fourth_district]
        return districts
    
    
    def __get_departments(self) : 
        factory = FactoryDepartment()
        first_department = factory.construct_department_from_bdd([1, "Ain", 1])
        second_department = factory.construct_department_from_bdd([2, "Aisne", 2])
        departments = [first_department, second_department]
        return departments
    
    
    @patch.object(DistrictRepository, "get_districts")
    def test_get_districts(self, mock_repo):
        mock_repo.get_districts.return_value = self.__get_districts()
        
        business = DistrictBusiness(mock_repo, None, None)
        districts = business.get_districts()
        
        self.assertEqual(4, len(districts))
        
        district_check = [1, 1,	"1ère circonscription",	1]
        self.assert_test.assert_district_dto(district_check, districts[0])
        
        district_check = [2, 2, "2ème circonscription", 2]
        self.assert_test.assert_district_dto(district_check, districts[1])
        
        district_check = [3, 3,	"3ème circonscription",	1]
        self.assert_test.assert_district_dto(district_check, districts[2])
        
        district_check = [4, 4, "4ème circonscription", 2]
        self.assert_test.assert_district_dto(district_check, districts[3])
        
    
    @patch.object(DistrictRepository, "get_districts")
    def test_get_districts_by_department_id(self, mock_repo):
        mock_repo.get_districts.return_value = self.__get_districts()
        
        business = DistrictBusiness(mock_repo, None, None)
        districts = business.get_districts_by_department_id(2)
        
        self.assertEqual(2, len(districts))
        
        district_check = [2, 2, "2ème circonscription", 2]
        self.assert_test.assert_district_dto(district_check, districts[0])
        
        district_check = [4, 4, "4ème circonscription", 2]
        self.assert_test.assert_district_dto(district_check, districts[1])
        
        
    @patch.object(DistrictRepository, "get_districts")
    @patch.object(DepartmentBusiness, "get_departments")
    def test_get_departments_by_department_name(self, mock_district_repo, mock_department_repo) :
        mock_district_repo.get_districts.return_value = self.__get_districts()
        mock_department_repo.get_departments.return_value = self.__get_departments()
        
        business = DistrictBusiness(mock_district_repo, mock_department_repo, None)
        districts = business.get_districts_by_department_name("Aisne")
        
        self.assertEqual(2, len(districts))
        
        district_check = [2, 2, "2ème circonscription", 2]
        self.assert_test.assert_district_dto(district_check, districts[0])
        
        district_check = [4, 4, "4ème circonscription", 2]
        self.assert_test.assert_district_dto(district_check, districts[1])
        
        
    @patch.object(DistrictRepository, "get_districts")
    @patch.object(DepartmentBusiness, "get_departments")
    def test_get_departments_by_department_name_from_unknow_department(self, mock_district_repo, mock_department_repo) :
        mock_district_repo.get_districts.return_value = self.__get_districts()
        mock_department_repo.get_departments.return_value = self.__get_departments()
        
        business = DistrictBusiness(mock_district_repo, mock_department_repo, None)
        districts = business.get_districts_by_department_name("XXX")
        
        self.assertEqual(districts, None)
        
        
    def __get_results_sorted(self) : 
        first_round_results = self.__get_result_from_specific_rounded(1)    
        second_round_results = self.__get_result_from_specific_rounded(2)
        round_results = {"first_round" : first_round_results, "second_round" : second_round_results}
        return round_results
    
        
    def __get_result_from_specific_rounded(self, round_number) :
        factory = FactoryResult()
        first_result = factory.construct_result(1, "Completed", round_number, 876, 5, 0.65, 666, 78.8, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 23)
        second_result = factory.construct_result(2, "Completed", round_number, 276, 23, 1.65, 866, 68.8, 3, 5.2, 1.7, 566, 88.8, 3, 5.2, 1.7, 2.7, 24)
        third_result = factory.construct_result(3, "Completed", round_number, 576, 23, 8.65, 566, 15.8, 8, 8.2, 8.7, 605, 68.8, 13, 3.2, 4.7, 5.7, 25)
        fourth_result = factory.construct_result(4, "Completed", round_number, 676, 50, 10.65, 266, 28.8, 5, 23.2, 4.7, 266, 48.8, 8, 4.2, 2.7, 0.9, 26)
        fifth_result = factory.construct_result(5, "Completed", round_number, 876, 5, 0.65, 666, 99.56, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 27)
        sixth_result = factory.construct_result(6, "Completed", round_number, 876, 5, 0.65, 666, 65.2, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 28)
        seventh_result = factory.construct_result(7, "Completed", round_number, 876, 5, 0.65, 666, 0.45, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 29)
        eighth_result = factory.construct_result(8, "Completed", round_number, 876, 5, 0.65, 666, 42.6, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 30)
        round_results = [first_result, second_result, third_result, fourth_result, fifth_result, sixth_result, seventh_result, eighth_result]  
        return round_results
    
    
    def __get_eight_districts_to_sorted(self) : 
        factory = FactoryDistrict()
        first_district= factory.construct_district(29, 29, "29ème circonscription", 2)
        second_district= factory.construct_district(25, 25, "25ème circonscription", 2)
        third_district= factory.construct_district(26, 26, "29ème circonscription", 2)
        fourth_district= factory.construct_district(30, 30, "30ème circonscription", 2)
        fifth_district= factory.construct_district(28, 28, "28ème circonscription", 2)
        sixth_district= factory.construct_district(24, 24, "24ème circonscription", 2)
        seventh_district= factory.construct_district(23, 23, "23ème circonscription", 2)
        eighth_district= factory.construct_district(27, 27, "27ème circonscription", 2)
        districts = [first_district, second_district, third_district, fourth_district, fifth_district, sixth_district, seventh_district, eighth_district]
        return districts
    
    
        
    #TODO improve this method
    #TODO rework this UT with this new code
    @patch.object(DistrictRepository, "get_districts")
    @patch.object(ResultBusiness, "get_rounds_participation_sorted")
    @patch.object(DepartmentBusiness, "get_department_name_from_department_id")
    def test_get_districts_sorted_by_voting_rate(self, mock_district_repo, mock_result_business, mock_department_business) : 
        mock_district_repo.get_districts.return_value = self.__get_eight_districts_to_sorted()
        mock_result_business.get_rounds_participation_sorted.return_value = self.__get_results_sorted()
        mock_department_business.get_department_name_from_department_id.return_value = "Aisne"
         
        business = DistrictBusiness(mock_district_repo, mock_department_business, mock_result_business)
        
        districts_sorted = business.get_districts_by_voting_rate()        
        first_list_districts_result = districts_sorted["first_round"]     
        second_list_districts_result = districts_sorted["second_round"]        
        
        self.assertEqual(2, len(districts_sorted))
        
        self.__assert_districts_sorted(first_list_districts_result)
        
        self.__assert_districts_sorted(second_list_districts_result)
        
        
    def __assert_districts_sorted(self, districts) : 
        self.assertEqual(8, len(districts))
        
        district_check = [23, 23, "23ème circonscription", 2, 78.8, "Aisne"]
        self.assert_test.assert_district_result_dto(district_check, districts[0])
        
        district_check = [24, 24, "24ème circonscription", 2, 68.8, "Aisne"]
        self.assert_test.assert_district_result_dto(district_check, districts[1])
        
        district_check = [25, 25, "25ème circonscription", 2, 15.8, "Aisne"]
        self.assert_test.assert_district_result_dto(district_check, districts[2])
        
        district_check = [26, 26, "29ème circonscription", 2, 28.8, "Aisne"]
        self.assert_test.assert_district_result_dto(district_check, districts[3])
        
        district_check = [27, 27, "27ème circonscription", 2, 99.56, "Aisne"]
        self.assert_test.assert_district_result_dto(district_check, districts[4])
        
        district_check = [28, 28, "28ème circonscription", 2, 65.2, "Aisne"]
        self.assert_test.assert_district_result_dto(district_check, districts[5])
        
        district_check = [29, 29, "29ème circonscription", 2, 0.45, "Aisne"]
        self.assert_test.assert_district_result_dto(district_check, districts[6])
        
        district_check = [30, 30, "30ème circonscription", 2, 42.6, "Aisne"]
        self.assert_test.assert_district_result_dto(district_check, districts[7])