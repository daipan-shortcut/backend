import time
import jwt
import uuid
from config.settings import SECRET_KEY
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from rest_framework.authentication import get_authorization_header
from API.models import t_user
from django.contrib.auth.hashers import check_password

class NormalAuthentication(BaseAuthentication):
    def authenticate(self, request):
        email = request._request.POST.get("email")
        password = request._request.POST.get("password")
        user_obj = t_user.objects.filter(email=email).first()
        if not user_obj:
            raise exceptions.AuthenticationFailed('認証失敗')
        elif not check_password(password, user_obj.password):
            raise exceptions.AuthenticationFailed('パスワードあってません')
        token = generate_jwt(user_obj)
        return (token, None)

    def authenticate_header(self, request):
        pass


def generate_jwt(user):
    timestamp = int(time.time()) + 60*60*24*7  # 7 days

    random_string = str(uuid.uuid4())

    return jwt.encode(
        {"userid": user.pk, "random_string": random_string},
        SECRET_KEY)


class JWTAuthentication(BaseAuthentication):
    keyword = 'JWT'
    model = None

    def authenticate(self, request):
        auth = get_authorization_header(request).split()

        if not auth or auth[0].lower() != self.keyword.lower().encode():
            return None

        if len(auth) == 1:
            msg = "Authorization 無効"
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = "Authorization 無効 (2)"
            raise exceptions.AuthenticationFailed(msg)

        try:
            jwt_token = auth[1]
            jwt_info = jwt.decode(jwt_token, SECRET_KEY , algorithms=["HS256"])
            userid = jwt_info.get("userid")
            try:
                user = t_user.objects.get(pk=userid)
                user.is_authenticated = True
                return (user, jwt_token)
            except:
                msg = "ユーザー存在しません"
                raise exceptions.AuthenticationFailed(msg)
        except jwt.ExpiredSignatureError:
            msg = "tokenはタイムアウトしました"
            raise exceptions.AuthenticationFailed(msg)
        except jwt.InvalidTokenError:
            msg = "tokenは無効です"
            raise exceptions.AuthenticationFailed(msg)

    def authenticate_header(self, request):
        pass