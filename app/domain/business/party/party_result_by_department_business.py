from app.domain.factory.factorydepartmentpartyresult import FactoryDepartmentPartyResult
from app.domain.business.candidate.sortered_candidate import SorteredCandidate
from app.domain.business.department.sortered_department import SorteredDepartment

class PartyResultByDepartmentBusiness : 
    def __init__(self, party_repo, candidate_repo, district_repo, department_repo) -> None:
        self.__all_candidates = []
        self.__all_parties = []
        self.__all_departments = []
        self.__all_districts = []
        self.party_repo = party_repo
        self.candidate_repo = candidate_repo
        self.district_repo = district_repo
        self.department_repo = department_repo
        self.factory_department_party_result = FactoryDepartmentPartyResult()
        
    def get_top_departments_for_each_party_all_rounds(self) :
        self.__get_all_datas_needed()
        all_district_ids_by_departments = self.__get_district_ids_by_departments()
        all_candidates_by_party_and_department = self.__get_candidates_by_party_and_departments(all_district_ids_by_departments)
        all_departments_party_result_created = self.__get_all_departments_party_result(all_candidates_by_party_and_department)
        results = self.__get_party_result_sortered_all_round_sorted(all_departments_party_result_created)
        return results
    
    def __get_all_datas_needed(self) :        
        self.__all_candidates = self.candidate_repo.get_candidates()
        self.__all_parties = self.party_repo.get_parties()         
        self.__all_departments = self.department_repo.get_departments()
        self.__all_districts = self.district_repo.get_districts()
        
    
    def __get_district_ids_by_departments(self) :
        sortered_departements = SorteredDepartment(self.__all_departments, self.__all_districts)
        results = sortered_departements.departments_sortered_by_districts()
        return results
    
    
    def __get_candidates_by_party_and_departments(self, all_district_ids_by_departments) : 
        sortered_candidates = SorteredCandidate(self.__all_candidates, self.__all_parties, self.__all_departments)
        results = sortered_candidates.get_candidates_by_party_and_departments(all_district_ids_by_departments)
        return results     
    
    
    def __get_all_departments_party_result(self, all_candidates_by_party_and_department) :
        all_departments_result_by_party_first_round = {}
        all_departments_result_by_party_second_round = {}
        for party_name in all_candidates_by_party_and_department : 
            candidates_specific_party = all_candidates_by_party_and_department[party_name]
            if (party_name in all_departments_result_by_party_first_round) == False : 
                all_departments_result_by_party_first_round[party_name] = []
            if (party_name in all_departments_result_by_party_second_round) == False : 
                all_departments_result_by_party_second_round[party_name] = []
            for department_name in candidates_specific_party : 
                all_candidates_from_same_party_in_specific_dep = candidates_specific_party[department_name]
                all_voting_expressed_first_round = []
                all_voting_expressed_second_round = []
                for candidate in all_candidates_from_same_party_in_specific_dep : 
                    all_voting_expressed_first_round.append(candidate.rate_vote_expressed_first_round)
                    all_voting_expressed_second_round.append(candidate.rate_vote_expressed_second_round)
                department = self.__get_department_from_department_name(department_name)
                department_result_first_round = self.factory_department_party_result.construct_department_party_result_from_list_voting_stats(department, all_voting_expressed_first_round)
                department_result_second_round = self.factory_department_party_result.construct_department_party_result_from_list_voting_stats(department, all_voting_expressed_second_round)
                all_departments_result_by_party_first_round[party_name].append(department_result_first_round)
                all_departments_result_by_party_second_round[party_name].append(department_result_second_round)
        return [all_departments_result_by_party_first_round, all_departments_result_by_party_second_round]
    
    
    #TODO arrange that later 
    def __get_department_from_department_name(self, department_name) : 
        department_result = None 
        for department in self.__all_departments : 
            if department_name == department.name : 
                department_result = department
                break
        return department_result
    
    
    def __get_party_result_sortered_all_round_sorted(self, all_departments_party_result) :
        all_datas_sorted = {}
        data_first_round = all_departments_party_result[0]
        data_second_round = all_departments_party_result[1]
        data_first_round_sorted = self.__browse_departments_party_result(data_first_round)
        data_second_round_sorted = self.__browse_departments_party_result(data_second_round)
        for party_name in data_first_round_sorted : 
            first_round_department_party_result_sorted = data_first_round_sorted[party_name]
            second_round_department_party_result_sorted = data_second_round_sorted[party_name]
            all_datas_sorted[party_name] =  {}
            all_datas_sorted[party_name]["first_round"] = first_round_department_party_result_sorted
            all_datas_sorted[party_name]["second_round"] =second_round_department_party_result_sorted
        return all_datas_sorted
        
        
    def __browse_departments_party_result(self, department_party_result) : 
        all_departments_result_all_parties = department_party_result.copy()
        departments_party_results_all_parties = {}
        for party_name in all_departments_result_all_parties : 
            all_departments_result_data = all_departments_result_all_parties[party_name]
            data_all_departments_sorted = self.__sort_all_departments_result_party(all_departments_result_data)  
            departments_party_results_all_parties[party_name] = data_all_departments_sorted 
        return departments_party_results_all_parties
             
        
    def __sort_all_departments_result_party(self, data_all_departments): 
        data_all_departments_sorted = []
        data_all_departments_to_sort = data_all_departments.copy()
        while len(data_all_departments) > len(data_all_departments_sorted) : 
            for department_party_result_examined in data_all_departments_to_sort : 
                department_result_sorted = self.__sortered_specific_department_result(data_all_departments_to_sort, department_party_result_examined, data_all_departments_sorted)
                if department_result_sorted != None : 
                    data_all_departments_to_sort.remove(department_result_sorted)
        return data_all_departments_sorted
            
    def __sortered_specific_department_result(self, department_results_to_sort, department_party_result_examined, data_all_departments_sorted) : 
        department_result_sorted = None
        for i in range(len(department_results_to_sort)) :
            is_end_loop = i + 1 == len(department_results_to_sort)
            department_party_result_compared = department_results_to_sort[i] 
            if department_party_result_examined.id == department_party_result_compared.id and is_end_loop == False:
                continue
            elif department_party_result_compared in data_all_departments_sorted : 
                continue
            elif department_party_result_examined.avg_vote_expressed > department_party_result_compared.avg_vote_expressed:
                break
            elif is_end_loop :
                data_all_departments_sorted.append(department_party_result_examined)
                department_result_sorted = department_party_result_examined
                break
            else : 
                continue
        return department_result_sorted        
           