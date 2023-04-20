from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    #class1 = models.TextField()
    #class2 = models.TextField()
    #class3 = models.TextField()
    #class4 = models.TextField()
    #class5 = models.TextField()
    #class6 = models.TextField()
    #class7 = models.TextField()
    #class8 = models.TextField()

    def __str__(self):
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)


#class Matches(models.Model):
#    name = models.CharField(max_length=255)
#    classes = models.TextField()
#    interests = models.TextField()
