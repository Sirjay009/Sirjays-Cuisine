from django.contrib import admin
from .models import Reservation

# Register your models here.


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):

    list_display = (
        'name', 'email', 'phone', 'reservation_date', 'reservation_time',
        'guests', 'special_request', 'status',
    )
