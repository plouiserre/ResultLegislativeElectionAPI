from app.domain.factory.factorydeputy import FactoryDeputy

import datetime

def getDeputies(ids_list) : 
    deputies_needed = []
    
    factory = FactoryDeputy()
    first_deputy = factory.construct_deputy(1, "M", "DUFREGNE", "Jean-Paul", datetime.datetime(1958, 3, 28), 2, True)
    second_deputy = factory.construct_deputy(2, "M", "PERCHE", "Philippe", datetime.datetime(1987, 11, 19), 3, False)
    third_deputy = factory.construct_deputy(3, "F", "BENOIT-GOLA", "Anne-Cécile", datetime.datetime(1973, 7, 24), 4, False)
    fourth_deputy = factory.construct_deputy(4, "M", "LEROUX", "Sylvain", datetime.datetime(1978, 6, 25), 987, False)
    deputies = [first_deputy, second_deputy, third_deputy, fourth_deputy]
    
    for deputy in deputies : 
        for id in ids_list :
            if deputy.id == id :
                deputies_needed.append(deputy)
                break
            
    return deputies_needed