from app.domain.DTO.candidateDTO import CandidateDTO

class FactoryCandidate : 
        
    #TODO after put district name and department name
    def construct_candidate(self, id, last_name, first_name, sexe, birthdate, party_id, job, is_sorting, vote_first_round,
                        rate_vote_registered_first_round, rate_vote_expressed_first_round, vote_second_round, 
                        rate_vote_registered_second_round, rate_vote_expressed_second_round) : 
        candidate = CandidateDTO()
        candidate.id = id
        candidate.last_name = last_name
        candidate.first_name = first_name
        candidate.sexe = sexe
        candidate.birthdate = birthdate
        candidate.party_id = party_id
        candidate.job = job
        candidate.is_sorting = is_sorting
        candidate.vote_first_round = vote_first_round
        candidate.rate_vote_registered_first_round = rate_vote_registered_first_round
        candidate.rate_vote_expressed_first_round = rate_vote_expressed_first_round
        candidate.vote_second_round = vote_second_round
        candidate.rate_vote_registered_second_round = rate_vote_registered_second_round
        candidate.rate_vote_expressed_second_round = rate_vote_expressed_second_round
        return candidate