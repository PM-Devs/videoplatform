from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import User, AppCredential
import jwt
from django.conf import settings

class AppCredentialAuthentication(BaseAuthentication):
    def authenticate(self, request):
        app_id = request.headers.get('App-Id')
        app_secret = request.headers.get('App-Secret')

        if not app_id or not app_secret:
            return None

        try:
            AppCredential.objects.get(app_id=app_id, app_secret=app_secret)
        except AppCredential.DoesNotExist:
            raise AuthenticationFailed('Invalid App Credentials')

        return (None, None)

class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return None

        try:
            access_token = auth_header.split(' ')[1]
            payload = jwt.decode(access_token, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Access token expired')
        except IndexError:
            raise AuthenticationFailed('Token prefix missing')
        except jwt.DecodeError:
            raise AuthenticationFailed('Invalid token')

        user = User.objects.filter(id=payload['user_id']).first()
        if user is None:
            raise AuthenticationFailed('User not found')

        if not user.is_active:
            raise AuthenticationFailed('User is inactive')

        return (user, None)