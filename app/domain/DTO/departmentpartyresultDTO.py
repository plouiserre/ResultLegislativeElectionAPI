from app.domain.DTO.departmentDTO import DepartmentDTO

class DepartmentPartyResultDTO(DepartmentDTO): 
    def __init__(self) -> None:
        super().__init__()
        self.avg_vote_expressed = 0.0