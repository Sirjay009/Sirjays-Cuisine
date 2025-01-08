from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
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


def reservation_edit(request, reservation_id):
    reservation = get_object_or_404(
        Reservation, id=reservation_id, user=request.user)
    if request.method == "POST":
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            messages.success(request, "Reservation updated successfully!")
            return redirect('reservation_data', id=reservation.id)
    else:
        form = ReservationForm(instance=reservation)
    return render(request, 'reservation/reservation_edit.html', {'form': form})
