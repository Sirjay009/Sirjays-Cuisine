from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Reservation
from .forms import CustomerForm, ReservationForm

# Create your views here.
def customer_details(request):
    if request.method == "POST":
        customer_form = CustomerForm(request.POST)
        if customer_form.is_valid():
            customer_form.save()
            messages.add_message(
                request, messages.SUCCESS, 
                'Thanks for your reservation. We look forward to hosting you!')
    else:
        customer_form = CustomerForm()
    return render(
        request, 'customer_data.html', {'form': customer_form},
    )

def book_table(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            # Validate and save the reservation
            reservation = form.save(commit=False)
            # Check for double booking
            existing = reservation.objects.filter(
                table=reservation.table,
                date=reservation.date,
                time=reservation.time,
            )
            if existing.exists():
                form.add_error(
                    None, "This table is already booked for the selected time."
                    )
            else:
                reservation.user = request.user
                reservation.save()
                return redirect('view_reservations')
    else:
        form = ReservationForm()
    return render(request, 'book_table.html', {'form': form})
