from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import User, Video, VideoPage, ShareLink

class VideoAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(email='testuser@example.com', password='testpass123')
        self.client.force_authenticate(user=self.user)

    def test_create_video(self):
        url = reverse('video-list')
        data = {
        'title': 'Test Video',
        'description': 'This is a test video',
        'file_path': 'path/to/test/video.mp4'
    }
        response = self.client.post(url, data)
        print(f"Response status code: {response.status_code}")
        print(f"Response content: {response.content}")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Video.objects.count(), 1)
        self.assertEqual(Video.objects.get().title, 'Test Video')

    def test_list_videos(self):
        Video.objects.create(title='Video 1', description='Description 1', uploaded_by=self.user)
        Video.objects.create(title='Video 2', description='Description 2', uploaded_by=self.user)
        
        url = reverse('video-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    # Add more tests for other views and functionalities