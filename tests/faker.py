from app.domain.factory.factorycandidate import FactoryCandidate
from app.domain.factory.factorydepartment import FactoryDepartment
from app.domain.factory.factorydeputy import FactoryDeputy
from app.domain.factory.factorydistrict import FactoryDistrict
from app.domain.factory.factoryparty import FactoryParty
from app.domain.factory.factoryresult import FactoryResult

import datetime

def getCandidates(ids_list) : 
    candidates_needed = []
    
    factory = FactoryCandidate()
    first_candidate = factory.construct_candidate(1, "VUITTON", "Brigitte", "F", datetime.datetime(1957,11,29), 1, "Professeur, profession scientifique", False, 10, 779, 0.98, 1.93, 0, 0, 0)
    second_candidate = factory.construct_candidate(2, "RAVACLEY", "Stéphane", "M", datetime.datetime(1970,6,6), 3, "Artisan", False, 330, 13112, 16.56, 32.51, 17594, 22.22, 47.75)
    third_candidate = factory.construct_candidate(3, "THOMASSIN", "Geoffrey", "M", datetime.datetime(1986,10,19),9, "Profession intermédiaire administrative et commerciale des entreprises", False, 331, 216, 0.27, 0.54, 0, 0, 0 )
    fourth_candidate = factory.construct_candidate(4, "ALAUZET", "Eric", "M", datetime.datetime(1958,6,7), 7, "Profession libérale", True, 331, 12647, 15.98, 31.36, 19255, 24.32, 52.25)
    fifth_candidate = factory.construct_candidate(5,"HERITIER", "Louise", "F", datetime.datetime(1997,2,25), 3, "Profession de l'information, des arts et des spectacles", False, 330, 89787, 23.2, 12.2, 9872, 21.32, 6.2 )
    candidates = [first_candidate, second_candidate, third_candidate, fourth_candidate, fifth_candidate]
    
    for candidate in candidates : 
        for number in ids_list : 
            if candidate.id == number :
                candidates_needed.append(candidate)
                break
    
    return candidates_needed


def getDepartments(numbers_list):
    departments_needed = []
    
    factory = FactoryDepartment() 
    first_department = factory.construct_department_from_bdd([1, "Ain", 1])
    second_department = factory.construct_department_from_bdd([2, "Aisne", 2])
    third_department = factory.construct_department_from_bdd([3, "Allier", 3])
    eleven_department = factory.construct_department_from_bdd([11, "Aude", 11])
    thirty_third_department = factory.construct_department_from_bdd([33, "Gironde", 33])
    thirty_fourth_department = factory.construct_department_from_bdd([34, "Herault", 34])
    sixty_nineth_department = factory.construct_department_from_bdd([69, "Nord", 69])
    departments = [first_department, second_department, third_department, eleven_department, thirty_third_department, 
                   thirty_fourth_department, sixty_nineth_department]
    
    for department in departments : 
        for number in numbers_list :
            if department.number == number :
                departments_needed.append(department)
                break
            
    return departments_needed


def getDeputies(ids_list) : 
    deputies_needed = []
    
    factory = FactoryDeputy()
    first_deputy = factory.construct_deputy(1, "M", "DUFREGNE", "Jean-Paul", datetime.datetime(1958, 3, 28), 2, True)
    second_deputy = factory.construct_deputy(2, "M", "PERCHE", "Philippe", datetime.datetime(1987, 11, 19), 3, False)
    third_deputy = factory.construct_deputy(3, "F", "BENOIT-GOLA", "Anne-Cécile", datetime.datetime(1973, 7, 24), 4, False)
    fourth_deputy = factory.construct_deputy(4, "M", "LEROUX", "Sylvain", datetime.datetime(1978, 6, 25), 987, False)
    deputies = [first_deputy, second_deputy, third_deputy, fourth_deputy]
    
    for deputy in deputies : 
        for id in ids_list :
            if deputy.id == id :
                deputies_needed.append(deputy)
                break
            
    return deputies_needed



def getDistricts(ids_list) : 
    districts_needed = []
    
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
    
    for district in districts : 
        for id in ids_list :
            if district.id == id :
                districts_needed.append(district)
                break
            
    return districts_needed


def getParties(ids_list) : 
    parties_needed = []
    
    factory = FactoryParty()
    first_party = factory.construct_party(1, "Divers extrême gauche", "DXG")
    second_party = factory.construct_party(3, "Nouvelle union populaire écologique et sociale", "NUP")
    third_party = factory.construct_party(7, "Ensemble ! (Majorité présidentielle)", "ENS")
    fourth_party = factory.construct_party(9, "Divers", "DIV")
    parties = [first_party, second_party, third_party, fourth_party]
    
    for party in parties : 
        for id in ids_list : 
            if party.id == id : 
                parties_needed.append(party)
                break
    
    return parties_needed

def getResults(ids_list) : 
    results_needed = []
    
    factory = FactoryResult()
    first_result_ten_district = factory.construct_result(100, "Completed", 1, 876, 5, 0.65, 666, 98.8, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 10)
    second_result_ten_district = factory.construct_result(105, "Completed", 2, 876, 5, 0.65, 666, 18.8, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 10)
    
    first_result_eleven_district = factory.construct_result(110, "Completed", 1, 276, 23, 1.65, 866, 38.8, 3, 5.2, 1.7, 566, 88.8, 3, 5.2, 1.7, 2.7, 11)
    second_result_eleven_district = factory.construct_result(115, "Completed", 2, 276, 23, 1.65, 866, 68.8, 3, 5.2, 1.7, 566, 88.8, 3, 5.2, 1.7, 2.7, 11)
    
    first_result_twelve_district = factory.construct_result(120, "Completed", 1, 576, 23, 8.65, 566, 35.8, 8, 8.2, 8.7, 605, 68.8, 13, 3.2, 4.7, 5.7, 12)
    second_result_twelve_district = factory.construct_result(125, "Completed", 2, 576, 23, 8.65, 566, 25.8, 8, 8.2, 8.7, 605, 68.8, 13, 3.2, 4.7, 5.7, 12)
    
    first_result_twenty_district = factory.construct_result(200, "Completed", 1, 876, 5, 0.65, 666, 78.8, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 20)
    second_result_twenty_district = factory.construct_result(205, "Completed", 2, 876, 5, 0.65, 666, 78.8, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 20)
    
    first_result_twenty_one_district = factory.construct_result(210, "Completed", 1, 276, 23, 1.65, 866, 68.8, 3, 5.2, 1.7, 566, 88.8, 3, 5.2, 1.7, 2.7, 21)
    second_result_twenty_one_district = factory.construct_result(215, "Completed", 2, 276, 23, 1.65, 866, 68.8, 3, 5.2, 1.7, 566, 88.8, 3, 5.2, 1.7, 2.7, 21)
    
    first_result_twenty_two_district = factory.construct_result(220, "Completed", 1, 576, 23, 8.65, 566, 15.8, 8, 8.2, 8.7, 605, 68.8, 13, 3.2, 4.7, 5.7, 22)
    second_result_twenty_two_district = factory.construct_result(225, "Completed", 2, 576, 23, 8.65, 566, 15.8, 8, 8.2, 8.7, 605, 68.8, 13, 3.2, 4.7, 5.7, 22)
    
    first_result_twenty_three_district = factory.construct_result(230, "Completed", 1, 676, 50, 10.65, 266, 28.8, 5, 23.2, 4.7, 266, 48.8, 8, 4.2, 2.7, 0.9, 23)
    second_result_twenty_three_district = factory.construct_result(235, "Completed", 2, 676, 50, 10.65, 266, 28.8, 5, 23.2, 4.7, 266, 48.8, 8, 4.2, 2.7, 0.9, 23)
    
    first_result_twenty_four_district = factory.construct_result(240, "Completed", 1, 876, 5, 0.65, 666, 99.56, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 24)
    second_result_twenty_four_district = factory.construct_result(245, "Completed", 2, 876, 5, 0.65, 666, 99.56, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 24)
    
    first_result_twenty_five_district = factory.construct_result(250, "Completed", 1, 876, 5, 0.65, 666, 65.2, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 25)
    second_result_twenty_five_district = factory.construct_result(255, "Completed", 2, 876, 5, 0.65, 666, 65.2, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 25)
    
    first_result_twenty_six_district = factory.construct_result(260, "Completed", 1, 876, 5, 0.65, 666, 0.45, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 26)
    second_result_twenty_six_district = factory.construct_result(265, "Completed", 2, 876, 5, 0.65, 666, 0.45, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 26)
    
    first_result_twenty_seven_district = factory.construct_result(270, "Completed", 1, 876, 5, 0.65, 666, 42.6, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 27)
    second_result_twenty_seven_district = factory.construct_result(275, "Completed", 2, 876, 5, 0.65, 666, 42.6, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 27)
    
    first_result_hundred_ten_district = factory.construct_result(1100, "Completed", 1, 876, 5, 0.65, 666, 12.8, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 110)
    second_result_hundred_ten_district = factory.construct_result(1105, "Completed", 2, 876, 5, 0.65, 666, 7.8, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 110)
    
    first_result_hundred_eleven_district = factory.construct_result(1110, "Completed", 1, 276, 23, 1.65, 866, 58.8, 3, 5.2, 1.7, 566, 88.8, 3, 5.2, 1.7, 2.7, 111)
    second_result_hundred_eleven_district = factory.construct_result(1115, "Completed", 2, 276, 23, 1.65, 866, 48.8, 3, 5.2, 1.7, 566, 88.8, 3, 5.2, 1.7, 2.7, 111)
    
    first_result_three_hundred_thirty_district = factory.construct_result(3300, "Completed", 1, 576, 23, 8.65, 566, 66.8, 8, 8.2, 8.7, 605, 68.8, 13, 3.2, 4.7, 5.7, 330)
    second_result_three_hundred_thirty_district = factory.construct_result(3305, "Completed", 2, 576, 23, 8.65, 566, 43.8, 8, 8.2, 8.7, 605, 68.8, 13, 3.2, 4.7, 5.7, 330)
    
    first_result_three_hundred_thirty_one_district = factory.construct_result(3310, "Completed", 1, 876, 5, 0.65, 666, 42.8, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 331)
    second_result_three_hundred_thirty_one_district = factory.construct_result(3315, "Completed", 2, 876, 5, 0.65, 666, 23.8, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 331)
    
    first_result_three_hundred_fourty_district = factory.construct_result(3400, "Completed", 1, 276, 23, 1.65, 866, 78.8, 3, 5.2, 1.7, 566, 88.8, 3, 5.2, 1.7, 2.7, 340)
    second_result_three_hundred_fourty_district = factory.construct_result(3405, "Completed", 2, 276, 23, 1.65, 866, 68.8, 3, 5.2, 1.7, 566, 88.8, 3, 5.2, 1.7, 2.7, 340)
    
    first_result_three_hundred_fourty_one_district = factory.construct_result(3410, "Completed", 1, 576, 23, 8.65, 566, 23.8, 8, 8.2, 8.7, 605, 68.8, 13, 3.2, 4.7, 5.7, 341)
    second_result_three_hundred_fourty_one_district = factory.construct_result(3415, "Completed", 2, 576, 23, 8.65, 566, 42.8, 8, 8.2, 8.7, 605, 68.8, 13, 3.2, 4.7, 5.7, 341)
    
    first_result_three_hundred_fourty_two_district = factory.construct_result(3420, "Completed", 1, 876, 5, 0.65, 666, 43.8, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 342)
    second_result_three_hundred_fourty_two_district = factory.construct_result(3425, "Completed", 2, 876, 5, 0.65, 666, 66.8, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 342)
    
    first_result_three_hundred_fourty_three_district = factory.construct_result(3430, "Completed", 1, 276, 23, 1.65, 866, 48.8, 3, 5.2, 1.7, 566, 88.8, 3, 5.2, 1.7, 2.7, 343)
    second_result_three_hundred_fourty_three_district = factory.construct_result(3435, "Completed", 2, 276, 23, 1.65, 866, 58.8, 3, 5.2, 1.7, 566, 88.8, 3, 5.2, 1.7, 2.7, 343)
    
    first_result_six_hundred_ninety_district = factory.construct_result(6900, "Completed", 1, 576, 23, 8.65, 566, 7.8, 8, 8.2, 8.7, 605, 68.8, 13, 3.2, 4.7, 5.7, 690)
    second_result_six_hundred_ninety_district = factory.construct_result(6905, "Completed", 2, 576, 23, 8.65, 566, 12.8, 8, 8.2, 8.7, 605, 68.8, 13, 3.2, 4.7, 5.7, 690)
    
    first_result_six_hundred_ninety_one_district = factory.construct_result(6910, "Completed", 1, 876, 5, 0.65, 666, 25.8, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 691)
    second_result_six_hundred_ninety_one_district = factory.construct_result(6915, "Completed", 2, 876, 5, 0.65, 666, 35.8, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 691)
    
    first_result_six_hundred_ninety_two_district = factory.construct_result(6920, "Completed", 1, 276, 23, 1.65, 866, 68.8, 3, 5.2, 1.7, 566, 88.8, 3, 5.2, 1.7, 2.7, 692)
    second_result_six_hundred_ninety_two_district = factory.construct_result(6925, "Completed", 2, 276, 23, 1.65, 866, 38.8, 3, 5.2, 1.7, 566, 88.8, 3, 5.2, 1.7, 2.7, 692)
    
    first_result_six_hundred_ninety_three_district = factory.construct_result(6930, "Completed", 1, 576, 23, 8.65, 566, 18.8, 8, 8.2, 8.7, 605, 68.8, 13, 3.2, 4.7, 5.7, 693)
    second_result_six_hundred_ninety_three_district = factory.construct_result(6935, "Completed", 2, 576, 23, 8.65, 566, 98.8, 8, 8.2, 8.7, 605, 68.8, 13, 3.2, 4.7, 5.7, 693)
        
    results = [first_result_ten_district, second_result_ten_district, first_result_eleven_district, second_result_eleven_district, first_result_twelve_district,
                second_result_twelve_district, first_result_twenty_district, second_result_twenty_district, first_result_twenty_one_district, 
                second_result_twenty_one_district, first_result_twenty_two_district, second_result_twenty_two_district, first_result_twenty_three_district, 
                second_result_twenty_three_district, first_result_twenty_four_district, second_result_twenty_four_district, first_result_twenty_five_district, 
                second_result_twenty_five_district, first_result_twenty_six_district, second_result_twenty_six_district, first_result_twenty_seven_district, 
                second_result_twenty_seven_district, first_result_hundred_ten_district, second_result_hundred_ten_district, first_result_hundred_eleven_district, 
                second_result_hundred_eleven_district, first_result_three_hundred_thirty_district, second_result_three_hundred_thirty_district, 
                first_result_three_hundred_thirty_one_district, second_result_three_hundred_thirty_one_district, first_result_three_hundred_fourty_district, 
                second_result_three_hundred_fourty_district, first_result_three_hundred_fourty_one_district, second_result_three_hundred_fourty_one_district, 
                first_result_three_hundred_fourty_two_district, second_result_three_hundred_fourty_two_district, first_result_three_hundred_fourty_three_district, 
                second_result_three_hundred_fourty_three_district, first_result_six_hundred_ninety_district, second_result_six_hundred_ninety_district, 
                first_result_six_hundred_ninety_one_district, second_result_six_hundred_ninety_one_district, first_result_six_hundred_ninety_two_district,
                second_result_six_hundred_ninety_two_district, first_result_six_hundred_ninety_three_district, second_result_six_hundred_ninety_three_district]
    
    
    
    for result in results : 
        for id in ids_list :
            if result.id == id :
                results_needed.append(result)
                break
            
    return results_needed