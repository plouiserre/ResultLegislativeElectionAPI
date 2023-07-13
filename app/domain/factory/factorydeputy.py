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