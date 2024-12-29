from django.db import models

# Create your models here.


class Home(models.Model):
    title = models.CharField(max_length=200)
    slogan = models.TextField()

    def __str__(self):
        return self.title


class Menu(models.Model):
    dish = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='menu_images/')

    def __str__(self):
        return self.dish
