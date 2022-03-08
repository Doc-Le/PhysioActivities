from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_services, name='services'),
    path('<int:service_id>/', views.get_service, name='get_service'),
]