class ResultDTO:
    def __init__(self) -> None :
        self.id = 0
        self.state_compute = ""
        self.round_number = 0
        self.registered = 0
        self.abstaining = 0
        self.rate_abstaining = 0.0
        self.voting = 0
        self.rate_voting = 0.0
        self.blank_balot = 0
        self.rate_blank_registered = 0.0
        self.rate_blank_voting = 0.0
        self.null_ballot = 0
        self.rate_null_registered = 0.0
        self.rate_null_voting = 0.0
        self.expressed = 0
        self.rate_express_registered = 0.0
        self.rate_express_voting = 0.0