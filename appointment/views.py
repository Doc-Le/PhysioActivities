import datetime
import stripe
import json
from django.core.mail import send_mail
from django.core.serializers import serialize
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.views import View
from django.db.models import Q
from .models import Appointment, CalendarDate, CalendarTime, Location, Resource, ResourceService, Service

TEMPLATE_ROOT = "appointment"
stripe.api_key = settings.STRIPE_SECRET_KEY

class SuccessView(TemplateView):
    template_name = TEMPLATE_ROOT + "/success.html"

class CancelView(TemplateView):
    template_name = TEMPLATE_ROOT + "/cancel.html"
    
class AppointmentView(TemplateView):
    template_name = TEMPLATE_ROOT + "/index.html"

    def get_context_data(self, **kwargs):
        locations = Location.objects.all()
        resources = Resource.objects.all()
        calendarDates = get_available_dates()
        
        context = super(AppointmentView, self).get_context_data(**kwargs)
        context = {
            "locations": locations,
            "resources": resources,
            "services": [],
            "calendarDates": calendarDates,
            "calendarTimes": [],
            "checkoutUri": "/create-checkout-session/",
            "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY
        }
        return context        

class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        payload = request.body
        service_id = self.kwargs["pk"]
        service = Service.objects.get(id=service_id)

        # save appointment
        appointment = add_appointment(request)

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            customer_email=appointment.email,
            line_items=[
                {
                    'price_data': {
                        'currency': 'eur',
                        'unit_amount': service.price,
                        'product_data': {
                            'name': service.name,
                        },
                    },
                    'quantity': 1,
                },
            ],
            metadata={
                "product_id": service.id
            },
            mode='payment',
            success_url=settings.HOST_DOMAIN + '/success/',
            cancel_url=settings.HOST_DOMAIN + '/cancel/',
        )
        
        return JsonResponse({
            'id': checkout_session.id
        })

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)    

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        customer_email = session["customer_details"]["email"]
        service_id = session["metadata"]["product_id"]
        service = Service.objects.get(id=service_id)

        send_mail(
            subject="Here is your Appointment",
            message=f"Thanks for your booking. The URL is {service.url}",
            recipient_list=[customer_email],
            from_email=settings.EMAIL_HOST_USER
        )

        # TODO - decide whether you want to send the file or the URL
    
    elif event["type"] == "payment_intent.succeeded":
        intent = event['data']['object']

        stripe_customer_id = intent["customer"]
        stripe_customer = stripe.Customer.retrieve(stripe_customer_id)

        customer_email = stripe_customer['email']
        service_id = intent["metadata"]["product_id"]

        service = Service.objects.get(id=service_id)

        send_mail(
            subject="Here is your product",
            message=f"Thanks for your purchase. Here is the product you ordered. The URL is {service.url}",
            recipient_list=[customer_email],
            from_email=settings.EMAIL_HOST_USER
        )

    return HttpResponse(status=200)

class StripeIntentView(View):
    def post(self, request, *args, **kwargs):
        try:
            req_json = json.loads(request.body)

            customer = stripe.Customer.create(
                email=req_json['email'],
            )
            service_id = self.kwargs["pk"]
            service = Service.objects.get(id=service_id)
            intent = stripe.PaymentIntent.create(
                amount=service.price,
                currency='eur',
                customer=customer['id'],
                metadata={
                    "product_id": service.id
                }
            )
            return JsonResponse({
                'clientSecret': intent['client_secret']
            })
        except Exception as e:
            return JsonResponse({ 'error': str(e) })

def get_services(request, resource_id):
    resource = Resource.objects.get(id=resource_id)
    resourceServices = ResourceService.objects.filter(resource=resource)

    services = []

    for resourceService in resourceServices:
        service = resourceService.service
        services.append({
            'id': str(service.id),
            'get_display_price': service.get_display_price(),
            'name': service.name,
        })

    return JsonResponse({
        'data': services
    })

def get_times(request, date_id):
    times = get_available_times(date_id)
    
    return JsonResponse({
        'data': times
    })

def get_available_dates():
    now = datetime.datetime.now()
    calendarDates = CalendarDate.objects.filter(Q(date__gt=now.date()))
    availableDates = []
    for calendarDate in calendarDates:
        any = get_available_times(calendarDate.id)
        if len(any) > 0:
            availableDates.append(calendarDate)

    return availableDates

def get_available_times(date_id):
    calendarTimes = CalendarTime.objects.all()

    times = []

    for time in calendarTimes:
        if has_time_available(date_id, time.id):
            times.append({
                'id': time.id,
                'hour': time.hour,
                'minute': time.minute
            })

    return times

def has_time_available(date_id, time_id):
    calendarDate = CalendarDate.objects.get(id=date_id)
    calendarTime = CalendarTime.objects.get(id=time_id)
    any = Appointment.objects.filter(date=calendarDate,time=calendarTime).count()
    if any > 0:
        return False
    else:
        return True

def add_appointment(request):
    """ Add an appointment """
    payload = json.loads(request.body)
    print(payload)
    
    location = Location.objects.get(id=payload['locationId'])
    service = Service.objects.get(id=payload['serviceId'])
    resource = Resource.objects.get(id=payload['resourceId'])
    date = CalendarDate.objects.get(id=payload['dateId'])
    time = CalendarTime.objects.get(id=payload['timeId'])

    appointment = Appointment(first_name=payload['firstName'], 
        last_name=payload['lastName'],
        gender=payload['gender'],
        phone=payload['phone'],
        email=payload['email'],
        location=location,
        service=service,
        resource=resource,
        date=date,
        time=time,
        paid=True,
    )

    appointment.save()

    return appointment
