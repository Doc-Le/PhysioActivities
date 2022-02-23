from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from appointment.views import (
    SuccessView,
    CancelView,
    AppointmentView,
    CreateCheckoutSessionView,
    StripeIntentView,
    get_services,
    get_times,
    stripe_webhook
)
from user import views as UserViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('user/', include('user.urls'), name='user'),
    path('login/', UserViews.login_form, name='login'),
    path('logout/', UserViews.logout_func, name='logout'),
    path('signup/', UserViews.signup_form, name='signup'),
    path('', include('home.urls')),
    path('webhooks/stripe/', stripe_webhook, name='stripe-webhook'),
    path('appointment/', AppointmentView.as_view(), name='appointment'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('create-payment-intent/<pk>/', StripeIntentView.as_view(), name='create-payment-intent'),
    path('services/<int:resource_id>/', get_services, name='get_services'),
    path('times/<int:date_id>/', get_times, name='get_times'),
    path('checkout/', include('checkout.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
