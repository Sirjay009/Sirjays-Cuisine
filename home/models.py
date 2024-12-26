from django.db import models

# Create your models here.
class Home(models.Model):
    body = models.TextField()
    title = models.CharField(max_length=15)
    content = models.TextField()

