from django.db import models

# Create your models here.
class UserProfile(models.Model):
    objects = None
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='media/profile_pictures/')
    profession = models.CharField(max_length=200, blank=True)
    education = models.CharField(max_length=200, default='No education')
    experience = models.CharField(max_length=200, default='No experience')
    skills = models.CharField(max_length=200, default='')
    languages = models.CharField(max_length=200, default='')
    website = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.full_name