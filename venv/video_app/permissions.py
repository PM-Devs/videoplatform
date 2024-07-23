from rest_framework.permissions import BasePermission
from rest_framework.exceptions import AuthenticationFailed
from .models import AppCredential

class HasAppCredentials(BasePermission):
    def has_permission(self, request, view):
        app_id = request.headers.get('App-Id')
        app_secret = request.headers.get('App-Secret')

        if not app_id or not app_secret:
            raise AuthenticationFailed('App-Id and App-Secret headers are required')

        try:
            AppCredential.objects.get(app_id=app_id, app_secret=app_secret)
        except AppCredential.DoesNotExist:
            raise AuthenticationFailed('Invalid App Credentials')

        return True

class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff
