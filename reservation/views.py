from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.http import HttpResponse
from .forms import ReservationForm

# Create your views here.
class ReservationView(View):
    def get(self, request):
        return HttpResponse("Reservation Page")
