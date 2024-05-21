from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    first_name = None
    last_name = None

    def __str__(self):
        return f'{self.id} - {self.username}'
