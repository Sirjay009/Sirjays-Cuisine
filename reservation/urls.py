from django.urls import path
from . import views

urlpatterns = [
    path('reservation/<int:id>/', views.reservation_data,
         name='reservation_data'),
    path('reservation/edit/<int:reservation_id>/', views.reservation_edit,
         name="reservation_edit"),
    path('reservation/', views.reservation_list, name='reservation'),
]
