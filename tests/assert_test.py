class AssertTest:
    def __init__(self, unit_test) -> None:
        self.unit_test = unit_test
    
    def assert_candidate_dto(self, candidate_check, candidate_dto) :
        if candidate_check[0] != "XXXX" :
            self.unit_test.assertEqual(candidate_check[0], candidate_dto.id)
            
        if candidate_check[1] != "XXXX" :        
            self.unit_test.assertEqual(candidate_check[1], candidate_dto.last_name)
        
        if candidate_check[2] != "XXXX" :        
            self.unit_test.assertEqual(candidate_check[2], candidate_dto.first_name)
        
        if candidate_check[3] != "XXXX" :        
            self.unit_test.assertEqual(candidate_check[3], candidate_dto.sexe)
        
        if candidate_check[4] != "XXXX" :        
            self.unit_test.assertTrue(candidate_check[4] == candidate_dto.birthdate)
        
        if candidate_check[5] != "XXXX" :        
            self.unit_test.assertEqual(candidate_check[5], candidate_dto.party_id)
        
        if candidate_check[6] != "XXXX" :        
            self.unit_test.assertEqual(candidate_check[6], candidate_dto.party_name)
        
        if candidate_check[7] != "XXXX" :        
            self.unit_test.assertEqual(candidate_check[7], candidate_dto.job)
        
        if candidate_check[8] != "XXXX" :        
            self.unit_test.assertEqual(candidate_check[8], candidate_dto.is_sorting)
        
        if candidate_check[9] != "XXXX" :        
            self.unit_test.assertEqual(candidate_check[9], candidate_dto.district_id)
        
        if candidate_check[10] != "XXXX" :        
            self.unit_test.assertEqual(candidate_check[10], candidate_dto.vote_first_round)
            
        if candidate_check[11] != "XXXX" :        
            self.unit_test.assertEqual(candidate_check[11], candidate_dto.rate_vote_registered_first_round)
        
        if candidate_check[12] != "XXXX" :
            self.unit_test.assertEqual(candidate_check[12], candidate_dto.rate_vote_expressed_first_round)
        
        if candidate_check[13] != "XXXX" :
            self.unit_test.assertEqual(candidate_check[13], candidate_dto.vote_second_round)
        
        if candidate_check[14] != "XXXX" :
            self.unit_test.assertEqual(candidate_check[14], candidate_dto.rate_vote_registered_second_round)
        
        if candidate_check[15] != "XXXX" :
            self.unit_test.assertEqual(candidate_check[15], candidate_dto.rate_vote_expressed_second_round)
        
        
    def assert_party_dto(self, party_check, party_dto) : 
        self.unit_test.assertEqual(party_check[0], party_dto.id)
        self.unit_test.assertEqual(party_check[1], party_dto.name)
        self.unit_test.assertEqual(party_check[2], party_dto.short_name)
        
    
    def assert_deputy_dto(self, deputy_check, deputy_dto) :
        self.unit_test.assertEqual(deputy_check[0], deputy_dto.id)
        self.unit_test.assertEqual(deputy_check[1], deputy_dto.last_name)
        self.unit_test.assertEqual(deputy_check[2], deputy_dto.first_name)
        self.unit_test.assertEqual(deputy_check[3], deputy_dto.sexe)
        self.unit_test.assertTrue(deputy_check[4] == deputy_dto.birthdate)
        self.unit_test.assertEqual(deputy_check[5], deputy_dto.candidate_id)
        self.unit_test.assertTrue(deputy_check[6] == deputy_dto.is_sorting)
        
        
    def assert_result_dto(self, result_check, result_dto) :
        self.unit_test.assertEqual(result_check[0], result_dto.id)
        self.unit_test.assertEqual(result_check[1], result_dto.state_compute)
        self.unit_test.assertEqual(result_check[2], result_dto.round_number)
        self.unit_test.assertEqual(result_check[3], result_dto.registered)
        self.unit_test.assertEqual(result_check[4], result_dto.abstaining)
        self.unit_test.assertEqual(result_check[5], result_dto.rate_abstaining)
        self.unit_test.assertEqual(result_check[6], result_dto.voting)
        self.unit_test.assertEqual(result_check[7], result_dto.rate_voting)
        self.unit_test.assertEqual(result_check[8], result_dto.blank_balot)
        self.unit_test.assertEqual(result_check[9], result_dto.rate_blank_registered)
        self.unit_test.assertEqual(result_check[10], result_dto.rate_blank_voting)
        self.unit_test.assertEqual(result_check[11], result_dto.null_ballot)
        self.unit_test.assertEqual(result_check[12], result_dto.rate_null_registered)
        self.unit_test.assertEqual(result_check[13], result_dto.rate_null_voting)
        self.unit_test.assertEqual(result_check[14], result_dto.expressed)
        self.unit_test.assertEqual(result_check[15], result_dto.rate_express_registered)
        self.unit_test.assertEqual(result_check[16], result_dto.rate_express_voting)
        self.unit_test.assertEqual(result_check[17], result_dto.district_id)
        
        
    def assert_department_dto(self, department_check, department_dto) :
        self.unit_test.assertEqual(department_check[0], department_dto.id)
        self.unit_test.assertEqual(department_check[1], department_dto.name)
        self.unit_test.assertEqual(department_check[2], department_dto.number)
        
        
    def assert_department_result_dto(self, department_check, department_result_dto) : 
        self.assert_department_dto(department_check[0 : 3], department_result_dto)
        self.unit_test.assertEqual(department_check[3], department_result_dto.rate_voting)
        
        
    def assert_department_party_result_dto(self, department_party_result_check, department_party_result_dto) : 
        self.assert_department_dto(department_party_result_check[0 : 3], department_party_result_dto)
        self.unit_test.assertEqual(department_party_result_check[3], department_party_result_dto.avg_vote_expressed)
        
        
    def assert_district_dto(self, district_check, district_dto) :
        self.unit_test.assertEqual(district_check[0], district_dto.id)
        self.unit_test.assertEqual(district_check[1], district_dto.position)
        self.unit_test.assertEqual(district_check[2], district_dto.name)
        self.unit_test.assertEqual(district_check[3], district_dto.department_id)
        
        
    def assert_district_result_dto(self, district_result_check, district_result_dto) :
        self.assert_district_dto(district_result_check[0 : 4], district_result_dto)
        self.unit_test.assertEqual(district_result_check[4], district_result_dto.rate_voting)
        self.unit_test.assertEqual(district_result_check[5], district_result_dto.department_name)