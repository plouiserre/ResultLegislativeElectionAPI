from app.domain.factory.factorydistrict import FactoryDistrict

def getDistricts_by_id(ids_list) : 
    districts_needed = []
    
    districts = __create_districts()
    
    for district in districts : 
        for id in ids_list :
            if district.id == id :
                districts_needed.append(district)
                break
            
    return districts_needed


def getDistricts_by_department_id(departments_id) : 
    districts_needed = []
    
    districts = __create_districts()
    
    for district in districts : 
        for department_id in departments_id :
            if district.department_id == department_id :
                districts_needed.append(district)
                break
            
    return districts_needed



def __create_districts() : 
    factory = FactoryDistrict()
    first_district = factory.construct_district(10, 1, "1ère circo", 1)
    second_district = factory.construct_district(11, 2, "2ème circo", 1)
    third_district = factory.construct_district(12, 3, "3ème circo", 1)
    fourth_district = factory.construct_district(20, 1, "1ère circo", 2)
    fifth_district = factory.construct_district(21, 2, "2ème circo", 2)
    sixth_district = factory.construct_district(22, 3, "3ème circo", 2)
    seventh_district = factory.construct_district(23, 4, "4ème circo", 2)
    eighth_district = factory.construct_district(24, 5, "5ème circo", 2)
    nineth_district = factory.construct_district(25, 6, "6ème circo", 2)
    tenth_district = factory.construct_district(26, 7, "7ème circo", 2)
    eleventh_district = factory.construct_district(27, 8, "8ème circo", 2) 
    twelfth_district = factory.construct_district(110, 1, "1ère circo", 11)
    thirteenth_district = factory.construct_district(111, 2, "2ème circo", 11)
    fourteenth_district = factory.construct_district(330, 1, "1ère circo", 33)
    fifteenth_district = factory.construct_district(331, 2, "2ème circo", 33)
    sixteenth_district = factory.construct_district(340, 1, "1ère circo", 34)
    seventeenth_district = factory.construct_district(341, 2, "2ème circo", 34)
    eighteenth_district = factory.construct_district(342, 3, "3ème circo", 34)
    nineteenth_district = factory.construct_district(343, 4, "4ème circo", 34)
    twentieth_district = factory.construct_district(690, 1, "1ère circo", 69)
    twenty_first_district = factory.construct_district(691, 2, "2ème circo", 69)
    twenty_second_district = factory.construct_district(692, 3, "3ème circo", 69)
    twenty_third_district = factory.construct_district(693, 4, "4ème circo", 69)
    districts = [first_district, second_district, third_district, fourth_district, fifth_district, sixth_district, 
                    seventh_district, eighth_district, nineth_district, tenth_district, eleventh_district, 
                    twelfth_district, thirteenth_district, fourteenth_district, fifteenth_district, 
                    sixteenth_district, seventeenth_district, eighteenth_district, nineteenth_district, 
                    twentieth_district, twenty_first_district, twenty_second_district, twenty_third_district]
    return districts