import unittest

from app.domain.DTO.districtDTO import DistrictDTO
from app.domain.factory.factorydistrict import FactoryDistrict
from app.domain.factory.factorydistrictresult import FactoryDistrictResult

from tests.assert_test import AssertTest

class FactoryDistrictResultTest(unittest.TestCase): 
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.assert_test = AssertTest(self)
        
        
    def test_factory_district_result(self) : 
        factory_district = FactoryDistrict()
        district = factory_district.construct_district(15, 15, "15ème circonscription", 33)
        rate_voting = 33.33
        department_name = "Gironde"
        
        factory = FactoryDistrictResult()
        
        result = factory.construct_district_result(district, rate_voting, department_name)
        
        district_result_check = [15, 15, "15ème circonscription", 33, 33.33, "Gironde"]
        self.assert_test.assert_district_result_dto(district_result_check, result)