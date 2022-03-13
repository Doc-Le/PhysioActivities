from django.urls import path
from . import views

urlpatterns = [
    path('', views.bookings, name='bookings'),
    path('success/<booking_number>/', views.bookings_success, name='bookings_success'),
    path('cache_bookings_data/', views.cache_bookings_data, name='cache_bookings_data'),
    # path('wh/', webhook, name='webhook'),
]
