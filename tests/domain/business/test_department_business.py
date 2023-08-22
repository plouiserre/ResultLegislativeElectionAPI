import unittest

from app.domain.business.department_business import DepartmentBusiness
from app.domain.factory.factorydepartment import FactoryDepartment
from app.domain.factory.factorydepartmentresult import FactoryDepartmentResult
from app.domain.factory.factorydistrict import FactoryDistrict
from app.domain.factory.factoryresult import FactoryResult
from app.domain.repository.department_repository import DepartmentRepository
from app.domain.repository.district_repository import DistrictRepository
from app.domain.repository.result_repository import ResultRepository
from tests.assert_test import AssertTest
from unittest.mock import patch

class DepartmentBusinessTest(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.assert_test = AssertTest(self)
        
        
    def __get_departments(self) :
        factory = FactoryDepartment()
        departments = []
        first_department = factory.construct_department_from_bdd([1, "Ain", 1])
        second_department = factory.construct_department_from_bdd([2, "Aisne", 2])
        third_department = factory.construct_department_from_bdd([3, "Allier", 3])
        thirty_third_department = factory.construct_department_from_bdd([33, "Gironde", 33])
        departments = [first_department, second_department, third_department, thirty_third_department]
        return departments
    
    
    @patch.object(DepartmentRepository, "get_departments")
    def test_get_departments(self, mock_repo):
        mock_repo.get_departments.return_value = self.__get_departments()
        
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
        mock_repo.get_departments.return_value = self.__get_departments()
        
        business = DepartmentBusiness(mock_repo, None, None)
        
        department = business.get_department_by_name("Gironde")
        
        department_check = [33, "Gironde", 33]
        self.assert_test.assert_department_dto(department_check, department)


    @patch.object(DepartmentRepository, "get_departments")
    def test_get_department_name_from_department_id(self, mock_dep_repo): 
        mock_dep_repo.get_departments.return_value = self.__get_departments()
        
        business = DepartmentBusiness(mock_dep_repo, None, None)
        
        result = business.get_department_name_from_department_id(33)
        
        self.assertEqual("Gironde", result)      
            
        
    def __get_five_departments(self) :
        factory = FactoryDepartment()
        departments = []
        first_department = factory.construct_department_from_bdd([1, "Ain", 1])
        eleventh_department = factory.construct_department_from_bdd([11, "Aude", 11])
        thirty_third_department = factory.construct_department_from_bdd([33, "Gironde", 33])
        thirty_fourth_department = factory.construct_department_from_bdd([34, "Herault", 34])
        sixty_nineth_department = factory.construct_department_from_bdd([69, "Nord", 69])
        departments = [first_department, eleventh_department, thirty_third_department, thirty_fourth_department, sixty_nineth_department]
        return departments
        
        
    # #TODO factoriser avec la classe de test district business and improve the test below
    def __get_fifteen_districts(self) : 
        factory = FactoryDistrict()
        first_district = factory.construct_district(1, 1, "1ère circo", 1)
        second_district = factory.construct_district(2, 2, "2ème circo", 1)
        third_district = factory.construct_district(3, 3, "3ème circo", 1)
        fourth_district = factory.construct_district(4, 1, "1ère circo", 11)
        fifth_district = factory.construct_district(5, 2, "1ème circo", 11)
        sixth_district = factory.construct_district(6, 1, "1ère circo", 33)
        seventh_district = factory.construct_district(7, 2, "2ème circo", 33)
        eighth_district = factory.construct_district(8, 1, "1ère circo", 34)
        nineth_district = factory.construct_district(9, 2, "2ème circo", 34)
        tenth_district = factory.construct_district(10, 3, "3ème circo", 34)
        eleventh_district = factory.construct_district(11, 4, "4ème circo", 34)
        twelfth_district = factory.construct_district(12, 1, "1ère circo", 69)
        thirteenth_district = factory.construct_district(13, 2, "2ème circo", 69)
        fourteenth_district = factory.construct_district(14, 3, "3ème circo", 69)
        fifteenth_district = factory.construct_district(15, 4, "4ème circo", 69)
        districts = [first_district, second_district, third_district, fourth_district, fifth_district, sixth_district, 
                     seventh_district, eighth_district, nineth_district, tenth_district, eleventh_district, 
                     twelfth_district, thirteenth_district, fourteenth_district, fifteenth_district]
        return districts
    
        
     #TODO factoriser avec la classe de test district business
    
    
    def __get_results_belonging_fifteen_districts(self) :
        results = []
        factory = FactoryResult()
        first_result_first_district = factory.construct_result(1, "Completed", 1, 876, 5, 0.65, 666, 98.8, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 1)
        second_result_first_district = factory.construct_result(2, "Completed", 2, 876, 5, 0.65, 666, 18.8, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 1)
        
        first_result_second_district = factory.construct_result(3, "Completed", 1, 276, 23, 1.65, 866, 38.8, 3, 5.2, 1.7, 566, 88.8, 3, 5.2, 1.7, 2.7, 2)
        second_result_second_district = factory.construct_result(4, "Completed", 2, 276, 23, 1.65, 866, 68.8, 3, 5.2, 1.7, 566, 88.8, 3, 5.2, 1.7, 2.7, 2)
        
        first_result_third_district = factory.construct_result(5, "Completed", 1, 576, 23, 8.65, 566, 35.8, 8, 8.2, 8.7, 605, 68.8, 13, 3.2, 4.7, 5.7, 3)
        second_result_third_district = factory.construct_result(6, "Completed", 2, 576, 23, 8.65, 566, 25.8, 8, 8.2, 8.7, 605, 68.8, 13, 3.2, 4.7, 5.7, 3)
        
        first_result_fourth_district = factory.construct_result(7, "Completed", 1, 876, 5, 0.65, 666, 12.8, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 4)
        second_result_fourth_district = factory.construct_result(8, "Completed", 2, 876, 5, 0.65, 666, 7.8, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 4)
        
        first_result_fifth_district = factory.construct_result(9, "Completed", 1, 276, 23, 1.65, 866, 58.8, 3, 5.2, 1.7, 566, 88.8, 3, 5.2, 1.7, 2.7, 5)
        second_result_fifth_district = factory.construct_result(10, "Completed", 2, 276, 23, 1.65, 866, 48.8, 3, 5.2, 1.7, 566, 88.8, 3, 5.2, 1.7, 2.7, 5)
        
        first_result_sixth_district = factory.construct_result(11, "Completed", 1, 576, 23, 8.65, 566, 66.8, 8, 8.2, 8.7, 605, 68.8, 13, 3.2, 4.7, 5.7, 6)
        second_result_sixth_district = factory.construct_result(12, "Completed", 2, 576, 23, 8.65, 566, 43.8, 8, 8.2, 8.7, 605, 68.8, 13, 3.2, 4.7, 5.7, 6)
        
        first_result_seventh_district = factory.construct_result(13, "Completed", 1, 876, 5, 0.65, 666, 42.8, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 7)
        second_result_seventh_district = factory.construct_result(14, "Completed", 2, 876, 5, 0.65, 666, 23.8, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 7)
        
        first_result_eighth_district = factory.construct_result(15, "Completed", 1, 276, 23, 1.65, 866, 78.8, 3, 5.2, 1.7, 566, 88.8, 3, 5.2, 1.7, 2.7, 8)
        second_result_eighth_district = factory.construct_result(16, "Completed", 2, 276, 23, 1.65, 866, 68.8, 3, 5.2, 1.7, 566, 88.8, 3, 5.2, 1.7, 2.7, 8)
        
        first_result_nineth_district = factory.construct_result(17, "Completed", 1, 576, 23, 8.65, 566, 23.8, 8, 8.2, 8.7, 605, 68.8, 13, 3.2, 4.7, 5.7, 9)
        second_result_nineth_district = factory.construct_result(18, "Completed", 2, 576, 23, 8.65, 566, 42.8, 8, 8.2, 8.7, 605, 68.8, 13, 3.2, 4.7, 5.7, 9)
        
        first_result_tenth_district = factory.construct_result(19, "Completed", 1, 876, 5, 0.65, 666, 43.8, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 10)
        second_result_tenth_district = factory.construct_result(20, "Completed", 2, 876, 5, 0.65, 666, 66.8, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 10)
        
        first_result_eleventh_district = factory.construct_result(21, "Completed", 1, 276, 23, 1.65, 866, 48.8, 3, 5.2, 1.7, 566, 88.8, 3, 5.2, 1.7, 2.7, 11)
        second_result_eleventh_district = factory.construct_result(22, "Completed", 2, 276, 23, 1.65, 866, 58.8, 3, 5.2, 1.7, 566, 88.8, 3, 5.2, 1.7, 2.7, 11)
        
        first_result_twelfth_district = factory.construct_result(23, "Completed", 1, 576, 23, 8.65, 566, 7.8, 8, 8.2, 8.7, 605, 68.8, 13, 3.2, 4.7, 5.7, 12)
        second_result_twelfth_district = factory.construct_result(24, "Completed", 2, 576, 23, 8.65, 566, 12.8, 8, 8.2, 8.7, 605, 68.8, 13, 3.2, 4.7, 5.7, 12)
        
        first_result_thirteenth_district = factory.construct_result(25, "Completed", 1, 876, 5, 0.65, 666, 25.8, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 13)
        second_result_thirteenth_district = factory.construct_result(26, "Completed", 2, 876, 5, 0.65, 666, 35.8, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 13)
        
        first_result_fourteenth_district = factory.construct_result(27, "Completed", 1, 276, 23, 1.65, 866, 68.8, 3, 5.2, 1.7, 566, 88.8, 3, 5.2, 1.7, 2.7, 14)
        second_result_fourteenth_district = factory.construct_result(28, "Completed", 2, 276, 23, 1.65, 866, 38.8, 3, 5.2, 1.7, 566, 88.8, 3, 5.2, 1.7, 2.7, 14)
        
        first_result_fifteenth_district = factory.construct_result(29, "Completed", 1, 576, 23, 8.65, 566, 18.8, 8, 8.2, 8.7, 605, 68.8, 13, 3.2, 4.7, 5.7, 15)
        second_result_fifteenth_district = factory.construct_result(30, "Completed", 2, 576, 23, 8.65, 566, 98.8, 8, 8.2, 8.7, 605, 68.8, 13, 3.2, 4.7, 5.7, 15)
        
        results = [first_result_first_district, second_result_first_district, first_result_second_district, second_result_second_district, first_result_third_district,
                   second_result_third_district, first_result_fourth_district, second_result_fourth_district, first_result_fifth_district, second_result_fifth_district,
                   first_result_sixth_district, second_result_sixth_district, first_result_seventh_district, second_result_seventh_district, first_result_eighth_district,
                   second_result_eighth_district, first_result_nineth_district, second_result_nineth_district, first_result_tenth_district, second_result_tenth_district,
                   first_result_eleventh_district, second_result_eleventh_district, first_result_twelfth_district, second_result_twelfth_district, first_result_thirteenth_district,
                   second_result_thirteenth_district, first_result_fourteenth_district, second_result_fourteenth_district, first_result_fifteenth_district,
                   second_result_fifteenth_district]
        return results
    
        
    @patch.object(DepartmentRepository, "get_departments")
    @patch.object(DistrictRepository, "get_districts")
    @patch.object(ResultRepository, "get_results")
    def test_get_departments_by_voting_rate(self, mock_department_repository, mock_district_repository, mock_result_business):
        mock_department_repository.get_departments.return_value = self.__get_five_departments()
        mock_district_repository.get_districts.return_value = self.__get_fifteen_districts()
        mock_result_business.get_results.return_value = self.__get_results_belonging_fifteen_districts()
        
        department_business = DepartmentBusiness(mock_department_repository, mock_district_repository, mock_result_business)
        
        departments_results_all_rounds = department_business.get_departments_by_voting_rate()
        
        self.assertEqual(2, len(departments_results_all_rounds))
        
        first_round_departments_results = departments_results_all_rounds["first_round"]     
        
        first_round_first_department_result = first_round_departments_results[0]
        first_round_first_department_check = [69, "Nord", 69, 30.3]
        self.assert_test.assert_department_result_dto(first_round_first_department_check, first_round_first_department_result)  
        
        first_round_second_department_result = first_round_departments_results[1]
        first_round_second_department_check = [11, "Aude", 11, 35.8]
        self.assert_test.assert_department_result_dto(first_round_second_department_check, first_round_second_department_result)  
        
        first_round_third_department_result = first_round_departments_results[2]
        first_round_third_department_check = [34, "Herault", 34, 48.8]
        self.assert_test.assert_department_result_dto(first_round_third_department_check, first_round_third_department_result)  
        
        first_round_fourth_department_result = first_round_departments_results[3]
        first_round_fourth_department_check = [33, "Gironde", 33, 54.8]
        self.assert_test.assert_department_result_dto(first_round_fourth_department_check, first_round_fourth_department_result)  
        
        first_round_fifth_department_result = first_round_departments_results[4]
        first_round_fifth_department_check = [1, "Ain", 1, 57.8]
        self.assert_test.assert_department_result_dto(first_round_fifth_department_check, first_round_fifth_department_result)
        
        second_round_departments_results = departments_results_all_rounds["second_round"]     
        
        second_round_first_department_result = second_round_departments_results[0]
        second_round_first_department_check = [11, "Aude", 11, 28.3]
        self.assert_test.assert_department_result_dto(second_round_first_department_check, second_round_first_department_result)  
        
        second_round_second_department_result = second_round_departments_results[1]
        second_round_second_department_check = [33, "Gironde", 33, 33.8]
        self.assert_test.assert_department_result_dto(second_round_second_department_check, second_round_second_department_result)  
        
        second_round_third_department_result = second_round_departments_results[2]
        second_round_third_department_check = [1, "Ain", 1, 37.8]
        self.assert_test.assert_department_result_dto(second_round_third_department_check, second_round_third_department_result)  
        
        second_round_fourth_department_result = second_round_departments_results[3]
        second_round_fourth_department_check = [69, "Nord", 69, 46.55]
        self.assert_test.assert_department_result_dto(second_round_fourth_department_check, second_round_fourth_department_result)  
        
        second_round_fifth_department_result = second_round_departments_results[4]
        second_round_fifth_department_check = [34, "Herault", 34, 59.3]
        self.assert_test.assert_department_result_dto(second_round_fifth_department_check, second_round_fifth_department_result)