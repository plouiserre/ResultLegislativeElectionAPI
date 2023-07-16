from app.domain.DTO.resultDTO import ResultDTO

class FactoryResult : 
    
    def construct_result(self, id, state_compute, round_number, registered, abstaining, rate_abstaining, voting,
                      rate_voting, blank_balot, rate_blank_registered, rate_blank_voting, null_ballot,
                      rate_null_registered, rate_null_voting, expressed, rate_express_registered, rate_express_voting) : 
        result = ResultDTO()
        result.id = id
        result.state_compute = state_compute
        result.round_number = round_number
        result.registered = registered
        result.abstaining = abstaining
        result.rate_abstaining = rate_abstaining
        result.voting = voting
        result.rate_voting = rate_voting
        result.blank_balot = blank_balot
        result.rate_blank_registered = rate_blank_registered
        result.rate_blank_voting = rate_blank_voting
        result.null_ballot = null_ballot
        result.rate_null_registered = rate_null_registered
        result.rate_null_voting = rate_null_voting
        result.expressed = expressed
        result.rate_express_registered = rate_express_registered
        result.rate_express_voting = rate_express_voting
        return result
    
    
    def construct_result_from_bdd(self, result_data) :
        result = ResultDTO()
        result.id = result_data[0]
        result.round_number = result_data[1]
        result.state_compute = result_data[2]
        result.registered = result_data[3]
        result.abstaining = result_data[4]
        result.rate_abstaining = result_data[5]
        result.voting = result_data[6]
        result.rate_voting = result_data[7]
        result.blank_balot = result_data[8]
        result.rate_blank_registered = result_data[9]
        result.rate_blank_voting = result_data[10]
        result.null_ballot = result_data[11]
        result.rate_null_registered = result_data[12]
        result.rate_null_voting = result_data[13]
        result.expressed = result_data[14]
        result.rate_express_registered = result_data[15]
        result.rate_express_voting = result_data[16]
        return result