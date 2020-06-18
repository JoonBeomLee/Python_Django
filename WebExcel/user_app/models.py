from django.db import models

# Create your models here.
class User(models.Model):
    usr_id = models.CharField(unique=True, max_length=20)
    pwd = models.CharField(max_length=100)
    name = models.CharField(max_length=20)
    email = models.EmailField(unique=True, max_length=255)
    validate = models.BooleanField(default=False)