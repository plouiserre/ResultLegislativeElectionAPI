from app.domain.factory.factoryresult import FactoryResult

def getResults(ids_list) : 
    results_needed = []
    
    factory = FactoryResult()
    first_result_ten_district = factory.construct_result(100, "Completed", 1, 876, 5, 0.65, 666, 98.8, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 10)
    second_result_ten_district = factory.construct_result(105, "Completed", 2, 876, 5, 0.65, 666, 18.8, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 10)
    
    first_result_eleven_district = factory.construct_result(110, "Completed", 1, 276, 23, 1.65, 866, 38.8, 3, 5.2, 1.7, 566, 88.8, 3, 5.2, 1.7, 2.7, 11)
    second_result_eleven_district = factory.construct_result(115, "Completed", 2, 276, 23, 1.65, 866, 68.8, 3, 5.2, 1.7, 566, 88.8, 3, 5.2, 1.7, 2.7, 11)
    
    first_result_twelve_district = factory.construct_result(120, "Completed", 1, 576, 23, 8.65, 566, 35.8, 8, 8.2, 8.7, 605, 68.8, 13, 3.2, 4.7, 5.7, 12)
    second_result_twelve_district = factory.construct_result(125, "Completed", 2, 576, 23, 8.65, 566, 25.8, 8, 8.2, 8.7, 605, 68.8, 13, 3.2, 4.7, 5.7, 12)
    
    first_result_twenty_district = factory.construct_result(200, "Completed", 1, 876, 5, 0.65, 666, 78.8, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 20)
    second_result_twenty_district = factory.construct_result(205, "Completed", 2, 876, 5, 0.65, 666, 78.8, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 20)
    
    first_result_twenty_one_district = factory.construct_result(210, "Completed", 1, 276, 23, 1.65, 866, 68.8, 3, 5.2, 1.7, 566, 88.8, 3, 5.2, 1.7, 2.7, 21)
    second_result_twenty_one_district = factory.construct_result(215, "Completed", 2, 276, 23, 1.65, 866, 68.8, 3, 5.2, 1.7, 566, 88.8, 3, 5.2, 1.7, 2.7, 21)
    
    first_result_twenty_two_district = factory.construct_result(220, "Completed", 1, 576, 23, 8.65, 566, 15.8, 8, 8.2, 8.7, 605, 68.8, 13, 3.2, 4.7, 5.7, 22)
    second_result_twenty_two_district = factory.construct_result(225, "Completed", 2, 576, 23, 8.65, 566, 15.8, 8, 8.2, 8.7, 605, 68.8, 13, 3.2, 4.7, 5.7, 22)
    
    first_result_twenty_three_district = factory.construct_result(230, "Completed", 1, 676, 50, 10.65, 266, 28.8, 5, 23.2, 4.7, 266, 48.8, 8, 4.2, 2.7, 0.9, 23)
    second_result_twenty_three_district = factory.construct_result(235, "Completed", 2, 676, 50, 10.65, 266, 28.8, 5, 23.2, 4.7, 266, 48.8, 8, 4.2, 2.7, 0.9, 23)
    
    first_result_twenty_four_district = factory.construct_result(240, "Completed", 1, 876, 5, 0.65, 666, 99.56, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 24)
    second_result_twenty_four_district = factory.construct_result(245, "Completed", 2, 876, 5, 0.65, 666, 99.56, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 24)
    
    first_result_twenty_five_district = factory.construct_result(250, "Completed", 1, 876, 5, 0.65, 666, 65.2, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 25)
    second_result_twenty_five_district = factory.construct_result(255, "Completed", 2, 876, 5, 0.65, 666, 65.2, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 25)
    
    first_result_twenty_six_district = factory.construct_result(260, "Completed", 1, 876, 5, 0.65, 666, 0.45, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 26)
    second_result_twenty_six_district = factory.construct_result(265, "Completed", 2, 876, 5, 0.65, 666, 0.45, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 26)
    
    first_result_twenty_seven_district = factory.construct_result(270, "Completed", 1, 876, 5, 0.65, 666, 42.6, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 27)
    second_result_twenty_seven_district = factory.construct_result(275, "Completed", 2, 876, 5, 0.65, 666, 42.6, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 27)
    
    first_result_hundred_ten_district = factory.construct_result(1100, "Completed", 1, 876, 5, 0.65, 666, 12.8, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 110)
    second_result_hundred_ten_district = factory.construct_result(1105, "Completed", 2, 876, 5, 0.65, 666, 7.8, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 110)
    
    first_result_hundred_eleven_district = factory.construct_result(1110, "Completed", 1, 276, 23, 1.65, 866, 58.8, 3, 5.2, 1.7, 566, 88.8, 3, 5.2, 1.7, 2.7, 111)
    second_result_hundred_eleven_district = factory.construct_result(1115, "Completed", 2, 276, 23, 1.65, 866, 48.8, 3, 5.2, 1.7, 566, 88.8, 3, 5.2, 1.7, 2.7, 111)
    
    first_result_three_hundred_thirty_district = factory.construct_result(3300, "Completed", 1, 576, 23, 8.65, 566, 66.8, 8, 8.2, 8.7, 605, 68.8, 13, 3.2, 4.7, 5.7, 330)
    second_result_three_hundred_thirty_district = factory.construct_result(3305, "Completed", 2, 576, 23, 8.65, 566, 43.8, 8, 8.2, 8.7, 605, 68.8, 13, 3.2, 4.7, 5.7, 330)
    
    first_result_three_hundred_thirty_one_district = factory.construct_result(3310, "Completed", 1, 876, 5, 0.65, 666, 42.8, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 331)
    second_result_three_hundred_thirty_one_district = factory.construct_result(3315, "Completed", 2, 876, 5, 0.65, 666, 23.8, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 331)
    
    first_result_three_hundred_fourty_district = factory.construct_result(3400, "Completed", 1, 276, 23, 1.65, 866, 78.8, 3, 5.2, 1.7, 566, 88.8, 3, 5.2, 1.7, 2.7, 340)
    second_result_three_hundred_fourty_district = factory.construct_result(3405, "Completed", 2, 276, 23, 1.65, 866, 68.8, 3, 5.2, 1.7, 566, 88.8, 3, 5.2, 1.7, 2.7, 340)
    
    first_result_three_hundred_fourty_one_district = factory.construct_result(3410, "Completed", 1, 576, 23, 8.65, 566, 23.8, 8, 8.2, 8.7, 605, 68.8, 13, 3.2, 4.7, 5.7, 341)
    second_result_three_hundred_fourty_one_district = factory.construct_result(3415, "Completed", 2, 576, 23, 8.65, 566, 42.8, 8, 8.2, 8.7, 605, 68.8, 13, 3.2, 4.7, 5.7, 341)
    
    first_result_three_hundred_fourty_two_district = factory.construct_result(3420, "Completed", 1, 876, 5, 0.65, 666, 43.8, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 342)
    second_result_three_hundred_fourty_two_district = factory.construct_result(3425, "Completed", 2, 876, 5, 0.65, 666, 66.8, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 342)
    
    first_result_three_hundred_fourty_three_district = factory.construct_result(3430, "Completed", 1, 276, 23, 1.65, 866, 48.8, 3, 5.2, 1.7, 566, 88.8, 3, 5.2, 1.7, 2.7, 343)
    second_result_three_hundred_fourty_three_district = factory.construct_result(3435, "Completed", 2, 276, 23, 1.65, 866, 58.8, 3, 5.2, 1.7, 566, 88.8, 3, 5.2, 1.7, 2.7, 343)
    
    first_result_six_hundred_ninety_district = factory.construct_result(6900, "Completed", 1, 576, 23, 8.65, 566, 7.8, 8, 8.2, 8.7, 605, 68.8, 13, 3.2, 4.7, 5.7, 690)
    second_result_six_hundred_ninety_district = factory.construct_result(6905, "Completed", 2, 576, 23, 8.65, 566, 12.8, 8, 8.2, 8.7, 605, 68.8, 13, 3.2, 4.7, 5.7, 690)
    
    first_result_six_hundred_ninety_one_district = factory.construct_result(6910, "Completed", 1, 876, 5, 0.65, 666, 25.8, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 691)
    second_result_six_hundred_ninety_one_district = factory.construct_result(6915, "Completed", 2, 876, 5, 0.65, 666, 35.8, 2, 1.2, 0.7, 666, 78.8, 2, 1.2, 0.7, 0.7, 691)
    
    first_result_six_hundred_ninety_two_district = factory.construct_result(6920, "Completed", 1, 276, 23, 1.65, 866, 68.8, 3, 5.2, 1.7, 566, 88.8, 3, 5.2, 1.7, 2.7, 692)
    second_result_six_hundred_ninety_two_district = factory.construct_result(6925, "Completed", 2, 276, 23, 1.65, 866, 38.8, 3, 5.2, 1.7, 566, 88.8, 3, 5.2, 1.7, 2.7, 692)
    
    first_result_six_hundred_ninety_three_district = factory.construct_result(6930, "Completed", 1, 576, 23, 8.65, 566, 18.8, 8, 8.2, 8.7, 605, 68.8, 13, 3.2, 4.7, 5.7, 693)
    second_result_six_hundred_ninety_three_district = factory.construct_result(6935, "Completed", 2, 576, 23, 8.65, 566, 98.8, 8, 8.2, 8.7, 605, 68.8, 13, 3.2, 4.7, 5.7, 693)
        
    results = [first_result_ten_district, second_result_ten_district, first_result_eleven_district, second_result_eleven_district, first_result_twelve_district,
                second_result_twelve_district, first_result_twenty_district, second_result_twenty_district, first_result_twenty_one_district, 
                second_result_twenty_one_district, first_result_twenty_two_district, second_result_twenty_two_district, first_result_twenty_three_district, 
                second_result_twenty_three_district, first_result_twenty_four_district, second_result_twenty_four_district, first_result_twenty_five_district, 
                second_result_twenty_five_district, first_result_twenty_six_district, second_result_twenty_six_district, first_result_twenty_seven_district, 
                second_result_twenty_seven_district, first_result_hundred_ten_district, second_result_hundred_ten_district, first_result_hundred_eleven_district, 
                second_result_hundred_eleven_district, first_result_three_hundred_thirty_district, second_result_three_hundred_thirty_district, 
                first_result_three_hundred_thirty_one_district, second_result_three_hundred_thirty_one_district, first_result_three_hundred_fourty_district, 
                second_result_three_hundred_fourty_district, first_result_three_hundred_fourty_one_district, second_result_three_hundred_fourty_one_district, 
                first_result_three_hundred_fourty_two_district, second_result_three_hundred_fourty_two_district, first_result_three_hundred_fourty_three_district, 
                second_result_three_hundred_fourty_three_district, first_result_six_hundred_ninety_district, second_result_six_hundred_ninety_district, 
                first_result_six_hundred_ninety_one_district, second_result_six_hundred_ninety_one_district, first_result_six_hundred_ninety_two_district,
                second_result_six_hundred_ninety_two_district, first_result_six_hundred_ninety_three_district, second_result_six_hundred_ninety_three_district] 
    
    for result in results : 
        for id in ids_list :
            if result.id == id :
                results_needed.append(result)
                break
            
    return results_needed