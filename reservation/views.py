from django.shortcuts import render
from django.contrib import messages
from .forms import ReservationForm
from .models import Reservation, Page

# Create your views here.


def reservation_view(request):

    if request.method == "POST":
        reservation_form = ReservationForm(data=request.POST)
        if reservation_form.is_valid():
            reservation_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Reservation successfully made!"
            )

    reservation = Reservation.objects.all()
    reservation_form = ReservationForm()
    page_items = Page.objects.all()

    context = {
        'reservation': reservation,
        'reservation_form': reservation_form,
        'page_items': page_items,
    }

    return render(
        request, 'reservation/reservation_list.html', context)
