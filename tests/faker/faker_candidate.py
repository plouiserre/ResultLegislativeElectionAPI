from app.domain.factory.factorycandidate import FactoryCandidate
from tests.faker.faker_party import getParties_id_by_name
from tests.faker.faker_district import getDistricts_by_department_id

import datetime

#TODO improve perf 
def getCandidates_by_id(ids_list) : 
    candidates_needed = []
    
    candidates = __create_candidates()
    
    for candidate in candidates : 
        for number in ids_list : 
            if candidate.id == number :
                candidates_needed.append(candidate)
                break
    
    return candidates_needed


def getCandidates_by_partys_departments(party_names, departments_ids) :
    candidates_needed = []
    party_ids = getParties_id_by_name(party_names)   
        
    districts = getDistricts_by_department_id(departments_ids)
    districts_id = []
    for district in districts : 
        districts_id.append(district.id)
        
    candidates = __create_candidates()
    
    #TODO improve this code
    for candidate in candidates : 
        for district_id in districts_id : 
            for party_id in party_ids :
                if candidate.district_id == district_id  and candidate.party_id == party_id:
                    candidates_needed.append(candidate)
                
    return candidates_needed
        

# def getCandidates_by_party(party_names) : 
#     candidates_needed = []
#     party_ids = getParties_id_by_name(party_names)        
    
#     candidates = __create_candidates()
    
#     for candidate in candidates : 
#         for party_id in party_ids : 
#             if candidate.party_id == party_id :
#                 candidates_needed.append(candidate)
#                 break
    
#     return candidates_needed


# def getCandidates_by_department(departments_name) :
#     candidates_needed = []
#     departments = getDepartments_by_names(departments_name)
    
#     departments_id = []
#     for department in departments : 
#         departments_id.append(department.id)
        
#     districts = getDistricts_by_department_id(departments_id)
#     districts_id = []
#     for district in districts : 
#         districts_id.append(district.id)
    
#     candidates = __create_candidates()
    
#     for candidate in candidates : 
#         for district_id in districts_id : 
#             if candidate.district_id == district_id :
#                 candidates_needed.append(candidate)
#                 break
            
#     return candidates_needed


def __create_candidates() :
    factory = FactoryCandidate()
    one_candidate = factory.construct_candidate(1, "VUITTON", "Brigitte", "F", datetime.datetime(1957,11,29), 1, "Professeur, profession scientifique", False, 10, 779, 0.98, 1.93, 0, 0, 0)
    two_candidate = factory.construct_candidate(2, "RAVACLEY", "Stéphane", "M", datetime.datetime(1970,6,6), 3, "Artisan", False, 330, 13112, 16.56, 32.51, 17594, 22.22, 47.75)
    three_candidate = factory.construct_candidate(3, "THOMASSIN", "Geoffrey", "M", datetime.datetime(1986,10,19),9, "Profession intermédiaire administrative et commerciale des entreprises", False, 331, 216, 0.27, 0.54, 0, 0, 0 )
    four_candidate = factory.construct_candidate(4, "ALAUZET", "Eric", "M", datetime.datetime(1958,6,7), 7, "Profession libérale", True, 331, 12647, 15.98, 31.36, 19255, 24.32, 52.25)
    five_candidate = factory.construct_candidate(5,"HERITIER", "Louise", "F", datetime.datetime(1997,2,25), 3, "Profession de l'information, des arts et des spectacles", False, 330, 89787, 23.2, 12.2, 9872, 21.32, 6.2 )
    six_candidate = factory.construct_candidate(6, "KASTLER", "Jean-Loup", "M", datetime.datetime(1982, 2, 12) , 5, "Professeur, profession scientifique", False, 110, 1763, 2.14, 4.93, 0, 0, 0)
    seven_candidate = factory.construct_candidate(7, "SEGUIN", "Isabelle", "F", datetime.datetime(1962, 5, 16), 7, "Chef d'entreprise de 10 salariés ou plus", False, 111, 7317, 7.71, 16.34, 0, 0, 0)
    eight_candidate = factory.construct_candidate(8 , "PARIS", "Stéphanie", "F", datetime.datetime(1975, 8, 15), 12, "Professeur des écoles, instituteur et assimilé", False, 340, 931, 1.2, 2.58, 0,	0, 0)
    nine_candidate = factory.construct_candidate(9, "MORVAN LEMBERT", "Marine", "F", datetime.datetime(1962, 3, 16), 5, "Profession libérale", False, 341, 528, 0.64,	1.48, 0, 0,	0)
    ten_candidate = factory.construct_candidate(10, "EYRAUD", "Olivier", "M", datetime.datetime(1955, 3, 8), 15, "Ancien artisan, commerçant, chef d'entreprise", False, 342, 11354, 11.36, 23.23, 0, 0, 0)
    eleven_candidate = factory.construct_candidate(11, "MOUGENOT", "Paul", "M", datetime.datetime(1988, 10, 13), 11, "Agriculteur sur moyenne exploitation", False,	343, 3853, 5.32,	11.35,	0,	0,	0)
    twelve_candidate = factory.construct_candidate(12, "EL OUASDI", "Fatima", "F", datetime.datetime(1994, 4, 28), 7, "Ingénieur et cadre technique d'entreprise", False, 690, 3755, 5.13, 11.52, 0, 0, 0)
    thirteen_candidate = factory.construct_candidate(13, "BOBIN", "David", "M", datetime.datetime(1984,8, 24), 11, "Personne diverse sans activité professionnelle de moins de 60 ans (sauf retraité)", False, 691, 4300,	5.46, 12.83, 0,	0, 0)
    fourteen_candidate = factory.construct_candidate(14, "AUTAIN", "Clémentine", "F", datetime.datetime(1973,5,26),	3, "Profession de l'information, des arts et des spectacles", True, 515, 9400, 14.83, 46.15, 11296, 17.753,	100)
    fifteen_candidate = factory.construct_candidate(15, "VACCA", "Françoise", "F", datetime.datetime(1963, 4, 6), 5, "Cadre de la fonction publique", False, 692, 892, 1.07, 2.31, 0, 0, 0)
    sixteen_candidate = factory.construct_candidate(16, "AFFRAIX", "Christophe", "M", datetime.datetime(1983, 8, 2), 13, "Contremaître, agent de maîtrise", False, 110, 440, 0.54, 1.1, 0, 0, 0)
    seventeen_candidate = factory.construct_candidate(17, "DE NICOLAY", "Axelle", "F", datetime.datetime(1988, 3, 26), 14, "Cadre administratif et commercial d'entreprise", False, 111, 1557,	1.92, 3.9, 0, 0, 0)
    eighteen_candidate = factory.construct_candidate(18, "RAY", "Nicolas", "M", datetime.datetime(1981,5,14), 11, "Cadre de la fonction publique",	False, 330, 9594, 11.96, 24.22, 19296, 26.194, 63.272)
    nineteen_candidate = factory.construct_candidate(19, "PEYROL", "Bénédicte",	"F", datetime.datetime(1991,3,23), 7, "Cadre administratif et commercial d'entreprise",	True, 331, 9219, 11.5, 23.27, 12347, 15.178, 36.728)
    twenty_candidate = factory.construct_candidate(20, "CHATEL", "Philippe", "M", datetime.datetime(1968, 4, 9), 6, "Cadre administratif et commercial d'entreprise", False, 340, 585, 0.72, 1.47, 0, 0, 0)
    twenty_one_candidate = factory.construct_candidate(21, "BIASOLI", "Gilbert", "M", datetime.datetime(1951, 12, 26), 13, "Ingénieur et cadre technique d'entreprise", False, 341,	623, 0.63, 1.29, 0,	0, 0)
    twenty_two_candidate = factory.construct_candidate(22, "SIKORA", "Juliette", "F", datetime.datetime(1960, 5, 17), 9, "Ouvrier qualifié de type industriel", False, 342, 0, 0, 0, 0, 0, 0)
    twenty_three_candidate = factory.construct_candidate(23, "BARTHÈS", "Christophe", "M", datetime.datetime(1966, 10, 12), 15, "Agriculteur sur moyenne exploitation", False, 343, 15871, 16.12, 32.8, 23914, 25.07, 50.815)
    twenty_four_candidate = factory.construct_candidate(24, "HÉRIN", "Danièle", "F", datetime.datetime(1947, 1, 14), 7, "Professeur, profession scientifique", True, 690, 10636,	10.8, 21.98, 0,	0,	0)
    twenty_five_candidate = factory.construct_candidate(25, "COURRIÈRE CALMON", "Sophie", "F", datetime.datetime(1965, 2, 24), 3, "Professeur, profession scientifique", False, 691, 13620, 13.83, 28.15,	20733, 24.87, 49.185)
    twenty_six_candidate = factory.construct_candidate(26, "BOUDIÉ", "Florent", "M", datetime.datetime(1973, 9, 22), 7, "Cadre de la fonction publique", True, 110, 13565, 16.29, 32.7, 19581, 24.502, 51.424)
    twenty_seven_candidate = factory.construct_candidate(27, "BOURGOIS", "Pascal", "M", datetime.datetime(1956, 7, 24), 3, "Cadre de la fonction publique", False, 111, 9705, 11.65,	23.4, 0, 0,	0)
    twenty_eight_candidate = factory.construct_candidate(28, "DIAZ", "Edwige", "F", datetime.datetime(1987, 10, 15), 15, "Cadre administratif et commercial d'entreprise", False, 330, 18662, 18.9, 39.42, 25092, 26.954, 59.467)
    twenty_nine_candidate = factory.construct_candidate(29, "FAURE", "Marylène", "F", datetime.datetime(1972, 2, 26), 3 , "Employé administratif d'entreprise", False, 331,	11269, 9.41, 18.84,	0, 0, 0)
    thirty_candidate = factory.construct_candidate(30, "RIVAULT", "Lydie", "F", datetime.datetime(1964, 3, 6), 13, "Ancienne profession intermédiaire", False, 341,	789, 0.66, 1.32, 0,	0,	0)
    thirty_one_candidate = factory.construct_candidate(31, "OZIOL", "Nathalie", "F", datetime.datetime(1990, 2, 18), 3, "Professeur, profession scientifique", False, 342, 11513, 17.6,	40.37, 17008, 25.99, 63.33)
    thirty_two_candidate = factory.construct_candidate(32, "ZBAIRI", "Kadija", "F", datetime.datetime(1968, 1, 18), 5, "Profession libérale", False, 343, 130, 0.2, 0.46, 0, 0,	0)
    thirty_three_candidate = factory.construct_candidate(33, "CRISTOL", "Laurence", "F", datetime.datetime(1967, 11, 8), 7, "Professeur, profession scientifique",	False, 690,	12457, 13.5, 26.68, 22907, 25.764, 54.725)
    thirty_four_candidate = factory.construct_candidate(34, "BERTHET", "Alain", "M", datetime.datetime(1959, 8, 21), 11, "Profession libérale",	False,	691, 2603, 2.82, 5.57, 0, 0, 0)
    thirty_five_candidate = factory.construct_candidate(35, "SAUREL", "Philippe", "M", datetime.datetime(1957, 12, 17), 4, "Profession intermédiaire de la santé et du travail social",	False, 692,	2070, 2.24,	4.43, 0, 0,	0)
    thirty_six_candidate = factory.construct_candidate(36, "LAÏ-KANE-CHEONG", "Alexandre", "M", datetime.datetime(1988, 12,1), 1, "Professeur des écoles, instituteur et assimilé",	False, 693, 3862, 4.71, 16.99, 11229, 13.845, 46.9)
    thirty_seven_candidate = factory.construct_candidate(37, "PINEL", "Sylvia",	"F", datetime.date(1977,9,28), 2, "Cadre de la fonction publique",  True, 110, 9892, 10.27, 20.19, 0, 0, 0)
    thirty_eight_candidate = factory.construct_candidate(38, "HABIB", "David", "M",	datetime.datetime(1961,3,16), 4, "Cadre administratif et commercial d'entreprise",	True, 111, 16345, 19.44, 36.61, 26414, 35.939, 70.602)
    thirty_nine_candidate = factory.construct_candidate(39,	"MOLAC", "Paul", "M", datetime.datetime(1962,5,21),	6,	"Professeur, profession scientifique",	True, 330,	21900,	19.6, 37.65, 37678,	35.727,	75.423)   
    forty_candidate = factory.construct_candidate(40, "SEO", "Mikaele",	"M", datetime.datetime(1971,12,27),	8,	"Profession intermédiaire administrative de la fonction publique", False, 331, 1622, 16.91,	21.8, 3717, 38.8, 50.11)
    forty_one_candidate = factory.construct_candidate(41, "LAGARDE", "Jean-Christophe",	"M", datetime.datetime(1967,10,24),	10,	"Cadre de la fonction publique", True,	340, 7745, 11.87, 33.41, 11395,	16.893,	44.413)
    forty_two_candidate = factory.construct_candidate(42, "NAEGELEN", "Christophe",	"M", datetime.datetime(1983,12,30),	12,	"Chef d'entreprise de 10 salariés ou plus",	True, 341, 15136, 23.67, 47.21, 21035, 33.633, 73.408)
    forty_three_candidate = factory.construct_candidate(43,	"TROCHU", "Laurence", "F", datetime.datetime(1973,7,4), 14,	"Personne diverse sans activité professionnelle de moins de 60 ans (sauf retraité)", False,	342, 5730, 6.88, 12.47,	0, 0, 0)
    forty_four_candidate = factory.construct_candidate(44, "DESSAUX", "Aurélien", "M",	datetime.datetime(1991,12,19), 16, "Profession intermédiaire administrative et commerciale des entreprises", False,	343, 1184,	1.49,	2.83,	0,	0,	0)
    #2 LR 33
    forty_five_candidate = factory.construct_candidate(45, "NJIKAM", "Pierre De Gaetan", "M", datetime.datetime(1966, 8, 7), 11, "Cadre administratif et commercial d'entreprise", False, 330, 4116, 3.95, 8.03, 0, 0, 0)
    forty_six_candidate = factory.construct_candidate(46, "MORIN", "Marc", "M", datetime.datetime(1985, 7, 31), 11, "Commerçant et assimilé", False, 331, 5964, 4.98, 9.97, 0, 0, 0)    
    #2 RN 33
    forty_seven_candidate = factory.construct_candidate(47, "DE FOURNAS", "Grégoire", "M", datetime.datetime(1985, 3, 19), 15, "Agriculteur sur moyenne exploitation", False, 330, 16672, 13.78, 28.55, 26263, 25.6, 60.041)
    forty_eight_candidate = factory.construct_candidate(48, "CHADOURNE", "Sandrine", "F", datetime.datetime(1970,12,12), 15, "Profession intermédiaire de la santé et du travail social", False, 331, 11628, 13.96, 28.03, 17185, 23.05, 48.577)
    #2 NUP 34
    forty_nine_candidate = factory.construct_candidate(49, "MIGNACCA", "Julia",	"F", datetime.datetime(1986,2,4), 3, "Cadre administratif et commercial d'entreprise",	False,	340, 12416,	13.45, 26.59, 20229, 21.141, 45.275)
    fifty_candidate = factory.construct_candidate(50, "ROME", "Sébastien", "M",	datetime.datetime(1978,10,12),	3,	"Professeur des écoles, instituteur et assimilé", False, 341, 16841, 14.13,	28.06,	26291,	26.072,	53.691)
    #2 LR 34
    fifty_one_candidate = factory.construct_candidate(51, "LEFEUVRE-ROUMANOS", "Nathalie", "F", datetime.datetime(1976,1,19), 11, "Profession libérale",	False, 342,	1570, 1.66,	3.65, 0, 0,	0)
    fifty_two_candidate = factory.construct_candidate(52, "BOUSCARAIN",	"Jean-François", "M", datetime.datetime(1974,9,2),	11,	"Profession intermédiaire de la santé et du travail social", False,	343, 2267, 2.54, 5.69, 0, 0, 0)
    #1 RN 34
    fifty_three_candidate = factory.construct_candidate(53, "LOPEZ LIGUORI", "Aurélien", "M", datetime.datetime(1993,5,17),	15,	"Cadre de la fonction publique", False,	340, 16079,	14.76,	31.01,	27378,	26.149,	60.62)
    #2 ENS 34
    fifty_four_candidate = factory.construct_candidate(54, "MIRALLES", "Patricia", "F",	datetime.datetime(1967,8,22), 7, "Personne diverse sans activité professionnelle de moins de 60 ans (sauf retraité)", True,	342, 10087,	11.2, 24.83, 19338,	23.9, 57.247)
    fifty_five_candidate = factory.construct_candidate(55, "AUDRIN", "Jean-François", "M", datetime.datetime(1964,10,19), 7, "Profession libérale",	False, 343,	10453, 11.08, 24.28, 0,	0,	0)
    #2 NUP 69
    fifty_six_candidate = factory.construct_candidate(56, "JULIEN-LAFERRIERE",	"Hubert", "M", datetime.datetime(1966,2,27), 3,	"Professeur, profession scientifique", True, 690, 15232, 20.57,	34.82,	20847,	28.15,	51.64)
    fifty_seven_candidate = factory.construct_candidate(57,	"GARIN", "Marie-Charlotte",	"F", datetime.datetime(1995,9,2), 3, "Personne diverse sans activité professionnelle de moins de 60 ans (sauf retraité)", False, 691, 18283, 25.24,	43.68,	21105, 29.13, 54.79)
    #2 LR 69
    fifty_eight_candidate = factory.construct_candidate(58, "PORTIER",	"Alexandre", "M", datetime.datetime(1990,4,21),	11,	"Professeur, profession scientifique", False, 692, 12885, 13.33, 27.64,	22385, 27.112, 65.084)
    fifty_nine_candidate = factory.construct_candidate(59, "MOROGE", "Jérôme", "M",	datetime.datetime(1979,8,23), 11, "Profession libérale", False,	693, 9647, 11.74, 22.08, 0,	0, 0)
    #2 RN 69
    sixty_candidate = factory.construct_candidate(60, "DULAC", "Michel", "M", datetime.datetime(1942,9,26),	15,	"Commerçant et assimilé", False, 690, 9271,	9.6, 20.07,	0,	0,	0)
    sixty_one_candidate = factory.construct_candidate(61, "PECHEREAU", "Alain",	"M", datetime.datetime(1955,8,30), 15, "Ancien cadre", False, 691, 8764,	9.89, 21.66, 0,	0,	0)
    #2 NUP 11
    sixty_two_candidate = factory.construct_candidate(62, "THIVENT", "Viviane",	"F", datetime.datetime(1977,5,1), 3, "Professeur, profession scientifique",	False, 110,	9204, 9.94,	20.94,	0,	0,	0)
    sixty_three_candidate = factory.construct_candidate(63,	"ADDA--NETTER",	"Johanna",	"F", datetime.datetime(1996,2,21),	3,	"Ingénieur et cadre technique d'entreprise", False,	111, 12547,	13.97,	25.8, 19894, 27.651, 52.078)    
    #2 LR 11
    sixty_four_candidate = factory.construct_candidate(64,	"PEREZ", "Laurent",	"M", datetime.datetime(1965,6,16),	11,	"Chef d'entreprise de 10 salariés ou plus",	False,	110, 2501, 2.54,	5.17, 0, 0,	0)
    sixty_five_candidate = factory.construct_candidate(65, "ESTRADE", "Quentin", "M", datetime.datetime(1996,5,4),	11,	"Elève, étudiant",	False, 111, 3706, 4,	8.43, 0, 0,	0)
    #2 RN 11
    sixty_six_candidate = factory.construct_candidate(66, "FALCON", "Frédéric", "M", datetime.datetime(1985,11,21), 15, "Commerçant et assimilé", False, 110, 12365, 13.35, 28.13,	20719, 23.81, 52.949)
    sixty_seven_candidate = factory.construct_candidate(67,	"RANCOULE",	"Julien", "M",	datetime.datetime(1993,7,31), 15, "Profession libérale", False,	111, 13838,	15.41, 28.45, 22725, 24.796, 47.922)
    #2 ENS 11
    sixty_eight_candidate = factory.construct_candidate(68,	"PEREA", "Alain", "M", datetime.datetime(1971,6,5),	7,	"Cadre de la fonction publique", True,	110,	9666, 10.44, 21.99,	18724,	21.134,	47.051)
    sixty_nine_candidate = factory.construct_candidate(69,	"ROBERT", "Mireille", "F", datetime.datetime(1962,3,1),	7, "Professeur des écoles, instituteur et assimilé", True,	111, 10624,	11.83,	21.84,	0,	0,	0)
  
    candidates = [one_candidate, two_candidate, three_candidate, four_candidate, five_candidate, six_candidate, seven_candidate, eight_candidate,
                  nine_candidate, ten_candidate, eleven_candidate, twelve_candidate, thirteen_candidate, fourteen_candidate, fifteen_candidate, 
                  sixteen_candidate, seventeen_candidate, eighteen_candidate, nineteen_candidate, twenty_candidate, twenty_one_candidate, 
                  twenty_two_candidate, twenty_three_candidate, twenty_four_candidate, twenty_five_candidate, twenty_six_candidate, twenty_seven_candidate,
                  twenty_eight_candidate, twenty_nine_candidate, thirty_candidate, thirty_one_candidate, thirty_two_candidate, thirty_three_candidate, 
                  thirty_four_candidate, thirty_five_candidate, thirty_six_candidate, thirty_seven_candidate, thirty_eight_candidate, thirty_nine_candidate,
                  forty_candidate, forty_one_candidate, forty_two_candidate, forty_three_candidate, forty_four_candidate, forty_five_candidate,
                  forty_six_candidate, forty_seven_candidate, forty_eight_candidate, forty_nine_candidate, fifty_candidate, fifty_one_candidate, 
                  fifty_two_candidate, fifty_three_candidate, fifty_four_candidate, fifty_five_candidate, fifty_six_candidate, fifty_seven_candidate, 
                  fifty_eight_candidate, fifty_nine_candidate, sixty_candidate, sixty_one_candidate, sixty_two_candidate, sixty_three_candidate, 
                  sixty_four_candidate, sixty_five_candidate, sixty_six_candidate, sixty_seven_candidate, sixty_eight_candidate, sixty_nine_candidate]
    
    return candidates