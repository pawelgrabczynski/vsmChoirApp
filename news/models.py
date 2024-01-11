from django.db import models
import uuid
from users.models import Profile
# Create your models here.

class News(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=200, null=True, blank = True)
    body = models.TextField(null=True, blank = True)
    featured_image = models.ImageField(null=True, blank=True, upload_to ="images/", default="images/default.jpg")
    link = models.CharField(max_length=200, null = True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default =uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title