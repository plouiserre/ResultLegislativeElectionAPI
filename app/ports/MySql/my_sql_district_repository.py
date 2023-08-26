from app.domain.factory.factorydistrict import FactoryDistrict
from app.domain.repository.district_repository import DistrictRepository
from app.ports.MySql.my_db import MyDb

class MySqlDistrictRepository(DistrictRepository):
    def __init__(self, cache) -> None:
        self.my_db = MyDb()
        self.__cache = cache
        
    
    def get_districts(self) : 
        districts = []
        
        if self.__cache.is_datas_cached("districts"):
            districts = self.__cache.get_datas("districts")
        else : 
            connexion = self.my_db.get_my_db()
            
            my_cursor = connexion.cursor()
            
            my_cursor.execute("SELECT * FROM ELECTIONSCONGRESSMANS.DISTRICT")
            
            districts_bdd = my_cursor.fetchall()
            
            factory = FactoryDistrict()
            for district_bdd in districts_bdd:
                district = factory.construct_district_from_bdd(district_bdd)
                districts.append(district)
                
            self.__cache.add_datas(districts, "districts")
            
        return districts