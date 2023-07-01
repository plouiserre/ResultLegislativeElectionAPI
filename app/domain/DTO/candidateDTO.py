import datetime

class CandidateDTO : 
    def __init__(self) -> None:
        self.id = 0
        self.last_name = ''
        self.first_name = ''
        self.sexe = ''
        self.birthdate = datetime.date
        self.party_id = 0
        self.party_name = ''
        self.district_id = 0
        self.job = ''
        self.is_sorting = False
        self.vote_first_round = 0
        self.rate_vote_registered_first_round = 0.0
        self.rate_vote_expressed_first_round = 0.0
        self.vote_second_round = 0
        self.rate_vote_registered_second_round = 0.0
        self.rate_vote_expressed_second_round = 0.0