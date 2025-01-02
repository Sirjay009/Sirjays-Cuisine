from django.db import models
from django.utils.timezone import now

# Create your models here.


class Reservation(models.Model):
    name = models.CharField(max_length=100, default="Unnamed Reservation")
    email = models.EmailField(default="noreply@example.com")
    phone = models.CharField(max_length=15, default="Unknown")
    created_at = models.DateTimeField(default=now)
    guests = models.IntegerField()
    message = models.TextField(default="Default message")

    def __str__(self):
        return self.name if self.name else "Unnamed Reservation"
