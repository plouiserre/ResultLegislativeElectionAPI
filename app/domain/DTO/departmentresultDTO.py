from app.domain.DTO.departmentDTO import DepartmentDTO

class DepartmentResultDTO(DepartmentDTO):
    def __init__(self) -> None:
        super().__init__()
        self.rate_voting = 0.0