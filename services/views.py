from django.shortcuts import render

from django.http import JsonResponse, HttpResponse
from .models import Service

def all_services(request):
    """ A view to show all services, including sorting and search queries """
    services = Service.objects.all()

    return JsonResponse({
        'data': services
    })

