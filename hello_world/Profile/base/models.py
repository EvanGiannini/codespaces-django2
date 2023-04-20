from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()
    name = models.TextField()
    grade = models.TextField()

    def __str__(self):
        return self.user.username

class Matches(models.Model):
    name = models.CharField(max_length=255)
    classes = models.TextField()
    interests = models.TextField()
