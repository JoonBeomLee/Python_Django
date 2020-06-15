from django.db import models

# Create your models here.
class user_info(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    pwd = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)