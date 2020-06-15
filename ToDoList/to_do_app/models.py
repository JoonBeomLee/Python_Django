from django.db import models

# Create your models here.
class to_do(models.Model):
    content = models.CharField(max_length=255)