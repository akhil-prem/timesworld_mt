from django.contrib.auth.models import AbstractUser
from django.db import models


class AppUser(AbstractUser):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    full_name = models.CharField(max_length=300)
    email = models.EmailField(unique=True)
    country = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('staff', 'Staff'),
        ('admin', 'Admin'),
        ('editor', 'Editor'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def save(self, *args, **kwargs):
        self.username = self.email
        self.full_name = f"{self.first_name} {self.last_name}"
        super().save(*args, **kwargs)
