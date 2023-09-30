import datetime
import unittest

from app.domain.business.candidate.candidate_business import CandidateBusiness
from app.domain.business.department_business import DepartmentBusiness
from app.domain.business.district_business import DistrictBusiness
from app.domain.business.party_business import PartyBusiness
from app.domain.repository.candidate_repository import CandidateRepository
from unittest.mock import patch
from tests.assert_test import AssertTest
from tests.faker.faker_department import getDepartments_by_ids
from tests.faker.faker_district import getDistricts_by_id
from tests.faker.faker_party import getParties_by_id
from tests.faker.faker_candidate import getCandidates_by_id

class CandidateBusinessTest(unittest.TestCase) :
    
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.assert_test = AssertTest(self)
    
    
    @patch.object(CandidateRepository, "get_candidates")
    @patch.object(PartyBusiness, "get_parties")
    def test_get_all_candidates(self, mock_candidate_repository, mock_party_business) : 
        mock_candidate_repository.get_candidates.return_value = getCandidates_by_id([1, 2, 3, 4, 5])
        mock_party_business.get_parties.return_value = getParties_by_id([1, 3, 7, 9])
        
        business = CandidateBusiness(mock_candidate_repository, mock_party_business, None, None)
        
        candidates = business.get_candidates("", "")
        
        self.assertEqual(5, len(candidates))
        
        first_candidate = candidates[0]
        candidate_check =[1, "VUITTON", "Brigitte", "F", datetime.datetime(1957,11,29), 1, "Divers extrême gauche", "Professeur, profession scientifique", False, 10, 779, 0.98, 1.93, 0, 0, 0]
        self.assert_test.assert_candidate_dto(candidate_check, first_candidate)
        
        second_candidate = candidates[1]
        candidate_check =[2, "RAVACLEY", "Stéphane", "M", datetime.datetime(1970,6,6), 3, "Nouvelle union populaire écologique et sociale", "Artisan", False, 330, 13112, 16.56, 32.51, 17594, 22.22, 47.75]
        self.assert_test.assert_candidate_dto(candidate_check, second_candidate)
        
        third_candidate = candidates[2]
        candidate_check =[3, "THOMASSIN", "Geoffrey", "M", datetime.datetime(1986,10,19), 9, "Divers", "Profession intermédiaire administrative et commerciale des entreprises", False, 331, 216, 0.27, 0.54, 0, 0, 0]
        self.assert_test.assert_candidate_dto(candidate_check, third_candidate)
            
        fourth_candidate = candidates[3]
        candidate_check =[4, "ALAUZET", "Eric", "M", datetime.datetime(1958,6,7), 7, "Ensemble ! (Majorité présidentielle)", "Profession libérale", True, 331, 12647, 15.98, 31.36, 19255, 24.32, 52.25]
        self.assert_test.assert_candidate_dto(candidate_check, fourth_candidate)
        
        fifth_candidate = candidates[4]
        candidate_check =[5, "HERITIER", "Louise", "F", datetime.datetime(1997,2,25), 3, "Nouvelle union populaire écologique et sociale", "Profession de l'information, des arts et des spectacles", False, 330, 89787, 23.2, 12.2, 9872, 21.32, 6.2]
        self.assert_test.assert_candidate_dto(candidate_check, fifth_candidate)
        
        
    @patch.object(CandidateRepository, "get_candidates")
    @patch.object(PartyBusiness, "get_parties")
    def test_get_specific_candidate(self, mock_party_business, mock_candidate_repository) : 
        mock_party_business.get_parties.return_value = getParties_by_id([1, 3, 7, 9])
        mock_candidate_repository.get_candidates.return_value = getCandidates_by_id([1, 2, 3, 4, 5])
        
        business = CandidateBusiness(mock_candidate_repository, mock_party_business, None, None)
        
        candidates = business.get_candidates("Stéphane", "RAVACLEY")
        
        self.assertEqual(1, len(candidates))
        
        first_candidate = candidates[0]
        candidate_check =[2, "RAVACLEY", "Stéphane", "M", datetime.datetime(1970,6,6), 3, "Nouvelle union populaire écologique et sociale", "Artisan", False, 330, 13112, 16.56, 32.51, 17594, 22.22, 47.75]
        self.assert_test.assert_candidate_dto(candidate_check, first_candidate)
        
        
    @patch.object(CandidateRepository, "get_candidates")
    @patch.object(PartyBusiness, "get_parties")
    def test_get_specific_candidate_managing_caps(self, mock_party_business, mock_candidate_repository) : 
        mock_party_business.get_parties.return_value = getParties_by_id([1, 3, 7, 9])
        mock_candidate_repository.get_candidates.return_value = getCandidates_by_id([1, 2, 3, 4, 5])
        
        business = CandidateBusiness(mock_candidate_repository, mock_party_business, None, None)
        
        candidates = business.get_candidates("stéphane", "ravacley")
        
        self.assertEqual(1, len(candidates))
        
        first_candidate = candidates[0]
        candidate_check =[2, "RAVACLEY", "Stéphane", "M", datetime.datetime(1970,6,6), 3, "Nouvelle union populaire écologique et sociale", "Artisan", False, 330, 13112, 16.56, 32.51, 17594, 22.22, 47.75]
        self.assert_test.assert_candidate_dto(candidate_check, first_candidate)
        
        
    @patch.object(CandidateRepository, "get_candidates")
    @patch.object(PartyBusiness, "get_parties")
    def test_get_specific_candidate_managing_accent(self, mock_party_business, mock_candidate_repository) : 
        mock_party_business.get_parties.return_value = getParties_by_id([1, 3, 7, 9])
        mock_candidate_repository.get_candidates.return_value = getCandidates_by_id([1, 2, 3, 4, 5])
        
        business = CandidateBusiness(mock_candidate_repository, mock_party_business, None, None)
        
        candidates = business.get_candidates("Stephane", "RAVACLEY")
        
        self.assertEqual(1, len(candidates))
        
        first_candidate = candidates[0]
        candidate_check =[2, "RAVACLEY", "Stéphane", "M", datetime.datetime(1970,6,6), 3, "Nouvelle union populaire écologique et sociale", "Artisan", False, 330, 13112, 16.56, 32.51, 17594, 22.22, 47.75]
        self.assert_test.assert_candidate_dto(candidate_check, first_candidate)
        
        
    @patch.object(CandidateRepository, "get_candidates")
    @patch.object(PartyBusiness, "get_parties")
    def test_get_candidates_from_specific_party(self, mock_party_business, mock_candidate_repository) :
        mock_party_business.get_party_by_short_name.return_value = getParties_by_id([3])[0]
        mock_candidate_repository.get_candidates.return_value = getCandidates_by_id([1, 2, 3, 4, 5])
        
        business = CandidateBusiness(mock_candidate_repository, mock_party_business, None, None)
        
        candidates = business.get_candidates_by_party("NUP")
        
        self.assertEqual(2, len(candidates))
        
        first_candidate = candidates[0]
        candidate_check =[2, "RAVACLEY", "Stéphane", "M", datetime.datetime(1970,6,6), 3, "Nouvelle union populaire écologique et sociale", "Artisan", False, 330, 13112, 16.56, 32.51, 17594, 22.22, 47.75]
        self.assert_test.assert_candidate_dto(candidate_check, first_candidate)
        
        second_candidate = candidates[1]
        candidate_check =[5, "HERITIER", "Louise", "F", datetime.datetime(1997,2,25), 3, "Nouvelle union populaire écologique et sociale", "Profession de l'information, des arts et des spectacles", False, 330, 89787, 23.2, 12.2, 9872, 21.32, 6.2]
        self.assert_test.assert_candidate_dto(candidate_check, second_candidate)
        
        
    @patch.object(CandidateRepository, "get_candidates")
    @patch.object(PartyBusiness, "get_parties")
    def test_get_candidates_from_unknown_party(self, mock_party_business, mock_candidate_repository) :
        mock_party_business.get_party_by_short_name.return_value = None
        mock_candidate_repository.get_candidates.return_value = getCandidates_by_id([1, 2, 3, 4, 5])
        
        business = CandidateBusiness(mock_candidate_repository, mock_party_business, None, None)
        
        candidates = business.get_candidates_by_party("XXX")
        
        self.assertEqual(None, candidates)
        
        
    @patch.object(CandidateRepository, "get_candidates")
    @patch.object(PartyBusiness, "get_parties")
    def test_get_all_candidates_by_district_id(self, mock_candidate_repository, mock_party_business) : 
        mock_candidate_repository.get_candidates.return_value = getCandidates_by_id([1, 2, 3, 4, 5])
        mock_party_business.get_parties.return_value = getParties_by_id([1, 3, 7, 9])
        
        business = CandidateBusiness(mock_candidate_repository, mock_party_business, None, None)
        
        candidates = business.get_candidates_by_district(330)
        
        self.assertEqual(2, len(candidates))

        first_candidate = candidates[0]
        candidate_check =[2, "RAVACLEY", "Stéphane", "M", datetime.datetime(1970,6,6), 3, "Nouvelle union populaire écologique et sociale", "Artisan", False, 330, 13112, 16.56, 32.51, 17594, 22.22, 47.75]
        self.assert_test.assert_candidate_dto(candidate_check, first_candidate)
        
        second_candidate = candidates[1]
        candidate_check =[5, "HERITIER", "Louise", "F", datetime.datetime(1997,2,25), 3, "Nouvelle union populaire écologique et sociale", "Profession de l'information, des arts et des spectacles", False, 330, 89787, 23.2, 12.2, 9872, 21.32, 6.2]
        self.assert_test.assert_candidate_dto(candidate_check, second_candidate)    
    
    
    @patch.object(CandidateRepository, "get_candidates")
    @patch.object(DepartmentBusiness, "get_department_by_name")
    @patch.object(DistrictBusiness, "get_districts_by_department_id")
    @patch.object(PartyBusiness, "get_parties")
    def test_get_all_candidates_from_department(self, mock_candidate_repository, mock_department_business, mock_district_business, mock_party_business):
        mock_candidate_repository.get_candidates.return_value = getCandidates_by_id([1, 2, 3, 4, 5])
        mock_department_business.get_department_by_name.return_value = getDepartments_by_ids([33])[0]
        mock_district_business.get_districts_by_department_id.return_value = getDistricts_by_id([330, 331])
        mock_party_business.get_parties.return_value = getParties_by_id([1, 3, 7, 9])
        
        business = CandidateBusiness(mock_candidate_repository, mock_party_business, mock_department_business, mock_district_business)
        
        candidates = business.get_candidates_by_departement("Gironde")
        
        self.assertEqual(4, len(candidates))
        
        first_candidate = candidates[0]
        candidate_check =[2, "RAVACLEY", "Stéphane", "M", datetime.datetime(1970,6,6), 3, "Nouvelle union populaire écologique et sociale", "Artisan", False, 330, 13112, 16.56, 32.51, 17594, 22.22, 47.75]
        self.assert_test.assert_candidate_dto(candidate_check, first_candidate)
        
        second_candidate = candidates[1]
        candidate_check =[3, "THOMASSIN", "Geoffrey", "M", datetime.datetime(1986,10,19), 9, "Divers", "Profession intermédiaire administrative et commerciale des entreprises", False, 331, 216, 0.27, 0.54, 0, 0, 0]
        self.assert_test.assert_candidate_dto(candidate_check, second_candidate)
            
        third_candidate = candidates[2]
        candidate_check =[4, "ALAUZET", "Eric", "M", datetime.datetime(1958,6,7), 7, "Ensemble ! (Majorité présidentielle)", "Profession libérale", True, 331, 12647, 15.98, 31.36, 19255, 24.32, 52.25]
        self.assert_test.assert_candidate_dto(candidate_check, third_candidate)
        
        fourth_candidate = candidates[3]
        candidate_check =[5, "HERITIER", "Louise", "F", datetime.datetime(1997,2,25), 3, "Nouvelle union populaire écologique et sociale", "Profession de l'information, des arts et des spectacles", False, 330, 89787, 23.2, 12.2, 9872, 21.32, 6.2]
        self.assert_test.assert_candidate_dto(candidate_check, fourth_candidate)
        
    
    @patch.object(CandidateRepository, "get_candidates")
    @patch.object(DepartmentBusiness, "get_department_by_name")
    @patch.object(DistrictBusiness, "get_districts_by_department_id")
    @patch.object(PartyBusiness, "get_parties")
    def test_get_all_candidates_from_unknown_department(self, mock_candidate_repository, mock_department_business, mock_district_business, mock_party_business):
        mock_candidate_repository.get_candidates.return_value = getCandidates_by_id([1, 2, 3, 4, 5])
        mock_department_business.get_department_by_name.return_value = None
        mock_district_business.get_districts_by_department_id.return_value = getDistricts_by_id([6, 7])
        mock_party_business.get_parties.return_value = getParties_by_id([1, 3, 7, 9])
        
        business = CandidateBusiness(mock_candidate_repository, mock_party_business, mock_department_business, mock_district_business)
        
        candidates = business.get_candidates_by_departement("azf")
        
        self.assertEqual(None, candidates)
        
        
    @patch.object(CandidateRepository, "get_candidates")
    @patch.object(PartyBusiness, "get_parties")
    def test_get_all_candidates_from_district(self, mock_candidate_repository, mock_party_business):
        mock_candidate_repository.get_candidates.return_value = getCandidates_by_id([1, 2, 3, 4, 5])
        mock_party_business.get_parties.return_value = getParties_by_id([1, 3, 7, 9])
        
        business = CandidateBusiness(mock_candidate_repository, mock_party_business, None, None)
        
        candidates = business.get_candidates_by_district(331)
        
        self.assertEqual(2, len(candidates))
        
        first_candidate = candidates[0]
        candidate_check =[3, "THOMASSIN", "Geoffrey", "M", datetime.datetime(1986,10,19), 9, "Divers", "Profession intermédiaire administrative et commerciale des entreprises", False, 331, 216, 0.27, 0.54, 0, 0, 0]
        self.assert_test.assert_candidate_dto(candidate_check, first_candidate)
            
        second_candidate = candidates[1]
        candidate_check =[4, "ALAUZET", "Eric", "M", datetime.datetime(1958,6,7), 7, "Ensemble ! (Majorité présidentielle)", "Profession libérale", True, 331, 12647, 15.98, 31.36, 19255, 24.32, 52.25]
        self.assert_test.assert_candidate_dto(candidate_check, second_candidate)
        
        
    @patch.object(CandidateRepository, "get_candidates")
    @patch.object(PartyBusiness, "get_parties")
    def test_get_all_candidates_from_unknown_district(self, mock_candidate_repository, mock_party_business):
        mock_candidate_repository.get_candidates.return_value = []
        mock_party_business.get_parties.return_value = getParties_by_id([1, 3, 7, 9])
        
        business = CandidateBusiness(mock_candidate_repository, mock_party_business, None, None)
        
        candidates = business.get_candidates_by_district('7')
        
        self.assertEqual(None, candidates)
        
    
    #TODO factorize with sortered tests all tests below
    @patch.object(CandidateRepository, "get_candidates")
    @patch.object(PartyBusiness, "get_parties")
    def test_get_top_candidates_results_small_samples(self, mock_candidate_repository, mock_party_business):
        mock_candidate_repository.get_candidates.return_value = getCandidates_by_id([2, 8, 14, 26, 28])
        mock_party_business.get_parties.return_value = getParties_by_id([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
        
        business = CandidateBusiness(mock_candidate_repository, mock_party_business, None, None)
        
        candidates_results = business.get_top_candidates_results(3)
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
          
        
    @patch.object(CandidateRepository, "get_candidates")
    @patch.object(PartyBusiness, "get_parties")
    def test_get_top_candidates_results(self, mock_candidate_repository, mock_party_business):
        mock_candidate_repository.get_candidates.return_value = getCandidates_by_id([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 
                                                                22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35])
        mock_party_business.get_parties.return_value = getParties_by_id([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
        
        business = CandidateBusiness(mock_candidate_repository, mock_party_business, None, None)
        
        candidates_results = business.get_top_candidates_results(6)
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