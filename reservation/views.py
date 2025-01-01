from django.shortcuts import render
from django.contrib import messages
from .forms import ReservationForm
from .models import Reservation

# Create your views here.


def reservation_view(request):
    reservation = Reservation.objects.all()
    reservation_form = ReservationForm()
    return render(
        request, 
        'reservation/reservation_list.html', 
        {
            'reservation': reservation,
            'reservation_form': reservation_form,
            },)
