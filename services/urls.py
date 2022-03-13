from django.urls import path
from . import views

urlpatterns = [
    path('', views.services, name='services'),
    path('all/', views.all_services, name='all_services'),
    path('<int:service_id>/', views.get_service, name='get_service'),
    path('dates/', views.get_dates, name='get_dates'),
    path('times/<int:date_id>/', views.get_times, name='get_times'),
]
