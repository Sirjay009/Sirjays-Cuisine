from django.shortcuts import render, get_object_or_404, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import ReservationForm
from .models import Reservation, Page

# Create your views here.


def reservation_list(request):

    if request.method == "POST":
        reservation_form = ReservationForm(data=request.POST)
        if reservation_form.is_valid():
            reservation = reservation_form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Reservation successfully made!"
            )

    reservations = Reservation.objects.filter(user=request.user)
    reservation_form = ReservationForm()
    page_items = Page.objects.all()

    context = {
        'reservations': reservations,
        'reservation_form': reservation_form,
        'page_items': page_items,
    }

    return render(
        request, 'reservation/reservation_list.html', context)


# View a single reservation's details
def reservation_data(request, id):
    reservation = get_object_or_404(Reservation, id=id, user=request.user)
    return render(request, 'reservation/reservation_data.html', {'reservation': reservation})

# Edit an existing reservation


def reservation_edit(request, id):
    if request.method == "POST":
        queryset = Reservation.objects.filter(user=request.user)
        reservation = get_object_or_404(queryset, id=id)
        reservations = get_object_or_404(Reservation, pk=id)
        reservation_form = ReservationForm(data=request.Reservation, instance=reservations)

        if reservation_form.is_valid() and reservation.user == request.user:
            reservations = reservation_form.save(commit=False)
            reservations.reservation = reservation
            reservations.approved = False
            reservations.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Reservation Updated!"
            )

        else:
            messages.add_message(
                request, messages.SUCCESS,
                "Error Updating Reservation!"
            )

        return HttpResponseRedirect(
            reverse("reservation_edit", kwargs=[id])
        )

    
    
    
