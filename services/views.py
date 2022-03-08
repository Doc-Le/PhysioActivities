from django.shortcuts import render

from django.http import JsonResponse
from .models import Service

SESSION_KEY = 'services'

def all_services(request):
    """ Get all services, including sorting and search queries """
    data = []
    services = Service.objects.all()
    for service in services:
        data.append({
            'id': service.id,
            'name': service.name,
            'price': service.get_display_price()
        })


    return JsonResponse({
        'data': data
    })

def get_service(request, service_id):
    service = Service.objects.get(id=service_id)
    clinicians = get_clinicians_json(service.clinicians.all())

    data = {
        'id': service.id,
        'name': service.name,
        'price': service.get_display_price(),
        'clinicians': clinicians
    }

    return JsonResponse({
        'data': data
    })

def get_clinicians_json(clinicians):
    data = []
    clinicians
    for clinician in clinicians:
        data.append({
            'id': clinician.id,
            'full_name': clinician.full_name,
            'gender': clinician.gender
        })
    
    return data