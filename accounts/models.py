from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # Custom User fields
    username = models.CharField(max_length=200, unique=True, null=False)
    email = models.EmailField(unique=True, null=False)
    password = models.CharField(max_length=50)

    # Change admin panel to email based login
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
