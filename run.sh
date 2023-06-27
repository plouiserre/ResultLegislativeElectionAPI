python3 -m unittest discover -v  2> "result_build.txt"

file='result_build.txt'

result=''

if grep -q FAILED "$file";
then 
    result="FAILING"
else
    result="WORKING"
fi 

rm result_build.txt

if [ $result == "WORKING" ];
then
    uvicorn app.main:app --reload
else
    echo "TEST KO donc pas de build"
fi