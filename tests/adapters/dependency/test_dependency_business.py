import unittest

from app.adapters.dependency.dependency_business import DependencyBusiness

class DependencyBusinessTest(unittest.TestCase) : 
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.dependency = DependencyBusiness()
        
        
    def test_party_business_not_null(self) : 
        self.assertIsNotNone(self.dependency.party_business)
        
        
    def test_result_business_not_null(self) : 
        self.assertIsNotNone(self.dependency.result_business)
        
        
    def test_district_business_not_null(self) : 
        self.assertIsNotNone(self.dependency.district_business)
        
        
    def test_department_business_not_null(self) : 
        self.assertIsNotNone(self.dependency.department_business)
        
        
    def test_candidate_business_not_null(self) : 
        self.assertIsNotNone(self.dependency.candidate_business)
        
        
    def test_deputy_business_not_null(self) :
        self.assertIsNotNone(self.dependency.deputy_business)