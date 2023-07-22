from app.domain.DTO.candidateDTO import CandidateDTO

class FactoryCandidate : 
        
    #TODO after put district name and department name
    def construct_candidate(self, id, last_name, first_name, sexe, birthdate, party_id, job, is_sorting, district_id,
                        vote_first_round, rate_vote_registered_first_round, rate_vote_expressed_first_round, 
                        vote_second_round, rate_vote_registered_second_round, rate_vote_expressed_second_round) : 
        candidate = CandidateDTO()
        candidate.id = id
        candidate.last_name = last_name
        candidate.first_name = first_name
        candidate.sexe = sexe
        candidate.birthdate = birthdate
        candidate.party_id = party_id
        candidate.job = job
        candidate.is_sorting = is_sorting
        candidate.district_id = district_id
        candidate.vote_first_round = vote_first_round
        candidate.rate_vote_registered_first_round = rate_vote_registered_first_round
        candidate.rate_vote_expressed_first_round = rate_vote_expressed_first_round
        candidate.vote_second_round = vote_second_round
        candidate.rate_vote_registered_second_round = rate_vote_registered_second_round
        candidate.rate_vote_expressed_second_round = rate_vote_expressed_second_round
        return candidate
    
    
    def construct_candidate_from_bdd(self, candidate_data_from_bdd) : 
        candidate = CandidateDTO()
        candidate.id = candidate_data_from_bdd[0]
        candidate.last_name = candidate_data_from_bdd[1]
        candidate.first_name = candidate_data_from_bdd[2]
        candidate.sexe = candidate_data_from_bdd[3]
        candidate.birthdate = candidate_data_from_bdd[4]
        candidate.party_id = candidate_data_from_bdd[5]
        candidate.job = candidate_data_from_bdd[6]
        if candidate_data_from_bdd[7] == 0 : 
            candidate.is_sorting = False
        else : 
            candidate.is_sorting = True
        candidate.district_id = candidate_data_from_bdd[8]
        candidate.vote_first_round = candidate_data_from_bdd[9]
        candidate.rate_vote_registered_first_round = candidate_data_from_bdd[10]
        candidate.rate_vote_expressed_first_round = candidate_data_from_bdd[11]
        candidate.vote_second_round = candidate_data_from_bdd[12]
        candidate.rate_vote_registered_second_round = candidate_data_from_bdd[13]
        candidate.rate_vote_expressed_second_round = candidate_data_from_bdd[14]
        return candidate