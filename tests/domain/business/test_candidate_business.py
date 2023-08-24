import datetime
import unittest

from app.domain.business.candidate_business import CandidateBusiness
from app.domain.business.department_business import DepartmentBusiness
from app.domain.business.district_business import DistrictBusiness
from app.domain.business.party_business import PartyBusiness
from app.domain.repository.candidate_repository import CandidateRepository
from unittest.mock import patch
from tests.assert_test import AssertTest
from tests.faker import getCandidates, getDepartments, getDistricts, getParties

class CandidateBusinessTest(unittest.TestCase) :
    
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.assert_test = AssertTest(self)
    
    
    @patch.object(CandidateRepository, "get_candidates")
    @patch.object(PartyBusiness, "get_parties")
    def test_get_all_candidates(self, mock_candidate_repository, mock_party_business) : 
        mock_candidate_repository.get_candidates.return_value = getCandidates([1, 2, 3, 4, 5])
        mock_party_business.get_parties.return_value = getParties([1, 3, 7, 9])
        
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
        mock_party_business.get_parties.return_value = getParties([1, 3, 7, 9])
        mock_candidate_repository.get_candidates.return_value = getCandidates([1, 2, 3, 4, 5])
        
        business = CandidateBusiness(mock_candidate_repository, mock_party_business, None, None)
        
        candidates = business.get_candidates("Stéphane", "RAVACLEY")
        
        self.assertEqual(1, len(candidates))
        
        first_candidate = candidates[0]
        candidate_check =[2, "RAVACLEY", "Stéphane", "M", datetime.datetime(1970,6,6), 3, "Nouvelle union populaire écologique et sociale", "Artisan", False, 330, 13112, 16.56, 32.51, 17594, 22.22, 47.75]
        self.assert_test.assert_candidate_dto(candidate_check, first_candidate)
        
        
    @patch.object(CandidateRepository, "get_candidates")
    @patch.object(PartyBusiness, "get_parties")
    def test_get_specific_candidate_managing_caps(self, mock_party_business, mock_candidate_repository) : 
        mock_party_business.get_parties.return_value = getParties([1, 3, 7, 9])
        mock_candidate_repository.get_candidates.return_value = getCandidates([1, 2, 3, 4, 5])
        
        business = CandidateBusiness(mock_candidate_repository, mock_party_business, None, None)
        
        candidates = business.get_candidates("stéphane", "ravacley")
        
        self.assertEqual(1, len(candidates))
        
        first_candidate = candidates[0]
        candidate_check =[2, "RAVACLEY", "Stéphane", "M", datetime.datetime(1970,6,6), 3, "Nouvelle union populaire écologique et sociale", "Artisan", False, 330, 13112, 16.56, 32.51, 17594, 22.22, 47.75]
        self.assert_test.assert_candidate_dto(candidate_check, first_candidate)
        
        
    @patch.object(CandidateRepository, "get_candidates")
    @patch.object(PartyBusiness, "get_parties")
    def test_get_specific_candidate_managing_accent(self, mock_party_business, mock_candidate_repository) : 
        mock_party_business.get_parties.return_value = getParties([1, 3, 7, 9])
        mock_candidate_repository.get_candidates.return_value = getCandidates([1, 2, 3, 4, 5])
        
        business = CandidateBusiness(mock_candidate_repository, mock_party_business, None, None)
        
        candidates = business.get_candidates("Stephane", "RAVACLEY")
        
        self.assertEqual(1, len(candidates))
        
        first_candidate = candidates[0]
        candidate_check =[2, "RAVACLEY", "Stéphane", "M", datetime.datetime(1970,6,6), 3, "Nouvelle union populaire écologique et sociale", "Artisan", False, 330, 13112, 16.56, 32.51, 17594, 22.22, 47.75]
        self.assert_test.assert_candidate_dto(candidate_check, first_candidate)
        
        
    @patch.object(CandidateRepository, "get_candidates")
    @patch.object(PartyBusiness, "get_parties")
    def test_get_candidates_from_specific_party(self, mock_party_business, mock_candidate_repository) :
        mock_party_business.get_party_by_short_name.return_value = getParties([3])[0]
        mock_candidate_repository.get_candidates.return_value = getCandidates([1, 2, 3, 4, 5])
        
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
        mock_candidate_repository.get_candidates.return_value = getCandidates([1, 2, 3, 4, 5])
        
        business = CandidateBusiness(mock_candidate_repository, mock_party_business, None, None)
        
        candidates = business.get_candidates_by_party("XXX")
        
        self.assertEqual(None, candidates)
        
        
    @patch.object(CandidateRepository, "get_candidates")
    @patch.object(PartyBusiness, "get_parties")
    def test_get_all_candidates_by_district_id(self, mock_candidate_repository, mock_party_business) : 
        mock_candidate_repository.get_candidates.return_value = getCandidates([1, 2, 3, 4, 5])
        mock_party_business.get_parties.return_value = getParties([1, 3, 7, 9])
        
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
        mock_candidate_repository.get_candidates.return_value = getCandidates([1, 2, 3, 4, 5])
        mock_department_business.get_department_by_name.return_value = getDepartments([33])[0]
        mock_district_business.get_districts_by_department_id.return_value = getDistricts([330, 331])
        mock_party_business.get_parties.return_value = getParties([1, 3, 7, 9])
        
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
        mock_candidate_repository.get_candidates.return_value = getCandidates([1, 2, 3, 4, 5])
        mock_department_business.get_department_by_name.return_value = None
        mock_district_business.get_districts_by_department_id.return_value = getDistricts([6, 7])
        mock_party_business.get_parties.return_value = getParties([1, 3, 7, 9])
        
        business = CandidateBusiness(mock_candidate_repository, mock_party_business, mock_department_business, mock_district_business)
        
        candidates = business.get_candidates_by_departement("azf")
        
        self.assertEqual(None, candidates)
        
        
    @patch.object(CandidateRepository, "get_candidates")
    @patch.object(PartyBusiness, "get_parties")
    def test_get_all_candidates_from_district(self, mock_candidate_repository, mock_party_business):
        mock_candidate_repository.get_candidates.return_value = getCandidates([1, 2, 3, 4, 5])
        mock_party_business.get_parties.return_value = getParties([1, 3, 7, 9])
        
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
        mock_party_business.get_parties.return_value = getParties([1, 3, 7, 9])
        
        business = CandidateBusiness(mock_candidate_repository, mock_party_business, None, None)
        
        candidates = business.get_candidates_by_district('7')
        
        self.assertEqual(None, candidates)