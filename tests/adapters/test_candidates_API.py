import unittest
from unittest.mock import Mock

from app.main import app
from app.adapters.candidatesAPI import init_candidate_business
from fastapi.testclient import TestClient


def override_candidate_business() :
    json = [{"LastName" : "Cazenave", "FirstName" : "Thomas", "Sexe" : "M"}, {"LastName" : "TRASTOUR-ISNART", "FirstName" : "Laurence", "Sexe" : "F"}]
    mock = Mock()
    mock.get_candidates.return_value = json
    return mock

   
def override_candidate_business_exception() :
    mock = Mock()
    mock.get_candidates.side_effect = Exception("Boom!")
    mock.get_candidates.return_value = ""
    return mock    
     

class CandidatesAPITest(unittest.TestCase) : 
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.app = app
        self.client = TestClient(app)
        
    
    def overriding_business_dependency(self, result_action) : 
        if result_action == "success" :
            app.dependency_overrides[init_candidate_business] = override_candidate_business  
        elif result_action == "error" : 
            app.dependency_overrides[init_candidate_business] = override_candidate_business_exception 
            
   
    def test_get_candidates_status_OK_when_no_errors(self) : 
        self.overriding_business_dependency("success")  
        response = self.client.get("/candidates")
        
        self.assertEqual(200, response.status_code)
        self.assertEqual([{"LastName" : "Cazenave", "FirstName" : "Thomas", "Sexe" : "M"}, {"LastName" : "TRASTOUR-ISNART", "FirstName" : "Laurence", "Sexe" : "F"}], response.json())  
    
      
    def test_get_candidates_status_500_when_errors(self) : 
        self.overriding_business_dependency("error")  
        response = self.client.get("/candidates")
        
        self.assertEqual(500, response.status_code)
        self.assertEqual({'detail': 'Treatment failed'}, response.json())