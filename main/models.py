from django.contrib.auth.models import AbstractUser
from django.db import models
class User(AbstractUser):
    pass

class CryptoApi(models.Model):
    slug = models.CharField(max_length=100, null=False, blank=False)
    convert = models.CharField(max_length=100, null=False, blank=False)