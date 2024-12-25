from django.contrib import admin
from .models import Customer, Table, Reservation
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(SummernoteModelAdmin):
    list_display = ('name', 'email', 'phone')
    summernote_fields = ('content',)

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('number', 'capacity')

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('customer', 'table', 'date', 'time', 'guests')
