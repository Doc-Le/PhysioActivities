from django.shortcuts import render

import services
from .models import services

# Create your views here.


def all_services(request):
    """ A view to show all services, including sorting and search queries """

    services = Services.objects.all()

    context = {
        'services': services,
    }

    return render(request, 'services/services.html', context)
