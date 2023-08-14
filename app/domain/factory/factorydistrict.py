from app.domain.DTO.districtDTO import DistrictDTO

class FactoryDistrict :
    def construct_district(self, id, position, name, department_id) : 
        district = DistrictDTO()
        district.id = id
        district.position = position
        district.name = name
        district.department_id = department_id
        return district
      
    
    def construct_district_from_bdd(self, district_data) : 
        district = DistrictDTO()
        district.id = district_data[0]
        district.position = district_data[1]
        district.name = district_data[2]
        district.department_id = district_data[3]
        return district