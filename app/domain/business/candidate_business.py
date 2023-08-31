from app.utils.helper import getLabelFormatted

class CandidateBusiness() : 
    def __init__(self, CandidateRepository, PartyBusiness, DepartmentBusiness, DistrictBusiness) -> None:
        self.candidate_repo = CandidateRepository
        self.party_business = PartyBusiness
        self.department_business = DepartmentBusiness
        self.district_business = DistrictBusiness
        self.first_name = ""
        self.last_name = ""
        self.candidates = []
        self.candidates_specific = []
        
        
    def get_candidates(self, first_name, last_name) : 
        self.first_name = first_name
        self.last_name = last_name
        self.candidates = self.candidate_repo.get_candidates()
        
        parties = self.party_business.get_parties()
        
        for candidate in self.candidates : 
            if first_name == "" and last_name == "" :
                self.__set_party_name_for_candidate(candidate, parties)
            else :
                self.__search_candidates_from_first_name_last_name(candidate, parties)
            
        if first_name == "" and last_name == "":
            return self.candidates
        else :
            return self.candidates_specific
                
                
    def __search_candidates_from_first_name_last_name(self, candidate, parties):
        first_name_lower_no_accent = getLabelFormatted(self.first_name)
        first_name_candidate_lower_no_accent = getLabelFormatted(candidate.first_name)
        last_name_lower_no_accent = getLabelFormatted(self.last_name)
        last_name_candidate_lower_no_accent = getLabelFormatted(candidate.last_name)
        if first_name_lower_no_accent == first_name_candidate_lower_no_accent and last_name_lower_no_accent == last_name_candidate_lower_no_accent : 
                self.__set_party_name_for_candidate(candidate, parties)
                self.candidates_specific.append(candidate)
    
    
    def __set_party_name_for_candidate(self, candidate, parties) : 
        for party in parties :
                if candidate.party_id == party.id :
                    candidate.party_name = party.name
                    break
                else : 
                    continue
                        
    
    def get_candidates_by_party(self, party_short_name) :
        candidates_from_parties = []
        
        party = self.party_business.get_party_by_short_name(party_short_name)
        
        if party != None :    
            candidates = self.candidate_repo.get_candidates() 
                
            for candidate in candidates : 
                if candidate.party_id == party.id :
                    candidate.party_name = party.name
                    candidates_from_parties.append(candidate)               
                    
            return candidates_from_parties
        else :
            return None
    
    
    def get_candidates_by_district(self, district_id) : 
        candidates_result = []
        
        candidates = self.get_candidates("", "")
        for candidate in candidates : 
            if candidate.district_id == district_id : 
                candidates_result.append(candidate)
                
        return candidates_result
    
    
    def get_candidates_by_departement(self, department_name) : 
        candidates_result = []
        
        department = self.department_business.get_department_by_name(department_name)
        
        if department != None : 
            districts = self.district_business.get_districts_by_department_id(department.id)
            candidates = self.candidate_repo.get_candidates()
            parties = self.party_business.get_parties()
            
            for candidate in candidates : 
                for district in districts :
                    if candidate.district_id == district.id :
                        self.__set_party_name_for_candidate(candidate, parties)
                        candidates_result.append(candidate)        
            return candidates_result        
        else :
            return None
        
        
    def get_candidates_by_district(self, district_id) : 
        district_id_needed = int(district_id)
        candidates_result = []
        
        candidates = self.candidate_repo.get_candidates()
        parties = self.party_business.get_parties()
        for candidate in candidates : 
            if candidate.district_id == district_id_needed :
                self.__set_party_name_for_candidate(candidate, parties)
                candidates_result.append(candidate)  
        if len(candidates_result) > 0 :
            return candidates_result
        else : 
            return None
                
        
    def get_top_candidates_results(self, limit) : 
        candidates_result = {}
        candidates_result["first_round"] = []
        candidates_result["second_round"] = []
        top_first_round_candidates_result = []
        top_second_round_candidates_result = []
        
        all_candidates = self.candidate_repo.get_candidates()
        
        parties = self.party_business.get_parties()
        
        for candidate in all_candidates : 
            self.__set_party_name_for_candidate(candidate, parties)
            if len(top_first_round_candidates_result) < limit and  len(top_second_round_candidates_result) < limit : 
                top_first_round_candidates_result.append(candidate)             
                top_second_round_candidates_result.append(candidate)
                continue 
            
            top_first_round_candidates_result = self.__remove_candidate_lowest_vote(top_first_round_candidates_result, candidate, 1)
            top_second_round_candidates_result = self.__remove_candidate_lowest_vote(top_second_round_candidates_result, candidate, 2)       
            
        
        self.__sort_candidates_specific_round(top_first_round_candidates_result, candidates_result["first_round"], 1)
        self.__sort_candidates_specific_round(top_second_round_candidates_result, candidates_result["second_round"], 2)        
        
        return candidates_result
    
    
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