import datetime
import unittest

from app.domain.business.candidate_business import CandidateBusiness
from app.domain.business.department_business import DepartmentBusiness
from app.domain.business.district_business import DistrictBusiness
from app.domain.factory.factorycandidate import FactoryCandidate
from app.domain.factory.factorydepartment import FactoryDepartment
from app.domain.factory.factorydistrict import FactoryDistrict
from app.domain.factory.factoryparty import FactoryParty
from app.domain.business.party_business import PartyBusiness
from app.domain.repository.candidate_repository import CandidateRepository
from unittest.mock import patch
from tests.assert_test import AssertTest

class CandidateBusinessTest(unittest.TestCase) :
    
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.assert_test = AssertTest(self)
        
        
    def __get_candidates(self) : 
        candidates = []
        factory = FactoryCandidate()
        first_candidate = factory.construct_candidate(1, "VUITTON", "Brigitte", "F", datetime.datetime(1957,11,29), 1, "Professeur, profession scientifique", False, 1, 779, 0.98, 1.93, 0, 0, 0)
        second_candidate = factory.construct_candidate(2, "RAVACLEY", "Stéphane", "M", datetime.datetime(1970,6,6), 3, "Artisan", False, 66, 13112, 16.56, 32.51, 17594, 22.22, 47.75)
        third_candidate = factory.construct_candidate(3, "THOMASSIN", "Geoffrey", "M", datetime.datetime(1986,10,19),9, "Profession intermédiaire administrative et commerciale des entreprises", False, 122, 216, 0.27, 0.54, 0, 0, 0 )
        fourth_candidate = factory.construct_candidate(4, "ALAUZET", "Eric", "M", datetime.datetime(1958,6,7), 7, "Profession libérale", True, 122, 12647, 15.98, 31.36, 19255, 24.32, 52.25)
        fifth_candidate = factory.construct_candidate(5,"HERITIER", "Louise", "F", datetime.datetime(1997,2,25), 3, "Profession de l'information, des arts et des spectacles", False, 66, 89787, 23.2, 12.2, 9872, 21.32, 6.2 )
        candidates = [first_candidate, second_candidate, third_candidate, fourth_candidate, fifth_candidate]
        return candidates
    
    
    def __get_parties(self) :
        parties = []
        factory = FactoryParty()
        first_party = factory.construct_party(1, "Divers extrême gauche", "DXG")
        second_party = factory.construct_party(3, "Nouvelle union populaire écologique et sociale", "NUP")
        third_party = factory.construct_party(7, "Ensemble ! (Majorité présidentielle)", "ENS")
        fourth_party = factory.construct_party(9, "Divers", "DIV")
        parties = [first_party, second_party, third_party, fourth_party]
        return parties
    
    
    @patch.object(CandidateRepository, "get_candidates")
    @patch.object(PartyBusiness, "get_parties")
    def test_get_all_candidates(self, mock_candidate_repository, mock_party_business) : 
        mock_candidate_repository.get_candidates.return_value = self.__get_candidates()
        mock_party_business.get_parties.return_value = self.__get_parties()
        
        business = CandidateBusiness(mock_candidate_repository, mock_party_business, None, None)
        
        candidates = business.get_candidates("", "")
        
        self.assertEqual(5, len(candidates))
        
        first_candidate = candidates[0]
        candidate_check =[1, "VUITTON", "Brigitte", "F", datetime.datetime(1957,11,29), 1, "Divers extrême gauche", "Professeur, profession scientifique", False, 1, 779, 0.98, 1.93, 0, 0, 0]
        self.assert_test.assert_candidate_dto(candidate_check, first_candidate)
        
        second_candidate = candidates[1]
        candidate_check =[2, "RAVACLEY", "Stéphane", "M", datetime.datetime(1970,6,6), 3, "Nouvelle union populaire écologique et sociale", "Artisan", False, 66, 13112, 16.56, 32.51, 17594, 22.22, 47.75]
        self.assert_test.assert_candidate_dto(candidate_check, second_candidate)
        
        third_candidate = candidates[2]
        candidate_check =[3, "THOMASSIN", "Geoffrey", "M", datetime.datetime(1986,10,19), 9, "Divers", "Profession intermédiaire administrative et commerciale des entreprises", False, 122, 216, 0.27, 0.54, 0, 0, 0]
        self.assert_test.assert_candidate_dto(candidate_check, third_candidate)
            
        fourth_candidate = candidates[3]
        candidate_check =[4, "ALAUZET", "Eric", "M", datetime.datetime(1958,6,7), 7, "Ensemble ! (Majorité présidentielle)", "Profession libérale", True, 122, 12647, 15.98, 31.36, 19255, 24.32, 52.25]
        self.assert_test.assert_candidate_dto(candidate_check, fourth_candidate)
        
        fifth_candidate = candidates[4]
        candidate_check =[5, "HERITIER", "Louise", "F", datetime.datetime(1997,2,25), 3, "Nouvelle union populaire écologique et sociale", "Profession de l'information, des arts et des spectacles", False, 66, 89787, 23.2, 12.2, 9872, 21.32, 6.2]
        self.assert_test.assert_candidate_dto(candidate_check, fifth_candidate)
        
        
    @patch.object(CandidateRepository, "get_candidates")
    @patch.object(PartyBusiness, "get_parties")
    def test_get_specific_candidate(self, mock_party_business, mock_candidate_repository) : 
        mock_party_business.get_parties.return_value = self.__get_parties() 
        mock_candidate_repository.get_candidates.return_value = self.__get_candidates()
        
        business = CandidateBusiness(mock_candidate_repository, mock_party_business, None, None)
        
        candidates = business.get_candidates("Stéphane", "RAVACLEY")
        
        self.assertEqual(1, len(candidates))
        
        first_candidate = candidates[0]
        candidate_check =[2, "RAVACLEY", "Stéphane", "M", datetime.datetime(1970,6,6), 3, "Nouvelle union populaire écologique et sociale", "Artisan", False, 66, 13112, 16.56, 32.51, 17594, 22.22, 47.75]
        self.assert_test.assert_candidate_dto(candidate_check, first_candidate)
        
        
    @patch.object(CandidateRepository, "get_candidates")
    @patch.object(PartyBusiness, "get_parties")
    def test_get_specific_candidate_managing_caps(self, mock_party_business, mock_candidate_repository) : 
        mock_party_business.get_parties.return_value = self.__get_parties() 
        mock_candidate_repository.get_candidates.return_value = self.__get_candidates()
        
        business = CandidateBusiness(mock_candidate_repository, mock_party_business, None, None)
        
        candidates = business.get_candidates("stéphane", "ravacley")
        
        self.assertEqual(1, len(candidates))
        
        first_candidate = candidates[0]
        candidate_check =[2, "RAVACLEY", "Stéphane", "M", datetime.datetime(1970,6,6), 3, "Nouvelle union populaire écologique et sociale", "Artisan", False, 66, 13112, 16.56, 32.51, 17594, 22.22, 47.75]
        self.assert_test.assert_candidate_dto(candidate_check, first_candidate)
        
        
    @patch.object(CandidateRepository, "get_candidates")
    @patch.object(PartyBusiness, "get_parties")
    def test_get_specific_candidate_managing_accent(self, mock_party_business, mock_candidate_repository) : 
        mock_party_business.get_parties.return_value = self.__get_parties() 
        mock_candidate_repository.get_candidates.return_value = self.__get_candidates()
        
        business = CandidateBusiness(mock_candidate_repository, mock_party_business, None, None)
        
        candidates = business.get_candidates("Stephane", "RAVACLEY")
        
        self.assertEqual(1, len(candidates))
        
        first_candidate = candidates[0]
        candidate_check =[2, "RAVACLEY", "Stéphane", "M", datetime.datetime(1970,6,6), 3, "Nouvelle union populaire écologique et sociale", "Artisan", False, 66, 13112, 16.56, 32.51, 17594, 22.22, 47.75]
        self.assert_test.assert_candidate_dto(candidate_check, first_candidate)
        
        
    @patch.object(CandidateRepository, "get_candidates")
    @patch.object(PartyBusiness, "get_parties")
    def test_get_candidates_from_specific_party(self, mock_party_business, mock_candidate_repository) :
        factory = FactoryParty()
        mock_party_business.get_party_by_short_name.return_value = factory.construct_party(3, "Nouvelle union populaire écologique et sociale", "NUP")
        mock_candidate_repository.get_candidates.return_value = self.__get_candidates()
        
        business = CandidateBusiness(mock_candidate_repository, mock_party_business, None, None)
        
        candidates = business.get_candidates_by_party("NUP")
        
        self.assertEqual(2, len(candidates))
        
        first_candidate = candidates[0]
        candidate_check =[2, "RAVACLEY", "Stéphane", "M", datetime.datetime(1970,6,6), 3, "Nouvelle union populaire écologique et sociale", "Artisan", False, 66, 13112, 16.56, 32.51, 17594, 22.22, 47.75]
        self.assert_test.assert_candidate_dto(candidate_check, first_candidate)
        
        second_candidate = candidates[1]
        candidate_check =[5, "HERITIER", "Louise", "F", datetime.datetime(1997,2,25), 3, "Nouvelle union populaire écologique et sociale", "Profession de l'information, des arts et des spectacles", False, 66, 89787, 23.2, 12.2, 9872, 21.32, 6.2]
        self.assert_test.assert_candidate_dto(candidate_check, second_candidate)
        
        
    @patch.object(CandidateRepository, "get_candidates")
    @patch.object(PartyBusiness, "get_parties")
    def test_get_candidates_from_unknown_party(self, mock_party_business, mock_candidate_repository) :
        mock_party_business.get_party_by_short_name.return_value = None
        mock_candidate_repository.get_candidates.return_value = self.__get_candidates()
        
        business = CandidateBusiness(mock_candidate_repository, mock_party_business, None, None)
        
        candidates = business.get_candidates_by_party("XXX")
        
        self.assertEqual(None, candidates)
        
        
    @patch.object(CandidateRepository, "get_candidates")
    @patch.object(PartyBusiness, "get_parties")
    def test_get_all_candidates_by_district_id(self, mock_candidate_repository, mock_party_business) : 
        mock_candidate_repository.get_candidates.return_value = self.__get_candidates()
        mock_party_business.get_parties.return_value = self.__get_parties()
        
        business = CandidateBusiness(mock_candidate_repository, mock_party_business, None, None)
        
        candidates = business.get_candidates_by_district(66)
        
        self.assertEqual(2, len(candidates))

        first_candidate = candidates[0]
        candidate_check =[2, "RAVACLEY", "Stéphane", "M", datetime.datetime(1970,6,6), 3, "Nouvelle union populaire écologique et sociale", "Artisan", False, 66, 13112, 16.56, 32.51, 17594, 22.22, 47.75]
        self.assert_test.assert_candidate_dto(candidate_check, first_candidate)
        
        second_candidate = candidates[1]
        candidate_check =[5, "HERITIER", "Louise", "F", datetime.datetime(1997,2,25), 3, "Nouvelle union populaire écologique et sociale", "Profession de l'information, des arts et des spectacles", False, 66, 89787, 23.2, 12.2, 9872, 21.32, 6.2]
        self.assert_test.assert_candidate_dto(candidate_check, second_candidate)
        
        
    def __get_department_by_name(self) :
        factory = FactoryDepartment()
        department = factory.construct_department_from_bdd([33, "Gironde", 33])
        return department
    
    
    def __get_districts(self) :
        districts = []
        factory = FactoryDistrict()
        third_district = factory.construct_district_from_bdd([66, 3, "1 ère circonscription", 33])
        fourth_district = factory.construct_district_from_bdd([122, 3, "2 ème circonscription", 33])
        districts = [third_district, fourth_district]
        return districts
    
    
    @patch.object(CandidateRepository, "get_candidates")
    @patch.object(DepartmentBusiness, "get_department_by_name")
    @patch.object(DistrictBusiness, "get_districts_by_department_id")
    @patch.object(PartyBusiness, "get_parties")
    def test_get_all_candidates_from_department(self, mock_candidate_repository, mock_department_business, mock_district_business, mock_party_business):
        mock_candidate_repository.get_candidates.return_value = self.__get_candidates()
        mock_department_business.get_department_by_name.return_value = self.__get_department_by_name()
        mock_district_business.get_districts_by_department_id.return_value = self.__get_districts()
        mock_party_business.get_parties.return_value = self.__get_parties()
        
        business = CandidateBusiness(mock_candidate_repository, mock_party_business, mock_department_business, mock_district_business)
        
        candidates = business.get_candidates_by_departement("Gironde")
        
        self.assertEqual(4, len(candidates))
        
        first_candidate = candidates[0]
        candidate_check =[2, "RAVACLEY", "Stéphane", "M", datetime.datetime(1970,6,6), 3, "Nouvelle union populaire écologique et sociale", "Artisan", False, 66, 13112, 16.56, 32.51, 17594, 22.22, 47.75]
        self.assert_test.assert_candidate_dto(candidate_check, first_candidate)
        
        second_candidate = candidates[1]
        candidate_check =[3, "THOMASSIN", "Geoffrey", "M", datetime.datetime(1986,10,19), 9, "Divers", "Profession intermédiaire administrative et commerciale des entreprises", False, 122, 216, 0.27, 0.54, 0, 0, 0]
        self.assert_test.assert_candidate_dto(candidate_check, second_candidate)
            
        third_candidate = candidates[2]
        candidate_check =[4, "ALAUZET", "Eric", "M", datetime.datetime(1958,6,7), 7, "Ensemble ! (Majorité présidentielle)", "Profession libérale", True, 122, 12647, 15.98, 31.36, 19255, 24.32, 52.25]
        self.assert_test.assert_candidate_dto(candidate_check, third_candidate)
        
        fourth_candidate = candidates[3]
        candidate_check =[5, "HERITIER", "Louise", "F", datetime.datetime(1997,2,25), 3, "Nouvelle union populaire écologique et sociale", "Profession de l'information, des arts et des spectacles", False, 66, 89787, 23.2, 12.2, 9872, 21.32, 6.2]
        self.assert_test.assert_candidate_dto(candidate_check, fourth_candidate)
        
    
    @patch.object(CandidateRepository, "get_candidates")
    @patch.object(DepartmentBusiness, "get_department_by_name")
    @patch.object(DistrictBusiness, "get_districts_by_department_id")
    @patch.object(PartyBusiness, "get_parties")
    def test_get_all_candidates_from_unknown_department(self, mock_candidate_repository, mock_department_business, mock_district_business, mock_party_business):
        mock_candidate_repository.get_candidates.return_value = self.__get_candidates()
        mock_department_business.get_department_by_name.return_value = None
        mock_district_business.get_districts_by_department_id.return_value = self.__get_districts()
        mock_party_business.get_parties.return_value = self.__get_parties()
        
        business = CandidateBusiness(mock_candidate_repository, mock_party_business, mock_department_business, mock_district_business)
        
        candidates = business.get_candidates_by_departement("azf")
        
        self.assertEqual(None, candidates)
        
        
    @patch.object(CandidateRepository, "get_candidates")
    @patch.object(PartyBusiness, "get_parties")
    def test_get_all_candidates_from_district(self, mock_candidate_repository, mock_party_business):
        mock_candidate_repository.get_candidates.return_value = self.__get_candidates()
        mock_party_business.get_parties.return_value = self.__get_parties()
        
        business = CandidateBusiness(mock_candidate_repository, mock_party_business, None, None)
        
        candidates = business.get_candidates_by_district('122')
        
        self.assertEqual(2, len(candidates))
        
        first_candidate = candidates[0]
        candidate_check =[3, "THOMASSIN", "Geoffrey", "M", datetime.datetime(1986,10,19), 9, "Divers", "Profession intermédiaire administrative et commerciale des entreprises", False, 122, 216, 0.27, 0.54, 0, 0, 0]
        self.assert_test.assert_candidate_dto(candidate_check, first_candidate)
            
        second_candidate = candidates[1]
        candidate_check =[4, "ALAUZET", "Eric", "M", datetime.datetime(1958,6,7), 7, "Ensemble ! (Majorité présidentielle)", "Profession libérale", True, 122, 12647, 15.98, 31.36, 19255, 24.32, 52.25]
        self.assert_test.assert_candidate_dto(candidate_check, second_candidate)
        
        
    @patch.object(CandidateRepository, "get_candidates")
    @patch.object(PartyBusiness, "get_parties")
    def test_get_all_candidates_from_unknown_district(self, mock_candidate_repository, mock_party_business):
        mock_candidate_repository.get_candidates.return_value = []
        mock_party_business.get_parties.return_value = self.__get_parties()
        
        business = CandidateBusiness(mock_candidate_repository, mock_party_business, None, None)
        
        candidates = business.get_candidates_by_district('122')
        
        self.assertEqual(None, candidates)