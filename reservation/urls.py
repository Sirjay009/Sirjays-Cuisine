from django.urls import path
from . import views

urlpatterns = [
    path('reservation/', views.reservation_view, name='reservation'),
    path('my-reservations/', views.my_reservations, name='my_reservations'),
    path('reservation/<int:id>/edit/', views.edit_reservation, name='edit_reservation'),
    path('reservation/<int:id>/delete/', views.delete_reservation, name='delete_reservation'),
]