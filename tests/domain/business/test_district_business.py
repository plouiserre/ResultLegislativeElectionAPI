import unittest

from app.domain.business.district_business import DistrictBusiness
from app.domain.factory.factorydistrict import FactoryDistrict
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
    
    @patch.object(DistrictRepository, "get_districts")
    def test_get_districts(self, mock_repo):
        mock_repo.get_districts.return_value = self.__get_districts()
        
        business = DistrictBusiness(mock_repo)
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
        
        business = DistrictBusiness(mock_repo)
        districts = business.get_districts_by_department_id(2)
        
        self.assertEqual(2, len(districts))
        
        district_check = [2, 2, "2ème circonscription", 2]
        self.assert_test.assert_district_dto(district_check, districts[0])
        
        district_check = [4, 4, "4ème circonscription", 2]
        self.assert_test.assert_district_dto(district_check, districts[1])