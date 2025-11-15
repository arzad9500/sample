from django.db import models
from django.contrib.auth.models import AbstractUser

# custamize user model

class user(AbstractUser):

    phone_number = models.CharField(max_length=13)
    
