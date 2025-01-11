from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    followers = models.ManyToManyField('self', related_name='following', symmetrical=False)
    following = models.ManyToManyField('self', related_name='followers', symmetrical=False)

    def __str__(self):
        return self.username