from datetime import datetime
import json

from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import redirect, render

from bookings.models import Booking
from .forms import ServiceForm
from .models import Clinician, Service, ServiceDate, ServiceTime


def services(request):
    bag = request.session.get('bag', {})

    if request.method == 'POST':
        bag = {
            'service': int(request.POST['service']),
            'clinician': int(request.POST['clinician']),
            'date': int(request.POST['date']),
            'time': int(request.POST['time'])
        }
        form = ServiceForm(bag)
        if form.is_valid():
            service = Service.objects.get(id=bag['service'])
            clinician = Clinician.objects.get(id=bag['clinician'])
            date = ServiceDate.objects.get(id=bag['date'])
            time = ServiceTime.objects.get(id=bag['time'])
            bag['service_name'] = service.name
            bag['clinician_full_name'] = clinician.full_name
            bag['datetime'] = str(date) + ', ' + str(time) + 'h'
            bag['total'] = float(service.price)
            request.session['bag'] = bag
            request.session['save_info'] = 'save-info' in request.POST
            return redirect('/bookings')
        else:
            messages.error(request, ('There was an error with your form. '
                                     'Please double check your information.'))
    else:
        form = ServiceForm(bag)

    template = 'services/services.html'
    context = {
        'form': form,
        'client_secret': 'test client secret',
    }

    return render(request, template, context)


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


def get_dates(request):
    dates = get_available_dates()

    return JsonResponse({
        'data': dates
    })


def get_times(request, date_id: int):
    times = get_available_times(date_id)

    return JsonResponse({
        'data': times
    })


def has_time_available(date_id: int, time_id: int):
    date = ServiceDate.objects.get(id=date_id)
    time = ServiceTime.objects.get(id=time_id)
    any = Booking.objects.filter(date=date, time=time).count()
    if any > 0:
        return False
    else:
        return True


def get_available_times(date_id: int):
    serviceTimes = ServiceTime.objects.all()
    data = []
    if date_id is None:
        return data

    for time in serviceTimes:
        if has_time_available(date_id, time.id):
            data.append({
                'id': time.id,
                'time': str(time)
            })

    return data


def get_available_dates():
    now = datetime.now()
    serviceDates = ServiceDate.objects.filter(Q(date__gt=now.date()))
    data = []
    for date in serviceDates:
        any = get_available_times(date.id)
        if len(any) > 0:
            data.append({
                'id': date.id,
                'date': str(date)
            })

    return data
