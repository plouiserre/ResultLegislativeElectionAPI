import unittest
import datetime

from app.domain.business.party_business import PartyBusiness
from app.domain.repository.candidate_repository import CandidateRepository
from app.domain.repository.department_repository import DepartmentRepository
from app.domain.repository.district_repository import DistrictRepository
from app.domain.repository.party_repository import PartyRepository
from tests.assert_test import AssertTest
from tests.faker.faker_candidate import getCandidates_by_id, getCandidates_by_partys_departments
from tests.faker.faker_department import getDepartments_by_ids
from tests.faker.faker_district import getDistricts_by_department_id
from tests.faker.faker_party import getParties_by_id
from unittest.mock import patch

class PartyBusinessTest(unittest.TestCase) : 
    
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.assert_test = AssertTest(self)
        
        
    @patch.object(PartyRepository, "get_parties")
    def test_get_parties(self, mock_party_repository) : 
        mock_party_repository.get_parties.return_value = getParties_by_id([1, 3, 7, 9])
        
        business = PartyBusiness(mock_party_repository, None, None, None)
        parties = business.get_parties()
        
        self.assertEqual(4, len(parties))
        
        party_check = [1, "Divers extrême gauche", "DXG"]
        self.assert_test.assert_party_dto(party_check, parties[0])
        
        party_check = [3, "Nouvelle union populaire écologique et sociale", "NUP"]
        self.assert_test.assert_party_dto(party_check, parties[1])
        
        party_check = [7, "Ensemble ! (Majorité présidentielle)", "ENS"]
        self.assert_test.assert_party_dto(party_check, parties[2])
        
        party_check = [9, "Divers", "DIV"]
        self.assert_test.assert_party_dto(party_check, parties[3])
        
        
    @patch.object(PartyRepository, "get_parties")
    def test_get_parties_by_short_name(self, mock_party_repository) : 
        mock_party_repository.get_parties.return_value = getParties_by_id([1, 3, 7, 9])
        
        business = PartyBusiness(mock_party_repository, None, None, None)
        party = business.get_party_by_short_name("ENS")
        
        party_check = [7, "Ensemble ! (Majorité présidentielle)", "ENS"]
        self.assert_test.assert_party_dto(party_check, party) 
        
        
    @patch.object(CandidateRepository, "get_candidates")
    @patch.object(PartyBusiness, "get_parties")
    def test_get_each_top_3_candidates_for_each_party_all_rounds(self, mock_candidate_repository, mock_party_business) : 
        mock_candidate_repository.get_candidates.return_value = getCandidates_by_id([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
                                                                               22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41,
                                                                               42, 43, 44])
        mock_party_business.get_parties.return_value = getParties_by_id([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
        
        business = PartyBusiness(mock_party_business, mock_candidate_repository, None, None)
        
        top_candidates = business.get_top_candidates_for_each_party_all_rounds(3)
        
        self.assertEqual(16, len(top_candidates))
        
        self.__assert_first_party_top_candidates(top_candidates["DXG"])
        
        self.__assert_second_party_top_candidates(top_candidates["RDG"])
        
        self.__assert_third_party_top_candidates(top_candidates["NUP"])
        
        self.__assert_four_party_top_candidates(top_candidates["DVG"])
        
        self.__assert_five_party_top_candidates(top_candidates["ECO"])
        
        self.__assert_six_party_top_candidates(top_candidates["REG"])
        
        self.__assert_seven_party_top_candidates(top_candidates["ENS"])
        
        self.__assert_eight_party_top_candidates(top_candidates["DVC"])
        
        self.__assert_nine_party_top_candidates(top_candidates["DIV"])
        
        self.__assert_ten_party_top_candidates(top_candidates["UDI"])
        
        self.__assert_eleven_party_top_candidates(top_candidates["LR"])
        
        self.__assert_twelve_party_top_candidates(top_candidates["DVD"])
        
        self.__assert_thirteen_party_top_candidates(top_candidates["DSV"])
        
        self.__assert_fourteen_party_top_candidates(top_candidates["REC"])
        
        self.__assert_fifteen_party_top_candidates(top_candidates["RN"])
        
        self.__assert_sixteen_party_top_candidates(top_candidates["DXD"])     
        
                
    def __assert_first_party_top_candidates(self, first_top_candidates) : 
        top_candidates_first_party = first_top_candidates
        first_party_candidate_id_thirty_six = [36, "LAÏ-KANE-CHEONG", "Alexandre", "M", datetime.datetime(1988, 12,1), 1, "Divers extrême gauche", 
                                                "Professeur des écoles, instituteur et assimilé",	False, "XXXX", 3862, 4.71, 16.99, 11229, 13.845, 46.9]
        first_party_candidate_id_one = [1, "VUITTON", "Brigitte", "F", datetime.datetime(1957,11,29), 1, "Divers extrême gauche", "Professeur, profession scientifique", 
                                      False, "XXXX", 779, 0.98, 1.93, 0, 0, 0]
        
        self.assert_test.assert_candidate_dto(first_party_candidate_id_thirty_six, top_candidates_first_party["first_round"][0])
        self.assert_test.assert_candidate_dto(first_party_candidate_id_one, top_candidates_first_party["first_round"][1])
        
        self.assert_test.assert_candidate_dto(first_party_candidate_id_thirty_six, top_candidates_first_party["second_round"][0])
        self.assert_test.assert_candidate_dto(first_party_candidate_id_one, top_candidates_first_party["second_round"][1])
        
        
    def __assert_second_party_top_candidates(self, second_top_candidates) : 
        top_candidates_second_party = second_top_candidates
        second_party_candidate_id_thirty_seven_check = [37, "PINEL", "Sylvia", "F", datetime.date(1977,9,28), 2, "Parti radical de gauche", "Cadre de la fonction publique",  
                                                        True, "XXXX", 9892, 10.27, 20.19, 0, 0, 0]
        self.assert_test.assert_candidate_dto(second_party_candidate_id_thirty_seven_check, top_candidates_second_party["first_round"][0])
        self.assert_test.assert_candidate_dto(second_party_candidate_id_thirty_seven_check, top_candidates_second_party["second_round"][0])
        
        
    def __assert_third_party_top_candidates(self, third_top_candidates) : 
        top_candidates_three_party = third_top_candidates
        third_party_candidate_id_fourteen_check = [14, "AUTAIN", "Clémentine", "F", datetime.datetime(1973,5,26),	3, "Nouvelle union populaire écologique et sociale",
                                                   "Profession de l'information, des arts et des spectacles", True, 515, 9400, 14.83, 46.15, 11296, 17.753,	100]
        third_party_candidate_id_thirty_one_check = [31, "OZIOL", "Nathalie", "F", datetime.datetime(1990, 2, 18), 3, "Nouvelle union populaire écologique et sociale",
                                                     "Professeur, profession scientifique", False, "XXXX", 11513, 17.6,	40.37, 17008, 25.99, 63.33]
        third_party_candidate_id_two_check = [2, "RAVACLEY", "Stéphane", "M", datetime.datetime(1970,6,6), 3, "Nouvelle union populaire écologique et sociale",
                                              "Artisan", False, 330, 13112, 16.56, 32.51, 17594, 22.22, 47.75]
        third_party_candidate_id_twenty_five_check = [25, "COURRIÈRE CALMON", "Sophie", "F", datetime.datetime(1965, 2, 24), 3, "Nouvelle union populaire écologique et sociale",
                                                      "Professeur, profession scientifique", False, "XXXX", 13620, 13.83, 28.15,	20733, 24.87, 49.185]
        self.assert_test.assert_candidate_dto(third_party_candidate_id_fourteen_check, top_candidates_three_party["first_round"][0])
        self.assert_test.assert_candidate_dto(third_party_candidate_id_thirty_one_check, top_candidates_three_party["first_round"][1])
        self.assert_test.assert_candidate_dto(third_party_candidate_id_two_check, top_candidates_three_party["first_round"][2])
        
        self.assert_test.assert_candidate_dto(third_party_candidate_id_fourteen_check, top_candidates_three_party["second_round"][0])
        self.assert_test.assert_candidate_dto(third_party_candidate_id_thirty_one_check, top_candidates_three_party["second_round"][1])
        self.assert_test.assert_candidate_dto(third_party_candidate_id_twenty_five_check, top_candidates_three_party["second_round"][2])
        
        
    def __assert_four_party_top_candidates(self, four_top_candidates) : 
        top_candidates_four_party = four_top_candidates
        four_party_candidate_id_thirty_eight_check = [38, "HABIB", "David", "M",	datetime.datetime(1961,3,16), 4, "Divers gauche",
                                                      "Cadre administratif et commercial d'entreprise",	True, "XXXX", 16345, 19.44, 36.61, 26414, 35.939, 70.602]
        four_party_candidate_id_thirty_five_check = [35, "SAUREL", "Philippe", "M", datetime.datetime(1957, 12, 17), 4, "Divers gauche",
                                                     "Profession intermédiaire de la santé et du travail social",	False, "XXXX", 2070, 2.24, 4.43, 0, 0, 0]
        self.assert_test.assert_candidate_dto(four_party_candidate_id_thirty_eight_check, top_candidates_four_party["first_round"][0])
        self.assert_test.assert_candidate_dto(four_party_candidate_id_thirty_five_check, top_candidates_four_party["first_round"][1])
        
        self.assert_test.assert_candidate_dto(four_party_candidate_id_thirty_eight_check, top_candidates_four_party["second_round"][0])
        self.assert_test.assert_candidate_dto(four_party_candidate_id_thirty_five_check, top_candidates_four_party["second_round"][1])
        
        
    def __assert_five_party_top_candidates(self, five_top_candidates) :
        top_candidates_five_party = five_top_candidates
        five_party_candidate_id_six_check = [6, "KASTLER", "Jean-Loup", "M", datetime.datetime(1982, 2, 12) , 5, "Ecologistes", 
                                             "Professeur, profession scientifique", False, "XXXX", 1763, 2.14, 4.93, 0, 0, 0]
        five_party_candidate_id_fifteen_check = [15, "VACCA", "Françoise", "F", datetime.datetime(1963, 4, 6), 5, "Ecologistes", "Cadre de la fonction publique", 
                                                 False, "XXXX", 892, 1.07,	2.31, 0, 0,	0]
        five_party_candidate_id_nine_check = [9, "MORVAN LEMBERT", "Marine", "F", datetime.datetime(1962, 3, 16), 5, "Ecologistes", "Profession libérale", 
                                              False, "XXXX", 528, 0.64, 1.48, 0, 0, 0]
        five_party_candidate_id_thirty_two_check = [32, "ZBAIRI", "Kadija", "F", datetime.datetime(1968, 1, 18), 5, "Ecologistes", "Profession libérale", 
                                                    False, "XXXX", 130, 0.2, 0.46, 0, 0, 0]
        self.assert_test.assert_candidate_dto(five_party_candidate_id_six_check, top_candidates_five_party["first_round"][0])
        self.assert_test.assert_candidate_dto(five_party_candidate_id_fifteen_check, top_candidates_five_party["first_round"][1])
        self.assert_test.assert_candidate_dto(five_party_candidate_id_nine_check, top_candidates_five_party["first_round"][2])        
        
        self.assert_test.assert_candidate_dto(five_party_candidate_id_nine_check, top_candidates_five_party["second_round"][0])
        self.assert_test.assert_candidate_dto(five_party_candidate_id_thirty_two_check, top_candidates_five_party["second_round"][1])
        self.assert_test.assert_candidate_dto(five_party_candidate_id_fifteen_check, top_candidates_five_party["second_round"][2])
        
        
    def __assert_six_party_top_candidates(self, six_top_candidates) : 
        top_candidates_six_party = six_top_candidates
        six_party_candidate_id_thirty_nine_check = [39,	"MOLAC", "Paul", "M", datetime.datetime(1962,5,21),	6,	"Régionaliste", 
                                                    "Professeur, profession scientifique",	True, "XXXX",	21900,	19.6, 37.65, 37678,	35.727,	75.423]
        six_party_candidate_id_twenty_check = [20, "CHATEL", "Philippe", "M", datetime.datetime(1968, 4, 9), 6, "Régionaliste", 
                                               "Cadre administratif et commercial d'entreprise", False, "XXXX", 585, 0.72, 1.47, 0, 0, 0]
        self.assert_test.assert_candidate_dto(six_party_candidate_id_thirty_nine_check, top_candidates_six_party["first_round"][0])
        self.assert_test.assert_candidate_dto(six_party_candidate_id_twenty_check, top_candidates_six_party["first_round"][1])
        
        self.assert_test.assert_candidate_dto(six_party_candidate_id_thirty_nine_check, top_candidates_six_party["second_round"][0])
        self.assert_test.assert_candidate_dto(six_party_candidate_id_twenty_check, top_candidates_six_party["second_round"][1])
        
    
    def __assert_seven_party_top_candidates(self, seven_top_candidates) : 
        top_candidates_seven_party = seven_top_candidates
        seven_party_candidate_id_four_check = [4, "ALAUZET", "Eric", "M", datetime.datetime(1958,6,7), 7, "Ensemble ! (Majorité présidentielle)", 
                                               "Profession libérale", True, 331, 12647, 15.98, 31.36, 19255, 24.32, 52.25]
        seven_party_candidate_id_thirty_three_check = [33, "CRISTOL", "Laurence", "F", datetime.datetime(1967, 11, 8), 7, "Ensemble ! (Majorité présidentielle)", 
                                                       "Professeur, profession scientifique", False, "XXXX", 12457, 13.5, 26.68, 22907, 25.764, 54.725]
        seven_party_candidate_id_twenty_six_check = [26, "BOUDIÉ", "Florent", "M", datetime.datetime(1973, 9, 22), 7, "Ensemble ! (Majorité présidentielle)", 
                                                     "Cadre de la fonction publique", True, "XXXX", 13565, 16.29, 32.7, 19581, 24.502, 51.424]
        self.assert_test.assert_candidate_dto(seven_party_candidate_id_twenty_six_check, top_candidates_seven_party["first_round"][0])
        self.assert_test.assert_candidate_dto(seven_party_candidate_id_four_check, top_candidates_seven_party["first_round"][1])
        self.assert_test.assert_candidate_dto(seven_party_candidate_id_thirty_three_check, top_candidates_seven_party["first_round"][2])
        
        self.assert_test.assert_candidate_dto(seven_party_candidate_id_thirty_three_check, top_candidates_seven_party["second_round"][0])
        self.assert_test.assert_candidate_dto(seven_party_candidate_id_four_check, top_candidates_seven_party["second_round"][1])
        self.assert_test.assert_candidate_dto(seven_party_candidate_id_twenty_six_check, top_candidates_seven_party["second_round"][2])
        
        
    def __assert_eight_party_top_candidates(self, eight_top_candidates) : 
        top_candidates_eight_party = eight_top_candidates
        eight_party_candidate_id_forty_check = [40, "SEO", "Mikaele",	"M", datetime.datetime(1971,12,27),	8,	"Divers Centre", 
                                                "Profession intermédiaire administrative de la fonction publique", False,  "XXXX", 1622, 16.91,	
                                                21.8, 3717, 38.8, 50.11]
        self.assert_test.assert_candidate_dto(eight_party_candidate_id_forty_check, top_candidates_eight_party["first_round"][0])
        
        self.assert_test.assert_candidate_dto(eight_party_candidate_id_forty_check, top_candidates_eight_party["second_round"][0])
        
        
    def __assert_nine_party_top_candidates(self, nine_top_candidates) : 
        top_candidates_nine_party = nine_top_candidates
        nine_party_candidate_id_three_check = [3, "THOMASSIN", "Geoffrey", "M", datetime.datetime(1986,10,19),9, "Divers", 
                                               "Profession intermédiaire administrative et commerciale des entreprises",  False, 331, 216, 0.27, 0.54, 0, 0, 0 ]
        nine_party_candidate_id_twenty_two_check = [22, "SIKORA", "Juliette", "F", datetime.datetime(1960, 5, 17), 9, "Divers", 
                                                    "Ouvrier qualifié de type industriel", False, "XXXX", 0, 0, 0, 0, 0, 0]
        
        self.assert_test.assert_candidate_dto(nine_party_candidate_id_three_check, top_candidates_nine_party["first_round"][0])
        self.assert_test.assert_candidate_dto(nine_party_candidate_id_twenty_two_check, top_candidates_nine_party["first_round"][1])
        
        self.assert_test.assert_candidate_dto(nine_party_candidate_id_three_check, top_candidates_nine_party["second_round"][0])
        self.assert_test.assert_candidate_dto(nine_party_candidate_id_twenty_two_check, top_candidates_nine_party["second_round"][1])
        
        
    def __assert_ten_party_top_candidates(self, ten_top_candidates) :
        top_candidates_ten_party = ten_top_candidates
        ten_party_candidate_id_forty_one_check = [41, "LAGARDE", "Jean-Christophe",	"M", datetime.datetime(1967,10,24),	10,	"Union des Démocrates et des Indépendants",
                                                  "Cadre de la fonction publique", True, "XXXX", 7745, 11.87, 33.41, 11395, 16.893, 44.413]
        
        self.assert_test.assert_candidate_dto(ten_party_candidate_id_forty_one_check, top_candidates_ten_party["first_round"][0])
        
        self.assert_test.assert_candidate_dto(ten_party_candidate_id_forty_one_check, top_candidates_ten_party["second_round"][0])
        
        
    def __assert_eleven_party_top_candidates(self, eleven_top_candidates) :
        top_candidates_eleven_party = eleven_top_candidates
        eleven_party_candidate_id_eighteen_check = [18, "RAY", "Nicolas", "M", datetime.datetime(1981,5,14), 11, "Les Républicains", "Cadre de la fonction publique",
                                                    False, "XXXX", 9594, 11.96,	 24.22, 19296, 26.194, 63.272]        
        eleven_party_candidate_id_thirteen_check = [13, "BOBIN", "David", "M", datetime.datetime(1984,8, 24), 11, "Les Républicains",
                                                    "Personne diverse sans activité professionnelle de moins de 60 ans (sauf retraité)",  False, "XXXX", 4300, 
                                                    5.46, 12.83, 0,	0, 0]
        eleven_party_candidate_id_eleven_check = [11, "MOUGENOT", "Paul", "M", datetime.datetime(1988, 10, 13), 11, "Les Républicains", 
                                                  "Agriculteur sur moyenne exploitation", False, "XXXX", 3853, 5.32, 11.35,	0, 0, 0]
        eleven_party_candidate_id_thirty_four_check = [34, "BERTHET", "Alain", "M", datetime.datetime(1959, 8, 21), 11, "Les Républicains", "Profession libérale",	
                                                    False,	"XXXX", 2603, 2.82, 5.57, 0, 0, 0]
    
        
        self.assert_test.assert_candidate_dto(eleven_party_candidate_id_eighteen_check, top_candidates_eleven_party["first_round"][0])
        self.assert_test.assert_candidate_dto(eleven_party_candidate_id_thirteen_check, top_candidates_eleven_party["first_round"][1])
        self.assert_test.assert_candidate_dto(eleven_party_candidate_id_eleven_check, top_candidates_eleven_party["first_round"][2])        
        
        self.assert_test.assert_candidate_dto(eleven_party_candidate_id_eighteen_check, top_candidates_eleven_party["second_round"][0])
        self.assert_test.assert_candidate_dto(eleven_party_candidate_id_thirteen_check, top_candidates_eleven_party["second_round"][1])
        self.assert_test.assert_candidate_dto(eleven_party_candidate_id_thirty_four_check, top_candidates_eleven_party["second_round"][2])
        
        
    def __assert_twelve_party_top_candidates(self, twelve_top_candidates) :
        top_candidates_twelve_party = twelve_top_candidates
        twelve_party_candidate_id_two_check = [42, "NAEGELEN", "Christophe",	"M", datetime.datetime(1983,12,30),	12,	"Divers droite",
                                               "Chef d'entreprise de 10 salariés ou plus",	True, "XXXX", 15136, 23.67,	47.21, 21035, 33.633, 73.408]
        twelve_party_candidate_id_eight_check = [8 , "PARIS", "Stéphanie", "F", datetime.datetime(1975, 8, 15), 12, "Divers droite", 
                                                 "Professeur des écoles, instituteur et assimilé", False, "XXXX", 931, 1.2, 2.58, 0, 0, 0]
        self.assert_test.assert_candidate_dto(twelve_party_candidate_id_two_check, top_candidates_twelve_party["first_round"][0])
        self.assert_test.assert_candidate_dto(twelve_party_candidate_id_eight_check, top_candidates_twelve_party["first_round"][1])
        
        self.assert_test.assert_candidate_dto(twelve_party_candidate_id_two_check, top_candidates_twelve_party["second_round"][0])
        self.assert_test.assert_candidate_dto(twelve_party_candidate_id_eight_check, top_candidates_twelve_party["second_round"][1])
        
        
    def __assert_thirteen_party_top_candidates(self, thirteen_top_candidates) : 
        top_candidates_thirteen_party = thirteen_top_candidates
        thirteen_party_candidate_id_thirty_check = [30, "RIVAULT", "Lydie", "F", datetime.datetime(1964, 3, 6), 13, "Droite souverainiste", 
                                                    "Ancienne profession intermédiaire", False, "XXXX", 789, 0.66, 1.32, 0,	0,	0]
        thirteen_party_candidate_id_twenty_one_check = [21, "BIASOLI", "Gilbert", "M", datetime.datetime(1951, 12, 26), 13, "Droite souverainiste",
                                                        "Ingénieur et cadre technique d'entreprise", False, "XXXX",	623, 0.63, 1.29, 0,	0, 0]
        thirteen_party_candidate_id_sixteen_check = [16, "AFFRAIX", "Christophe", "M", datetime.datetime(1983, 8, 2), 13, "Droite souverainiste",
                                                     "Contremaître, agent de maîtrise", False, "XXXX", 440, 0.54, 1.1, 0, 0, 0]
        
        self.assert_test.assert_candidate_dto(thirteen_party_candidate_id_thirty_check, top_candidates_thirteen_party["first_round"][0])
        self.assert_test.assert_candidate_dto(thirteen_party_candidate_id_twenty_one_check, top_candidates_thirteen_party["first_round"][1])
        self.assert_test.assert_candidate_dto(thirteen_party_candidate_id_sixteen_check, top_candidates_thirteen_party["first_round"][2])
        
        self.assert_test.assert_candidate_dto(thirteen_party_candidate_id_sixteen_check, top_candidates_thirteen_party["second_round"][0])
        self.assert_test.assert_candidate_dto(thirteen_party_candidate_id_thirty_check, top_candidates_thirteen_party["second_round"][1])
        self.assert_test.assert_candidate_dto(thirteen_party_candidate_id_twenty_one_check, top_candidates_thirteen_party["second_round"][2])
        
        
    def __assert_fourteen_party_top_candidates(self, fourteen_top_candidates) : 
        top_candidates_fourteen_party = fourteen_top_candidates
        fourteen_party_candidate_id_forty_three_check = [43, "TROCHU", "Laurence", "F", datetime.datetime(1973,7,4), 14, "Reconquête !", 
                                                         "Personne diverse sans activité professionnelle de moins de 60 ans (sauf retraité)", False, "XXXX", 5730, 6.88, 
                                                         12.47,	0, 0, 0]
        fourteen_party_candidate_id_seventeen_check = [17, "DE NICOLAY", "Axelle", "F", datetime.datetime(1988, 3, 26), 14, "Reconquête !",
                                                        "Cadre administratif et commercial d'entreprise", False, "XXXX", 1557, 1.92, 3.9, 0, 0, 0]
        self.assert_test.assert_candidate_dto(fourteen_party_candidate_id_forty_three_check, top_candidates_fourteen_party["first_round"][0])
        self.assert_test.assert_candidate_dto(fourteen_party_candidate_id_seventeen_check, top_candidates_fourteen_party["first_round"][1])
        
        self.assert_test.assert_candidate_dto(fourteen_party_candidate_id_seventeen_check, top_candidates_fourteen_party["second_round"][0])
        self.assert_test.assert_candidate_dto(fourteen_party_candidate_id_forty_three_check, top_candidates_fourteen_party["second_round"][1])
        
        
    def __assert_fifteen_party_top_candidates(self, fifteen_top_candidates) : 
        top_candidates_fifteen_party = fifteen_top_candidates
        fifteen_party_candidate_id_twenty_eight_check = [28, "DIAZ", "Edwige", "F", datetime.datetime(1987, 10, 15), 15, "Rassemblement National", 
                                                         "Cadre administratif et commercial d'entreprise", False, "XXXX", 18662, 18.9, 39.42, 25092, 26.954, 59.467]
        fifteen_party_candidate_id_twenty_three_check = [23, "BARTHÈS", "Christophe", "M", datetime.datetime(1966, 10, 12), 15, "Rassemblement National", 
                                                         "Agriculteur sur moyenne exploitation", False, "XXXX", 15871, 16.12, 32.8, 23914, 25.07, 50.815]
        fifteen_party_candidate_id_ten_check = [10, "EYRAUD", "Olivier", "M", datetime.datetime(1955, 3, 8), 15, "Rassemblement National", 
                                                "Ancien artisan, commerçant, chef d'entreprise", False, "XXXX",	11354,	11.36,	23.23,	0, 0, 0]
        self.assert_test.assert_candidate_dto(fifteen_party_candidate_id_twenty_eight_check, top_candidates_fifteen_party["first_round"][0])
        self.assert_test.assert_candidate_dto(fifteen_party_candidate_id_twenty_three_check, top_candidates_fifteen_party["first_round"][1])
        self.assert_test.assert_candidate_dto(fifteen_party_candidate_id_ten_check, top_candidates_fifteen_party["first_round"][2])
        
        self.assert_test.assert_candidate_dto(fifteen_party_candidate_id_twenty_eight_check, top_candidates_fifteen_party["second_round"][0])
        self.assert_test.assert_candidate_dto(fifteen_party_candidate_id_twenty_three_check, top_candidates_fifteen_party["second_round"][1])
        self.assert_test.assert_candidate_dto(fifteen_party_candidate_id_ten_check, top_candidates_fifteen_party["second_round"][2])
        
        
    def __assert_sixteen_party_top_candidates(self, sixteen_top_candidates) : 
        top_candidates_sixteen_party = sixteen_top_candidates
        sixteen_party_candidate_id_forty_four = [44, "DESSAUX", "Aurélien", "M", datetime.datetime(1991,12,19), 16, "Divers extrême droite",
                                                 "Profession intermédiaire administrative et commerciale des entreprises", False, "XXXX", 1184, 1.49, 2.83, 0,	0, 0]
        self.assert_test.assert_candidate_dto(sixteen_party_candidate_id_forty_four, top_candidates_sixteen_party["first_round"][0])
        
        self.assert_test.assert_candidate_dto(sixteen_party_candidate_id_forty_four, top_candidates_sixteen_party["second_round"][0]) 
        
        
    @patch.object(CandidateRepository, "get_candidates")
    @patch.object(PartyBusiness, "get_parties")
    @patch.object(DistrictRepository, "get_districts")
    @patch.object(DepartmentRepository, "get_departments")
    def test_get_top_departments_for_each_four_specifics_parties_all_rounds(self, mock_candidate_repository, mock_party_business, mock_district_repository, mock_department_repository) :
        mock_candidate_repository.get_candidates.return_value = getCandidates_by_partys_departments(["NUP", "LR", "ENS", "RN"], [11, 33, 34, 69])
        
        mock_party_business.get_parties.return_value = getParties_by_id([3, 7, 11, 15])        
        
        mock_department_repository.get_departments.return_value = getDepartments_by_ids([11, 33, 34, 69])
        
        mock_district_repository.get_districts.return_value = getDistricts_by_department_id([11, 33, 34, 69])
        
        business = PartyBusiness(mock_party_business, mock_candidate_repository, mock_district_repository, mock_department_repository)
        
        top_departments = business.get_top_departments_for_each_party_all_rounds()
        
        self.assertEqual(len(top_departments), 4)        
        
        nup_departments = top_departments["NUP"]
        self.__assert_third_party_top_department(nup_departments)
        
        ens_departments = top_departments["ENS"]
        self.__assert_seven_party_top_department(ens_departments)
        
        lr_departments = top_departments["LR"]
        self.__assert_eleven_party_top_department(lr_departments)
        
        rn_departments = top_departments["RN"]
        self.__assert_fifteen_party_top_department(rn_departments)
        
        
    def __assert_third_party_top_department(self, third_top_department) : 
        nup_departments_first_round = third_top_department["first_round"]
        self.assert_test.assert_department_result_dto([33, "Gironde", 33, 21.18], nup_departments_first_round[0]) 
        self.assert_test.assert_department_result_dto([11, "Aude", 11, 23.35], nup_departments_first_round[1]) 
        self.assert_test.assert_department_result_dto([34, "Herault", 34, 31.67], nup_departments_first_round[2]) 
        self.assert_test.assert_department_result_dto([69, "Rhône", 69, 35.55], nup_departments_first_round[3]) 
        
        nup_departments_second_round = third_top_department["second_round"]
        self.assert_test.assert_department_result_dto([11, "Aude", 11, 17.35], nup_departments_second_round[0])
        self.assert_test.assert_department_result_dto([33, "Gironde", 33, 17.91], nup_departments_second_round[1])
        self.assert_test.assert_department_result_dto([69, "Rhône", 69, 51.87], nup_departments_second_round[2])
        self.assert_test.assert_department_result_dto([34, "Herault", 34, 54.10], nup_departments_second_round[3])
        
        
    def __assert_seven_party_top_department(self, seven_top_department) : 
        ens_departments_first_round = seven_top_department["first_round"]
        self.assert_test.assert_department_result_dto([11, "Aude", 11, 20.06], ens_departments_first_round[0]) 
        self.assert_test.assert_department_result_dto([69, "Rhône", 69, 20.06], ens_departments_first_round[1]) 
        self.assert_test.assert_department_result_dto([34, "Herault", 34, 24.55], ens_departments_first_round[2]) 
        self.assert_test.assert_department_result_dto([33, "Gironde", 69, 35.55], ens_departments_first_round[3]) 
        
        ens_departments_second_round = seven_top_department["second_round"]
        self.assert_test.assert_department_result_dto([11, "Aude", 11, 15.68], ens_departments_second_round[0])
        self.assert_test.assert_department_result_dto([69, "Rhône", 69, 18.24], ens_departments_second_round[1])
        self.assert_test.assert_department_result_dto([34, "Herault", 34, 28.62], ens_departments_second_round[2])
        self.assert_test.assert_department_result_dto([33, "Gironde", 33, 46.80], ens_departments_second_round[3])
        
        
    def __assert_eleven_party_top_department(self, eleven_top_department) : 
        lr_departments_first_round = eleven_top_department["first_round"]
        self.assert_test.assert_department_result_dto([11, "Aude", 11, 6.8], lr_departments_first_round[0]) 
        self.assert_test.assert_department_result_dto([34, "Herault", 34, 6.90], lr_departments_first_round[1]) 
        self.assert_test.assert_department_result_dto([33, "Gironde", 33, 14.07], lr_departments_first_round[2]) 
        self.assert_test.assert_department_result_dto([69, "Rhône", 69, 17.07], lr_departments_first_round[3]) 
        
        lr_departments_second_round = eleven_top_department["second_round"]
        self.assert_test.assert_department_result_dto([11, "Aude", 11, 0], lr_departments_second_round[0])
        self.assert_test.assert_department_result_dto([34, "Herault", 34, 0], lr_departments_second_round[1])
        self.assert_test.assert_department_result_dto([69, "Rhône", 69, 16.271], lr_departments_second_round[2])
        self.assert_test.assert_department_result_dto([33, "Gironde", 33, 21.05], lr_departments_second_round[3])
        
        
    def __assert_fifteen_party_top_department(self, fifteen_top_department) : 
        rn_departments_first_round = fifteen_top_department["first_round"]
        self.assert_test.assert_department_result_dto([69, "Rhône", 69, 20.865], rn_departments_first_round[0]) 
        self.assert_test.assert_department_result_dto([11, "Aude", 11, 28.29], rn_departments_first_round[1]) 
        self.assert_test.assert_department_result_dto([34, "Herault", 34, 29.01], rn_departments_first_round[2]) 
        self.assert_test.assert_department_result_dto([33, "Gironde", 33, 32], rn_departments_first_round[3]) 
        
        rn_departments_second_round = fifteen_top_department["second_round"]
        self.assert_test.assert_department_result_dto([69, "Rhône", 69, 0], rn_departments_second_round[0])
        self.assert_test.assert_department_result_dto([34, "Herault", 34, 37.145], rn_departments_second_round[1])
        self.assert_test.assert_department_result_dto([11, "Aude", 11, 50.43], rn_departments_second_round[2])
        self.assert_test.assert_department_result_dto([33, "Gironde", 33, 56.03], rn_departments_second_round[3])