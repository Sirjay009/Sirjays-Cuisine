from django import forms
from .models import Customer, Reservation


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'email', 'phone')


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('customer', 'table', 'date', 'time', 'guests')
