import unittest

from app.main import app
from fastapi.testclient import TestClient

class ResultsAPITest(unittest.TestCase) : 
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.client = TestClient(app)
        
        
    def test_get_results_status_OK_when_no_errors(self):
        response = self.client.get("/results")
        
        result_first = {"state_compute" : "Completed", "round_number" : 1, "registered" : 8765, "abstaining":65, "rate_abstaining":8.6}
        result_second = {"state_compute" : "Completed", "round_number" : 2, "registered" : 666, "abstaining":25, "rate_abstaining":12.6}
        results = [result_first, result_second]
        
        self.assertEqual(200, response.status_code)
        self.assertEqual(results, response.json())