# ResultLegislativeElectionAPI

## GOAL
This website helps you to understand the result of legistive election in 2022.

## INSTALLATION
The script run.sh execute of all unit tests and build the website if all tests are OK. 
After you can go to http://127.0.0.1:8080/docs to see all apis.

## WORKS 
At first the api of the website is developping.
Feature to developped : 
1. Create the structure of the hexagonale architecture for the project. DONE
2. New method in candidates.py to get all the candidates from the database DONE
3. Create in routers deputies.py with a method to get all the deputies DONE
4. Create in routers results.py with a method to get all the results DONE
5. Add three new methods
- Find candidates from his last name and first name DONE
- Find deputies from last name and first name and from his candidate DONE
6. Connect this API with the database and mysqlrepository DONE
7. Create a cache to load data only one time DONE
8. In Candidates py, add this three methods :
- Retrieve all candidates from a specific party. DONE
- Retrieve all candidates from a specific department. DONE
- Retrieve all candidates from a specific district. DONE
9. Create a method to find all districts of a department DONE
10. Create a method to class all districts by participation in first round and second round DONE
11. Create a method to class all departments by participation in first round and second round DONE
12. Give the possibility to choose  > or < for sorting datas and add interface to separate api and domain. DONE
13. Create a method to find all X candidates with the hightest result in first and second round. DONE
14. Create a method to find for each party all X candidates with the hightest result in first and second round. DONE
15. Create a method to find for each party all X departments with the hightest result. DOING
16. Modify architecture of the project to improve hexa architecture