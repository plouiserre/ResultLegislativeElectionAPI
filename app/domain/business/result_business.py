class ResultBusiness() :
    
    def __init__(self, result_repository) -> None:
        self.result_repository = result_repository
    
    def get_results(self):
        results = self.result_repository.get_results()
        
        return results
        
       