from django.urls import path
from . import views

urlpatterns = [
    path('', views.reservation_list, name='reservation'),
    path('<int:id>/edit/', views.reservation_edit,
         name="reservation_edit"),
    path('delete_reservation/<int:id>', views.reservation_delete,
         name="reservation_delete"),
]
