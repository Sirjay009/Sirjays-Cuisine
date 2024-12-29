from django.shortcuts import render
from django.views import generic
from .models import Home, Menu


# Create your views here


class HomeList(generic.ListView):
    queryset = Home.objects.all()
    template_name = "home/list.html"


def menu_detail(request):
    menu = Menu.objects.all()
    return render(
        request,
        "home/home_list.html",
        {"menu": menu}
    )
