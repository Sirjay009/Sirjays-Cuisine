from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
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


@login_required
def my_reservations(request):
    user_reservations = Reservation.objects.get(user=request.user)
    return render(request, 'reservation/my_reservations.html', {'reservations': user_reservations})

@login_required
def edit_reservation(request, id):
    reservation = get_object_or_404(Reservation, id=id, user=request.user)

    if request.method == "POST":
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('my_reservations')
    else:
        form = ReservationForm(instance=reservation)

    return render(request, 'reservation/edit_reservation.html', {'form': form})

@login_required
def delete_reservation(request, id):
    reservation = get_object_or_404(Reservation, id=id, user=request.user)

    if request.method == "POST":
        reservation.delete()
        return redirect('my_reservations')

    return render(request, 'reservation/confirm_delete.html', {'reservation': reservation})

