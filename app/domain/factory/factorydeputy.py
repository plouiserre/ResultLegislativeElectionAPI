from app.domain.DTO.deputyDTO import DeputyDTO

class FactoryDeputy : 
    def construct_deputy(self, id, sexe, last_name, first_name, birthdate, candidate_id, is_sorting) : 
        deputy = DeputyDTO()
        deputy.id = id
        deputy.sexe = sexe
        deputy.last_name = last_name
        deputy.first_name = first_name
        deputy.birthdate = birthdate
        deputy.candidate_id = candidate_id
        deputy.is_sorting = is_sorting
        return deputy
    
    
    def construct_deputy_from_bdd(self, deputy_data_from_bdd) :
        deputy = DeputyDTO()
        deputy.id = deputy_data_from_bdd[0]
        deputy.last_name =  deputy_data_from_bdd[1]
        deputy.first_name = deputy_data_from_bdd[2]
        deputy.sexe = deputy_data_from_bdd[3]
        deputy.birthdate = deputy_data_from_bdd[4]
        if deputy_data_from_bdd[5] == 0 :
            deputy.is_sorting = False 
        else :
            deputy.is_sorting = True
        deputy.candidate_id = deputy_data_from_bdd[6]
        return deputy