from django.db import models
from django.contrib.auth.models import User
from datetime import date, time

# Create your models here.

class Page(models.Model):
    label = models.CharField(max_length=200)
    banner = models.TextField()

    def __str__(self):
        return self.label


class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(default="no-email@example.com")
    phone = models.CharField(max_length=15, default="Unknown")
    guests = models.IntegerField(default=1)
    reservation_date = models.DateField(default=date.today)
    reservation_time = models.TimeField(default=time(13, 0))
    special_request = models.TextField(null=True, blank=True)
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reservations")

    def __str__(self):
        return self.name

