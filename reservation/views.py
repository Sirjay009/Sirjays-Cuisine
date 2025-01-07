from django.shortcuts import render, get_list_or_404, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import ReservationForm
from .models import Reservation, Page

# Create your views here.


def reservation_detail(request):

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


def reservation_edit(request, reservation_id):
    if request.method == "POST":
        queryset = Reservation.objects.all()
        reservation = get_list_or_404(queryset, id=id)
        detail = get_list_or_404(Reservation, pk=reservation_id)
        reservation_form = ReservationForm(data=request.POST, instance=detail)

        if reservation_form.is_valid() and reservation.user == request.user:
            reservation = reservation_form.save(commit=False)
            detail.reservation = reservation
            detail.approved = False
            detail.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Reservation Updated!"
            )
        else:
            messages.add_message(
                request, messages.ERROR,
                "Error updating reservation!"
            )
    
    return HttpResponseRedirect(
        reverse("reservation_detail", args=[id])
    )

