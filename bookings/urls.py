from django.urls import path
from . import views

urlpatterns = [
    path('', views.bookings, name='bookings'),
    #path('cancel/', views.bookings(), name='cancel'),
    #path('bookings_success/', views.bookings_success(), name='success'),
]