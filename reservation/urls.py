from django.urls import path
from . import views

urlpatterns = [
    path("<int:reservation_id>/", views.reservation_edit,
         name="reservation_edit"),
    path('reservation/', views.reservation_detail, name='reservation'),
]