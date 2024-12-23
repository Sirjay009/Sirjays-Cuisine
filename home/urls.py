from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReserveList.as_view(), name='home'),
]