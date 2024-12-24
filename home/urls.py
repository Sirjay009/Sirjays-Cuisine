from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReserveList.as_view(), name='home'),
    path('customer/', views.customer_details, name='customer_detail'),
]