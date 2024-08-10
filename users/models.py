from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

class User(AbstractBaseUser):
    username = None

    email = models.EmailField(verbose_name='e-mail', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
