from django.urls import path
from . import views

urlpatterns = [
    path('', views.bookings, name='bookings'),
    # path('cancel/', views.as_view(), name='cancel'),
    # path('success/', views.as_view(), name='success'),
]