from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Reservation, Page

# Register your models here.


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):

    list_display = (
        'name', 'email', 'phone', 'guests', 'reservation_date',
        'reservation_time', 'special_request',
    )


@admin.register(Page)
class PageAdmin(SummernoteModelAdmin):

    summernote_fields = ('banner',)
