import unittest
from unittest.mock import Mock

from app.main import app
from app.adapters.resultsAPI import init_result_business
from fastapi.testclient import TestClient

def render_result_json_mock() :
    result_first = {"state_compute" : "Completed", "round_number" : 1, "registered" : 8765, "abstaining":65, "rate_abstaining":8.6}
    result_second = {"state_compute" : "Completed", "round_number" : 2, "registered" : 666, "abstaining":25, "rate_abstaining":12.6}
    results = [result_first, result_second]
    return results

def override_result_business():
    results = render_result_json_mock()
    json = results
    mock = Mock()
    mock.get_results.return_value = json
    return mock


def override_result_business_exception() :
    mock = Mock()
    mock.get_results.side_effect = Exception("Boom!")
    mock.get_results.return_value = ""
    return mock


class ResultsAPITest(unittest.TestCase) : 
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.client = TestClient(app)
        
        
    def overriding_business_dependency(self, result_action) :
        if result_action == "success" :
            app.dependency_overrides[init_result_business] = override_result_business
        elif result_action == "error" :
            app.dependency_overrides[init_result_business] = override_result_business_exception
         
        
    def test_get_results_status_OK_when_no_errors(self):
        self.overriding_business_dependency("success")
        response = self.client.get("/results")
        results = render_result_json_mock()
        
        self.assertEqual(200, response.status_code)
        self.assertEqual(results, response.json())
        
        
    def test_get_results_status_500_when_errors(self) : 
        self.overriding_business_dependency("error")
        response = self.client.get("/results")
        
        self.assertEqual(500, response.status_code)
        self.assertEqual({'detail': 'Treatment failed'}, response.json())