from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    signup_date = models.DateField(auto_now_add=True, null=True, blank=True)
    following = models.ManyToManyField('self', symmetrical=False)
    profile_pic = models.ImageField(null=True, blank=True)
    REQUIRED_FIELDS = ['full_name', 'email']

    def __str__(self):
        return self.username
