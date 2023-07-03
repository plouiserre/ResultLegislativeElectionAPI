class AssertTest:
    def __init__(self, unit_test) -> None:
        self.unit_test = unit_test
    
    def assert_candidate_dto(self, candidate_check, candidate_dto) :
        self.unit_test.assertEqual(candidate_check[0], candidate_dto.id)
        self.unit_test.assertEqual(candidate_check[1], candidate_dto.last_name)
        self.unit_test.assertEqual(candidate_check[2], candidate_dto.first_name)
        self.unit_test.assertEqual(candidate_check[3], candidate_dto.sexe)
        self.unit_test.assertTrue(candidate_check[4] == candidate_dto.birthdate)
        self.unit_test.assertEqual(candidate_check[5], candidate_dto.party_id)
        self.unit_test.assertEqual(candidate_check[6], candidate_dto.party_name)
        self.unit_test.assertEqual(candidate_check[7], candidate_dto.job)
        self.unit_test.assertEqual(candidate_check[8], candidate_dto.is_sorting)
        self.unit_test.assertEqual(candidate_check[9], candidate_dto.vote_first_round)
        self.unit_test.assertEqual(candidate_check[10], candidate_dto.rate_vote_registered_first_round)
        self.unit_test.assertEqual(candidate_check[11], candidate_dto.rate_vote_expressed_first_round)
        self.unit_test.assertEqual(candidate_check[12], candidate_dto.vote_second_round)
        self.unit_test.assertEqual(candidate_check[13], candidate_dto.rate_vote_registered_second_round)
        self.unit_test.assertEqual(candidate_check[14], candidate_dto.rate_vote_expressed_second_round)
        
        
    def assert_party_dto(self, party_check, party_dto) : 
        self.unit_test.assertEqual(party_check[0], party_dto.id)
        self.unit_test.assertEqual(party_check[1], party_dto.name)
        self.unit_test.assertEqual(party_check[2], party_dto.short_name)