from datetime import datetime

from django.db.models import Q
from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import JsonResponse, HttpResponse

from .forms import BookingForm
from .models import Booking, BookingDate, BookingTime

@login_required(login_url='/login?show_signup=true')
def bookings(request):    
    form = BookingForm()
    template = 'bookings/bookings.html'
    context = {
        'form': form,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'client_secret': 'test client secret',
    }

    return render(request, template, context)

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
    date = BookingDate.objects.get(id=date_id)
    time = BookingTime.objects.get(id=time_id)
    any = Booking.objects.filter(date=date,time=time).count()
    if any > 0:
        return False
    else:
        return True

def get_available_times(date_id: int):
    bookingTimes = BookingTime.objects.all()
    data = []
    if date_id is None:
        return data
        
    for time in bookingTimes:
        if has_time_available(date_id, time.id):
            data.append({
                'id': time.id,
                'time': str(time)
            })

    return data

def get_available_dates():
    now = datetime.now()
    bookingDates = BookingDate.objects.filter(Q(date__gt=now.date()))
    data = []
    for date in bookingDates:
        any = get_available_times(date.id)
        if len(any) > 0:
            data.append({
                'id': date.id,
                'date': str(date)
            })

    return data