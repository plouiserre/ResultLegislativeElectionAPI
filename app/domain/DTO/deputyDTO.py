import datetime

class DeputyDTO:
    def __init__(self) -> None:
        self.id = 0
        self.sexe = ''
        self.last_name = ''
        self.first_name = ''
        self.birthdate = datetime.date
        self.candidate_id = 0
        self.is_sorting = False