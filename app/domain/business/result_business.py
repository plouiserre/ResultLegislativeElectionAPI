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
    
    
    def __process_results_sorted(self, round_number) :
        all_results = self.result_repository.get_results()
        
        results_specific_round = self.__get_results_by_specific_rounded(all_results, round_number)      
        
        results_sorted = self.__get_results_sorted(results_specific_round)  
                    
        return results_sorted 
    
    
    def __get_results_by_specific_rounded(self, all_rounds, round_number) :
        results = []
        for result in all_rounds : 
            if result.round_number == round_number :
                results.append(result)    
        return results
    
    
    def __get_results_sorted(self, results_sorting) : 
        results_sorted = []
        results_to_sort = results_sorting.copy()
        while len(results_sorting) > len(results_sorted):
            for result_examined in results_to_sort :
                result_sorted = self.__sortered_specific_result(results_to_sort, result_examined, results_sorted)
                if result_sorted != None : 
                    results_to_sort.remove(result_sorted)
        return results_sorted
    
    
    def __sortered_specific_result(self, results_to_sort, result_examined, results_sorted) :
        result_sorted = None
        for i in range(len(results_to_sort)) :
            is_end_loop = i + 1 == len(results_to_sort)
            result_compared = results_to_sort[i] 
            if result_examined.id == result_compared.id and is_end_loop == False:
                continue
            elif result_compared in results_sorted : 
                continue
            elif result_examined.rate_voting > result_compared.rate_voting :
                break
            elif is_end_loop :
                results_sorted.append(result_examined)
                result_sorted = result_examined
                break
            else : 
                continue
        return result_sorted