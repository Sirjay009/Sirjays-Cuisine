from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = (
            'name', 'email', 'phone', 'guests', 'reservation_date',
            'reservation_time', 'special_request'
            )
