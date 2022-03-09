from datetime import datetime

from django.db.models import Q
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.urls import reverse
from django.views.decorators.http import require_POST

from .models import Booking

import stripe
import json

@login_required(login_url='/login?show_signup=true')
def bookings(request):    

    bag = request.session.get('bag', {})
    user = request.user

    template = 'bookings/bookings.html'
    context = {
        'user': user,
        'bag': bag,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'client_secret': 'test client secret',
    }

    return render(request, template, context)


# @require_POST
# def cache_booking_data(request):
#     try:
#         pid = request.POST.get('client_secret').split('_secret')[0]
#         stripe.api_key = settings.STRIPE_SECRET_KEY
#         stripe.PaymentIntent.modify(pid, metadata={
#             'bag': json.dumps(request.session.get('bag', {})),
#             'save_info': request.POST.get('save_info'),
#             'username': request.user,
#         })
#         return HttpResponse(status=200)
#     except Exception as e:
#         messages.error(request, ('Sorry, your payment cannot be '
#                                  'processed right now. Please try '
#                                  'again later.'))
#         return HttpResponse(content=e, status=400)


# def checkout(request):
#     stripe_public_key = settings.STRIPE_PUBLIC_KEY
#     stripe_secret_key = settings.STRIPE_SECRET_KEY

#     if request.method == 'POST':
#         form_data = {
#             'service': request.POST['service'],
#             'clinician': request.POST['clinician'],
#             'date': request.POST['date'],
#             'time': request.POST['time'],
#             'total': request.POST['total'],
#         }

#         booking_form = BookingForm(form_data)
#         if order_form.is_valid():
#             booking = booking_form.save(commit=False)
#             pid = request.POST.get('client_secret').split('_secret')[0]
#             booking.stripe_pid = pid
#             booking.save()
#             # Save the info to the user's profile if all is well
#             request.session['save_info'] = 'save-info' in request.POST
#             return redirect(reverse('checkout_success',
#                                     args=[booking.booking_number]))
#         else:
#             messages.error(request, ('There was an error with your form. '
#                                      'Please double check your information.'))
#     else:
#         bag = request.session.get('bag', {})
#         if not bag:
#             messages.error(request,
#                            "There's nothing in your bag at the moment")
#             return redirect(reverse('products'))

#         current_bag = bag_contents(request)
#         total = current_bag['grand_total']
#         stripe_total = round(total * 100)
#         stripe.api_key = stripe_secret_key
#         intent = stripe.PaymentIntent.create(
#             amount=stripe_total,
#             currency=settings.STRIPE_CURRENCY,
#         )

#         # Attempt to prefill the form with any info
#         # the user maintains in their profile
#         if request.user.is_authenticated:
#             try:
#                 profile = UserProfile.objects.get(user=request.user)
#                 order_form = OrderForm(initial={
#                     'full_name': profile.user.get_full_name(),
#                     'email': profile.user.email,
#                     'phone_number': profile.default_phone_number,
#                     'country': profile.default_country,
#                     'postcode': profile.default_postcode,
#                     'town_or_city': profile.default_town_or_city,
#                     'street_address1': profile.default_street_address1,
#                     'street_address2': profile.default_street_address2,
#                     'county': profile.default_county,
#                 })
#             except UserProfile.DoesNotExist:
#                 order_form = OrderForm()
#         else:
#             order_form = OrderForm()

#     if not stripe_public_key:
#         messages.warning(request, ('Stripe public key is missing. '
#                                    'Did you forget to set it in '
#                                    'your environment?'))

#     template = 'checkout/checkout.html'
#     context = {
#         'order_form': order_form,
#         'stripe_public_key': stripe_public_key,
#         'client_secret': intent.client_secret,
#     }

#     return render(request, template, context)


# def checkout_success(request, order_number):
#     """
#     Handle successful checkouts
#     """
#     save_info = request.session.get('save_info')
#     order = get_object_or_404(Order, order_number=order_number)

#     if request.user.is_authenticated:
#         profile = UserProfile.objects.get(user=request.user)
#         # Attach the user's profile to the order
#         order.user_profile = profile
#         order.save()

#         # Save the user's info
#         if save_info:
#             profile_data = {
#                 'default_phone_number': order.phone_number,
#                 'default_country': order.country,
#                 'default_postcode': order.postcode,
#                 'default_town_or_city': order.town_or_city,
#                 'default_street_address1': order.street_address1,
#                 'default_street_address2': order.street_address2,
#                 'default_county': order.county,
#             }
#             user_profile_form = UserProfileForm(profile_data, instance=profile)
#             if user_profile_form.is_valid():
#                 user_profile_form.save()

#     messages.success(request, f'Order successfully processed! \
#         Your order number is {order_number}. A confirmation \
#         email will be sent to {order.email}.')

#     if 'bag' in request.session:
#         del request.session['bag']

#     template = 'checkout/checkout_success.html'
#     context = {
#         'order': order,
#     }

#     return render(request, template, context)
