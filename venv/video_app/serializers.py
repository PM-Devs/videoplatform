from rest_framework import serializers
from .models import User, Video, AppCredential

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'title', 'description', 'file_path', 'uploaded_by', 'created_at']
        read_only_fields = ['uploaded_by']

class AppCredentialSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppCredential
        fields = ['id', 'app_id', 'app_secret', 'created_at', 'updated_at']
        read_only_fields = ['app_id', 'app_secret']