import unittest
from unittest.mock import Mock

from app.main import app
from app.adapters.API.departementsAPI import init_department_business
from fastapi.testclient import TestClient

def override_department_business() :
    mock = Mock()
    mock.get_departments.return_value = [{"Name" : "Ain", "Id" : 1, "Number" : 1}, {"Name" : "Aisne", "Id" : 2, "Number" : 2}]
    mock.get_departments_by_voting_rate.return_value = [{"Name" : "Gironde", "Id" : 33, "Number" : 33, "rate_voting" : 65.56}, {"Name" : "Hauts de Seine", "Id" : 92, "Number" : 92, "rate_voting" : 62.35}]
    return mock


def override_department_business_exception() : 
    mock = Mock()    
    mock.get_departments.side_effect = Exception("Boom!")
    mock.get_departments.return_value = ""
    mock.get_departments_by_voting_rate.side_effect = Exception("Boom!")
    mock.get_departments_by_voting_rate.return_value = ""
    return mock


class DepartmentsAPITest(unittest.TestCase) : 
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)        
        self.client = TestClient(app)
        
        
    def overriding_business_dependency(self, result_action) : 
        if result_action == "success" :
            app.dependency_overrides[init_department_business] = override_department_business  
        elif result_action == "error" : 
            app.dependency_overrides[init_department_business] = override_department_business_exception            
        
    
    def test_get_departments_status_OK_when_no_errors(self) : 
        self.overriding_business_dependency("success")
        response = self.client.get("departments/")
        
        self.assertEqual(200, response.status_code)
        self.assertEqual([{"Name" : "Ain", "Id" : 1, "Number" : 1}, {"Name" : "Aisne", "Id" : 2, "Number" : 2}], response.json())
        
        
    def test_get_departments_status_500_when_errors(self) : 
        self.overriding_business_dependency("error")
        response = self.client.get("departments/")
        
        self.assertEqual(500, response.status_code)
        self.assertEqual({'detail': 'Treatment failed'}, response.json())
        
        
    def test_get_departments_sort_by_rate_voting_status_OK_when_no_errors(self) : 
        self.overriding_business_dependency("success")
        response_first = self.client.get("departments/?sort=result&type=ascending")
        response_second = self.client.get("departments/?sort=result&type=descending")
        self.__assert_response_sorting_request(response_first)
        self.__assert_response_sorting_request(response_second)
        
                
    def __assert_response_sorting_request(self, response) :
        self.assertEqual(200, response.status_code)
        self.assertEqual([{"Name" : "Gironde", "Id" : 33, "Number" : 33, "rate_voting" : 65.56}, {"Name" : "Hauts de Seine", "Id" : 92, "Number" : 92, "rate_voting" : 62.35}], response.json())
     
    
    def test_get_departments_sort_by_rate_voting_status_OK_when_bad_request(self) : 
        response_first = self.client.get("departments/?sort=result")
        response_second = self.client.get("departments/?sort=result&type=deescending")
        self.__assert_response_sorting_request_bad_request(response_first)
        self.__assert_response_sorting_request_bad_request(response_second)
        
                
    def __assert_response_sorting_request_bad_request(self, response) :
        self.assertEqual(400, response.status_code)
        self.assertEqual({'detail': 'Bad Request'}, response.json())
        
        
    def test_get_departments_sort_by_rate_voting_status_500_when_errors(self) : 
        self.overriding_business_dependency("error")
        response = self.client.get("departments/?sort=result&type=ascending")
        
        self.assertEqual(500, response.status_code)
        self.assertEqual({'detail': 'Treatment failed'}, response.json())