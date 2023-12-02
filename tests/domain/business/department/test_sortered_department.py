import unittest

from app.domain.business.department.sortered_department import SorteredDepartment
from faker.faker_department import getDepartments_by_ids
from faker.faker_district import getDistricts_by_id

from tests.assert_test import AssertTest

class SorteredDepartmentTest(unittest.TestCase) : 
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.assert_test = AssertTest(self)
        
        
    def test_get_departments_sortered_by_districts(self) : 
        departments = getDepartments_by_ids([11, 33])
        districts = getDistricts_by_id([110, 111, 330, 331])
        
        business = SorteredDepartment(departments,districts)
        
        departments_sortered = business.departments_sortered_by_districts()
        
        self.assertEqual(4, len(departments_sortered))
        
        first_department  = departments_sortered[110]
        first_department_check = [11, "Aude", 11]
        self.assert_test.assert_department_dto(first_department_check, first_department)
        
        second_department = departments_sortered[111]
        second_department_check = [11, "Aude", 11]
        self.assert_test.assert_department_dto(second_department_check, second_department)
        
        third_department = departments_sortered[330]
        third_department_check = [33, "Gironde", 33]
        self.assert_test.assert_department_dto(third_department_check, third_department)
    
        fourth_department = departments_sortered[331]
        fourth_department_check = [33, "Gironde", 33]
        self.assert_test.assert_department_dto(fourth_department_check, fourth_department)
         