import mysql.connector

class MyDb : 
    def __init__(self) :
        pass
    
    def get_my_db(self) :
        mydb = mysql.connector.connect(
            host="localhost",
            user="ElectionsCongressmans",
            password="ASimpleP@ssW0rd"
        )
        return mydb