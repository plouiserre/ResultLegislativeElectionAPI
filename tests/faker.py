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
    one_candidate = factory.construct_candidate(1, "VUITTON", "Brigitte", "F", datetime.datetime(1957,11,29), 1, "Professeur, profession scientifique", False, 10, 779, 0.98, 1.93, 0, 0, 0)
    two_candidate = factory.construct_candidate(2, "RAVACLEY", "Stéphane", "M", datetime.datetime(1970,6,6), 3, "Artisan", False, 330, 13112, 16.56, 32.51, 17594, 22.22, 47.75)
    three_candidate = factory.construct_candidate(3, "THOMASSIN", "Geoffrey", "M", datetime.datetime(1986,10,19),9, "Profession intermédiaire administrative et commerciale des entreprises", False, 331, 216, 0.27, 0.54, 0, 0, 0 )
    four_candidate = factory.construct_candidate(4, "ALAUZET", "Eric", "M", datetime.datetime(1958,6,7), 7, "Profession libérale", True, 331, 12647, 15.98, 31.36, 19255, 24.32, 52.25)
    five_candidate = factory.construct_candidate(5,"HERITIER", "Louise", "F", datetime.datetime(1997,2,25), 3, "Profession de l'information, des arts et des spectacles", False, 330, 89787, 23.2, 12.2, 9872, 21.32, 6.2 )
    six_candidate = factory.construct_candidate(6, "KASTLER", "Jean-Loup", "M", datetime.datetime(1982, 2, 12) , 5, "Professeur, profession scientifique", False, 3, 1763, 2.14, 4.93, 0, 0, 0)
    seven_candidate = factory.construct_candidate(7, "SEGUIN", "Isabelle", "F", datetime.datetime(1962, 5, 16), 7, "Chef d'entreprise de 10 salariés ou plus", False, 4, 7317, 7.71, 16.34,	0,	0,	0)
    eight_candidate = factory.construct_candidate(8 , "PARIS", "Stéphanie", "F", datetime.datetime(1975, 8, 15), 12, "Professeur des écoles, instituteur et assimilé", False, 5, 931, 1.2, 2.58, 0,	0, 0)
    nine_candidate = factory.construct_candidate(9, "MORVAN LEMBERT", "Marine", "F", datetime.datetime(1962, 3, 16), 5, "Profession libérale", False, 3, 528, 0.64,	1.48, 0, 0,	0)
    ten_candidate = factory.construct_candidate(10, "EYRAUD", "Olivier", "M", datetime.datetime(1955, 3, 8), 15, "Ancien artisan, commerçant, chef d'entreprise", False, 2,	11354,	11.36,	23.23,	0, 0, 0)
    eleven_candidate = factory.construct_candidate(11, "MOUGENOT", "Paul", "M", datetime.datetime(1988, 10, 13), 11, "Agriculteur sur moyenne exploitation", False,	6, 3853, 5.32,	11.35,	0,	0,	0)
    twelve_candidate = factory.construct_candidate(12, "EL OUASDI", "Fatima", "F", datetime.datetime(1994, 4, 28), 7, "Ingénieur et cadre technique d'entreprise", False, 7, 3755, 5.13, 11.52,	0, 0, 0)
    thirteen_candidate = factory.construct_candidate(13, "BOBIN", "David", "M", datetime.datetime(1984,8, 24), 11, "Personne diverse sans activité professionnelle de moins de 60 ans (sauf retraité)", False, 9, 4300,	5.46, 12.83, 0,	0, 0)
    fourteen_candidate = factory.construct_candidate(14, "AUTAIN", "Clémentine", "F", datetime.datetime(1973,5,26),	3, "Profession de l'information, des arts et des spectacles", True, 515, 9400, 14.83, 46.15, 11296, 17.753,	100)
    fifteen_candidate = factory.construct_candidate(15, "VACCA", "Françoise", "F", datetime.datetime(1963, 4, 6), 5, "Cadre de la fonction publique", False, 10, 892, 1.07,	2.31, 0, 0,	0)
    sixteen_candidate = factory.construct_candidate(16, "AFFRAIX", "Christophe", "M", datetime.datetime(1983, 8, 2), 13, "Contremaître, agent de maîtrise", False, 12, 440, 0.54, 1.1, 0, 0, 0)
    seventeen_candidate = factory.construct_candidate(17, "DE NICOLAY", "Axelle", "F", datetime.datetime(1988, 3, 26), 14, "Cadre administratif et commercial d'entreprise", False, 12, 1557,	1.92, 3.9, 0, 0, 0)
    eighteen_candidate = factory.construct_candidate(18, "RAY", "Nicolas", "M", datetime.datetime(1981,5,14), 11, "Cadre de la fonction publique",	False, 13, 9594, 11.96,	24.22, 19296, 26.194, 63.272)
    nineteen_candidate = factory.construct_candidate(19, "PEYROL", "Bénédicte",	"F", datetime.datetime(1991,3,23), 7, "Cadre administratif et commercial d'entreprise",	True, 13, 9219,	11.5, 23.27, 12347,	15.178,	36.728)
    twenty_candidate = factory.construct_candidate(20, "CHATEL", "Philippe", "M", datetime.datetime(1968, 4, 9), 6, "Cadre administratif et commercial d'entreprise", False, 12, 585, 0.72, 1.47, 0, 0, 0)
    twenty_one_candidate = factory.construct_candidate(21, "BIASOLI", "Gilbert", "M", datetime.datetime(1951, 12, 26), 13, "Ingénieur et cadre technique d'entreprise", 0, 38,	623, 0.63, 1.29, 0,	0, 0)
    twenty_two_candidate = factory.construct_candidate(22, "SIKORA", "Juliette", "F", datetime.datetime(1960, 5, 17), 9, "Ouvrier qualifié de type industriel", False, 38, 0, 0, 0, 0, 0, 0)
    twenty_three_candidate = factory.construct_candidate(23, "BARTHÈS", "Christophe", "M", datetime.datetime(1966, 10, 12), 15, "Agriculteur sur moyenne exploitation", False, 38, 15871, 16.12, 32.8, 23914, 25.07, 50.815)
    twenty_four_candidate = factory.construct_candidate(24, "HÉRIN", "Danièle", "F", datetime.datetime(1947, 1, 14), 7, "Professeur, profession scientifique", True, 38, 10636,	10.8, 21.98, 0,	0,	0)
    twenty_five_candidate = factory.construct_candidate(25, "COURRIÈRE CALMON", "Sophie", "F", datetime.datetime(1965, 2, 24), 3, "Professeur, profession scientifique", False, 38, 13620, 13.83, 28.15,	20733, 24.87, 49.185)
    twenty_six_candidate = factory.construct_candidate(26, "BOUDIÉ", "Florent", "M", datetime.datetime(1973, 9, 22), 7, "Cadre de la fonction publique", True, 151, 13565, 16.29, 32.7, 19581, 24.502, 51.424)
    twenty_seven_candidate = factory.construct_candidate(27, "BOURGOIS", "Pascal", "M", datetime.datetime(1956, 7, 24), 3, "Cadre de la fonction publique", False, 151, 9705, 11.65,	23.4, 0, 0,	0)
    twenty_eight_candidate = factory.construct_candidate(28, "DIAZ", "Edwige", "F", datetime.datetime(1987, 10, 15), 15, "Cadre administratif et commercial d'entreprise", False, 152, 18662, 18.9, 39.42, 25092, 26.954, 59.467)
    twenty_nine_candidate = factory.construct_candidate(29, "FAURE", "Marylène", "F", datetime.datetime(1972, 2, 26), 3 , "Employé administratif d'entreprise", False, 149,	11269, 9.41, 18.84,	0, 0, 0)
    thirty_candidate = factory.construct_candidate(30, "RIVAULT", "Lydie", "F", datetime.datetime(1964, 3, 6), 13, "Ancienne profession intermédiaire", False, 149,	789, 0.66, 1.32, 0,	0,	0)
    thirty_one_candidate = factory.construct_candidate(31, "OZIOL", "Nathalie", "F", datetime.datetime(1990, 2, 18), 3, "Professeur, profession scientifique", False, 155, 11513, 17.6,	40.37, 17008, 25.99, 63.33)
    thirty_two_candidate = factory.construct_candidate(32, "ZBAIRI", "Kadija", "F", datetime.datetime(1968, 1, 18), 5, "Profession libérale", False, 155, 130, 0.2, 0.46, 0, 0,	0)
    thirty_three_candidate = factory.construct_candidate(33, "CRISTOL", "Laurence", "F", datetime.datetime(1967, 11, 8), 7, "Professeur, profession scientifique",	False, 156,	12457, 13.5, 26.68, 22907, 25.764, 54.725)
    thirty_four_candidate = factory.construct_candidate(34, "BERTHET", "Alain", "M", datetime.datetime(1959, 8, 21), 11, "Profession libérale",	False,	156, 2603, 2.82, 5.57, 0, 0, 0)
    thirty_five_candidate = factory.construct_candidate(35, "SAUREL", "Philippe", "M", datetime.datetime(1957, 12, 17), 4, "Profession intermédiaire de la santé et du travail social",	False, 156,	2070, 2.24,	4.43, 0, 0,	0)
    thirty_six_candidate = factory.construct_candidate(36, "LAÏ-KANE-CHEONG", "Alexandre", "M", datetime.datetime(1988, 12,1), 1, "Professeur des écoles, instituteur et assimilé",	False, 553, 3862, 4.71, 16.99, 11229, 13.845, 46.9)
    thirty_seven_candidate = factory.construct_candidate(37, "PINEL", "Sylvia",	"F", datetime.date(1977,9,28), 2, "Cadre de la fonction publique",  True, 447, 9892, 10.27, 20.19, 0, 0, 0)
    thirty_eight_candidate = factory.construct_candidate(38, "HABIB", "David", "M",	datetime.datetime(1961,3,16), 4, "Cadre administratif et commercial d'entreprise",	True, 323, 16345, 19.44, 36.61, 26414, 35.939, 70.602)
    thirty_nine_candidate = factory.construct_candidate(39,	"MOLAC", "Paul", "M", datetime.datetime(1962,5,21),	6,	"Professeur, profession scientifique",	True, 259,	21900,	19.6, 37.65, 37678,	35.727,	75.423)   
    forty_candidate = factory.construct_candidate(40, "SEO", "Mikaele",	"M", datetime.datetime(1971,12,27),	8,	"Profession intermédiaire administrative de la fonction publique", False, 563, 1622, 16.91,	21.8, 3717, 38.8, 50.11)
    forty_one_candidate = factory.construct_candidate(41, "LAGARDE", "Jean-Christophe",	"M", datetime.datetime(1967,10,24),	10,	"Cadre de la fonction publique", True,	509, 7745, 11.87, 33.41, 11395,	16.893,	44.413)
    forty_two_candidate = factory.construct_candidate(42, "NAEGELEN", "Christophe",	"M", datetime.datetime(1983,12,30),	12,	"Chef d'entreprise de 10 salariés ou plus",	True,	475, 15136,	23.67,	47.21, 21035, 33.633, 73.408)
    forty_three_candidate = factory.construct_candidate(43,	"TROCHU", "Laurence", "F", datetime.datetime(1973,7,4), 14,	"Personne diverse sans activité professionnelle de moins de 60 ans (sauf retraité)", False,	423, 5730, 6.88, 12.47,	0, 0, 0)
    forty_four_candidate = factory.construct_candidate(44, "DESSAUX", "Aurélien", "M",	datetime.datetime(1991,12,19), 16, "Profession intermédiaire administrative et commerciale des entreprises", False,	467, 1184,	1.49,	2.83,	0,	0,	0)
       
    candidates = [one_candidate, two_candidate, three_candidate, four_candidate, five_candidate, six_candidate, seven_candidate, eight_candidate,
                  nine_candidate, ten_candidate, eleven_candidate, twelve_candidate, thirteen_candidate, fourteen_candidate, fifteen_candidate, 
                  sixteen_candidate, seventeen_candidate, eighteen_candidate, nineteen_candidate, twenty_candidate, twenty_one_candidate, 
                  twenty_two_candidate, twenty_three_candidate, twenty_four_candidate, twenty_five_candidate, twenty_six_candidate, twenty_seven_candidate,
                  twenty_eight_candidate, twenty_nine_candidate, thirty_candidate, thirty_one_candidate, thirty_two_candidate, thirty_three_candidate, 
                  thirty_four_candidate, thirty_five_candidate, thirty_six_candidate, thirty_seven_candidate, thirty_eight_candidate, thirty_nine_candidate,
                  forty_candidate, forty_one_candidate, forty_two_candidate, forty_three_candidate, forty_four_candidate]
    
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
    one_party = factory.construct_party(1, "Divers extrême gauche", "DXG")
    two_party = factory.construct_party(2, "Parti radical de gauche", "RDG")
    three_party = factory.construct_party(3, "Nouvelle union populaire écologique et sociale", "NUP")
    four_party = factory.construct_party(4, "Divers gauche", "DVG")
    five_party = factory.construct_party(5, "Ecologistes", "ECO")
    six_party = factory.construct_party(6, "Régionaliste", "REG")
    seven_party = factory.construct_party(7, "Ensemble ! (Majorité présidentielle)", "ENS")
    eight_party = factory.construct_party(8, "Divers Centre", "DVC")
    nine_party = factory.construct_party(9, "Divers", "DIV")
    ten_party = factory.construct_party(10, "Union des Démocrates et des Indépendants", "UDI")
    eleven_party = factory.construct_party(11, "Les Républicains", "LR")
    twelve_party = factory.construct_party(12, "Divers droite", "DVD")
    thirteen_party = factory.construct_party(13, "Droite souverainiste", "DSV")
    fourteen_party = factory.construct_party(14, "Reconquête !", "REC")
    fifteen_party = factory.construct_party(15, "Rassemblement National", "RN")
    sixteen_party = factory.construct_party(16, "Divers extrême droite", "DXD")
    parties = [one_party, two_party, three_party, four_party, five_party, six_party, seven_party, eight_party, nine_party,
               ten_party, eleven_party, twelve_party, thirteen_party, fourteen_party, fifteen_party, sixteen_party]
    
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