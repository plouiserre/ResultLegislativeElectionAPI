from app.domain.factory.factorydepartmentresult import FactoryDepartmentResult

class DepartmentBusiness : 
    
    def __init__(self, department_repo, district_repo, result_repo) -> None:
        self.department_repo = department_repo
        self.district_repo = district_repo
        self.result_repo = result_repo
        self.sorting_type = ""
        
    
    def get_departments(self) : 
        departments = self.department_repo.get_departments()
        return departments
    
    
    def get_department_by_name(self, department_name):
        department_result = None
        departments = self.get_departments()
        
        for department in departments:
            if department.name == department_name : 
                department_result = department
                break
        return department_result
    
    
    def get_department_name_from_department_id(self, department_id) : 
        department_name = ""
        departments = self.department_repo.get_departments()
       
        for department in departments : 
           if department.id == department_id : 
               department_name = department.name
               break
        
        return department_name
    
    
    def get_departments_by_voting_rate(self, sorting_type) :
        self.sorting_type = sorting_type
        departments_results = {}
        departments_results["first_round"] = []
        departments_results["second_round"] = []
        departments_results_sorted = {}
        departments = self.department_repo.get_departments()
        factory = FactoryDepartmentResult()
                
        for department in departments : 
            avg_rate_voting = self.__get_avg_rate_voting_from_districts_in_specific_department(department.id)
            
            if "first_round" in avg_rate_voting :
                department_result_first_round = factory.construct_department_result_from_department(department, avg_rate_voting["first_round"])
                departments_results["first_round"].append(department_result_first_round)
            
            if "second_round" in avg_rate_voting : 
                department_result_second_round = factory.construct_department_result_from_department(department, avg_rate_voting["second_round"])
                departments_results["second_round"].append(department_result_second_round)
            
        departments_results_sorted["first_round"] = self.__get_departments_results_sorted(departments_results["first_round"])
        departments_results_sorted["second_round"] = self.__get_departments_results_sorted(departments_results["second_round"])
        
        return departments_results_sorted 
    
    
    def __get_avg_rate_voting_from_districts_in_specific_department(self, deparment_id) : 
        avg_rate_voting = {}
        districts = self.district_repo.get_districts()
        results = self.result_repo.get_results()
        
        first_round_results_belongs_dept = []
        second_round_results_belongs_dept = []
        for district in districts : 
            if district.department_id == deparment_id : 
                for result in results : 
                    if result.district_id == district.id : 
                        if result.round_number == 1 :
                            first_round_results_belongs_dept.append(result)
                        else : 
                            second_round_results_belongs_dept.append(result)        
            
        if len(first_round_results_belongs_dept) > 0 : 
            avg_rate_voting["first_round"] = self.__calculate_avg_rate_voting_specific_round(first_round_results_belongs_dept)
            
        if len(second_round_results_belongs_dept) > 0 : 
            avg_rate_voting["second_round"] = self.__calculate_avg_rate_voting_specific_round(second_round_results_belongs_dept)
        
        return avg_rate_voting
    
    
    def __calculate_avg_rate_voting_specific_round(self, results):
        avg_rate_voting = 0.0
        sum_rate_voting = 0
        for result in results : 
            sum_rate_voting += result.rate_voting
        avg_rate_voting = round(sum_rate_voting / len(results), 2)
        return avg_rate_voting
            
    
    def __get_departments_results_sorted(self, departments_result) : 
        results_sorted = []
        results_to_sort = departments_result.copy()
        while len(departments_result) > len(results_sorted):
            for result_examined in results_to_sort :
                result_sorted = self.__sortered_specific_department_result(results_to_sort, result_examined, results_sorted)
                if result_sorted != None : 
                    results_to_sort.remove(result_sorted)
        return results_sorted
    
    
    def __sortered_specific_department_result(self, department_results_to_sort, department_result_examined, department_results_sorted) :
        department_result_sorted = None
        for i in range(len(department_results_to_sort)) :
            is_end_loop = i + 1 == len(department_results_to_sort)
            department_result_compared = department_results_to_sort[i] 
            if department_result_examined.id == department_result_compared.id and is_end_loop == False:
                continue
            elif department_result_compared in department_results_sorted : 
                continue
            elif department_result_examined.rate_voting > department_result_compared.rate_voting and self.sorting_type == "ascending" :
                break
            elif department_result_examined.rate_voting < department_result_compared.rate_voting and self.sorting_type == "descending" :
                break
            elif is_end_loop :
                department_results_sorted.append(department_result_examined)
                department_result_sorted = department_result_examined
                break
            else : 
                continue
        return department_result_sorted