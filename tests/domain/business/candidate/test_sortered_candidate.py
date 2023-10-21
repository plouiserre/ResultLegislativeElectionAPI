import unittest
import datetime

from app.domain.business.candidate.sortered_candidate import SorteredCandidate
from app.domain.business.department.sortered_department import SorteredDepartment
from tests.assert_test import AssertTest
from tests.faker.faker_candidate import getCandidates_by_id, getCandidates_by_partys_departments
from tests.faker.faker_department import getDepartments_by_ids
from tests.faker.faker_district import getDistricts_by_department_id
from tests.faker.faker_party import getParties_by_id


class SorteredCandidateTest(unittest.TestCase) : 
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.assert_test = AssertTest(self)
        
        
    def test_get_top_candidates_results_small_samples(self):
        candidates = getCandidates_by_id([2, 8, 14, 26, 28])
        parties = getParties_by_id([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
        
        business = SorteredCandidate(candidates, parties, None)
        
        candidates_results = business.sort_all_candidates(3)
        candidates_results_first_round = candidates_results["first_round"]
        candidates_results_second_round = candidates_results["second_round"]
        
        self.assertEqual(2, len(candidates_results))
        
        self.assertEqual(3, len(candidates_results_first_round))
        
        one_candidate = candidates_results_first_round[0]
        one_candidate_check = [14, "AUTAIN", "Clémentine", "F", datetime.datetime(1973,5,26), 3, "Nouvelle union populaire écologique et sociale", "Profession de l'information, des arts et des spectacles", True, "XXXX", 9400, 14.83, 46.15, 11296, 17.753,	100]
        self.assert_test.assert_candidate_dto(one_candidate_check, one_candidate)
        
        two_candidate = candidates_results_first_round[1]
        two_candidate_check = [28, "DIAZ", "Edwige", "F", datetime.datetime(1987, 10, 15), 15, "Rassemblement National", "Cadre administratif et commercial d'entreprise", False, "XXXX", 18662, 18.9, 39.42, 25092, 26.954, 59.467]
        self.assert_test.assert_candidate_dto(two_candidate_check, two_candidate)
        
        three_candidate = candidates_results_first_round[2]
        three_candidate_check = [26, "BOUDIÉ", "Florent", "M", datetime.datetime(1973, 9, 22), 7, "Ensemble ! (Majorité présidentielle)", "Cadre de la fonction publique", True, "XXXX", 13565, 16.29, 32.7, 19581, 24.502, 51.424]
        self.assert_test.assert_candidate_dto(three_candidate_check, three_candidate)
                
        self.assertEqual(3, len(candidates_results_second_round))
        
        one_candidate = candidates_results_second_round[0]
        one_candidate_check = [14, "AUTAIN", "Clémentine", "F", datetime.datetime(1973,5,26), 3, "Nouvelle union populaire écologique et sociale", "Profession de l'information, des arts et des spectacles", True, "XXXX", 9400, 14.83, 46.15, 11296, 17.753,	100]
        self.assert_test.assert_candidate_dto(one_candidate_check, one_candidate)
        
        two_candidate = candidates_results_second_round[1]
        two_candidate_check = [28, "DIAZ", "Edwige", "F", datetime.datetime(1987, 10, 15), 15, "Rassemblement National", "Cadre administratif et commercial d'entreprise", False, "XXXX", 18662, 18.9, 39.42, 25092, 26.954, 59.467]
        self.assert_test.assert_candidate_dto(two_candidate_check, two_candidate)
        
        three_candidate = candidates_results_second_round[2]
        three_candidate_check = [26, "BOUDIÉ", "Florent", "M", datetime.datetime(1973, 9, 22), 7, "Ensemble ! (Majorité présidentielle)", "Cadre de la fonction publique", True, "XXXX", 13565, 16.29, 32.7, 19581, 24.502, 51.424]
        self.assert_test.assert_candidate_dto(three_candidate_check, three_candidate)        
          
        
    def test_get_top_candidates_results(self):
        candidates = getCandidates_by_id([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 
                                                                22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35])
        parties= getParties_by_id([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
        
        business = SorteredCandidate(candidates, parties, None)
        
        candidates_results = business.sort_all_candidates(6)
        candidates_results_first_round = candidates_results["first_round"]
        candidates_results_second_round = candidates_results["second_round"]
        
        self.assertEqual(2, len(candidates_results))
        
        self.assertEqual(6, len(candidates_results_first_round))
        
        one_candidate = candidates_results_first_round[0]
        one_candidate_check = [14, "AUTAIN", "Clémentine", "F", datetime.datetime(1973,5,26), 3, "Nouvelle union populaire écologique et sociale", "Profession de l'information, des arts et des spectacles", True, "XXXX", 9400, 14.83, 46.15, 11296, 17.753,	100]
        self.assert_test.assert_candidate_dto(one_candidate_check, one_candidate)
        
        two_candidate = candidates_results_first_round[1]
        two_candidate_check = [31, "OZIOL", "Nathalie", "F", datetime.datetime(1990, 2, 18), 3, "Nouvelle union populaire écologique et sociale", "Professeur, profession scientifique", False, "XXXX", 11513, 17.6,	40.37, 17008, 25.99, 63.33]
        self.assert_test.assert_candidate_dto(two_candidate_check, two_candidate)
        
        three_candidate = candidates_results_first_round[2]
        three_candidate_check = [28, "DIAZ", "Edwige", "F", datetime.datetime(1987, 10, 15), 15, "Rassemblement National", "Cadre administratif et commercial d'entreprise", False, "XXXX", 18662, 18.9, 39.42, 25092, 26.954, 59.467]
        self.assert_test.assert_candidate_dto(three_candidate_check, three_candidate)
            
        four_candidate = candidates_results_first_round[3]
        four_candidate_check = [23, "BARTHÈS", "Christophe", "M", datetime.datetime(1966, 10, 12), 15, "Rassemblement National", "Agriculteur sur moyenne exploitation", False, "XXXX", 15871, 16.12, 32.8, 23914, 25.07, 50.815]
        self.assert_test.assert_candidate_dto(four_candidate_check, four_candidate)
        
        five_candidate = candidates_results_first_round[4]
        five_candidate_check = [26, "BOUDIÉ", "Florent", "M", datetime.datetime(1973, 9, 22), 7, "Ensemble ! (Majorité présidentielle)", "Cadre de la fonction publique", True, "XXXX", 13565, 16.29, 32.7, 19581, 24.502, 51.424]
        self.assert_test.assert_candidate_dto(five_candidate_check, five_candidate)
        
        six_candidate = candidates_results_first_round[5]
        six_candidate_check = [2, "RAVACLEY", "Stéphane", "M", datetime.datetime(1970,6,6), 3, "Nouvelle union populaire écologique et sociale", "Artisan", False, "XXXX", 13112, 16.56, 32.51, 17594, 22.22, 47.75]
        self.assert_test.assert_candidate_dto(six_candidate_check, six_candidate)
        
        self.assertEqual(6, len(candidates_results_second_round))
        
        one_candidate = candidates_results_second_round[0]
        one_candidate_check = [14, "AUTAIN", "Clémentine", "F", datetime.datetime(1973,5,26), 3, "Nouvelle union populaire écologique et sociale", "Profession de l'information, des arts et des spectacles", True, "XXXX", 9400, 14.83, 46.15, 11296, 17.753,	100]
        self.assert_test.assert_candidate_dto(one_candidate_check, one_candidate)
        
        two_candidate = candidates_results_second_round[1]
        two_candidate_check = [31, "OZIOL", "Nathalie", "F", datetime.datetime(1990, 2, 18), 3, "Nouvelle union populaire écologique et sociale", "Professeur, profession scientifique", False, "XXXX", 11513, 17.6,	40.37, 17008, 25.99, 63.33]
        self.assert_test.assert_candidate_dto(two_candidate_check, two_candidate)
        
        three_candidate = candidates_results_second_round[2]
        three_candidate_check = [18, "RAY", "Nicolas", "M", datetime.datetime(1981, 5, 14), 11, "Les Républicains", "Cadre de la fonction publique", False, "XXXX", 9594, 11.96, 24.22, 19296, 26.194, 63.272]
        self.assert_test.assert_candidate_dto(three_candidate_check, three_candidate)
        
        four_candidate = candidates_results_second_round[3]
        four_candidate_check = [28, "DIAZ", "Edwige", "F", datetime.datetime(1987, 10, 15), 15, "Rassemblement National", "Cadre administratif et commercial d'entreprise", False, "XXXX", 18662, 18.9, 39.42, 25092, 26.954, 59.467]
        self.assert_test.assert_candidate_dto(four_candidate_check, four_candidate)
        
        five_candidate = candidates_results_second_round[4]
        five_candidate_check = [33, "CRISTOL", "Laurence", "F", datetime.datetime(1967, 11, 8), 7, "Ensemble ! (Majorité présidentielle)",  "Professeur, profession scientifique", False, "XXXX",	12457, 13.5, 26.68, 22907, 25.764, 54.725]
        self.assert_test.assert_candidate_dto(five_candidate_check, five_candidate)
        
        six_candidate = candidates_results_second_round[5]
        six_candidate_check = [4, "ALAUZET", "Eric", "M", datetime.datetime(1958,6,7), 7, "Ensemble ! (Majorité présidentielle)", "Profession libérale", True, "XXXX", 12647, 15.98, 31.36, 19255, 24.32, 52.25]
        self.assert_test.assert_candidate_dto(six_candidate_check, six_candidate)        
        
        
    def test_get_candidates_by_party_and_departments(self) :
        candidates = getCandidates_by_partys_departments(["NUP", "LR"], [11, 33])        
        parties = getParties_by_id([3, 11])                
        departments = getDepartments_by_ids([11, 33])
        districts = getDistricts_by_department_id([11, 33])
        all_departments_by_districts = self.__get_datas_department_by_district_id(departments, districts)
        
        business = SorteredCandidate(candidates, parties, departments)
        
        candidates_ordered_by_party_department = business.get_candidates_by_party_and_departments(all_departments_by_districts)
        
        self.assertEqual(4, len(candidates_ordered_by_party_department))
        
        first_candidate = candidates_ordered_by_party_department["NUP"]["Gironde"][0]
        first_candidate_check = [2, "RAVACLEY", "Stéphane", "M", datetime.datetime(1970,6,6), 3, "Artisan", False, 330, 13112, 16.56, 32.51, 17594, 22.22, 47.75]
        self.assert_test.assert_candidate_dto(first_candidate_check, first_candidate)
        
        second_candidate = candidates_ordered_by_party_department["NUP"]["Gironde"][1]
        second_candidate_check = [5,"HERITIER", "Louise", "F", datetime.datetime(1997,2,25), 3, "Profession de l'information, des arts et des spectacles", False, 330, 89787, 23.2, 12.2, 9872, 21.32, 6.2]
        self.assert_test.assert_candidate_dto(second_candidate_check, second_candidate)
            
        third_candidate = candidates_ordered_by_party_department["NUP"]["Gironde"][2]
        third_candidate_check = [29, "FAURE", "Marylène", "F", datetime.datetime(1972, 2, 26), 3 , "Employé administratif d'entreprise", False, 331,	11269, 9.41, 18.84,	0, 0, 0]
        self.assert_test.assert_candidate_dto(third_candidate_check, third_candidate)
        
        fourth_candidate = candidates_ordered_by_party_department["LR"]["Gironde"][0]
        fourth_candidate_check = [18, "RAY", "Nicolas", "M", datetime.datetime(1981,5,14), 11, "Cadre de la fonction publique",	False, 330, 9594, 11.96, 24.22, 19296, 26.194, 63.272]
        self.assert_test.assert_candidate_dto(fourth_candidate_check, fourth_candidate)  
        
        fifth_candidate = candidates_ordered_by_party_department["LR"]["Gironde"][1]
        fifth_candidate_check = [45, "NJIKAM", "Pierre De Gaetan", "M", datetime.datetime(1966, 8, 7), 11, "Cadre administratif et commercial d'entreprise", False, 330, 4116, 3.95, 8.03, 0, 0, 0]
        self.assert_test.assert_candidate_dto(fifth_candidate, fifth_candidate_check)
        
        sixth_candidate = candidates_ordered_by_party_department["LR"]["Gironde"][2]
        sixth_candidate_check = [46, "MORIN", "Marc", "M", datetime.datetime(1985, 7, 31), 11, "Commerçant et assimilé", False, 331, 5964, 4.98, 9.97, 0, 0, 0]
        self.assert_test.assert_candidate_dto(sixth_candidate, sixth_candidate_check)
        
        seven_candidate = candidates_ordered_by_party_department["NUP"]["Aude"][0]
        seven_candidate_check = [27, "BOURGOIS", "Pascal", "M", datetime.datetime(1956, 7, 24), 3, "Cadre de la fonction publique", False, 111, 9705, 11.65,	23.4, 0, 0,	0]
        self.assert_test.assert_candidate_dto(seven_candidate, seven_candidate_check)
        
        eighth_candidate = candidates_ordered_by_party_department["NUP"]["Aude"][1]
        eighth_candidate_check = [62, "THIVENT", "Viviane",	"F", datetime.datetime(1977,5,1), 3, "Professeur, profession scientifique",	False, 110,	9204, 9.94,	20.94,	0,	0,	0]
        self.assert_test.assert_candidate_dto(eighth_candidate, eighth_candidate_check)
        
        nineth_candidate = candidates_ordered_by_party_department["NUP"]["Aude"][2]
        nineth_candidate_check = [63,	"ADDA--NETTER",	"Johanna",	"F", datetime.datetime(1996,2,21),	3,	"Ingénieur et cadre technique d'entreprise", False,	111, 12547,	13.97,	25.8, 19894, 27.651, 52.078]
        self.assert_test.assert_candidate_dto(nineth_candidate, nineth_candidate_check)
        
        tenth_candidate = candidates_ordered_by_party_department["LR"]["Aude"][0]
        tenth_candidate_check = [64, "PEREZ", "Laurent",	"M", datetime.datetime(1965,6,16),	11,	"Chef d'entreprise de 10 salariés ou plus",	False,	110, 2501, 2.54,	5.17, 0, 0,	0]
        self.assert_test.assert_candidate_dto(tenth_candidate, tenth_candidate_check)
        
        eleventh_candidate = candidates_ordered_by_party_department["LR"]["Aude"][1]
        eleventh_candidate_check = [65, "ESTRADE", "Quentin", "M", datetime.datetime(1996,5,4),	11,	"Elève, étudiant",	False, 111, 3706, 4,	8.43, 0, 0,	0]
        self.assert_test.assert_candidate_dto(eleventh_candidate, eleventh_candidate_check)
        
        
    def __get_datas_department_by_district_id(self, departments, districts) : 
        sortered = SorteredDepartment(departments, districts)
        all_departments_by_districts = sortered.departments_sortered_by_districts()
        return all_departments_by_districts