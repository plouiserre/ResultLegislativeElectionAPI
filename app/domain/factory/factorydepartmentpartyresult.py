from app.domain.DTO.departmentpartyresultDTO import DepartmentPartyResultDTO

class FactoryDeartmentPartyResult: 
    #TODO delete if useless
    def construct_department_party_result(self, id, name, number, rate_voting) : 
        department_party_result = DepartmentPartyResultDTO()
        department_party_result.id = id
        department_party_result.name = name
        department_party_result.number = number
        department_party_result.avg_vote_expressed = rate_voting
        return department_party_result