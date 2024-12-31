from django.db import models

# Create your models here.

class Reservation(models.Model):
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField()

    def __str__(self):
        return f"Reservation for {self.guests} guests on {self.date} at {self.time}"
