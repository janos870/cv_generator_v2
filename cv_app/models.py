from django.db import models

# Create your models here.
class UserProfile(models.Model):
    objects = None
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='media/profile_pictures/')

    def __str__(self):
        return self.full_name