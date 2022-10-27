from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    is_seller = models.BooleanField()
    updated_at = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ["is_seller", "first_name", "last_name"]
