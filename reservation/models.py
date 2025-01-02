from django.db import models
from datetime import date, time

# Create your models here.


class Reservation(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, default="Unknown")
    reservation_date = models.DateField(default=date.today)
    reservation_time = models.TimeField(default=time(13, 0))
    guests = models.IntegerField(default=1)
    special_request = models.TextField(null=True, blank=True)
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return
        f"Reservation for {self.name} on {self.reservation_date} at {self.reservation_time}"
