from app.domain.factory.factoryparty import FactoryParty

def getParties_by_id(ids_list) : 
    parties_needed = []
    
    parties = createParties()
    
    for party in parties : 
        for id in ids_list : 
            if party.id == id : 
                parties_needed.append(party)
                break
    
    return parties_needed


def getParties_id_by_name(short_names_list) : 
    parties_ids = []
    
    parties = createParties()
    
    for party in parties : 
        for short_name in short_names_list : 
            if party.short_name == short_name : 
                parties_ids.append(party.id)
                break
    
    return parties_ids


def createParties() : 
    factory = FactoryParty()
    one_party = factory.construct_party(1, "Divers extrême gauche", "DXG")
    two_party = factory.construct_party(2, "Parti radical de gauche", "RDG")
    three_party = factory.construct_party(3, "Nouvelle union populaire écologique et sociale", "NUP")
    four_party = factory.construct_party(4, "Divers gauche", "DVG")
    five_party = factory.construct_party(5, "Ecologistes", "ECO")
    six_party = factory.construct_party(6, "Régionaliste", "REG")
    seven_party = factory.construct_party(7, "Ensemble ! (Majorité présidentielle)", "ENS")
    eight_party = factory.construct_party(8, "Divers Centre", "DVC")
    nine_party = factory.construct_party(9, "Divers", "DIV")
    ten_party = factory.construct_party(10, "Union des Démocrates et des Indépendants", "UDI")
    eleven_party = factory.construct_party(11, "Les Républicains", "LR")
    twelve_party = factory.construct_party(12, "Divers droite", "DVD")
    thirteen_party = factory.construct_party(13, "Droite souverainiste", "DSV")
    fourteen_party = factory.construct_party(14, "Reconquête !", "REC")
    fifteen_party = factory.construct_party(15, "Rassemblement National", "RN")
    sixteen_party = factory.construct_party(16, "Divers extrême droite", "DXD")
    parties = [one_party, two_party, three_party, four_party, five_party, six_party, seven_party, eight_party, nine_party,
               ten_party, eleven_party, twelve_party, thirteen_party, fourteen_party, fifteen_party, sixteen_party]
    return parties 