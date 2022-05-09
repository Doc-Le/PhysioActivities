import datetime
from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from services.models import Service, Clinician, ServiceDate, ServiceTime

from .models import Booking
from user.models import UserProfile
from bookings.models import Booking

import json
import time


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, booking):
        """Send the user a confirmation email"""

        contact_email = settings.DEFAULT_FROM_EMAIL
        subject_email_template = 'bookings/emails/confirmation_email_subject.txt'
        body_email_template = 'bookings/emails/confirmation_email_body.txt'

        user_email = UserProfile.email

        subject = render_to_string(subject_email_template, {'booking': booking})
        body = render_to_string(body_email_template, {'booking': booking, 'contact_email': contact_email})

        send_mail(
            subject,
            body,
            contact_email,
            [user_email]
        )

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info
        username = intent.metadata.username

        user = UserProfile.objects.get(user__username=username)
        service = Service.objects.get(id=bag['service'])
        clinician = Clinician.objects.get(id=bag['clinician'])
        date = ServiceDate.objects.get(id=bag['date'])
        time = ServiceTime.objects.get(id=bag['time'])
        date_time = datetime.strptime(bag['datetime'][:-1], '%d/%m/%Y %H:%M')
        total = float(bag['total'])

        # Update profile information if save_info was checked
        profile = None

        booking_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                booking = Booking.objects.get(
                    user=user,
                    service=service,
                    clinician=clinician,
                    date=date,
                    time=time,
                    date_time=date_time,
                    total=total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                booking_exists = True
                break
            except Booking.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if booking_exists:
            self._send_confirmation_email(booking)
            return HttpResponse(
                content=(f'Webhook received: {event["type"]} | SUCCESS: '
                         'Verified Booking already in database'),
                status=200)
        else:
            booking = None
            try:
                booking = Booking.objects.create(
                    user=user,
                    service=service,
                    clinician=clinician,
                    date=date,
                    time=time,
                    date_time=date_time,
                    total=total,
                    stripe_pid=pid,
                )
            except Exception as e:
                if booking:
                    booking.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        self._send_confirmation_email(booking)
        return HttpResponse(
            content=(f'Webhook received: {event["type"]} | SUCCESS: '
                     'Created Booking in webhook'),
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
