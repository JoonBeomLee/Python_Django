from django.db import models

# Create your models here.
class to_do(models.Model):
    usr_id = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    is_done = models.BooleanField(default=False)
