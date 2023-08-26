import unittest

from app.domain.business.department_business import DepartmentBusiness
from app.domain.repository.department_repository import DepartmentRepository
from app.domain.repository.district_repository import DistrictRepository
from app.domain.repository.result_repository import ResultRepository
from tests.assert_test import AssertTest
from tests.faker import getDepartments, getDistricts, getResults
from unittest.mock import patch

class DepartmentBusinessTest(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.assert_test = AssertTest(self)
    
    
    @patch.object(DepartmentRepository, "get_departments")
    def test_get_departments(self, mock_repo):
        mock_repo.get_departments.return_value = getDepartments([1, 2, 3, 33])
        
        business = DepartmentBusiness(mock_repo, None, None)
        
        departments = business.get_departments()
        
        self.assertEqual(4, len(departments))
        
        department_check = [1, "Ain", 1]
        self.assert_test.assert_department_dto(department_check, departments[0])
        
        department_check = [2, "Aisne", 2]
        self.assert_test.assert_department_dto(department_check, departments[1])
        
        department_check = [3, "Allier", 3]
        self.assert_test.assert_department_dto(department_check, departments[2])
        
        department_check = [33, "Gironde", 33]
        self.assert_test.assert_department_dto(department_check, departments[3])
        
        
    @patch.object(DepartmentRepository, "get_departments")
    def test_get_departments_by_name(self, mock_repo):
        mock_repo.get_departments.return_value = getDepartments([1, 2, 3, 33])
        
        business = DepartmentBusiness(mock_repo, None, None)
        
        department = business.get_department_by_name("Gironde")
        
        department_check = [33, "Gironde", 33]
        self.assert_test.assert_department_dto(department_check, department)


    @patch.object(DepartmentRepository, "get_departments")
    def test_get_department_name_from_department_id(self, mock_dep_repo): 
        mock_dep_repo.get_departments.return_value = getDepartments([1, 2, 3, 33])
        
        business = DepartmentBusiness(mock_dep_repo, None, None)
        
        result = business.get_department_name_from_department_id(33)
        
        self.assertEqual("Gironde", result)         
    
        
    @patch.object(DepartmentRepository, "get_departments")
    @patch.object(DistrictRepository, "get_districts")
    @patch.object(ResultRepository, "get_results")
    def test_get_departments_by_voting_rate_ascending(self, mock_department_repository, mock_district_repository, mock_result_business):
        mock_department_repository.get_departments.return_value = getDepartments([1, 11, 33, 34, 69])
        mock_district_repository.get_districts.return_value = getDistricts([10, 11, 12, 110, 111, 330, 331, 340, 341, 342, 343, 690, 691, 692, 693])
        mock_result_business.get_results.return_value =  getResults([100, 105, 110, 115, 120, 125, 1100, 1105, 1110, 1115, 3300, 3305, 3310, 3315, 
                                                                     3400, 3405, 3410, 3415, 3420, 3425, 3430, 3435, 6900, 6905, 6910, 6915, 6920, 6925, 6930, 6935])    
               
        
        department_business = DepartmentBusiness(mock_department_repository, mock_district_repository, mock_result_business)
        
        departments_results_all_rounds = department_business.get_departments_by_voting_rate("ascending")
        
        self.assertEqual(2, len(departments_results_all_rounds))
        
        first_round_departments_results = departments_results_all_rounds["first_round"]     
        
        self.assert_test.assert_department_result_dto([69, "Nord", 69, 30.3], first_round_departments_results[0])
        self.assert_test.assert_department_result_dto([11, "Aude", 11, 35.8], first_round_departments_results[1])
        self.assert_test.assert_department_result_dto([34, "Herault", 34, 48.8], first_round_departments_results[2])
        self.assert_test.assert_department_result_dto([33, "Gironde", 33, 54.8], first_round_departments_results[3])
        self.assert_test.assert_department_result_dto([1, "Ain", 1, 57.8], first_round_departments_results[4])  
        
        second_round_departments_results = departments_results_all_rounds["second_round"]     
        
        self.assert_test.assert_department_result_dto([11, "Aude", 11, 28.3], second_round_departments_results[0])  
        self.assert_test.assert_department_result_dto([33, "Gironde", 33, 33.8], second_round_departments_results[1]) 
        self.assert_test.assert_department_result_dto([1, "Ain", 1, 37.8], second_round_departments_results[2])  
        self.assert_test.assert_department_result_dto([69, "Nord", 69, 46.55], second_round_departments_results[3]) 
        self.assert_test.assert_department_result_dto([34, "Herault", 34, 59.3], second_round_departments_results[4])       
        
        
    @patch.object(DepartmentRepository, "get_departments")
    @patch.object(DistrictRepository, "get_districts")
    @patch.object(ResultRepository, "get_results")    
    def test_get_departments_by_voting_rate_with_creuse_have_only_district_and_one_result(self, mock_department_repository, mock_district_repository, mock_result_business):
        mock_department_repository.get_departments.return_value = getDepartments([1, 11])
        mock_district_repository.get_districts.return_value = getDistricts([10, 11, 12, 110, 111])
        mock_result_business.get_results.return_value =  getResults([100, 105, 110, 115, 120, 125, 1105, 1115])
        
        department_business = DepartmentBusiness(mock_department_repository, mock_district_repository, mock_result_business)
        
        departments_results_all_rounds = department_business.get_departments_by_voting_rate("ascending")
        
        self.assertEqual(2, len(departments_results_all_rounds))
        
        first_round_departments_results = departments_results_all_rounds["first_round"]     
        
        self.assert_test.assert_department_result_dto([1, "Ain", 1, 57.8], first_round_departments_results[0])  
        
        second_round_departments_results = departments_results_all_rounds["second_round"]     
        
        self.assert_test.assert_department_result_dto([11, "Aude", 11, 28.3], second_round_departments_results[0])  
        self.assert_test.assert_department_result_dto([1, "Ain", 1, 37.8], second_round_departments_results[1])  
        
        
        
    @patch.object(DepartmentRepository, "get_departments")
    @patch.object(DistrictRepository, "get_districts")
    @patch.object(ResultRepository, "get_results")
    def test_get_departments_by_voting_rate_descending(self, mock_department_repository, mock_district_repository, mock_result_business):
        mock_department_repository.get_departments.return_value = getDepartments([1, 11, 33, 34, 69])
        mock_district_repository.get_districts.return_value = getDistricts([10, 11, 12, 110, 111, 330, 331, 340, 341, 342, 343, 690, 691, 692, 693])
        mock_result_business.get_results.return_value =  getResults([100, 105, 110, 115, 120, 125, 1100, 1105, 1110, 1115, 3300, 3305, 3310, 3315, 
                                                                     3400, 3405, 3410, 3415, 3420, 3425, 3430, 3435, 6900, 6905, 6910, 6915, 6920, 6925, 6930, 6935])    
               
        
        department_business = DepartmentBusiness(mock_department_repository, mock_district_repository, mock_result_business)
        
        departments_results_all_rounds = department_business.get_departments_by_voting_rate("descending")
        
        self.assertEqual(2, len(departments_results_all_rounds))
        
        first_round_departments_results = departments_results_all_rounds["first_round"]     
        
        self.assert_test.assert_department_result_dto([1, "Ain", 1, 57.8], first_round_departments_results[0])  
        self.assert_test.assert_department_result_dto([33, "Gironde", 33, 54.8], first_round_departments_results[1])
        self.assert_test.assert_department_result_dto([34, "Herault", 34, 48.8], first_round_departments_results[2])
        self.assert_test.assert_department_result_dto([11, "Aude", 11, 35.8], first_round_departments_results[3])
        self.assert_test.assert_department_result_dto([69, "Nord", 69, 30.3], first_round_departments_results[4])
        
        second_round_departments_results = departments_results_all_rounds["second_round"]     
        
        self.assert_test.assert_department_result_dto([34, "Herault", 34, 59.3], second_round_departments_results[0])              
        self.assert_test.assert_department_result_dto([69, "Nord", 69, 46.55], second_round_departments_results[1]) 
        self.assert_test.assert_department_result_dto([1, "Ain", 1, 37.8], second_round_departments_results[2])  
        self.assert_test.assert_department_result_dto([33, "Gironde", 33, 33.8], second_round_departments_results[3]) 
        self.assert_test.assert_department_result_dto([11, "Aude", 11, 28.3], second_round_departments_results[4])          