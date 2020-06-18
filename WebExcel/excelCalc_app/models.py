from django.db import models

# Create your models here.
class uploadFile(models.Model):
    user_upload_file = models.FileField(upload_to='user_upload_files/%Y%m%d/')