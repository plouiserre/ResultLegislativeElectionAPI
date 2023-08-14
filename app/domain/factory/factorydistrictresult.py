from app.domain.DTO.districtresultDTO import DistrictResultDTO

class FactoryDistrictResult : 
    def construct_district_result(self, district, rate_voting, department_name) : 
        result = DistrictResultDTO()
        result.id = district.id
        result.name = district.name
        result.position = district.position
        result.department_id = district.department_id
        result.rate_voting = rate_voting
        result.department_name = department_name        
        return result