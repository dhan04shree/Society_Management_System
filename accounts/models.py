from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('MEMBER', 'Member'),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    flat_no = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.role})"
