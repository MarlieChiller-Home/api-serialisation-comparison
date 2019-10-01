export FLASK_APP=flask/main.py
flask run &
cd fast
uvicorn main:app --reload &
cd ../test
pytest test.py -s
