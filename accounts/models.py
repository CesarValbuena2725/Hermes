from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Developer(AbstractUser):
    github = models.CharField(max_length=200, unique=True, blank=True, null=True)
    
    def __str__(self):
        return self.first_name or self.username
