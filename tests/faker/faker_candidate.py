from app.domain.factory.factorycandidate import FactoryCandidate
from tests.faker.faker_department import getDepartments_by_names
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


def getCandidates_by_party(party_names) : 
    candidates_needed = []
    party_ids = getParties_id_by_name(party_names)        
    
    candidates = __create_candidates()
    
    for candidate in candidates : 
        for party_id in party_ids : 
            if candidate.party_id == party_id :
                candidates_needed.append(candidate)
                break
    
    return candidates_needed


def getCandidates_by_department(departments_name) :
    candidates_needed = []
    departments = getDepartments_by_names(departments_name)
    
    departments_id = []
    for department in departments : 
        departments_id.append(department.id)
        
    districts = getDistricts_by_department_id(departments_id)
    districts_id = []
    for district in districts : 
        districts_id.append(district.id)
    
    candidates = __create_candidates()
    
    for candidate in candidates : 
        for district_id in districts_id : 
            if candidate.district_id == district_id :
                candidates_needed.append(candidate)
                break
            
    return candidates_needed


def __create_candidates() :
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
    
    return candidates