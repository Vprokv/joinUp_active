import jwt
import re
import os
from django.http import HttpResponse

jwt_secret = os.environ['JWT_SECRET']

def auth_middleware(get_response):
    def middleware(request):
        result = re.match(r'^\/api-active', request.path)
        if result is not None:
            authorization_header = request.headers.get("Authorization")
            if authorization_header is None:
                return HttpResponse("Отсуствует токен авторизации", status=401)
            try:
                user_obj = jwt.decode(authorization_header, jwt_secret, algorithms=["HS256"])
                request.user = user_obj
            except:
                return HttpResponse("Не верный токен авторизации", status=401)

        response = get_response(request)
        # Код должен быть выполнен ответа после view
        return response
    return middleware