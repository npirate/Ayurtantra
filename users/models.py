from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser (AbstractUser):
    #age = models.PositiveIntegerField (null = True, blank = True)
    email = models.EmailField (unique=True,)
    user_type = models.IntegerField(default = 1, blank=False,)