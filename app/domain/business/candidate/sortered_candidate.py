from app.domain.business.department.sortered_department import SorteredDepartment

class SorteredCandidate() : 
    def __init__(self, candidates, parties, departments) -> None:
        self.candidates = candidates
        self.parties = parties
        self.departments = departments
        self.candidates_result = {}        
        self.candidates_result["first_round"] = []
        self.candidates_result["second_round"] = []
    
    def sort_all_candidates(self, limit) :
        top_first_round_candidates_result = []
        top_second_round_candidates_result = []
        for candidate in self.candidates : 
            self.__set_party_name_for_candidate(candidate)
            if len(top_first_round_candidates_result) < limit and  len(top_second_round_candidates_result) < limit : 
                top_first_round_candidates_result.append(candidate)             
                top_second_round_candidates_result.append(candidate)
                continue 
            
            top_first_round_candidates_result = self.__remove_candidate_lowest_vote(top_first_round_candidates_result, candidate, 1)
            top_second_round_candidates_result = self.__remove_candidate_lowest_vote(top_second_round_candidates_result, candidate, 2)       
            
        
        self.__sort_candidates_specific_round(top_first_round_candidates_result, self.candidates_result["first_round"], 1)
        self.__sort_candidates_specific_round(top_second_round_candidates_result, self.candidates_result["second_round"], 2)   
        
        return self.candidates_result 
    
    
    def __remove_candidate_lowest_vote(self, top_candidate_specific_round, candidate, round_number) : 
        candidates_observing = top_candidate_specific_round.copy()
        candidates_observing.append(candidate)
        minimal_candidate = None
        for candidate_observing in candidates_observing : 
            if minimal_candidate == None : 
                minimal_candidate = candidate_observing
                continue
            if candidate_observing.rate_vote_expressed_first_round < minimal_candidate.rate_vote_expressed_first_round and round_number == 1 : 
                minimal_candidate = candidate_observing
            elif candidate_observing.rate_vote_expressed_second_round < minimal_candidate.rate_vote_expressed_second_round and round_number == 2 : 
                minimal_candidate = candidate_observing
                
        candidates_observing.remove(minimal_candidate)
        top_candidate_specific_round = candidates_observing  
        return top_candidate_specific_round
            
       
    def __sort_candidates_specific_round(self, top_candidates_specific_round, candidates_results_specific_round, round) : 
        candidates_to_sort = top_candidates_specific_round.copy()
        while len(top_candidates_specific_round) > len(candidates_results_specific_round):
            for candidate_examined in candidates_to_sort :
                candidate_sorted = self.__sortered_specific_candidate(candidates_to_sort, candidate_examined, candidates_results_specific_round, round)
                if candidate_sorted != None : 
                    candidates_to_sort.remove(candidate_sorted)
                    
    
    def __sortered_specific_candidate(self, candidates_to_sort, candidate_examined, candidates_sorted, round_number) :
        candidate_sorted = None
        for i in range(len(candidates_to_sort)) :
            is_end_loop = i + 1 == len(candidates_to_sort)
            candidate_compared = candidates_to_sort[i] 
            if candidate_examined.id == candidate_compared.id and is_end_loop == False:
                continue
            elif candidate_compared in candidates_sorted : 
                continue
            elif candidate_examined.rate_vote_expressed_first_round < candidate_compared.rate_vote_expressed_first_round  and round_number == 1:
                break
            elif candidate_examined.rate_vote_expressed_second_round < candidate_compared.rate_vote_expressed_second_round  and round_number == 2:
                break
            elif is_end_loop :
                candidates_sorted.append(candidate_examined)
                candidate_sorted = candidate_examined
                break
            else : 
                continue
        return candidate_sorted
    
    #TODO erase duplication with candidate_business
    def __set_party_name_for_candidate(self, candidate) : 
        for party in self.parties :
                if candidate.party_id == party.id :
                    candidate.party_name = party.name
                    break
                else : 
                    continue
                
                
    def get_candidates_by_party_and_departments(self, all_district_ids_by_departments) : 
        results = {}       
        for candidate in self.candidates :
                for party in self.parties : 
                    if party.id == candidate.party_id :
                        for department in self.departments :                        
                            department_candidate = all_district_ids_by_departments[candidate.district_id]
                            if department_candidate.id == department.id : 
                                if (party.short_name in results) == False  : 
                                    results[party.short_name] = {}
                                if (department.name in results[party.short_name]) == False : 
                                    results[party.short_name][department.name] = []
                                results[party.short_name][department.name].append(candidate)
                                break
        return results   
        