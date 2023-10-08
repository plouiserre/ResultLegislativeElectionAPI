from app.domain.business.candidate.sortered_candidate import SorteredCandidate
from app.domain.factory.factorydepartmentpartyresult import FactoryDepartmentPartyResult

class PartyBusiness :
    def __init__(self, party_repo, candidate_repo, district_repo, department_repo) -> None:
        self.party_repo = party_repo
        self.candidate_repo = candidate_repo
        self.district_repo = district_repo
        self.department_repo = department_repo
        self.factory_department_party_result = FactoryDepartmentPartyResult()
        
    
    def get_parties(self) : 
        parties = self.party_repo.get_parties()
        return parties
    
    
    def get_party_by_short_name(self, short_name):
        party_by_short_name = None
        parties = self.party_repo.get_parties()
        for party in parties : 
            if party.short_name == short_name : 
                party_by_short_name = party
                break
        return party_by_short_name
    
    
    def get_top_candidates_for_each_party_all_rounds(self, limit) :
        all_candidates = self.candidate_repo.get_candidates()
        all_parties = self.party_repo.get_parties()
        all_candidates_by_party = {}
        
        for candidate in all_candidates :
            for party in all_parties : 
                if candidate.party_id == party.id : 
                    if (party.short_name in all_candidates_by_party) == False:
                        all_candidates_by_party[party.short_name] = []
                    all_candidates_by_party[party.short_name].append(candidate)
                    break

        for party in all_parties :
            candidates = all_candidates_by_party[party.short_name]
            sortered  = SorteredCandidate(candidates, all_parties)
            candidates_sortered = sortered.sort_all_candidates(limit)
            all_candidates_by_party[party.short_name] = candidates_sortered        
            
        return all_candidates_by_party
    
    #externalize in a specific class
    def get_top_departments_for_each_party_all_rounds(self) :
        all_candidates = self.candidate_repo.get_candidates()
        all_parties = self.party_repo.get_parties()         
        all_departments = self.department_repo.get_departments()
        all_districts = self.district_repo.get_districts()
        all_district_ids_by_departments = self.__get_district_ids_by_departments(all_departments, all_districts)
        all_candidates_by_party_and_department = self.__get_candidates_by_party_and_departments(all_departments, all_parties, all_candidates, all_district_ids_by_departments)
        all_departments_party_result_created = self.__get_all_departments_party_result(all_candidates_by_party_and_department)
        return {}       
    
    
    def __get_district_ids_by_departments(self, all_departments, all_districts) :
        results = {}
        for department in all_departments : 
            for district in all_districts : 
                if district.department_id == department.id : 
                    results[district.id] = department
        return results
    
    
    def __get_candidates_by_party_and_departments(self, all_departments, all_parties, all_candidates, all_district_ids_by_departments) : 
        results = {}       
        for candidate in all_candidates :
                for party in all_parties : 
                    if party.id == candidate.party_id :
                        for department in all_departments :                        
                            department_candidate = all_district_ids_by_departments[candidate.district_id]
                            if department_candidate.id == department.id : 
                                if (party.short_name in results) == False  : 
                                    results[party.short_name] = {}
                                if (department in results[party.short_name]) == False : 
                                    results[party.short_name][department] = []
                                results[party.short_name][department].append(candidate)
                                break
        return results     
    
    
    def __get_all_departments_party_result(self, all_candidates_by_party_and_department) :
        all_departments_result_by_party_first_round = {}
        all_departments_result_by_party_second_round = {}
        for party_name in all_candidates_by_party_and_department : 
            candidates_specific_party = all_candidates_by_party_and_department[party_name]
            if (party_name in all_departments_result_by_party_first_round) == False : 
                all_departments_result_by_party_first_round[party_name] = []
            if (party_name in all_departments_result_by_party_second_round) == False : 
                all_departments_result_by_party_second_round[party_name] = []
            for department in candidates_specific_party : 
                all_candidates_from_same_party_in_specific_dep = candidates_specific_party[department]
                all_voting_expressed_first_round = []
                all_voting_expressed_second_round = []
                for candidate in all_candidates_from_same_party_in_specific_dep : 
                    all_voting_expressed_first_round.append(candidate.rate_vote_expressed_first_round)
                    all_voting_expressed_second_round.append(candidate.rate_vote_expressed_second_round)
                department_result_first_round = self.factory_department_party_result.construct_department_party_result_from_list_voting_stats(department, all_voting_expressed_first_round)
                department_result_second_round = self.factory_department_party_result.construct_department_party_result_from_list_voting_stats(department, all_voting_expressed_second_round)
                all_departments_result_by_party_first_round[party_name].append(department_result_first_round)
                all_departments_result_by_party_second_round[party_name].append(department_result_second_round)
        return [all_departments_result_by_party_first_round, all_departments_result_by_party_second_round]