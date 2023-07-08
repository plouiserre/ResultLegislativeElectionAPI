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
    