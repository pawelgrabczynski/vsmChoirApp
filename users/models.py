from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

VOICES = (
        ("Sopran", 'Sopran'),
        ("Alt", 'Alt'),
        ("Tenor", 'Tenor'),
        ("Bas", 'Bas'),
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null = True, blank=True)
    email = models.EmailField(max_length=500, null = True, blank = True)
    username = models.CharField(max_length=200, null = True, blank=True)
    location = models.CharField(max_length=200, null = True, blank=True)
    voice = models.CharField(max_length=200, choices=VOICES, null=True, blank=True)
    bio = models.TextField(null = True, blank=True)
    profile_image = models.ImageField(null=True, blank = True, upload_to='images/profiles/', default='images/profiles/user-default.png')
    social_facebook = models.CharField(max_length=200, null = True, blank=True)
    social_instagram = models.CharField(max_length=200, null = True, blank=True)
    social_twitter = models.CharField(max_length=200, null = True, blank=True)
    social_youtube = models.CharField(max_length=200, null = True, blank=True)
    social_website = models.CharField(max_length=200, null = True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default =uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.username)

