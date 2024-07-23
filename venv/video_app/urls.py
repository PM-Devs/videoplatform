# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, VideoViewSet, AppCredentialViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'videos', VideoViewSet)
router.register(r'app-credentials', AppCredentialViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
