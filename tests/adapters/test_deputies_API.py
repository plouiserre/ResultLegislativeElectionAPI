import unittest

from app.main import app
from fastapi.testclient import TestClient

class DeputiesAPITest(unittest.TestCase) : 
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.app = app
        self.client = TestClient(app)
        
    
    def test_get_deputies_status_OK_when_no_errors(self) : 
        response = self.client.get("/deputies")
        
        self.assertEqual(200, response.status_code)
        self.assertEqual([{"LastName":"CARPENTIER", "FirstName":"Julien", "Sexe":"M"},{"LastName":"DUFREGNE", "FirstName":"Jean-Paul", "Sexe":"M"},{"LastName":"BENOIT-GOLA", "FirstName":"Anne-Cécile", "Sexe":"F"}], response.json())
        
        
# M	CARPENTIER	Julien	17/02/1979	Non
# M	DUFREGNE	Jean-Paul	28/03/1958	Oui
# M	PERCHE	Philippe	19/11/1987	Non
# F	BENOIT-GOLA	Anne-Cécile	24/07/1973	Non