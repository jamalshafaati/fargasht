from django.db import models

# Create your models here.
class Comment(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    body=models.TextField()
class News(models.Model):
    title=models.CharField(max_length=200)
    body=models.TextField()
    Image=models.ImageField()