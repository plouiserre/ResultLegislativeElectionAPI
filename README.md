# ResultLegislativeElectionAPI

## GOAL
This website helps you to understand the result of legistive election in 2022.

## INSTALLATION
The script run.sh execute of all unit tests and build the website if all tests are OK. 
After you can go to http://127.0.0.1:8080/docs to see all apis.

## WORKS 
At first the api of the website is developping.
Feature to developped : 
1. Create the structure of the hexagonale architecture for the project.
2. New method in candidates.py to get all the candidates from the database and a method to get a candidate through last name and first name.
3. Create in routers deputies.py with a method to get all the deputies, a method to get a specific deputy through last name and first name, a method to get a specific deputy through his candidate.
4. Create in routers results.py with a method to get all the results, a method to get result's candidate.
5. Create a method in candidates.py to retrieve all candidates from a specific party.
6. Create a method in candidates.py to retrieve all candidates from a specific district.
7. Create a method in candidates.py to retrieve all candidates from a specific department.
8. Create a method to find all 10 candidates with the hightest result in second round.
9. Create a method to find for each party all 10 candidates with the hightest result in second round.
10. Create a method to find for each party all 10 departments with the hightest result.
11. Create a method to find the top 10 jobs of the new congressmans.
12. Create a method to return the average age of the new congressmans and for each party.
13. Create a method to return in the good order the list of the party order by the score of the election. 
14. Create a method to return with parties have the most fight
