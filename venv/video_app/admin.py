from django.contrib import admin
from .models import User, Video
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active', 'is_staff', 'is_verified')
    search_fields = ('email',)

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_by', 'created_at')
    search_fields = ('title', 'description')


