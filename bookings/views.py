from django.shortcuts import render, redirect, reverse

from django.contrib import messages
from django.conf import settings
from .models import Order, OrderLineItem
from appointment.models import Appointment

from .forms import OrderForm


def checkout(request):
    
    Appointment = request.session.get('appointment', {})
    if not Appointment:
        messages.error(request, "There is no appoiment schedules")
        return redirect(reverse('appointment'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': "settings.STRIPE_PUBLIC_KEY",
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
