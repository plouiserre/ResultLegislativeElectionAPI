import unittest
from unittest.mock import Mock

from app.main import app
from app.adapters.API.deputiesAPI import init_deputy_business
from fastapi.testclient import TestClient

def override_deputies_business() :
    json = [{"LastName" : "CARPENTIER", "FirstName" : "Julien", "Sexe" : "M"}, {"LastName" : "DUFREGNE", "FirstName" : "Jean-Paul", "Sexe" : "M"}, {"LastName" : "BENOIT-GOLA", "FirstName" : "Anne-Cécile", "Sexe" : "F"}]
    mock = Mock()
    mock.get_deputies.return_value = json 
    mock.get_deputy_from_candidate_identity.return_value = json 
    return mock


def override_deputies_business_exception() :
    mock = Mock()
    mock.get_deputies.side_effect = Exception("Boom!")
    mock.get_deputy_from_candidate_identity.side_effect = Exception("Boom!")
    mock.get_deputy_from_candidate_identity.return_value = ""
    mock.get_deputies.return_value = ""
    return mock
    
    
def override_deputies_business_not_found():
    mock = Mock()
    mock.get_deputy_from_candidate_identity.return_value = None 
    return mock

    
class DeputiesAPITest(unittest.TestCase) : 
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.client = TestClient(app)
        
    
    def overriding_business_dependency(self, result_action):
        if result_action == "success" :
            app.dependency_overrides[init_deputy_business] = override_deputies_business
        elif result_action == "error" :
            app.dependency_overrides[init_deputy_business] = override_deputies_business_exception
        elif result_action == "no_result":
            app.dependency_overrides[init_deputy_business] = override_deputies_business_not_found
        
    
    def test_get_deputies_status_OK_when_no_errors(self) : 
        self.overriding_business_dependency("success")
        response = self.client.get("/deputies")
        
        self.assertEqual(200, response.status_code)
        self.assertEqual([{"LastName":"CARPENTIER", "FirstName":"Julien", "Sexe":"M"},{"LastName":"DUFREGNE", "FirstName":"Jean-Paul", "Sexe":"M"},{"LastName":"BENOIT-GOLA", "FirstName":"Anne-Cécile", "Sexe":"F"}], response.json())
        
        
    def test_get_deputies_status_500_when_errors(self) : 
        self.overriding_business_dependency("error")
        response = self.client.get("/deputies")
        
        self.assertEqual(500, response.status_code)
        self.assertEqual({'detail': 'Treatment failed'}, response.json())
        
        
    def test_get_deputies_from_candidates_status_OK_when_no_errors(self) : 
        self.overriding_business_dependency("success")
        response = self.client.get("/deputies/candidates/?first_name=john&last_name=doe")
        
        self.assertEqual(200, response.status_code)
        self.assertEqual([{"LastName" : "CARPENTIER", "FirstName" : "Julien", "Sexe" : "M"}, {"LastName" : "DUFREGNE", "FirstName" : "Jean-Paul", "Sexe" : "M"}, {"LastName" : "BENOIT-GOLA", "FirstName" : "Anne-Cécile", "Sexe" : "F"}], response.json())
        
        
    def test_get_deputies_from_candidates_status_500_when_errors(self) : 
        self.overriding_business_dependency("error")
        response = self.client.get("/deputies/candidates/?first_name=john&last_name=doe")
        
        self.assertEqual(500, response.status_code)
        self.assertEqual({'detail': 'Treatment failed'}, response.json())
        
        
    def test_get_deputies_from_candidates_status_404_no_result(self) : 
        self.overriding_business_dependency("no_result")
        response = self.client.get("/deputies/candidates/?first_name=john&last_name=doe")
        
        self.assertEqual(404, response.status_code)
        self.assertEqual({'detail': 'No result'}, response.json())