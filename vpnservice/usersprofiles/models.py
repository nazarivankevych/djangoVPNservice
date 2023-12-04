from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add other fields as needed
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    name = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return str(self.user)
