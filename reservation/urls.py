from django.urls import path
from . import views

urlpatterns = [
    path('reservation/', views.reservation_view, name='reservation'),
]