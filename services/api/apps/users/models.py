from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    admission_number = models.CharField(max_length=32, unique=True, null=True, blank=True)
    department = models.CharField(max_length=128, null=True, blank=True)
    school = models.CharField(max_length=128, null=True, blank=True)
    is_student = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.username

