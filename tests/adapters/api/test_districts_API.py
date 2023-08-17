import unittest
from unittest.mock import Mock

from app.main import app
from app.adapters.API.districtsAPI import init_district_business
from fastapi.testclient import TestClient

def override_district_business() :
    mock = Mock()
    mock.get_districts_by_department_name.return_value = [{"Name" : "1 ère circonscription", "Id" : 1}, {"Name" : "2 ème circonscription", "Id" : 2}]
    mock.get_districts_by_voting_rate.return_value = [{"Name" : "2 ème circonscription", "Id" : 2}, {"Name" : "1 ère circonscription", "Id" : 1}]
    return mock


def override_district_business_exception() :
    mock = Mock()    
    mock.get_districts_by_department_name.side_effect = Exception("Boom!")
    mock.get_districts_by_department_name.return_value = ""
    mock.get_districts_by_voting_rate.side_effect = Exception("Boom!")
    mock.get_districts_by_voting_rate.return_value = ""
    return mock


def override_district_no_result() : 
    mock = Mock()
    mock.get_districts_by_department_name.return_value = None
    return mock


class DistrictsTest(unittest.TestCase) :
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.client = TestClient(app)
        
        
    def overriding_business_dependency(self, result_action) : 
        if result_action == "success" :
            app.dependency_overrides[init_district_business] = override_district_business  
        elif result_action == "error" : 
            app.dependency_overrides[init_district_business] = override_district_business_exception 
        elif result_action == "no_result": 
            app.dependency_overrides[init_district_business] = override_district_no_result 
            
        
    def test_get_districts_by_departments_status_OK_when_no_error(self) : 
        self.overriding_business_dependency("success")
        response = self.client.get("districts/?department=toto")
        
        self.assertEqual(200, response.status_code)
        self.assertEqual([{"Name" : "1 ère circonscription", "Id" : 1}, {"Name" : "2 ème circonscription", "Id" : 2}], response.json())
        
        
    def test_get_districts_by_departments_status_500_when_errors(self) : 
        self.overriding_business_dependency("error")
        response = self.client.get("districts/?department=toto")
        
        self.assertEqual(500, response.status_code)
        self.assertEqual({'detail': 'Treatment failed'}, response.json())
        
        
    def test_get_districts_by_departments_status_404_when_no_results(self) : 
        self.overriding_business_dependency("no_result")
        response = self.client.get("districts/?department=toto")

        self.assertEqual(404, response.status_code)
        self.assertEqual({'detail': 'No result'}, response.json())
        
        
    def test_get_districts_by_voting_rate_status_OK_when_no_error(self) : 
        self.overriding_business_dependency("success")
        response = self.client.get("districts/?sort=result")
        
        self.assertEqual(200, response.status_code)
        self.assertEqual([{"Name" : "2 ème circonscription", "Id" : 2}, {"Name" : "1 ère circonscription", "Id" : 1}], response.json())  
        
        
    def test_get_districts_by_voting_status_500_when_errors(self) : 
        self.overriding_business_dependency("error")
        response = self.client.get("districts/?sort=result")
        
        self.assertEqual(500, response.status_code)
        self.assertEqual({'detail': 'Treatment failed'}, response.json())
        