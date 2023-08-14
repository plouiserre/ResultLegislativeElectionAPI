from app.domain.DTO.districtDTO import DistrictDTO

class DistrictResultDTO(DistrictDTO):
    def __init__(self) -> None:
        super().__init__()
        self.rate_voting = 0.0
        self.department_name = ""