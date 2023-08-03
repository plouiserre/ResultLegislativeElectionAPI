class ResultBusiness() :
    
    def __init__(self, result_repository) -> None:
        self.result_repository = result_repository
    
    def get_results(self):
        results = self.result_repository.get_results()
        
        return results
    
    
    def get_rounds_participation_sorted(self) : 
        results_sorted_by_round = {}
        first_round_sorted = self.__process_results_sorted(1)
        second_round_sorted = self.__process_results_sorted(2)
        results_sorted_by_round["first_round"] = first_round_sorted
        results_sorted_by_round["second_round"] = second_round_sorted
        return results_sorted_by_round
    
    
    # def get_first_round_participation_sorted(self) : 
    #     results_sorted = self.__process_results_sorted(1)
        
    #     return results_sorted
    
    
    # def get_second_round_participation_sorted(self) : 
    #     results_sorted = self.__process_results_sorted(2)
        
    #     return results_sorted
    
    
    def __process_results_sorted(self, round_number) :
        all_results = self.result_repository.get_results()
        
        results_second_round = self.__get_results_by_specific_rounded(all_results, round_number)      
        
        results_sorted = self.__get_results_sorted(results_second_round)  
                    
        return results_sorted 
    
    
    def __get_results_by_specific_rounded(self, all_rounds, round_number) :
        results = []
        for result in all_rounds : 
            if result.round_number == round_number :
                results.append(result)    
        return results
    
    
    #TODO optimized
    def __get_results_sorted(self, results_sorting) : 
        results_sorted = []
        while len(results_sorting) > len(results_sorted):
            results_first_round_updated = self.__get_results_updated(results_sorting, results_sorted)
            for result_examined in results_first_round_updated :
                for i in range(len(results_first_round_updated)) :
                    is_end_loop = i + 1 == len(results_first_round_updated)
                    result_compared = results_first_round_updated[i] 
                    if is_end_loop and len(results_sorted) + 1 == len(results_first_round_updated) :
                        results_sorted.append(result_compared)
                    elif result_examined.id == result_compared.id and is_end_loop == False:
                        continue
                    elif result_compared in results_sorted : 
                        continue
                    elif result_examined.rate_voting > result_compared.rate_voting :
                        break
                    elif is_end_loop :
                        results_sorted.append(result_examined)
                        break
                    else : 
                        continue
        return results_sorted
    
    
    def __get_results_updated(self, results_first_round, results_sorted) : 
        results_first_rounded_updated = []
        for result in results_first_round : 
            is_sorted = False
            for result_sorted in results_sorted : 
                if result_sorted.id == result.id : 
                    is_sorted = True
            if is_sorted == False :
                results_first_rounded_updated.append(result)
            else :
                continue
        return results_first_rounded_updated