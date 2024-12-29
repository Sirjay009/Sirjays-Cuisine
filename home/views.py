from django.shortcuts import render
from django.views import generic
from .models import Home


# Create your views here


class HomeList(generic.ListView):
    queryset = Home.objects.all()
    template_name = "home/list.html"
