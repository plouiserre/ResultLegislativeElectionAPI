from app.utils.helper import getLabelFormatted

class DeputyBusiness : 
    def __init__(self, DeputyRepository) -> None:
        self.deputy_repo = DeputyRepository
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