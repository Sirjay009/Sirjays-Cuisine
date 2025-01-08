from django.urls import path
from . import views

urlpatterns = [
    path('reservation/', views.reservation_list, name='reservation'),
    path('<int:id>/edit/', views.reservation_edit,
         name="reservation_edit"),
]
