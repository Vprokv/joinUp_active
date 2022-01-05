command start project
for docker
1. docker-compose build
2. docker-compose up

for back-end(required postgres instance on 5430 port)
1. replace joinup/settings.py/DATABASES/HOST by 'postgres' -> 'localhost'
2. pip install -r requirements.txt
3. python3 manage.py migrate
4. python3 manage.py runserver

API
1. for docker: http://127.0.0.1:8000/api/
2. for python: http://0.0.0.0:9000/api/

Swagger
1. for docker: http://127.0.0.1:8000/api/swagger
2. for python: http://0.0.0.0:9000/api/swagger
