import unittest

from fastapi.testclient import TestClient
from app.main import app

class CandidatesAPITest(unittest.TestCase) : 
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.client = TestClient(app)
    
    
    #TODO add mock when services will be created
    def test_get_candidates_status_OK_when_no_errors(self) : 
        response = self.client.get("/candidates")
        
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.json(), [{"LastName" : "Cazenave", "FirstName" : "Thomas", "Sexe" : "M"}, {"LastName" : "TRASTOUR-ISNART", "FirstName" : "Laurence", "Sexe" : "F"}])
        
      
    #TODO à faire quand j'aurai le code du service  
    # def test_get_candidates_status_500_when_errors(self) : 
    #     response = None
    #     with self.assertRaises(Exception) as context :
    #         response = self.client.get("/candidates")
            
    #     self.assertEqual(500, response.status_code)
    #     self.assertEqual(response.json(), "")