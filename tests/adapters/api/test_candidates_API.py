import unittest
from unittest.mock import Mock

from app.main import app
from app.adapters.API.candidatesAPI import init_candidate_business
from app.adapters.dependency.dependency_business import DependencyBusiness
from fastapi.testclient import TestClient


def override_candidate_business() :
    mock = Mock()
    mock.get_candidates.return_value = [{"LastName" : "Cazenave", "FirstName" : "Thomas", "Sexe" : "M"}, {"LastName" : "TRASTOUR-ISNART", "FirstName" : "Laurence", "Sexe" : "F"}]
    mock.get_candidates_by_party.return_value = [{"LastName" : "LAPRAY", "FirstName" : "Lumir", "Sexe" : "F"}, {"LastName" : "DAUBIÉ", "FirstName" : "Romain", "Sexe" : "M"}]
    mock.get_candidates_by_departement.return_value = [{"LastName" : "EL OUASDI", "FirstName" : "Fatima", "Sexe" : "F"}, {"LastName" : "DELATTE", "FirstName" : "Marc", "Sexe" : "M"}]
    mock.get_candidates_by_district.return_value = [{"LastName" : "Cazenave", "FirstName" : "Thomas", "Sexe" : "M"},{"LastName" : "LAPRAY", "FirstName" : "Lumir", "Sexe" : "F"},{"LastName" : "EL OUASDI", "FirstName" : "Fatima", "Sexe" : "F"}]
    return mock

   
def override_candidate_business_exception() :
    mock = Mock()
    mock.get_candidates.side_effect = Exception("Boom!")
    mock.get_candidates.return_value = ""
    mock.get_candidates_by_party.side_effect = Exception("Boom!")
    mock.get_candidates_by_party.return_value = ""
    mock.get_candidates_by_departement.side_effect = Exception("Boom!")
    mock.get_candidates_by_departement.return_value = ""
    mock.get_candidates_by_district.side_effect = Exception("Boom!")
    mock.get_candidates_by_district.return_value = ""
    return mock    
    
    
def override_candidate_no_result():
    mock = Mock()
    mock.get_candidates_by_departement.return_value = None
    mock.get_candidates_by_district.return_value = None
    mock.get_candidates_by_party.return_value = None
    return mock


class CandidatesAPITest(unittest.TestCase) : 
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.client = TestClient(app)
        
    
    def overriding_business_dependency(self, result_action) : 
        if result_action == "success" :
            app.dependency_overrides[init_candidate_business] = override_candidate_business  
        elif result_action == "error" : 
            app.dependency_overrides[init_candidate_business] = override_candidate_business_exception 
        elif result_action == "no_result": 
            app.dependency_overrides[init_candidate_business] = override_candidate_no_result 
            
   
    def test_get_candidates_status_OK_when_no_error(self) : 
        self.overriding_business_dependency("success")  
        response = self.client.get("/candidates")
        
        self.assertEqual(200, response.status_code)
        self.assertEqual([{"LastName" : "Cazenave", "FirstName" : "Thomas", "Sexe" : "M"}, {"LastName" : "TRASTOUR-ISNART", "FirstName" : "Laurence", "Sexe" : "F"}], response.json())  
    
      
    def test_get_candidates_status_500_when_errors(self) : 
        self.overriding_business_dependency("error")  
        response = self.client.get("/candidates")
        
        self.assertEqual(500, response.status_code)
        self.assertEqual({'detail': 'Treatment failed'}, response.json())
        
        
    def test_get_candidates_by_party_OK_when_no_error(self) : 
        self.overriding_business_dependency("success")  
        response = self.client.get("/candidates/?party=ENS")
        
        self.assertEqual(200, response.status_code)
        self.assertEqual([{"LastName" : "LAPRAY", "FirstName" : "Lumir", "Sexe" : "F"}, {"LastName" : "DAUBIÉ", "FirstName" : "Romain", "Sexe" : "M"}], response.json())
        
        
    def test_get_candidates_by_party_status_404_when_no_result(self) : 
        self.overriding_business_dependency("no_result")  
        response = self.client.get("/candidates/?party=XXX")
        
        self.assertEqual(404, response.status_code)
        self.assertEqual({'detail': 'No result'}, response.json())
        
        
    def test_get_candidates_by_party_status_500_when_errors(self) : 
        self.overriding_business_dependency("error")  
        response = self.client.get("/candidates/?party=ENS")
        
        self.assertEqual(500, response.status_code)
        self.assertEqual({'detail': 'Treatment failed'}, response.json()) 
        
        
    def test_get_candidates_by_department_OK_when_no_error(self) : 
        self.overriding_business_dependency("success")  
        response = self.client.get("candidates/?department=Gironde")
        
        self.assertEqual(200, response.status_code)
        self.assertEqual([{"LastName" : "EL OUASDI", "FirstName" : "Fatima", "Sexe" : "F"}, {"LastName" : "DELATTE", "FirstName" : "Marc", "Sexe" : "M"}], response.json())
        
        
    def test_get_candidates_by_department_status_500_when_errors(self) : 
        self.overriding_business_dependency("error")  
        response = self.client.get("candidates/?department=Gironde")
        
        self.assertEqual(500, response.status_code)
        self.assertEqual({'detail': 'Treatment failed'}, response.json()) 
        
        
    def test_get_candidates_by_department_status_404_when_no_results(self) :
        self.overriding_business_dependency("no_result")
        response = self.client.get("candidates/?department=Gironde")

        self.assertEqual(404, response.status_code)
        self.assertEqual({'detail': 'No result'}, response.json())
        
        
    def test_get_candidates_by_district_OK_when_no_error(self) : 
        self.overriding_business_dependency("success")
        response = self.client.get("candidates/?district=33")
        
        self.assertEqual(200, response.status_code)
        self.assertEqual([{"LastName" : "Cazenave", "FirstName" : "Thomas", "Sexe" : "M"},{"LastName" : "LAPRAY", "FirstName" : "Lumir", "Sexe" : "F"},{"LastName" : "EL OUASDI", "FirstName" : "Fatima", "Sexe" : "F"}], response.json())


    def test_get_candidates_by_district_status_500_when_errors(self) : 
        self.overriding_business_dependency("error")
        response = self.client.get("candidates/?district=33")
        
        self.assertEqual(500, response.status_code)
        self.assertEqual({'detail': 'Treatment failed'}, response.json()) 
        
        
    def test_get_candidates_by_district_status_404_when_no_results(self) : 
        self.overriding_business_dependency("no_result")
        response = self.client.get("candidates/?district=33")

        self.assertEqual(404, response.status_code)
        self.assertEqual({'detail': 'No result'}, response.json())