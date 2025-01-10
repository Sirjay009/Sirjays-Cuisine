from django.shortcuts import render
from .models import Home, Menu

# Create your views here


def home_view(request):
    """
    Renders the landing page.
    Displays an individual instance of :model:`home.Menu`.

    **Context**
    ``home``
         The most recent instance of :model:`home.Menu`.

    **Template**
         :template:`home/home_list.html`.

    """
    home = Home.objects.all()  # Query all home items
    menu_items = Menu.objects.all()      # Query all menu items
    context = {
        'home': home,
        'menu_items': menu_items,
    }
    return render(request, 'home/home_list.html', context)
