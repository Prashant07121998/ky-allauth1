
from django.contrib.auth.models import AbstractUser
from django.db import models



class CustomUser(AbstractUser):

    full_name = models.CharField(max_length= 100, blank=True)
    college_name = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    fb_profile_link = models.CharField(max_length=200)

    REQUIRED_FIELDS = ["email"]