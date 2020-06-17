from django.db import models

# Create your models here.
class category(models.Model):
    category_name = models.CharField(max_length=100)

class restaurant(models.Model):
    # category 삭제시 같이 삭제
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    rst_name = models.CharField(max_length=100)
    rst_link = models.URLField()
    rst_content = models.TextField()
    rst_keyword = models.CharField(max_length=50)