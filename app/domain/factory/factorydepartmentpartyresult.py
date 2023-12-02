from app.domain.DTO.departmentpartyresultDTO import DepartmentPartyResultDTO

class FactoryDepartmentPartyResult: 
    #TODO delete if useless
    def construct_department_party_result(self, id, name, number, rate_voting) : 
        department_party_result = DepartmentPartyResultDTO()
        department_party_result.id = id
        department_party_result.name = name
        department_party_result.number = number
        department_party_result.avg_vote_expressed = rate_voting
        return department_party_result
    
    
    def construct_department_party_result_from_list_voting_stats(self, department, all_rates_voting_specific_round) : 
        sum_rate_voting = 0
        for rate_voting in all_rates_voting_specific_round : 
            sum_rate_voting += rate_voting
        avg_rate_voting_specific_round = round(sum_rate_voting / len(all_rates_voting_specific_round),2)
        department_party_result = self.construct_department_party_result(department.id, department.name, department.number, avg_rate_voting_specific_round)
        return department_party_result