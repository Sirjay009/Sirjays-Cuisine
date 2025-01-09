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
    reservation = get_object_or_404(Reservation, id=id, user=request.user)

    if request.method == "POST":
        reservation_form = ReservationForm(
            data=request.POST, instance=reservation)

        if reservation_form.is_valid():
            reservation_form.save()
            messages.success(request, "Reservation updated successfully!")
            return HttpResponseRedirect(reverse("reservation"))
        else:
            messages.error(request, "Error updating reservation!")

    else:
        reservation_form = ReservationForm(instance=reservation)

    return render(
        request,
        "reservation/reservation_edit.html",
        {"reservation_form": reservation_form, "reservation": reservation},
    )


def reservation_delete(request, id):
    reservation = get_object_or_404(Reservation, id=id, user=request.user)

    reservation.delete()
    messages.success(request, "Reservation deleted successfully!")

    return HttpResponseRedirect(
        reverse("reservation"))
