from django.contrib import admin
from .models import Reservation
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'guests')

