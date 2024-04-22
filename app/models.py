from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    GENDER_CHOICES = {
        "m": "Male",
        "v": "Female",
        "u": "Undefined"
    }

    EMPLOYEE_TYPE_CHOICES = {
        "contractor": "Contractor",
        "internal": "Internal"
    }

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField(null=True, blank=True)
    employment_type = models.CharField(
        choices=EMPLOYEE_TYPE_CHOICES,
        default="internal",
        max_length=20
    )
    gender = models.CharField(
        choices=GENDER_CHOICES,
        default="u",
        max_length=10
    )
    github_username = models.CharField(null=True, blank=True, max_length=255)
    picture = models.TextField(null=True, blank=True)

    # Add more fields here when needed
    def __str__(self):
        return self.user.username