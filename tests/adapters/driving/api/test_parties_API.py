import unittest
from unittest.mock import Mock

from app.main import app
from app.adapters.driving.API.partiesAPI import init_party_business
from fastapi.testclient import TestClient

def override_party_business() : 
    mock = Mock()
    mock.get_top_candidates_for_each_party_all_rounds.return_value = [{"party" : "paradise"}, [{"LastName" : "Cazenave", "FirstName" : "Thomas", "Sexe" : "M"}, {"LastName" : "TRASTOUR-ISNART", "FirstName" : "Laurence", "Sexe" : "F"}]]
    return mock


def override_party_business_exception() : 
    mock = Mock()
    mock.get_top_candidates_for_each_party_all_rounds.side_effect = Exception("Boom!")
    mock.get_top_candidates_for_each_party_all_rounds.return_value = ""
    return mock


class PartiesAPITest(unittest.TestCase) : 
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.client = TestClient(app)
        
        
    def overriding_business_dependency(self, result_action) : 
        if result_action == "success" : 
            app.dependency_overrides[init_party_business] = override_party_business
        elif result_action == "error" :
            app.dependency_overrides[init_party_business] = override_party_business_exception
        
        
    def test_get_top_five_candidates_by_parties_status_OK_when_no_error(self) : 
        self.overriding_business_dependency("success")
        response = self.client.get("/parties/?sort=rate_voting&top=2")
        
        self.assertEqual(200, response.status_code)
        self.assertEqual([{"party" : "paradise"}, [{"LastName" : "Cazenave", "FirstName" : "Thomas", "Sexe" : "M"}, {"LastName" : "TRASTOUR-ISNART", "FirstName" : "Laurence", "Sexe" : "F"}]], response.json())
        
        
    def test_get_top_five_candidates_by_parties_status_500_when_errors(self) : 
        self.overriding_business_dependency("error")
        response = self.client.get("/parties/?sort=rate_voting&top=2")
        
        self.assertEqual(500, response.status_code)
        self.assertEqual({'detail': 'Treatment failed'}, response.json())
        
        
    def test_get_top_five_candidates_by_parties_status_400_when_top_forgotten_uri(self) :
        self.overriding_business_dependency("success")
        response = self.client.get("/parties/?sort=rate_voting")
        
        self.assertEqual(400, response.status_code)
        self.assertEqual({'detail': 'Bad request dumbass'}, response.json())
        
        
    def test_get_top_five_candidates_by_parties_status_400_when_sort_bad_fill(self) :
        self.overriding_business_dependency("success")
        response = self.client.get("/parties/?sort=age&top=2")
        
        self.assertEqual(400, response.status_code)
        self.assertEqual({'detail': 'Bad request dumbass'}, response.json())