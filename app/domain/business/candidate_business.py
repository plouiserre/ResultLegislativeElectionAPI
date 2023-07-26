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
           
        candidates = self.candidate_repo.get_candidates() 
            
        for candidate in candidates : 
            if candidate.party_id == party.id :
                candidate.party_name = party.name
                candidates_from_parties.append(candidate)
                
        return candidates_from_parties
    
    
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