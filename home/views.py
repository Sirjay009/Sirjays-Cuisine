from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from .forms import CustomerForm

# Create your views here


def home(request):
    return HttpResponse('Hello Home!')


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
