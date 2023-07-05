import unittest
from unittest.mock import Mock

from app.main import app
from app.adapters.deputiesAPI import init_deputy_business
from fastapi.testclient import TestClient


def override_deputy_business() :
    json = [{"LastName" : "CARPENTIER", "FirstName" : "Julien", "Sexe" : "M"}, {"LastName" : "DUFREGNE", "FirstName" : "Jean-Paul", "Sexe" : "M"}, {"LastName" : "BENOIT-GOLA", "FirstName" : "Anne-Cécile", "Sexe" : "F"}]
    mock = Mock()
    mock.get_deputies.return_value = json 
    return mock


def override_deputy_business_exception() :
    mock = Mock()
    mock.get_deputies.side_effect = Exception("Boom!")
    mock.get_deputies.return_value = ""
    return mock

    
class DeputiesAPITest(unittest.TestCase) : 
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.app = app
        self.client = TestClient(app)
        
    
    def overriding_business_dependency(self, result_action):
        if result_action == "success" :
            app.dependency_overrides[init_deputy_business] = override_deputy_business
        elif result_action == "error" :
            app.dependency_overrides[init_deputy_business] = override_deputy_business_exception
        
    
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
        