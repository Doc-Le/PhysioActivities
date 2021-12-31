import uuid

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class UserProfile(models.Model):
    """
    A user sign-up model for maintaining default
    information and appointment history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_first_name = models.CharField(max_length=50)
    default_last_name = models.CharField(max_length=50)
    default_gender = models.CharField(max_length=10, null=True, blank=True)
    default_phone = models.CharField(max_length=10)
    default_email = models.CharField(max_length=100)
    # default_location = models.ForeignKey('Location', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.username
