from app.domain.business.candidate_business import CandidateBusiness
from app.domain.DTO.deputyDTO import DeputyDTO
from app.utils.helper import getLabelFormatted

class DeputyBusiness : 
    def __init__(self, DeputyRepository, CandidateRepository) -> None:
        self.deputy_repo = DeputyRepository
        self.candidate_repo = CandidateRepository
        self.deputies = []
        self.first_name = ""
        self.last_name = ""
        
    
    def get_deputies(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
        if first_name == "" and last_name == "":
            self.deputies = self.deputy_repo.get_deputies()
        else :
            deputies_from_bdd = self.deputy_repo.get_deputies()
            for deputy in deputies_from_bdd :
                self.__search_deputies_from_first_name_last_name(deputy)
        return self.deputies
    
    
    def __search_deputies_from_first_name_last_name(self, deputy) :
        first_name_lower = getLabelFormatted(self.first_name.lower())
        first_name_deputy_lower = getLabelFormatted(deputy.first_name.lower())
        last_name_lower = getLabelFormatted(self.last_name.lower())
        last_name_deputy_lower = getLabelFormatted(deputy.last_name.lower())
        if first_name_deputy_lower == first_name_lower and last_name_deputy_lower == last_name_lower :
                    self.deputies.append(deputy)
                    
              
    def get_deputy_from_candidate_identity(self, candidate_first_name, candidate_last_name):
        deputy_result = DeputyDTO()
        candidate_business = CandidateBusiness(None, None)
        candidates = self.candidate_repo.get_candidates()
        candidate_id = candidate_business.get_candidate_id(candidates, candidate_first_name, candidate_last_name)  
        deputies = self.deputy_repo.get_deputies()
        for deputy in deputies:
            if deputy.candidate_id == candidate_id :
                deputy_result = deputy
                break
        if deputy_result.last_name == '' and deputy_result.first_name == '' and deputy_result.sexe == '' :
            return None
        else :
            return deputy_result

        