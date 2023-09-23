from app.domain.factory.factorydepartment import FactoryDepartment

def getDepartments_by_ids(numbers_list):
    departments_needed = []    
    
    departments = __create_departments()
    
    for department in departments : 
        for number in numbers_list :
            if department.number == number :
                departments_needed.append(department)
                break
            
    return departments_needed


def getDepartments_by_names(departments_name) : 
    departments_needed = []    
    
    departments = __create_departments()
    
    for department in departments : 
        for name in departments_name :
            if department.name == name :
                departments_needed.append(department)
                break
            
    return departments_needed


def __create_departments() : 
    factory = FactoryDepartment() 
    first_department = factory.construct_department_from_bdd([1, "Ain", 1])
    second_department = factory.construct_department_from_bdd([2, "Aisne", 2])
    third_department = factory.construct_department_from_bdd([3, "Allier", 3])
    eleven_department = factory.construct_department_from_bdd([11, "Aude", 11])
    thirty_third_department = factory.construct_department_from_bdd([33, "Gironde", 33])
    thirty_fourth_department = factory.construct_department_from_bdd([34, "Herault", 34])
    sixty_nineth_department = factory.construct_department_from_bdd([69, "Nord", 69])
    departments = [first_department, second_department, third_department, eleven_department, thirty_third_department, 
                   thirty_fourth_department, sixty_nineth_department]
    return departments