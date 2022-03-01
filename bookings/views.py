from re import template
from django.shortcuts import render, redirect, reverse

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings

from .forms import OrderForm

@login_required(login_url='/login?show_signup=true')
def bookings(request):    
    # Booking = request.session.get('booking', {})
    # if not Booking:
    #     messages.error(request, "There is no appoiment schedules")
    #     return redirect(reverse('bookings'))

    order_form = OrderForm()
    template = 'bookings/bookings.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
