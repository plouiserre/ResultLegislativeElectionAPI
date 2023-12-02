from app.utils.helper import getLabelFormatted

from app.domain.business.candidate.sortered_candidate import SorteredCandidate

#TODO reorganise this class
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
        self.parties = []
        self.candidates_result = {}   
        
        
    def get_candidates(self, first_name, last_name) : 
        self.first_name = first_name
        self.last_name = last_name
        self.candidates = self.candidate_repo.get_candidates()
        
        self.parties = self.party_business.get_parties()
        
        for candidate in self.candidates : 
            if first_name == "" and last_name == "" :
                self.__set_party_name_for_candidate(candidate)
            else :
                self.__search_candidates_from_first_name_last_name(candidate)
            
        if first_name == "" and last_name == "":
            return self.candidates
        else :
            return self.candidates_specific
                
                
    def __search_candidates_from_first_name_last_name(self, candidate):
        first_name_lower_no_accent = getLabelFormatted(self.first_name)
        first_name_candidate_lower_no_accent = getLabelFormatted(candidate.first_name)
        last_name_lower_no_accent = getLabelFormatted(self.last_name)
        last_name_candidate_lower_no_accent = getLabelFormatted(candidate.last_name)
        if first_name_lower_no_accent == first_name_candidate_lower_no_accent and last_name_lower_no_accent == last_name_candidate_lower_no_accent : 
                self.__set_party_name_for_candidate(candidate)
                self.candidates_specific.append(candidate)
    
    
    def __set_party_name_for_candidate(self, candidate) : 
        for party in self.parties :
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
            self.parties = self.party_business.get_parties()
            
            for candidate in candidates : 
                for district in districts :
                    if candidate.district_id == district.id :
                        self.__set_party_name_for_candidate(candidate)
                        candidates_result.append(candidate)        
            return candidates_result        
        else :
            return None
        
        
    def get_candidates_by_district(self, district_id) : 
        district_id_needed = int(district_id)
        candidates_result = []
        
        candidates = self.candidate_repo.get_candidates()
        self.parties = self.party_business.get_parties()
        for candidate in candidates : 
            if candidate.district_id == district_id_needed :
                self.__set_party_name_for_candidate(candidate)
                candidates_result.append(candidate)  
        if len(candidates_result) > 0 :
            return candidates_result
        else : 
            return None
                
        
    def get_top_candidates_results(self, limit) : 
        self.candidates_result["first_round"] = []
        self.candidates_result["second_round"] = []
        
        self.candidates = self.candidate_repo.get_candidates()
        
        self.parties = self.party_business.get_parties()
        
        #TODO add in the dependency
        sortered = SorteredCandidate(self.candidates, self.parties, None)
              
        self.candidates_result = sortered.sort_all_candidates(limit)
        
        return self.candidates_result