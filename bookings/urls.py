from django.urls import path
from . import views

urlpatterns = [
    path('', views.bookings, name='bookings'),
    path('dates/', views.get_dates, name='get_dates'),
    path('times/<int:date_id>/', views.get_times, name='get_times'),
]