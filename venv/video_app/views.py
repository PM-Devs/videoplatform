# views.py
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import User, Video, AppCredential
from .serializers import UserSerializer, VideoSerializer, AppCredentialSerializer
from django.core.mail import send_mail
from django.conf import settings
import random
import string
import jwt
from datetime import datetime, timedelta
from .authentication import AppCredentialAuthentication, JWTAuthentication
from .permissions import IsAdminUser

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            verification_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
            user.verification_code = verification_code
            user.save()

            send_mail(
                'Verify your email',
                f'Your verification code is: {verification_code}',
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=False,
            )

            return Response({'status': 'Verification code sent to email'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def verify_email(self, request):
        email = request.data.get('email')
        verification_code = request.data.get('verification_code')
        
        try:
            user = User.objects.get(email=email, verification_code=verification_code)
            user.is_active = True
            user.verification_code = ''
            user.save()
            return Response({'status': 'Email verified'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'Invalid email or verification code'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def login(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        
        user = User.objects.filter(email=email).first()
        if user is None or not user.check_password(password):
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

        if not user.is_active:
            return Response({'error': 'Email not verified'}, status=status.HTTP_400_BAD_REQUEST)

        access_token = jwt.encode({
            'user_id': user.id,
            'exp': datetime.utcnow() + timedelta(days=1)
        }, settings.SECRET_KEY, algorithm='HS256')

        return Response({'access_token': access_token})

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    authentication_classes = [AppCredentialAuthentication, JWTAuthentication]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAdminUser]
        else:
            self.permission_classes = [permissions.AllowAny]
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user)

class AppCredentialViewSet(viewsets.ModelViewSet):
    queryset = AppCredential.objects.all()
    serializer_class = AppCredentialSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [AppCredentialAuthentication, JWTAuthentication]

    @action(detail=False, methods=['post'], permission_classes=[permissions.AllowAny], authentication_classes=[])
    def create_app_credentials(self, request):
        app_credential = AppCredential()
        app_credential.save()
        serializer = self.get_serializer(app_credential)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
