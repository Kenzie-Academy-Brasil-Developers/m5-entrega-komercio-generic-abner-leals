from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=50)

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    is_seller = models.BooleanField()
    updated_at = models.DateField(auto_now=True)

    REQUIRED_FIELDS = ["is_seller", "first_name", "last_name"]
