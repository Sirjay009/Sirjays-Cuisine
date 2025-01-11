from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class Home(models.Model):
    """
    Stores a single title and slogan text.
    """
    title = models.CharField(max_length=200)
    slogan = models.TextField()

    def __str__(self):
        return self.title


class Menu(models.Model):
    """
    Stores a single dish entry.

    """
    dish = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    featured_image = CloudinaryField("image", default="placeholder")

    def __str__(self):
        return self.dish
