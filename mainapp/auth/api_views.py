import json
import redis
import re
import jwt
import venv
import os
from random import randint
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from django.conf import settings

redis_instance = redis.StrictRedis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    password=settings.REDIS_PASSWORD,
    db=0,
    decode_responses=True
)

from ..models import (
    Employee,
    Candidate,
)

jwt_secret = os.environ['JWT_SECRET']


class EmployeeAuth(APIView):
    def post(self, request, *args, **kwargs):
        body = json.loads(request.body.decode('utf-8'))
        email = body.get("email")
        password = body.get("password")
        employee = Employee.objects.get(email=email)
        encoded_jwt = jwt.encode({"employee_id": employee.id}, jwt_secret, algorithm="HS256")

        return Response(encoded_jwt, status=200)

class CandidateAuth(APIView):
    def post(self, request, *args, **kwargs):
        body = json.loads(request.body.decode('utf-8'))
        phone = body.get("phone")
        user_code = body.get("code")
        if user_code is not None:
            stored_object = redis_instance.hgetall(phone)
            if stored_object.get("code") == user_code:
                return Response(stored_object.get("token"), status=200)
            return Response("Неправильный код", status=400)

        result = re.match(r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$', phone)

        if result is None:
            return Response("Неправильный телефонный номер", status=400)

        if redis_instance.ttl(phone) > 240:
            return Response("SMS уже в пути, попробуйте запросить повторную SMS через минуту", status=400)

        code = str(randint(10 ** 5, (10 ** 6) - 1))

        api_response = requests.get(
            "https://prokopchuk_veron@mail.ru:4YouuhbmytB4jLRUI2GufyAH3gRf@gate.smsaero.ru/v2/sms/send?number={phone}&text={text}&sign=SMS".format(
                phone=phone,
                text='JoinUs код авторизации {code}'.format(code=code)
            ))

        if api_response.status_code != 200:
            return Response("Невозможно доставить код авторизации", status=500)

        candidate = Candidate.objects.get(mobile_phone = phone)


        encoded_jwt = jwt.encode({"candidate_id": candidate.id}, jwt_secret, algorithm="HS256")

        redis_instance.hset(phone, "code", code)
        redis_instance.hset(phone, "token", encoded_jwt)
        redis_instance.expire(phone, 300)

        return Response(status=200)