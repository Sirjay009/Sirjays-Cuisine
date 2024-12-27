from django.db import models

# Create your models here.
class Home(models.Model):
    title = models.CharField(max_length=200)
    slogan = models.TextField()
    menu = models.CharField(max_length=20)
    dish = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.title

