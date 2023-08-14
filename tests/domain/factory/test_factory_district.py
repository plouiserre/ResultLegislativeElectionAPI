import unittest

from app.domain.factory.factorydistrict import FactoryDistrict
from tests.assert_test import AssertTest

class FactoryDistrictTest(unittest.TestCase) : 
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.assert_test = AssertTest(self)
        
    def test_construct_district(self) : 
        factory = FactoryDistrict()
        
        district = factory.construct_district(29, 29, "29ème circonscription", 2)
        
        district_data = [29, 29, "29ème circonscription", 2]
        self.assert_test.assert_district_dto(district_data, district)
        
    
    def test_construct_district_from_bdd(self):
        factory = FactoryDistrict()
        
        district_data = [8,	3, "3ème circonscription", 2]
        district = factory.construct_district_from_bdd(district_data)
        
        self.assert_test.assert_district_dto(district_data, district)