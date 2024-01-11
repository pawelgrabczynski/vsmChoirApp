from django.db import models
import uuid
from users.models import Profile
# Create your models here.

class Project(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    composer = models.CharField(max_length=200, null=True, blank=True)
    soprano_track = models.FileField(upload_to="songs/", null=True, blank=True, default=None)
    alto_track = models.FileField(upload_to="songs/", null=True, blank=True, default=None)
    tenor_track = models.FileField(upload_to="songs/", null=True, blank=True, default=None)
    bass_track = models.FileField(upload_to="songs/", null=True, blank=True, default=None)
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(null=True, blank=True, upload_to ="images/", default="images/default.jpg")
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default =uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title


class Review(models.Model):
    
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank = True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default =uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    # def __str__(self):
    #     return self.created

